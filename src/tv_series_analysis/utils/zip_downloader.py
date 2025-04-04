import os
import sys
import zipfile

import requests
from zipfile import ZipFile
from io import BytesIO

from requests import HTTPError

from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger


class ZipDownloader:
    def __init__(self, url, output_folder):
        self.class_name = self.__class__.__name__
        self.url = url
        self.output_folder = output_folder

    def download_and_extract(self):
        tag: str = f"[{self.class_name}]::[download_and_extract]"
        try:
            # Create the output folder if it doesn't exist
            os.makedirs(self.output_folder, exist_ok=True)

            # Download the ZIP file
            response = requests.get(self.url)
            if response.status_code == 404:
                message = f"{tag}::[HTTPError 404]::The requested URL {self.url} was not found on the server. Please download the file manually."
                logger.error(message)
                raise HTTPError(message)
            else:
                response.raise_for_status()  # Raise other HTTP errors
            response.raise_for_status()  # Raise an error for failed requests

            # Open the ZIP file in memory
            with ZipFile(BytesIO(response.content)) as zip_file:
                # Extract all files into the output folder
                zip_file.extractall(self.output_folder)
                logger.info(f"{tag}::Files extracted to: {self.output_folder}")

        except requests.RequestException as e:
            message = f"{tag}::[RequestException]::Error while downloading the file: {e}"
            logger.error(message)
            raise CustomException(message, sys)
        except zipfile.BadZipFile:
            message = f"[BadZipFile]::{tag}::The downloaded file from {self.url} is not a valid ZIP file."
            logger.error(message)
            raise CustomException(message, sys)

# Example usage
# Replace 'your_url' and 'your_output_folder' with actual values
# zip_downloader = ZipDownloader("your_url", "your_output_folder")
# zip_downloader.download_and_extract()

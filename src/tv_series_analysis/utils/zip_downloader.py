import os
import sys
import zipfile

import requests
from zipfile import ZipFile
from io import BytesIO

from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger


class ZipDownloader:
    def __init__(self, url, output_folder):
        self.url = url
        self.output_folder = output_folder

    def download_and_extract(self):
        try:
            # Create the output folder if it doesn't exist
            os.makedirs(self.output_folder, exist_ok=True)

            # Download the ZIP file
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for failed requests

            # Open the ZIP file in memory
            with ZipFile(BytesIO(response.content)) as zip_file:
                # Extract all files into the output folder
                zip_file.extractall(self.output_folder)
                logger.info(f"Files extracted to: {self.output_folder}")

        except requests.RequestException as e:
            message = f"Error while downloading the file: {e}"
            logger.error(message)
            raise CustomException(message, sys)
        except zipfile.BadZipFile:
            message = f"The downloaded file from {self.url} is not a valid ZIP file."
            print(message)
            raise CustomException(message, sys)

# Example usage
# Replace 'your_url' and 'your_output_folder' with actual values
# zip_downloader = ZipDownloader("your_url", "your_output_folder")
# zip_downloader.download_and_extract()

import os
import subprocess
import zipfile
from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger

class KaggleDatasetDownloader:
    def __init__(self, kaggle_config_dir=os.path.expanduser('~/.kaggle/')):
        self.class_name = self.__class__.__name__
        # Initialize with the directory of Kaggle API credentials
        self.kaggle_config_dir = kaggle_config_dir
        os.environ['KAGGLE_CONFIG_DIR'] = self.kaggle_config_dir

    def download_and_extract(self, dataset_slug, output_dir='.'):
        tag: str = f"[{self.class_name}]::[download_and_extract]"
        try:
            """
                    Downloads and extracts a Kaggle dataset.

                    :param dataset_slug: Kaggle dataset slug (e.g., 'heptapod/titanic').
                    :param output_dir: Directory to extract dataset files.
                    """
            logger.info(f"{tag}::Downloading dataset '{dataset_slug}'...")

            # Download the dataset
            subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset_slug], check=True)

            # Unzip the dataset
            dataset_zip = f"{dataset_slug.split('/')[-1]}.zip"
            if os.path.exists(dataset_zip):
                logger.info(f"{tag}::Extracting '{dataset_zip}' into '{output_dir}'...")
                with zipfile.ZipFile(dataset_zip, 'r') as zip_ref:
                    zip_ref.extractall(output_dir)
                logger.info("{tag}::Extraction complete!")
            else:
                logger.error(f"{tag}::[Error]::Could not find the zip file '{dataset_zip}'.")
                raise FileNotFoundError(f"Zip file '{dataset_zip}' not found.")
        except subprocess.CalledProcessError as e:
            message = f"{tag}::[CalledProcessError]::Error occurred while downloading the dataset: {e}"
            logger.error(message)
            raise CustomException(message, e)
        except zipfile.BadZipFile:
            message = f"{tag}::[BadZipFile]::The downloaded file is not a valid zip file."
            logger.error(message)
            raise CustomException(message, zipfile.BadZipFile)
        except Exception as e:
            message = f"{tag}::[Exception]::An unexpected error occurred: {e}"
            logger.error(message)
            raise CustomException(message, e)

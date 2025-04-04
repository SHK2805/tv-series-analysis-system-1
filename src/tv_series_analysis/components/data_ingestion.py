import os
import sys

from src.tv_series_analysis.entity.artifact_entity import DataIngestionArtifact
from src.tv_series_analysis.entity.config_entity import DataIngestionConfig
from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger
from src.tv_series_analysis.utils.kaggle_dataset_downloader import KaggleDatasetDownloader
from src.tv_series_analysis.utils.zip_downloader import ZipDownloader


# Data Ingestion
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.class_name = self.__class__.__name__
        self.config = config

    def download_and_extract_subtitles(self):
        tag: str = f"[{self.class_name}]::[download_and_extract_subtitles]"
        try:
            logger.info(f"{tag}::started.")
            zip_downloader = ZipDownloader(self.config.data_ingestion_subtitles_url,
                                           self.config.data_ingestion_subtitles_dir)
            zip_downloader.download_and_extract()
            logger.info(f"{tag}::downloaded from {self.config.data_ingestion_subtitles_url} "
                        f"and extracted subtitles to {self.config.data_ingestion_subtitles_dir}.")
            logger.info(f"{tag}::complete.")
            return self.config.data_ingestion_subtitles_dir
        except Exception as e:
            message:str = f"{tag}::Error occurred: {e}"
            logger.error(message)
            raise CustomException(message, sys)

    def download_and_extract_transcripts(self):
        tag: str = f"[{self.class_name}]::[download_and_extract_transcripts]"
        try:
            logger.info(f"{tag}::started.")
            # Initialize the downloader
            downloader = KaggleDatasetDownloader(kaggle_config_dir=os.path.expanduser('~/.kaggle/'))

            # Download and extract Titanic dataset
            downloader.download_and_extract(self.config.data_ingestion_kaggle_transcripts_name,
                                            output_dir=self.config.data_ingestion_transcripts_dir_name)

            logger.info(f"{tag}::downloaded from {self.config.data_ingestion_subtitles_url} "
                        f"and extracted subtitles to {self.config.data_ingestion_subtitles_dir}.")
            logger.info(f"{tag}::complete.")
            return self.config.data_ingestion_subtitles_dir
        except Exception as e:
            message:str = f"{tag}::Error occurred: {e}"
            logger.error(message)
            raise CustomException(message, sys)

    def initiate_data_ingestion(self):
        tag: str = f"[{self.class_name}]::[initiate_data_ingestion]"
        try:
            logger.info(f"{tag}::started.")
            # self.download_and_extract_subtitles()
            # self.download_and_extract_transcripts()
            # BYPASS the downloading and extracting for now
            logger.info(f"{tag}::**********"
                        f"Due to the large number of files, I have opted NOT to download them automatically. "
                        f"Instead, I have downloaded them MANUALLY for better control and convenience."
                        f"**********")
            logger.info(f"{tag}::complete.")
            return DataIngestionArtifact(self.config.data_ingestion_subtitles_dir)
        except Exception as e:
            message:str = f"{tag}::Error occurred: {e}"
            logger.error(message)
            raise CustomException(message, sys)

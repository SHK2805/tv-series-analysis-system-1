import sys

from src.tv_series_analysis.entity.artifact_entity import DataIngestionArtifact
from src.tv_series_analysis.entity.config_entity import DataIngestionConfig
from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger
from src.tv_series_analysis.utils.zip_downloader import ZipDownloader


# Data Ingestion
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.class_name = self.__class__.__name__
        self.config = config

    def initiate_data_ingestion(self):
        tag: str = f"[{self.class_name}]::[initiate_data_ingestion]"
        try:
            logger.info(f"{tag}::started.")
            zip_downloader = ZipDownloader(self.config.data_ingestion_subtitles_url,
                                           self.config.data_ingestion_subtitles_dir)
            zip_downloader.download_and_extract()
            logger.info(f"{tag}::downloaded from {self.config.data_ingestion_subtitles_url} "
                        f"and extracted subtitles to {self.config.data_ingestion_subtitles_dir}.")
            logger.info(f"{tag}::complete.")
            return DataIngestionArtifact(self.config.data_ingestion_subtitles_dir)
        except Exception as e:
            message:str = f"{tag}::Error occurred: {e}"
            logger.error(message)
            raise CustomException(message, sys)

import sys
import pandas as pd
from nltk import sent_tokenize

from src.tv_series_analysis.entity.artifact_entity import DataTransformationArtifact, DataProcessorArtifact
from src.tv_series_analysis.entity.config_entity import DataProcessorConfig
from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger


# Data Processor
class DataProcessor:
    def __init__(self, data_transformation_artifact: DataTransformationArtifact,
                 data_processor_config: DataProcessorConfig):
        self.class_name = self.__class__.__name__
        self.data_transformation_artifact = data_transformation_artifact
        self.data_processor_config = data_processor_config

    def load_data_into_dataframe(self) -> pd.DataFrame:
        tag: str = f"[{self.class_name}]::[load_data_into_dataframe]"
        try:
            logger.info(f"{tag}::started.")
            # Placeholder for loading data into DataFrame
            # check if the data is in csv format
            if not self.data_transformation_artifact.transformed_subtitles_file_path.endswith('.csv'):
                message: str = f"Data is not in CSV format: {self.data_transformation_artifact.transformed_subtitles_file_path}"
                logger.error(message)
                raise ValueError(message)
            df = pd.read_csv(self.data_transformation_artifact.transformed_subtitles_file_path)
            logger.info(f"{tag}::loaded data into DataFrame with shape {df.shape}.")
            logger.info(f"{tag}::complete.")
            return df
        except Exception as e:
            message: str = f"{tag}::Error occurred: {e}"
            logger.error(message)
            raise CustomException(message, sys)

    def initiate_data_processor(self) -> DataProcessorArtifact:
        tag: str = f"[{self.class_name}]::[initiate_data_processing]"
        try:
            logger.info(f"{tag}::started.")
            df = self.load_data_into_dataframe()
            logger.info(f"{tag}::loaded data into DataFrame with shape {df.shape}.")
            # print(df.head())
            logger.info(f"{tag}::complete.")
            return DataProcessorArtifact("processed_file_path")
        except Exception as e:
            message: str = f"{tag}::Error occurred: {e}"
            logger.error(message)
            raise CustomException(message, sys)
import os.path
import sys
import pandas as pd
from src.tv_series_analysis.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from src.tv_series_analysis.entity.config_entity import ModelTrainerConfig
from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger
from src.tv_series_analysis.utils.utils import get_columns_from_yaml, validate_columns


class ModelTrainer:
    def __init__(self, data_transformation_artifact: DataTransformationArtifact,
                 model_trainer_config: ModelTrainerConfig):
        try:
            self.class_name = self.__class__.__name__
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            logger.error(f"Error in initializing ModelTrainer: {str(e)}")
            raise CustomException(e, sys)

    def validate_data_columns(self, df: pd.DataFrame) -> bool:
        tag: str = f"[{self.class_name}]::[validate_data_columns]"
        try:
            schema_file_path = self.model_trainer_config.schema_file_path
            if not schema_file_path:
                logger.error(f"{tag}::Schema file path is not provided")
                return False
            if not os.path.exists(schema_file_path):
                logger.error(f"{tag}::Schema file path does not exist: {schema_file_path}")
                return False
            actual_columns = get_columns_from_yaml(schema_file_path)
            expected_columns = df.columns.tolist()
            return validate_columns(actual_columns, expected_columns)
        except Exception as e:
            message:str = f"{tag}::Error in validating data columns: {str(e)}"
            logger.error(message)
            raise CustomException(message, sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        tag: str = f"[{self.class_name}]::[initiate_model_trainer]"
        try:
            logger.info(f"{tag}::Initiating model training")
            df = pd.read_csv(self.data_transformation_artifact.tokenized_subtitles_file_path)
            # Validate data columns
            if not self.validate_data_columns(df):
                message: str = f"{tag}::Dataframe schema does not match the required schema"
                logger.error(message)
                raise ValueError(message)
            logger.info(f"{tag}::Complete model training")
            return ModelTrainerArtifact("trained_model.pkl")
        except Exception as e:
            message: str = f"{tag}::Error in model training: {str(e)}"
            logger.error(message)
            raise CustomException(message, sys)
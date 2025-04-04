import sys
from src.tv_series_analysis.components.data_transformation import DataTransformation
from src.tv_series_analysis.config.configuration import TrainingPipelineConfig
from src.tv_series_analysis.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact
from src.tv_series_analysis.entity.config_entity import DataTransformationConfig
from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger

STAGE_NAME: str = "Data Transformation Pipeline"
class DataTransformationTrainingPipeline:
    def __init__(self, data_validation_artifact: DataValidationArtifact):
        self.class_name = self.__class__.__name__
        self.stage_name = STAGE_NAME
        self.data_validation_artifact = data_validation_artifact

    def data_transformation(self) -> DataTransformationArtifact:
        tag: str = f"[{self.class_name}]::[data_transformation]::"
        try:
            config: TrainingPipelineConfig = TrainingPipelineConfig()
            logger.info(f"{tag}::Configuration object created")

            data_transformation_config: DataTransformationConfig = DataTransformationConfig(config)
            logger.info(f"{tag}::Data Transformation configuration obtained")

            data_transformation: DataTransformation = DataTransformation(self.data_validation_artifact, data_transformation_config)
            logger.info(f"{tag}::Data Transformation object created")

            logger.info(f"{tag}::Running the data Transformation pipeline")

            data_transformation_artifact: DataTransformationArtifact = data_transformation.initiate_data_transformation()
            logger.info(f"Data Transformation Artifact: {data_transformation_artifact}")
            logger.info(f"{tag}::Data Transformation completed successfully")
            return data_transformation_artifact
        except Exception as e:
            logger.error(f"{tag}::Error running the data Transformation pipeline: {e}")
            raise CustomException(e, sys)
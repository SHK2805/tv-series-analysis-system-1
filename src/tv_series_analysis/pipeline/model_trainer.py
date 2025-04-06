import sys

from src.tv_series_analysis.components.model_trainer import ModelTrainer
from src.tv_series_analysis.config.configuration import TrainingPipelineConfig
from src.tv_series_analysis.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from src.tv_series_analysis.entity.config_entity import ModelTrainerConfig
from src.tv_series_analysis.logging.logger import logger
from src.tv_series_analysis.exception.exception import CustomException

STAGE_NAME: str = "Model Trainer Pipeline"
class ModelTrainerTrainingPipeline:
    def __init__(self, data_transformation_artifact: DataTransformationArtifact):
        self.class_name = self.__class__.__name__
        self.stage_name = STAGE_NAME
        self.data_transformation_artifact = data_transformation_artifact

    def train_model(self):
        tag: str = f"{self.class_name}::train_model::"
        try:
            logger.info(f"{tag}::Training model")
            config: TrainingPipelineConfig = TrainingPipelineConfig()
            logger.info(f"{tag}::Configuration object created")

            model_trainer_config: ModelTrainerConfig = ModelTrainerConfig(config)
            logger.info(f"{tag}::Model trainer configuration obtained")

            model_trainer = ModelTrainer(self.data_transformation_artifact, model_trainer_config)
            logger.info(f"{tag}::Model trainer object created")

            logger.info(f"{tag}::Running the model training pipeline")
            model_trainer_artifact: ModelTrainerArtifact = model_trainer.initiate_model_trainer()
            logger.info(f"{tag}::Model training completed successfully")
            return model_trainer_artifact

        except Exception as e:
            logger.error(f"{tag}::Error running the model training pipeline: {e}")
            raise CustomException(e, sys)
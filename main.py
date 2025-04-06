import sys

from env_config.set_config import Config
from src.tv_series_analysis.entity.artifact_entity import (DataIngestionArtifact,
                                                           DataValidationArtifact,
                                                           DataTransformationArtifact, ModelTrainerArtifact)
from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger
from src.tv_series_analysis.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.tv_series_analysis.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.tv_series_analysis.pipeline.data_validation import DataValidationTrainingPipeline
from src.tv_series_analysis.pipeline.model_trainer import ModelTrainerTrainingPipeline


class RunPipeline:
    def __init__(self):
        self.class_name = self.__class__.__name__

    def run_data_ingestion_pipeline(self) -> DataIngestionArtifact:
        tag: str = f"[{self.class_name}]::[run_data_ingestion_pipeline]::"
        try:
            data_ingestion_pipeline: DataIngestionTrainingPipeline = DataIngestionTrainingPipeline()
            logger.info(f"[STARTED]>>>>>>>>>>>>>>>>>>>> {data_ingestion_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<")
            logger.info(f"{tag}::Running the data ingestion pipeline")
            data_ingestion_artifact = data_ingestion_pipeline.data_ingestion()
            logger.info(f"{tag}::Data ingestion pipeline completed")
            logger.info(
                f"[COMPLETE]>>>>>>>>>>>>>>>>>>>> {data_ingestion_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<\n\n\n")
            return data_ingestion_artifact
        except Exception as e:
            logger.error(f"{tag}::Error running the data ingestion pipeline: {e}")
            raise CustomException(e, sys)

    def run_data_validation_pipeline(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        tag: str = f"[{self.class_name}]::[run_data_validation_pipeline]::"
        try:
            data_validation_pipeline: DataValidationTrainingPipeline = DataValidationTrainingPipeline(
                data_ingestion_artifact)
            logger.info(f"[STARTED]>>>>>>>>>>>>>>>>>>>> {data_validation_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<")
            logger.info(f"{tag}::Running the data validation pipeline")
            data_validation_artifact = data_validation_pipeline.data_validation()
            logger.info(f"{tag}::Data validation pipeline completed")
            logger.info(
                f"[COMPLETE]>>>>>>>>>>>>>>>>>>>> {data_validation_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<\n\n\n")
            return data_validation_artifact
        except Exception as e:
            logger.error(f"{tag}::Error running the data validation pipeline: {e}")
            raise CustomException(e, sys)

    def run_data_transformation_pipeline(self, data_validation_artifact: DataValidationArtifact) -> DataTransformationArtifact:
        tag: str = f"[{self.class_name}]::[run_data_transformation_pipeline]::"
        try:
            data_transformation_pipeline: DataTransformationTrainingPipeline = DataTransformationTrainingPipeline(
                data_validation_artifact)
            logger.info(f"[STARTED]>>>>>>>>>>>>>>>>>>>> {data_transformation_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<")
            logger.info(f"{tag}::Running the data transformation pipeline")
            data_transformation_artifact = data_transformation_pipeline.data_transformation()
            logger.info(f"{tag}::Data transformation pipeline completed")
            logger.info(
                f"[COMPLETE]>>>>>>>>>>>>>>>>>>>> {data_transformation_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<\n\n\n")
            return data_transformation_artifact
        except Exception as e:
            logger.error(f"{tag}::Error running the data transformation pipeline: {e}")
            raise CustomException(e, sys)

    def run_model_trainer_pipeline(self,
                                   data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        tag: str = f"{self.class_name}::run_model_trainer_pipeline::"
        try:
            model_trainer_pipeline: ModelTrainerTrainingPipeline = ModelTrainerTrainingPipeline(
                data_transformation_artifact)
            logger.info(f"[STARTED]>>>>>>>>>>>>>>>>>>>> {model_trainer_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<")
            logger.info(f"{tag}::Running the model trainer pipeline")
            model_trainer_artifact = model_trainer_pipeline.train_model()
            logger.info(f"{tag}::Model trainer pipeline completed")
            logger.info(
                f"[COMPLETE]>>>>>>>>>>>>>>>>>>>> {model_trainer_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<\n\n\n")
            return model_trainer_artifact
        except Exception as e:
            logger.error(f"{tag}::Error running the model trainer pipeline: {e}")
            raise CustomException(e, sys)

    def run(self) -> None:
        data_ingestion_artifact: DataIngestionArtifact = self.run_data_ingestion_pipeline()
        # logger.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")
        data_validation_artifact: DataValidationArtifact = self.run_data_validation_pipeline(data_ingestion_artifact)
        # logger.info(f"Data Validation Artifact: {data_validation_artifact}")
        data_transformation_artifact: DataTransformationArtifact = self.run_data_transformation_pipeline(data_validation_artifact)
        # logger.info(f"Data Transformation Artifact: {data_transformation_artifact}")
        model_trainer_artifact: ModelTrainerArtifact = self.run_model_trainer_pipeline(data_transformation_artifact)

if __name__ == "__main__":
    try:
        config = Config()
        if config.set():
            logger.info("Environment variables set")
        else:
            logger.error("Environment variables NOT set")
            raise CustomException("Environment variables NOT set", sys)
        # Run the pipelines
        run_pipeline = RunPipeline()
        run_pipeline.run()
    except Exception as ex:
        logger.error(f"Error running the pipeline: {ex}")
        raise CustomException(ex, sys)

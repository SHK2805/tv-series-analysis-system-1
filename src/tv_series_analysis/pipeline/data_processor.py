import sys
from src.tv_series_analysis.components.data_processor import DataProcessor
from src.tv_series_analysis.config.configuration import TrainingPipelineConfig
from src.tv_series_analysis.entity.artifact_entity import DataTransformationArtifact, DataProcessorArtifact
from src.tv_series_analysis.entity.config_entity import DataProcessorConfig
from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger

STAGE_NAME: str = "Data Processing Pipeline"
class DataProcessorTrainingPipeline:
    def __init__(self, data_transformation_artifact: DataTransformationArtifact):
        self.class_name = self.__class__.__name__
        self.stage_name = STAGE_NAME
        self.data_transformation_artifact = data_transformation_artifact

    def data_processor(self) -> DataProcessorArtifact:
        tag: str = f"[{self.class_name}]::[data_processor]::"
        try:
            config: TrainingPipelineConfig = TrainingPipelineConfig()
            logger.info(f"{tag}::Configuration object created")

            data_processor_config: DataProcessorConfig = DataProcessorConfig(config)
            logger.info(f"{tag}::Data Processor configuration obtained")

            data_processor: DataProcessor = DataProcessor(self.data_transformation_artifact, data_processor_config)
            logger.info(f"{tag}::Data Processor object created")

            logger.info(f"{tag}::Running the data processor pipeline")

            data_processor_artifact: DataProcessorArtifact = data_processor.initiate_data_processor()
            logger.info(f"Data Processor Artifact: {data_processor_artifact}")
            logger.info(f"{tag}::Data Processor completed successfully")
            return data_processor_artifact
        except Exception as e:
            logger.error(f"{tag}::Error running the data processor pipeline: {e}")
            raise CustomException(e, sys)
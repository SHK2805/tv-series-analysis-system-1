import os
import sys

from src.tv_series_analysis.entity.artifact_entity import DataValidationArtifact, DataIngestionArtifact
from src.tv_series_analysis.entity.config_entity import DataValidationConfig
from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger


class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config: DataValidationConfig):
        try:
            self.class_name = self.__class__.__name__
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise CustomException(e, sys)

    def validate_subtitles(self) -> bool:
        tag: str = f"{self.class_name}::validate_subtitles::"
        try:
            logger.info(f"{tag}::Validating subtitles")
            if os.path.exists(self.data_validation_config.subtitles_dir_path):
                logger.info(f"{tag}::Subtitles folder check passed")
                path_status = True
            else:
                logger.error(f"{tag}::Subtitles folder {self.data_validation_config.subtitles_dir_path} does not exist")
                path_status = False

            # check the number of files in the subtitles directory
            subtitles_files = os.listdir(self.data_validation_config.subtitles_dir_path)
            if len(subtitles_files) != self.data_validation_config.subtitles_file_count:
                logger.error(f"{tag}::Subtitles file count mismatch: expected {self.data_validation_config.subtitles_file_count}, found {len(subtitles_files)}")
                count_status = False
            else:
                logger.info(f"{tag}::Subtitles file count validation passed")
                count_status = True
            return path_status and count_status
        except Exception as e:
            logger.error(f"{tag}::Error validating subtitles: {e}")
            raise CustomException(e, sys)

    def validate_transcripts(self) -> bool:
        tag: str = f"{self.class_name}::validate_transcripts::"
        try:
           # check the transcript file exists
            if os.path.exists(self.data_validation_config.transcripts_file_path):
                logger.info(f"{tag}::Transcripts file path check passed")
                path_status = True
            else:
                logger.error(f"{tag}::Transcripts file {self.data_validation_config.transcripts_file_path} does not exist")
                path_status = False

            return path_status
        except Exception as e:
            logger.error(f"{tag}::Error validating transcripts: {e}")
            raise CustomException(e, sys)

    def validate_jutsus(self) -> bool:
        tag: str = f"{self.class_name}::validate_jutsus::"
        try:
            # check the jutsus file exists
            if os.path.exists(self.data_validation_config.jutsus_file_path):
                logger.info(f"{tag}::Jutsus file path check passed")
                path_status = True
            else:
                logger.error(f"{tag}::Jutsus file {self.data_validation_config.jutsus_file_path} does not exist")
                path_status = False

            return path_status
        except Exception as e:
            logger.error(f"{tag}::Error validating jutsus: {e}")
            raise CustomException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        tag: str = f"{self.class_name}::initiate_data_validation::"
        try:
            status = False
            logger.info(f"{tag}::Initiating data validation")
            validate_subtitles:bool = self.validate_subtitles()
            validate_transcripts:bool = self.validate_transcripts()
            validate_jutsus:bool = self.validate_jutsus()
            status = validate_subtitles and validate_transcripts and validate_jutsus
            logger.info(f"Status: {status}")
            logger.info(f"Subtitles Validation: {validate_subtitles}")
            logger.info(f"Transcripts Validation: {validate_transcripts}")
            logger.info(f"Jutsus Validation: {validate_jutsus}")
            # create the data validation directory if it doesn't exist
            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
            logger.info(f"{tag}::Data validation directory created at {self.data_validation_config.data_validation_dir}")
            # save the validation status to a file
            with open(self.data_validation_config.data_validation_status_file_path, 'w') as f:
                f.write(f"Status: {status}\n")
                f.write(f"Subtitles Validation: {validate_subtitles}\n")
                f.write(f"Transcripts Validation: {validate_transcripts}\n")
                f.write(f"Jutsus Validation: {validate_jutsus}\n")
            logger.info(f"{tag}::Validation status {status} saved to {self.data_validation_config.data_validation_status_file_path} successfully")
            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                validation_status_file_path=self.data_validation_config.data_validation_status_file_path)
            return data_validation_artifact
        except Exception as e:
            logger.error(f"{tag}::Error running the data validation pipeline: {e}")
            raise CustomException(e, sys)
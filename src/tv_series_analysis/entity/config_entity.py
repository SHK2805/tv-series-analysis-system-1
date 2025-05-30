import os
from src.tv_series_analysis.config.configuration import TrainingPipelineConfig
from src.tv_series_analysis.constants import (subtitles_dir_name,
                                              data_ingestion_subtitles_url, kaggle_transcripts_name,
                                              transcripts_dir_name, jutsus_dir_name,
                                              data_ingestion_dir_name, data_validation_dir_name,
                                              data_validation_status_file_name, subtitles_file_count,
                                              transcripts_file_name, jutsus_file_name, data_folder_name,
                                              data_transformation_dir_name,
                                              data_transformation_transformed_subtitles_file_name,
                                              data_transformation_tokenized_subtitles_file_name, model_trainer_dir_name,
                                              model_trainer_schema_file_path, model_trainer_batch_size,
                                              model_trainer_target_column,
                                              )


class DataIngestionConfig:
    def __init__(self, config: TrainingPipelineConfig):
        self.class_name = self.__class__.__name__
        self.data_ingestion_dir = data_ingestion_dir_name
        self.data_ingestion_subtitles_url = data_ingestion_subtitles_url
        self.data_ingestion_subtitles_dir_path = os.path.join(self.data_ingestion_dir, subtitles_dir_name)
        self.data_ingestion_kaggle_transcripts_name = kaggle_transcripts_name
        self.data_ingestion_transcripts_dir_path: str = os.path.join(self.data_ingestion_dir, transcripts_dir_name)
        self.data_ingestion_jutsus_dir_name: str = os.path.join(self.data_ingestion_dir, jutsus_dir_name)

class DataValidationConfig:
    def __init__(self, config: TrainingPipelineConfig):
        self.class_name = self.__class__.__name__
        # folders
        self.data_dir = data_folder_name
        self.data_validation_dir = os.path.join(config.artifact_dir,data_validation_dir_name)
        # files
        self.data_validation_status_file_path = os.path.join(self.data_validation_dir, data_validation_status_file_name)
        # subtitles
        self.subtitles_dir_path = os.path.join(self.data_dir, subtitles_dir_name)
        self.subtitles_file_count = subtitles_file_count
        # transcripts
        self.transcripts_file_path = os.path.join(self.data_dir, transcripts_dir_name, transcripts_file_name)
        # jutsus
        self.jutsus_file_path = os.path.join(self.data_dir, jutsus_dir_name, jutsus_file_name)

class DataTransformationConfig:
    def __init__(self, config: TrainingPipelineConfig):
        self.class_name = self.__class__.__name__
        # folders
        self.data_dir = data_folder_name
        self.data_transformation_dir = os.path.join(config.artifact_dir,data_transformation_dir_name)
        # subtitles
        self.subtitles_dir_path = os.path.join(self.data_dir, subtitles_dir_name)
        # transcripts
        self.transcripts_file_path = os.path.join(self.data_dir, transcripts_dir_name, transcripts_file_name)
        # jutsus
        self.jutsus_file_path = os.path.join(self.data_dir, jutsus_dir_name, jutsus_file_name)
        # transformed subtitles
        self.transformed_subtitles_file_path = os.path.join(self.data_transformation_dir,
                                                            data_transformation_transformed_subtitles_file_name)
        self.tokenized_subtitles_file_name = os.path.join(self.data_transformation_dir,
                                                            data_transformation_tokenized_subtitles_file_name)


class ModelTrainerConfig:
    def __init__(self, config: TrainingPipelineConfig):
        self.class_name = self.__class__.__name__
        # folders
        self.model_trainer_dir = os.path.join(config.artifact_dir, model_trainer_dir_name)
        self.schema_file_path = model_trainer_schema_file_path
        self.batch_size = model_trainer_batch_size
        self.target_column = model_trainer_target_column


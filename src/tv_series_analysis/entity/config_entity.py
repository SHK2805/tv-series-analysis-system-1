import os
from src.tv_series_analysis.config.configuration import TrainingPipelineConfig
from src.tv_series_analysis.constants import (data_ingestion_subtitles_dir_name,
                                              data_ingestion_subtitles_url, data_ingestion_kaggle_transcripts_name,
                                              data_ingestion_transcripts_dir_name)


class DataIngestionConfig:
    def __init__(self, config: TrainingPipelineConfig):
        self.class_name = self.__class__.__name__
        self.data_ingestion_dir = config.data_dir
        self.data_ingestion_subtitles_url = data_ingestion_subtitles_url
        self.data_ingestion_subtitles_dir = os.path.join(
            self.data_ingestion_dir, data_ingestion_subtitles_dir_name
        )
        self.data_ingestion_kaggle_transcripts_name = data_ingestion_kaggle_transcripts_name
        self.data_ingestion_transcripts_dir_name: str = os.path.join(
            self.data_ingestion_dir, data_ingestion_transcripts_dir_name
        )
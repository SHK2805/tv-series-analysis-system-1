import os
from datetime import datetime

from src.tv_series_analysis.constants import *


class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now().strftime("%d_%m_%Y_%H_%M_%S")):
        self.class_name = self.__class__.__name__
        self.timestamp = timestamp
        self.pipeline = pipeline_name
        self.data_dir = data_file_folder_name
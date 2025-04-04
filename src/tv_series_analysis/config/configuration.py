import os
from datetime import datetime

from src.tv_series_analysis.constants import *


class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now().strftime("%d_%m_%Y_%H_%M_%S")):
        self.class_name = self.__class__.__name__
        self.timestamp = timestamp
        self.pipeline = pipeline_name
        self.artifact_name = artifact_dir
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)
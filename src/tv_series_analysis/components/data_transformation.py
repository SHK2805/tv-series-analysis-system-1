import os
import sys
import pandas as pd
from glob import glob
from src.tv_series_analysis.entity.artifact_entity import DataValidationArtifact, DataTransformationArtifact
from src.tv_series_analysis.entity.config_entity import DataTransformationConfig
from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger
from src.tv_series_analysis.utils.utils import extract_text_with_pattern, extract_episode_number


# Data Transformation
class DataTransformation:
    def __init__(self, data_validation_artifact: DataValidationArtifact,
                 data_transformation_config: DataTransformationConfig):
        self.class_name = self.__class__.__name__
        self.data_validation_artifact = data_validation_artifact
        self.data_transformation_config = data_transformation_config

    def get_subtitles_filenames(self) -> list[str]:
        tag: str = f"[{self.class_name}]::[load_subtitles_data]"
        try:
            logger.info(f"{tag}::started.")
            subtitles_files = glob(f"{self.data_transformation_config.subtitles_dir_path}/*.ass") # + glob(f"{self.data_transformation_config.subtitles_dir_path}/*.srt")
            if not subtitles_files:
                message: str = f"Number of subtitle files found in {self.data_transformation_config.subtitles_dir_path}"
                logger.error(message)
                raise FileNotFoundError(message)
            # logger.info(f"{tag}::loaded subtitles data from {subtitles_files}.")
            logger.info(f"{tag}::loaded total subtitle files count {len(subtitles_files)}.")
            logger.info(f"{tag}::complete.")
            return subtitles_files
        except Exception as e:
            message: str = f"{tag}::Error occurred: {e}"
            logger.error(message)
            raise CustomException(message, sys)

    def transform_subtitles(self, subtitles_files: list[str]) -> str:
        tag: str = f"[{self.class_name}]::[transform_subtitles]"
        try:
            logger.info(f"{tag}::started.")
            # Placeholder for transformation logic
            scripts = []
            episode_number = []
            for file in subtitles_files:
                with open(file, 'r', encoding='utf-8') as f:
                    # content = f.read()
                    lines = f.readlines()
                    lines = lines[27:]  # Skip the first 27 lines
                    """
                    Dialogue: 0,0:00:59.40,0:01:01.81,Default,,0000,0000,0000,,Tearing through the dark
                    Here there are 9 commas before the text
                    We are extracting the text portion by removing all the data before the first 9 commas
                    """
                    # lines = [",".join(line.split(",")[9:]) for line in lines if line.startswith("Dialogue:")]
                    # Extract the text portion using regex
                    lines = [extract_text_with_pattern(line) for line in lines]
                # there are some \N characters in the text. Replace that with space
                lines = [line.replace("\\N", " ") for line in lines]
                # join the lines into a single string in batch of 10
                scripts.append(" ".join(lines))
                # get the season and episode number from the file name
                file_name = os.path.basename(file)
                season_episode = extract_episode_number(file_name)
                episode_number.append(season_episode)

            df = pd.DataFrame.from_dict({"episode": episode_number, "script": scripts})
            # save the transformed data to a csv file
            # create the transformed subtitles directory if it doesn't exist
            transformed_subtitles_dir_path = os.path.dirname(self.data_transformation_config.transformed_subtitles_file_path)
            os.makedirs(transformed_subtitles_dir_path, exist_ok=True)
            logger.info(f"{tag}::Transformed subtitles directory created at {transformed_subtitles_dir_path}")
            df.to_csv(self.data_transformation_config.transformed_subtitles_file_path, index=False)
            logger.info(f"{tag}::complete.")
            return self.data_transformation_config.transformed_subtitles_file_path
        except Exception as e:
            message: str = f"{tag}::Error occurred: {e}"
            logger.error(message)
            raise CustomException(message, sys)

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        tag: str = f"[{self.class_name}]::[initiate_data_transformation]"
        try:
            logger.info(f"{tag}::started.")
            # read the data validation status
            if not self.data_validation_artifact.validation_status:
                raise ValueError("Data validation failed. Cannot proceed with data transformation.")
            subtitles_files = self.get_subtitles_filenames()
            # print(subtitles_files)
            # transform the subtitle data
            transformed_subtitles_file_path = self.transform_subtitles(subtitles_files)
            logger.info(f"{tag}::complete.")
            return DataTransformationArtifact(transformed_subtitles_file_path)
        except Exception as e:
            message: str = f"{tag}::Error occurred: {e}"
            logger.error(message)
            raise CustomException(message, sys)


import os
#  NAMES
pipeline_name:str = "tv_series_analysis"
artifact_dir: str = "artifacts"

# DATA CONSTANTS
data_folder_name:str="data"
subtitles_dir_name: str = "subtitles"
subtitles_file_count: int = 220
kaggle_transcripts_name="leonzatrax/naruto-ep-1-transcript"
transcripts_dir_name: str = "transcripts"
transcripts_file_name: str = "naruto.csv"
transcripts_file_count: int = 1
jutsus_dir_name: str = "jutsus"
jutsus_file_name: str = "jutsus.jsonl"
jutsus_file_count: int = 1
schema_yaml_file_path: str = "data_schema/schema.yaml"



# DATA INGESTION CONSTANTS
data_ingestion_dir_name: str = data_folder_name
data_ingestion_subtitles_url="https://subtitlist.com/subs/naruto-season-1/english/2206507"

# DATA VALIDATION CONSTANTS
data_validation_dir_name: str = "data_validation"
data_validation_status_file_name: str = "status.txt"

# DATA TRANSFORMATION CONSTANTS
data_transformation_dir_name: str = "data_transformation"
data_transformation_transformed_subtitles_file_name: str = "transformed_subtitles.csv"
data_transformation_tokenized_subtitles_file_name: str = "tokenized_subtitles.csv"

# MODEL TRAINER CONSTANTS
model_trainer_dir_name: str = "model_trainer"
model_trainer_schema_file_path: str = "data_schema/schema.yaml"


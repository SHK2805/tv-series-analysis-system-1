from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    subtitles_dir: str
    transcripts_file_path: str
    jutsus_file_path: str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    validation_status_file_path: str

@dataclass
class DataTransformationArtifact:
    transformed_subtitles_file_path: str
    tokenized_subtitles_file_path: str

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
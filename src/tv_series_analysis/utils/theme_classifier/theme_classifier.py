import sys

from transformers import pipeline
import nltk
import torch
from typing import List, Dict

from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger


class ThemeClassifier:
    def __init__(self, task: str = "zero-shot-classification", model: str = "facebook/bart-large-mnli"):
        self.class_name = self.__class__.__name__
        try:
            nltk.download("punkt")
            self.device = 0 if torch.cuda.is_available() else -1
            logger.info(f"{self.class_name}::Device set to {self.device}")

            if task != "zero-shot-classification":
                message = f"{self.class_name}::Invalid task '{task}'. Only 'zero-shot-classification' is supported."
                logger.error(message)
                raise ValueError(message)
            self.task = task

            if model != "facebook/bart-large-mnli":
                message = f"{self.class_name}::Invalid model '{model}'. Only 'facebook/bart-large-mnli' is supported."
                logger.error(message)
                raise ValueError(message)
            self.model = model

            # Initialize the zero-shot classification pipeline
            # with the specified model and device
            logger.info(f"{self.class_name}::Initializing zero-shot classification pipeline...")
            self.theme_classifier = pipeline(
                task=self.task,
                model=self.model,
                device=self.device
            )
        except Exception as e:
            message = f"{self.class_name}::Failed to initialize zero-shot classification pipeline: {e}"
            logger.error(message)
            raise CustomException(message, sys)

    def get_classifier(self):
        """
        Returns the zero-shot classification model.
        """
        return self.theme_classifier

    def classify_themes(self, sequence_to_classify: str,
                        candidate_labels: List[str] = None,
                        multi_label: bool = True) -> Dict:
        """
        Classify the themes in the given text using zero-shot classification.

        Args:
            sequence_to_classify (str): The input text to classify.
            candidate_labels (List[str]): A list of candidate labels to classify against.
            multi_label (bool): Whether to allow multiple labels for classification.

        Returns:
            Dict: A dictionary containing the classification results.
        """
        tag:str = f"[{self.class_name}]::[classify_themes]"
        try:
            if not sequence_to_classify.strip():
                message = f"{tag}::Input sequence to classify is empty."
                logger.error(message)
                raise ValueError(message)

            labels = candidate_labels or [
                "friendship", "hope", "sacrifice", "battle",
                "self development", "betrayal", "love",
                "romance", "death",
            ]
            return self.theme_classifier(sequence_to_classify, labels, multi_label=multi_label)
        except Exception as e:
            message = f"{tag}::An error occurred while classifying themes: {e}"
            logger.error(message)
            raise CustomException(message, sys)


if __name__ == "__main__":
    classifier = ThemeClassifier()

    test_texts = [
        "The story is about a war between two countries about a woman's love.",
        "A tale of betrayal and sacrifice in pursuit of justice.",
    ]
    test_candidate_labels = [
        "friendship", "hope", "sacrifice", "battle",
        "self development", "betrayal", "love",
        "romance", "death",
    ]

    for text in test_texts:
        try:
            result = classifier.classify_themes(text, test_candidate_labels, False)
            print(f"Text: {text}")
            print(f"Classification Results: {result}")
        except ValueError as ex:
            print(f"Error: {ex}")

import sys

from transformers import pipeline
import nltk
import torch
from typing import List, Dict

from src.tv_series_analysis.exception.exception import CustomException
from src.tv_series_analysis.logging.logger import logger

nltk.download("punkt")


class ThemeClassifier:
    def __init__(self):
        self.class_name = self.__class__.__name__
        self.device = 0 if torch.cuda.is_available() else -1
        self.theme_classifier = pipeline(
            task="zero-shot-classification",
            model="facebook/bart-large-mnli",
            device=self.device,
        )
        logger.info(f"{self.class_name}::Initialized on {'GPU' if self.device == 0 else 'CPU'}")

    def get_model(self):
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
        tag:str = f"{self.class_name}::classify_themes"
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
        except ValueError as e:
            print(f"Error: {e}")

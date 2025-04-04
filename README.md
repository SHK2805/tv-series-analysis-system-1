# AI/NLP TV Series Analysis System with Python, Hugging Face, Chatbots, Spacy, Gradio

### Dataset
* For this project, we need to choose a TV series dataset.
* We need the below from the dataset
  * A sub-titles dataset
  * A transcript dataset
  * A classification dataset
* In this project, we are choosing the TV series "Naruto" dataset.

#### [Scrapy](https://scrapy.org/)
* Scrapy is a web crawling and web scraping framework for Python.
* It is used to extract data from the site [Naruto Wiki](https://naruto.fandom.com/wiki/)
* Install Scrapy using the command below or add this to the requirements.txt file.:
```bash
pip install scrapy
```
* The code for the crawlers is in the folder `utils/crawler/`

### Steps
#### Coding steps
* Constants
* Config
  * Configuration
* Entity
  * Config Entity
* Entity
  * Artifact Entity
* Components
  * Data Ingestion
  * Data Validation
  * Data Classification
* Pipeline
  * Data Ingestion
  * Data Validation
  * Data Classification
* Main

## Theme Classification
* For a given theme like friendship, love, hope, betrayal, etc. the system will give how much that theme is present in the series using the subtitles.
* We use `Zero-Shot Classification` for this.

#### Zero-Shot Classification
* In NLP, a **zero-shot classifier** is a model capable of classifying text into categories it hasn't been explicitly trained on, using natural language descriptions of the target labels to generalize new tasks.
* Zero-shot classification is powerful for tasks lacking labeled data, as it enables models to adapt using pre-existing knowledge.
* We are using the `Hugging Face` library for this.

##### Inputs:
* **Input Text**: The text you want to classify (e.g., "The movie was fantastic!").
* **Candidate Labels**: Categories for classification (e.g., ["positive," "negative," "neutral"]).
* *(Optional)* **Hypothesis Template**: A phrase linking text to labels, such as "This text is about {}."

##### Outputs:
* **Predicted Label**: The most relevant label for the text.
* **Confidence Scores**: Likelihoods for each label (e.g., {"positive": 0.85, "neutral": 0.10, "negative": 0.05}).

## Data Formats
#### Subtitles
* The subtitles are in the `.ass` format.
* The first **27** lines of the file are metadata.
* The subtitles are in the format:
```plaintext
Dialogue: 0,0:00:05.95,0:00:11.99,Default,,0000,0000,0000,,<text>
Dialogue: 0,0:00:11.99,0:00:17.99,Default,,0000,0000,0000,,<text>
```
* The text is in the last part of the line that we need to extract.
* We use regex and python to extract the text from the subtitles.

import re

import pandas as pd


def extract_text_with_pattern(dialogue_line:str, pattern:str=r",,.*?,,(.*)"):
    """
    # Example usage
    data_input = "Dialogue: 0,0:09:07.99,0:09:09.83,Default,,0000,0000,0000,,Wake up, Iruka Sensei!"
    extracted_text = extract_text_with_pattern(data_input)
    print(f"Extracted text: {extracted_text}")
    """
    """
    Extracts the <text> portion from a dialogue line.

    Args:
        dialogue_line (str): The input dialogue string.
        pattern (str): The regex pattern to match the text. Default is set to match the <text> portion.

    Returns:
        str: The extracted text, or an empty string if no match is found.
    """
    match = re.search(pattern, dialogue_line)
    return match.group(1) if match else ""

def extract_episode_number(file_name:str):
    """
    # Example usage
    filename = "Naruto Season 1 - 08.ass"
    episode_number = extract_episode_number(filename)
    print(f"Extracted episode number: {episode_number}")
    """
    """
    Extracts the season and episode number from a file name.

    Args:
        file_name (str): The input file name string.

    Returns:
        tuple: A tuple containing the extracted season and episode numbers, or None if no match is found.
    """
    match = int(file_name.split('-')[-1].split('.')[0].strip())
    return match

def create_batches(df_or_path, column_name, batch_size=20):
    """
    Creates batches of sentences either from a DataFrame or a file path.

    Parameters:
        df_or_path (pd.DataFrame or str): Either a DataFrame or a file path to the CSV.
        column_name (str): The name of the column containing tokenized text.
        batch_size (int): The number of sentences to include in each batch.

    Returns:
        List[str]: A list of batches, where each batch is a string of concatenated sentences.
    """
    # If a file path is provided, read the CSV into a DataFrame
    if isinstance(df_or_path, str):
        df = pd.read_csv(df_or_path)
    else:
        df = df_or_path

    # Initialize an empty list to store batches
    batches = []

    # Loop through the DataFrame in steps of 'batch_size'
    for i in range(0, len(df), batch_size):
        batch = " ".join(df[column_name].iloc[i:i + batch_size].dropna().tolist())
        batches.append(batch)

    return batches


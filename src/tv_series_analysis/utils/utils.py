import re

def extract_text_with_pattern(dialogue_line:str, pattern:str=r",,.*?,,(.*)"):
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
    Extracts the season and episode number from a file name.

    Args:
        file_name (str): The input file name string.

    Returns:
        tuple: A tuple containing the extracted season and episode numbers, or None if no match is found.
    """
    match = int(file_name.split('-')[-1].split('.')[0].strip())
    return match
"""
# Example usage
data_input = "Dialogue: 0,0:09:07.99,0:09:09.83,Default,,0000,0000,0000,,Wake up, Iruka Sensei!"
extracted_text = extract_text_with_pattern(data_input)
print(f"Extracted text: {extracted_text}")
# Example usage
filename = "Naruto Season 1 - 08.ass"
episode_number = extract_episode_number(filename)
print(f"Extracted episode number: {episode_number}")
"""
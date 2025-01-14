import json
from textwrap import indent

def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    filename=open(filename).read()

    data=json.loads(filename)  
    return data
print(get_data("randomuser_data.json"))

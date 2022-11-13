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

    s=json.loads(filename)['results']
    d=''
    for i in s:
        d+=str(i)
    m=json.dumps(d,indent=4)  
    return m

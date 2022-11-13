
import json

def get_email(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    

    s=json.loads(filename)['results']
    d=''
    for i in range(len(s)):
        d+=s[i].get('email')+'\n'
    return d[:-1]
data=open("randomuser_data.json").read()
print(get_data(data))
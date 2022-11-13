# import get_data
import json
def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """    
    filename=open(data).read()

    data=json.loads(filename)['results']  
    s=[]
    for i in data:
        s.append(i['email'])
    return s

print(get_email("randomuser_data.json"))

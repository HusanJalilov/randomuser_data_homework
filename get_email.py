import email
import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    s=data[results]
    m=[]
    for i in s:
        m.append(i['email'])
    return m
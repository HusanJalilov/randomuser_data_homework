import get_data

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    s=data['results']
    m=[]
    for i in s:
        m.append({"first_name":i['name']['first']})
        m.append({"last_name": i["name"]["last"]})
        m.append({"user":i["phone"]})
    return m
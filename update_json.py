import json
import logging

#Create and configure logger
logging.basicConfig(filename="update_json.log",
                    format='%(asctime)s %(name)s - %(levelname)s :: %(message)s ',
                    filemode='w',level=logging.DEBUG)

#Creating an object
log=logging.getLogger()


def get_data():
    """
    Read data from json file
    """
    with open("test_payload.json",'r') as fr:
        data = json.load(fr)

    log.debug(f"data from json :: {data}")
    return data


def find_remove_item(data:dict, remove_key:str) -> dict:
    """
    recursive function to find and remove the give item.
    :param data : dictionary
    :param remove_key : key to be removed
    :return : dictionary(updated)
    """
    if remove_key in data.keys():
        data.pop(remove_key)
        return data

    for key, value in data.items():
        if isinstance(value,dict):
            item = find_remove_item(value, remove_key)
            if item is not None:
                return data

def write_data(data):
    """
    write given data to a json file.
    :param data : dictionary
    :return : None 
    """
    with open('new_test_data.json',"w") as fw:
        json.dump(data,fw,indent=4)

if __name__ == "__main__":
    remove_param = input("Please enter a element to be removed from JSON : ")
    json_data = get_data()
    updated_data = find_remove_item(json_data, remove_param)
    if updated_data:
        log.debug(f"updated json is :: {updated_data}")
    else:
        log.debug(f"{remove_param} not found in given json data")
    write_data(updated_data)
    log.debug("End of script")

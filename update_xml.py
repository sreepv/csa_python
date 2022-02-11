from datetime import datetime
import xml.dom.minidom
from datetime import timedelta
import logging

#Create and configure logger
logging.basicConfig(filename="update_xml.log",
                    format='%(asctime)s %(name)s - %(levelname)s :: %(message)s ',
                    filemode='w',level=logging.DEBUG)

#Creating an object
log=logging.getLogger()

def update_data(add_depart:int,add_return:int) -> None:
    """
    Parse data from xml and update depart and retune values.
    :param add_depart : number of days to add to depart
    :param add_return : number of days to add  to return
    :return None
    """
    try:
        # Pass the path of the xml document
        xml_tree = xml.dom.minidom.parse('test_payload1.xml')


        depart  = xml_tree.getElementsByTagName("DEPART")[0]
        log.debug(f"depart data is :: {depart.firstChild.data}")
        new_depart_date = add_date(depart.firstChild.data,add_depart)
        xml_tree.getElementsByTagName("DEPART")[0].firstChild.nodeValue = new_depart_date

        ret  = xml_tree.getElementsByTagName("RETURN")[0]
        log.debug(f"return data is :: {ret.firstChild.data}")
        new_return_date = add_date(ret.firstChild.data,add_return)
        xml_tree.getElementsByTagName("RETURN")[0].firstChild.nodeValue = new_return_date

        with open('test_payload10.xml',"w") as fw:
            fw.write(xml_tree.toxml())
    except Exception as ex:
        log.exception(f"Exception occured in reading or updating XML :: {ex}")


def add_date(date_str:str, num_days:int) -> str:
    """
    for a given date string, covert it to date object and 
    add given number of days.
    :param date_str : date string read from xml file
    :param num_days :  number of days to add 
    :return date in string format
    """
    date_obj = datetime.strptime(date_str,"%Y%m%d")
    new_date = date_obj + timedelta(days=num_days)
    log.debug(f"new date after adding days :: {new_date}")
    return new_date.strftime("%Y%m%d")

if __name__ == "__main__":
    x_val = int(input("Please enter an Integer: "))
    y_val = int(input("Please enter an Integer: "))
    log.debug(f"Given x_val is  :: {x_val}")
    log.debug(f"Given y_val is  :: {y_val}")
    update_data(x_val,y_val)
    log.debug("End of script")
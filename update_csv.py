import csv
import pytz
from datetime import datetime
import logging

#Create and configure logger
logging.basicConfig(filename="update_csv.log",
                    format='%(asctime)s %(name)s - %(levelname)s :: %(message)s ',
                    filemode='w',level=logging.DEBUG)

#Creating an object
log=logging.getLogger()

def update_csv():
    """
    Reads data from file and extracts required part of data.
    :return : None
    """
    li = []
    with open("Jmeter_log1.jtl","r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            li.append(row)

    for each_item in li:
        if each_item['responseCode'] != '200':
            readable_timestamp = get_pacific_time(each_item["timeStamp"])
            log.debug(f"{readable_timestamp},{each_item['label']},{each_item['responseCode']},{each_item['responseMessage']}{each_item['failureMessage']}")


def get_pacific_time(timestamp:str):
    """
    for a given time stamp return date string in pacific time zone in human readable format.
    :param timestamp : timestamp read from csv file
    :return : date string in pacific time zone and readable format.
    """
    ts = int(timestamp)/1000
    tz = pytz.timezone('US/Pacific')
    pacific_timestamp = datetime.fromtimestamp(ts, tz).strftime('%Y-%m-%d %H:%M:%S')
    return pacific_timestamp

if __name__ == "__main__":
    update_csv()
    log.debug("End of script")

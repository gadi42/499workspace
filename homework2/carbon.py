#!/usr/bin/env python3

import urllib.request as req
import json
import time

def get_current_day (timestamp=()):
    """
    Returns the current date at the time of calling
    :param timestamp:
    :return:
    """
    timestamp =[]
    timestamp = time.time()
    return timestamp


def get_data (url = 'https://api.carbonintensity.org.uk/intensity/date/{date}'):
    # make a routine that does stuff?
    with req.urlopen(url) as source:
        data = json.loads(source.read().decode())
    return data

# def query_carbon (iso_date, use_cache = True.query_carbon):

if __name__ == '__main__':
    foo = get_data()

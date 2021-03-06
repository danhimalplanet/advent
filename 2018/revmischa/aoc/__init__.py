from logging import getLogger
import datetime
import boto3
import os


getLogger('flake8').propagate = False

# get current day
current_day = int(os.getenv("AOC_DAY", datetime.datetime.now().day))


# boto3 session
def get_boto_session():
    boto_session = boto3.session.Session(region_name='eu-central-1')
    return boto_session

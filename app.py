from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import datetime
from job import *

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', minute=2)
def scheduled_job():
    callUpdateApi()

sched.start()

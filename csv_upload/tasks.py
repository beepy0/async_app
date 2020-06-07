import csv, io
from celery import shared_task

from .models import User


@shared_task
def push_data_to_db(data):
    io_string = io.StringIO(data)
    for column in csv.reader(io_string, delimiter=','):
        # some email entries might be empty, we assume this to be a non-NULL field
        if column[1] == '':
            continue
        User.objects.get_or_create(email=column[1], defaults={'real_name': column[0]})

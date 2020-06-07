from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse

from .tasks import push_data_to_db


# Create your views here.
def index(request):
    return render(request, 'csv_upload/index.html')


def upload_csv(request):
    try:
        csv_file = request.FILES['file']
    except KeyError:
        return render(request, 'csv_upload/upload_error.html', context={'message': 'No file supplied'})

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please use a CSV file.')
        return render(request, 'csv_upload/index.html')

    try:
        csv_data = csv_file.read().decode('UTF-8')
    except Exception:
        return render(request, 'csv_upload/upload_error.html', context={'message': 'Invalid or broken CSV file'})
    else:
        push_data_to_db.delay(csv_data)
        return render(request, 'csv_upload/upload_success.html')

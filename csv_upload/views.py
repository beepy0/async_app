from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse

from .tasks import push_data_to_db


# Create your views here.
def index(request):
    return render(request, 'csv_upload/index.html')


def upload_csv(request):
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please use a CSV file.')
        return render(request, 'csv_upload/index.html')

    try:
        csv_data = csv_file.read().decode('UTF-8')
    except Exception:
        return HttpResponse('Invalid CSV file')
    else:
        push_data_to_db.delay(csv_data)
        return render(request, 'csv_upload/upload_success.html')

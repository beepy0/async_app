# async_app

### Prerequisites
- Python 3.6
- Pip
- RabbitMQ (can be changed to another service in the Celery settings)
- Run `pip install -r requirements.txt`


Currently uses SQLite but can be plugged to any DB.

### Start the services
- Start the Django server e.g. `python manage.py runserver`
- Start the Celery service e.g. `celery -A csv_upload worker -l info`

### Use the service
- Navigate to `http://127.0.0.1:8000/`

### Notes
- **App1** is the index page where a user can upload the CSV file. It will then check if the file is valid CSV 
and pass it to the message queue.
- **App2** is a Celery task that will async push the data to the DB if an e-mail is not already present. There are constraints
for this on database and form validation level so that there are no two users with the same email or an empty email.
Only possible way to bypass it is via direct Django API call through Python console.
- I haven't done async before and learned a ton so would like to thank you for the opportunity regardless.

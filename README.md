# async_app

A simple Django app to simulate distributed async upload of data. The app itself is found in `csv_upload`. `csv_upload.views.upload_csv` handles the transfer of data to a message queue. `csv_upload.tasks.push_data_to_db` processes the data and stores it to a DB in an async fashion.


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
- From my understanding Celery already allows for multiple processes/threads and does that automatically. The task can be deployed on different servers and only some additional routing is required to pass the data from the csv_upload view to it. 
- I did not use commenting unless strictly necessary and instead try to convey the meaning of the code with proper naming and code structure. For larger, more complex functions it could make more sense to add comments.
- I think the thing that is missing here for me is more context, which comes with real business projects, so in that case I would have talked with the team and worked to fit the code better to the codebase. Since I don't have that I decided to keep things minimal.
- I haven't done async before and learned a ton so would like to thank you for the opportunity regardless.

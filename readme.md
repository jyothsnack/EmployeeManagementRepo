# EmployeeManagementRepo
## Prerequisites
    python3.7
    redis

## Setup
    Open teminal and run the following commands
### Create virtual environment in python3.7
     virtualenv venv --python=python3.7
### Activate Virtual environment
     source venv/bin/activate
### Move to project direactory
     cd employee_management
### Install requirements
     pip install -r requirements.txt
### Migrate
     python manage.py migrate
### Create User
     python manage.py createsuperuser
### Run project
     python manage.py runserver
### Run celery(For weekly task report generation)
     Execute these commands in three different terminals
     1. redis-server
     2. celery -A employee_management worker -l info
     3. celery -A employee_management beat -l info
     
## API details
     Go to url - http://127.0.0.1:8000 and login using the user credentials to see the API details
     

  

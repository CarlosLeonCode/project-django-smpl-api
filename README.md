## Getting Started

First, setup virtual environment and activate

```shell
# Create
python3 -m venv venv

# Activate
source venv/bin/activate
```

Then, install packages from requirements.txt

```shell
pip install -r requirements.txt
```

Now, let's to connect to your Database following next steps:

1. Set your credencias into the .env file, look .env_example as guide.
2. Execute `python manage.py migrate`

Finally, let's to rise our server executing `python manage.py runserver` and type in your browser `http://localhost:8000/`

### Alternative Admin Section

We have an admin section that we can use.
Just execute the following: 

1. command `python manage.py createsuperuser` and type your credentials.
2. enter throught this url `http://localhost:8000/admin` and type your credentials that you joined in the previous step.

### Try Out the API
You can access to `http://localhost:8000/api/v1/` and check what endpoints exists and make CRUD operations.

## DEMO
In this demo we use **Postman**, we have the following request:
<img width="999" alt="Screenshot 2024-06-27 at 2 08 52 AM" src="https://github.com/CarlosLeonCode/project-django-smpl-api/assets/40130036/6136604f-04c9-4b3a-8d46-0adc08380595">
and we have the following response:
<img width="999" alt="Screenshot 2024-06-27 at 2 09 34 AM" src="https://github.com/CarlosLeonCode/project-django-smpl-api/assets/40130036/adf19c52-028c-4a71-b861-03b5bfdcc752">

### Checking Database
If we chake our database, the `api_movie` and `api_rating` filled with the previous data. 

#### api_movie table
<img width="1191" alt="Screenshot 2024-06-27 at 2 13 17 AM" src="https://github.com/CarlosLeonCode/project-django-smpl-api/assets/40130036/33112d0c-1577-4ff3-9b86-5229309e1b18">

#### api_rating table
<img width="515" alt="Screenshot 2024-06-27 at 2 14 21 AM" src="https://github.com/CarlosLeonCode/project-django-smpl-api/assets/40130036/c7956850-ce55-4431-a2d4-41fc46e2a940">


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


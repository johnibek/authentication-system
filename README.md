# Installation guide
## Description
### This is a simple authentication / authorization system built using django rest framework

## Setup
### Create virtual env

```shell
python3 -m venv venv
```

### Activate it

`For Mac/Linux users`
```shell
source venv/bin/activate
```

`For windows users`
```shell
.venv\Scripts\activate
```

### Install requirements
```shell
pip install -r requirements.txt
```

### Create .env file in where your manage.py file resides. And put your environment variables into this file like this.
```dotenv
# Django settings
SECRET_KEY=SECRET_KEY
DEBUG=True

# Database settings
DB_ENGINE=django.db.backends.postgresql
DB_NAME=DB_NAME
DB_USER=DB_USER
DB_PASSWORD=DB_PASSWORD
DB_HOST=localhost
DB_PORT=5432
```

### Run migrations
```shell
./manage.py migrate
```

### Start the server
```shell
./manage.py runserver
```

### Open swagger documentation
http://127.0.0.1:8000/swagger/

Now you are ready to try the endpoints. Good luck :)
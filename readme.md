# **Steps Installation**


### 1. Virtual Environment Activate
```
venv\Scripts\activate
```

### 2. Install requirements.txt
```
pip install -r /path/to/requirements.txt
```

### 3. Make Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 4. Migrate Error codes

```
python manage.py makeerrors
``` 

### 5. Create Super User

```
python manage.py createsuperuser
# 🎁 About SCIdrop
Simple website made with Django and Vue frameworks. It implements opening chests with customisable skins. Everything works on the user's account balance based on the real currency.

# ⚙️ Setup guide
<b>Install necessary libraries (Pillow, Django)</b>
```
> pip install -r requirements.txt
```

<b>Start instructions</b>
```
> python manage.py makemigrations
> python manage.py migrate
```

<b>If you want to start with example 2 chests, type:</b>
```
> python manage.py loaddata app/fixtures/example_chests.json
```
and unzip ```media.zip``` file into media folder

<b>To run frontend and backend, type this in different terminals:</b>
```
> python manage.py runserver
> npm run dev
```

And go to ```localhost:8000```


# 💻 Used technologies
<b>🖼️ Frontend:</b>
- HTML
- CSS
- JavaScript with Vue

<b>🔧 Backend:</b>
- Python with Django
- SQLite
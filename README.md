# ❗ PROJECT IS NOT FINISHED YET!
To-do list:
- [ ] user balance
- [ ] roulette logic

# 🎁 About SCIdrop
Simple website made with Django and Vue frameworks. It implements opening chests with customisable skins. Everything works on the user's account balance based on the real currency.

# ⚙️ Setup guide
<b>Install necessary libraries (Pillow, Django)</b>
```
> pip install -r requirements.txt
```
<b>Install frontend dependencies</b>
```
> npm install frontend
```

<b>Start instructions</b>
```
> python manage.py makemigrations backend

or (if above not works):
> python manage.py makemigrations

then:
> python manage.py migrate
```

<b>If you want to start with example 2 chests, type:</b>
```
> python manage.py loaddata example_chests.json
```
and unzip ```media.zip``` file into media folder

<b>To run frontend and backend, type this in different terminals:</b>
```
> python manage.py runserver
> npm run dev
```

And go to ```localhost:5173```


# 💻 Used technologies
<b>🖼️ Frontend:</b>
- HTML
- CSS
- JavaScript with Vue

<b>🔧 Backend:</b>
- Python with Django
- SQLite
# 🎁 About SCIdrop
Simple website made with Django and Vue frameworks. It implements opening chests with customisable skins. Everything works on the user's account balance based on the real currency.


### 🎥 Here you can watch [video presenting the website](https://youtu.be/tjasRk32dJI)
# ⚙️ Setup guide:
### The best way to start is to open two different terminals - one for backend commands, and another one for frontend

### ❗You need to have **Python3** and **NPM package manager**  installed 

### 🔧 Backend:
<b>1. Install necessary libraries (Pillow, Django):</b>
```
> pip install -r requirements.txt
```

<b>2. Migrate to create database:</b>
```
> python manage.py makemigrations backend
```
or (if above returned anything):
```
> python manage.py makemigrations
```
then:
```
> python manage.py migrate
```

<b>3. If you want to start with two example chests, type:</b>
```
> python manage.py loaddata example_chests.json
```
and unzip ```media.zip``` file in to the media folder. Hierarchy should look like this:
<br>
```SCIdrop/media/chestCovers``` and ```SCIdrop/media/skinCovers```

<b> 4. To run backend API:</b>
```
> python manage.py runserver
```

### 🖼️ Frontend:
<b>1. Install all dependencies</b>
```
> cd frontend
> npm install
```
<b>2. To run frontend:</b>
```
> npm run dev
```

### To start, go in the browser to <b>```localhost:5173```</b>


# 💻 Used technologies
<b>Frontend:</b>
- HTML
- CSS
- JavaScript (with Vue, Vite and Axios)

<b>Backend:</b>
- Python (with Django and Pillow)
- SQLite3

### 🎨 All drawings in media folder were made by Mewash
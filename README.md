# 🎁 About SCIdrop
Simple website made with Django and Vue frameworks. It contains openable chests with custom items (e.g. skins for the SCImulator game). Everything works on the user's account balance based on the real currency.

<img width="1932" height="1088" alt="image" src="https://github.com/user-attachments/assets/28f06f41-4a42-48de-943c-df093f1c6d5b" />

### 🎥 Here you can watch [video presenting the website](https://youtu.be/tjasRk32dJI)<br><br>
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

<b> 4. To run a backend API:</b>
```
> python manage.py runserver
```

### 🖼️ Frontend:
<b>1. Install dependencies</b>
```
> cd frontend
> npm install
```
<b>2. To run a frontend:</b>
```
> npm run dev
```

### To start, go to <b>```localhost:5173```</b><br><br>


# 💻 Used technologies
<b>Frontend:</b>
- HTML
- CSS
- JavaScript (with Vue, Vite and Axios)

<b>Backend:</b>
- Python (with Django and Pillow)
- SQLite3

### 🎨 All of the drawings in the media folder were made by Mewash

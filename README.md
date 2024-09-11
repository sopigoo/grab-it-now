# Grab It Now! (Tugas Individu PBP)

Nama : Siti Shofi Nadhifa

NPM : 2306152172

Kelas : PBP D

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat proyek Django baru
- Membuat direktori baru bernama `grab-it-now` yang akan dijadikan direktori lokal dari repository yang akan dibuat di github.
- Membuka direktori `grab-it-now` pada terminal lalu membuat sebuah virtual environment baru dengan perintah `python3 -m venv env`.
- Mengaktifkan virtual environment dengan perintah `source env/bin/activate`.
- Membuat berkas `requirements.txt` dan mengisinya dengan beberapa dependencies yang akan dibutuhkan pada proyek ini.
```bash
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
- Menjalankan perintah `pip install -r requirements.txt` untuk melakukan instalasi terhadap dependencies yang sudah dituliskan pada berkas `requirements.txt` sebelumnya.
- Menjalankan perintah `django-admin startproject grab_it_now .` untuk membuat proyek Django bernama `grab_it_now`.
- Menambahkan daftar host pada `ALLOWED_HOSTS` di `settings.py` dengan local host dan pws untuk keperluan deployment
```python
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "siti-shofi-grabitnow.pbp.cs.ui.ac.id"]
```
- Menambahkan file `.gitignore` dan diisi dengan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git.
```
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml
.DS_Store

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod]
*$py.class

# Distribution / packaging
.Python build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
.pytest_cache/
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery
celerybeat-schedule.*

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# mkdocs documentation
/site

# mypy
.mypy_cache/

# Sublime Text
*.tmlanguage.cache
*.tmPreferences.cache
*.stTheme.cache
*.sublime-workspace
*.sublime-project

# sftp configuration file
sftp-config.json

# Package control specific files Package
Control.last-run
Control.ca-list
Control.ca-bundle
Control.system-ca-bundle
GitHub.sublime-settings

# Visual Studio Code
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
.history
```

2. Membuat aplikasi `main`
- Menjalankan perintah `python3 manage.py startapp main` untuk membuat aplikasi baru bernama `main`
- Menambahkan aplikasi `main` pada `INSTALLED_APPS` di `settings.py`
- Membuat model pada aplikasi `main` bernama `Product` dengan attributes yang diperlukan.
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
```
- Migrasi model dengan menjalankan perintah `python3 manage.py makemigrations` kemudian jalankan perintah `python3 manage.py migrate` untuk menerapkan migrasi ke basis data lokal.
- Buka berkas `views.py`, import fungsi render, dan definisikan fungsi `show_main` dengan dictionary `context` berisi data untuk dikirimkan ke tampilan. Render tampilan pada `main.html` dengan menggunakan fungsi `render`.
- Buat sebuah direktori `templates` pada aplikasi `main`.
- Buat sebuah berkas baru bernama `main.html` pada berkas `templates` untuk menampilkan data yang telah diambil dari `model`.
- Tambahkan routing `show_main` pada berkas `urls.py` dalam direktori aplikasi `main`.
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

3. Push project ke GitHub
- Membuat sebuah public repository bernama `grab-it-now`.
- Lakukan inisiasi dan push repositori lokal ke GitHub
```bash
git init
git add -A
git commit -m "Initial Commit"
git branch -M main
git remote add origin https://github.com/sopigoo/grab-it-now.git
git push -u origin main
```

4. Deploy project ke PWS
- Akses halaman PWS pada https://pbp.cs.ui.ac.id lalu login dengan akun yang sudah dibuat.
- Membuat proyek baru dengan cara menekan tombol `Create New Project`.
- Mengisi `Project Name` dengan `grabitnow`, lalu menekan tombol `Create New Project`.
- Menambahkan url deployment PWS pada `ALLOWED_HOSTS` di `settings.py`.
```python
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "siti-shofi-grabitnow.pbp.cs.ui.ac.id"]
```
- Menjalankan perintah-perintah yang ada pada informasi `Project Command` pada PWS. Ganti perintah `git remote add pws <link>` menjadi `git remote set-url pws <link>` jika sebelumnya sudah pernah membuat projek pada PWS.
- Menjalankan perintah `git branch -M main` untuk kembali mengubah branch utama menjadi `main`.
- Menggunakan perintah `git push pws main::master` untuk melakukan push pada setiap perubahan yang dilakukan.

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![User Request Flow](grab-it-now/images/user_request_flow.png)
Kaitan antara urls.py, views.py, models.py, dan berkas html:
- Ketika user/client pertama kali mengirim request, Django akan memeriksa `urls.py` untuk mencocokkan URL yang diminta dengan yang terdaftar. `urls.py` sendiri bertugas untuk memetakan URL ke fungsi atau class di `views.py`.
- Apabila URL yang diminta cocok degan yang ada pada `urls.py`, Django akan menjalankan fungsi `show_main` pada `views.py`.
- Jika diperlukan data dari database, view akan mengakses `models.py`. `models.py` berisi definisi dari model-model databse.
- Setelah data selesai diproses, view akan melakukan rendering template html dan memberikan respon pada request client.

## 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah sistem kontrol versi terdistribusi yang dirancang untuk melacak dan mengelola perubahan pada source code selama pengembangan perangkat lunak. Beberapa fungsi Git dalam pengembangan perangkat lunak meliputi:
- Version control: memudahkan pengembang untuk melacak perubahan yang terjadi dari waktu ke waktu.
- Kolaborasi: memudahkan kolaborasi antar pengembang karena setiap pengembang dan bekerja secara paralel dan semua perubahan pada kode direkam dan dikelola secara terpusat.
- Branching: memungkinkan adanya percabangan dari proyek utama, sehingga pengembang dapat fokus mengerjakan suatu fitur btanpa mengganggu kode utama. Cabang ini kemudian bisa di-merge dengan kode utama setelah selesai dikerjakan.

## 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django cocok dijadikan permulaan pembelajaran pengembangan perangkat lunak karena Django menyediakan banyak fitur bawaan yang mempermudah pengembangan aplikasi web. Django juga menggunakan filosofi "batteries included" yang berarti menyediakan banyak fitur dan fungsi penting bawaan. Hal ini tentu saja memudahkan pemula karena bisa fokus pada pengembangan perangkat lunaknya tanpa perlu menyiapkan dan mengonfigurasi hal-hal yang dibutuhkan untuk pengembangan. Selain itu, Django juga memiliki dokumentasi yang lengkap dan sangat baik, sehingga memudahkan pemula dalam mempelajari dan memahami framework ini.

## 5. Mengapa model pada Django disebut sebagai ORM?
Orbject-relational mapping (ORM) adalah teknik pemrograman yang mengonversi atau menghubungkan sistem basis data relasional dengan sistem berbasis objek seperti object-oriented programming.
Model pada Django disebut sebagai ORM karena memiliki cara kerja dengan menghubungkan atau memetakan objek-objek pada Python ke struktur data basis rasional. ORM ini memungkinkan pengembang/developers untuk berinteraksi dengan basis data relasional menggunakan model berorientasi objek tingkat tinggi (model objek Python), tanpa perlu menulis kueri SQL secara langsung.
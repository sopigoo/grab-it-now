# Grab It Now! (Tugas Individu PBP)

Deployed at: http://siti-shofi-grabitnow.pbp.cs.ui.ac.id

Nama : Siti Shofi Nadhifa
<br>
NPM : 2306152172
<br>
Kelas : PBP D

<details>
<summary>Tugas 3</summary>

## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dalam pengimplementasian sebuah platform diperlukan untuk mengirimkan dan menerima informasi antara komponen yang berbeda, seperti user dan server, atau server dan database. Dengan interaksi yang dinamis dan langsung/real-time pada platform, pengguna bisa mendapatkan data yang relevan dan sistem bisa merespons permintaan dari pengguna. Dalam web, data delivery digunakan seperti ketika pengguna mengisi form atau menerima data yang ditampilkan.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik dari XML karena beberapa alasan, yaitu:
- Lebih ringan:
JSON memiliki struktur yang lebih ringkas dan memiliki ukuran file yang lebih kecil dibandingkan dengan XML, sehingga proses pengiriman data lebih cepat dan mengurangi bandwidth yang dibutuhkan.
- Lebih gampang dibaca:
Sintaks JSON lebih lebih sederhana dan lebih mudah dibaca oleh manusia dibanding sintaks XML yang menggunakan banyak tag dan membutuhkan referensi entitas untuk beberapa karakter, sehingga lebih sulit untuk dibaca. 
- Lebih mudah diuraikan:
Penguraian (parsing) data pada JSON cepat dan efisien sedangkan XML membutuhkan lebih banyak langkah karena strukturnya yang lebih kompleks, sehingga JSON lebih cocok untuk menangani data dengan volume yang besar.
- Integrasi langsung dengan JavaScript:
JSON dipetakan langsung ke objek JavaScript tanpa konversi yang rumit, sehingga integrasi dengan aplikasi dan API JavaScript dapat lebih lancar.

## 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Pada form Django, method `is_valid()` digunakan untuk memeriksa apakah data yang dikirimkan oleh user sesuai dengan aturan validasi yang sudah ditetapkan untuk setiap field pada form sesuai dengan field pada model. Pengecekan ini dibutuhkan agar kita dapat menjaga kualitas data dengan memastikan bahwa data yang disimpan hanya data yang valid dan meningkatkan keamanan dengan mencegah pengiriman data yang tidak sesuai atau berbahaya. Selain itu, dengan penggunaan method `is_valid()`, kita juga dapat memberikan umpan balik jika terjadi kesalahan pengisian data pada form oleh user, sehingga user bisa memperbaiki input yang diberikan.

## 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` dibutuhkan untuk mencegah serangan CSRF, di mana penyerang mencoba membuat pengguna sah melakukan hal yang tidak diinginkan. `csrf_token` diperiksa oleh server untuk memverifikasi bahwa permintaan atau pengisian data pada form dikirim oleh pengguna yang sah atau diautentikasi, bukan dari sumber yang berbahaya. Tanpa adanya `csrf_token`, situs akan menjadi rentan terhadap serangan CSRF, di mana penyerang dapat membuat skrip berbahaya yang dapat membuat user melakukan tindakan yang tidak mereka sadari, seperti mengirim permintaan ke server yang terlihat sah namun sebenarnya berbahaya.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat kerangka views
- Membuat direktori `templates` pada direktori utama `grab-it-now`, kemudian membuat sebuah berkas baru bernama `base.html`.
- Mengisi berkas `base.html` sebagai berikut:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
Tag `{% block %}` digunakan untuk mendefinisikan struktur dasar lalu kemudian mewarisi template nya. Nantinya template turunan dapat meng-extend template dasar tersebut dan mengisinya sesuai dengan kebutuhan.
Tag `{% load static %}` memungkinkan untuk menyertakan file statis pada template.
- Menambahkan path `templates` pada variabel `TEMPLATES` di `settings.py` yang menangani rendering template, sehingga Django dapat menemukan dan menggunakan berkas yang ada pada direktori templates untuk struktur halaman situs.
```python
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
...
```
- Menggunakan `base.html` sebagai template utama dengan mengubah isi pada `main.html` pada direktori `main/templates/`
```html
{% extends 'base.html' %}
{% block content %}
<h1>Grab It Now!</h1>
...
{% endblock content %}
```
`{% extends 'base.html' %}` menandakan bahwa saya menggunakan `base.html` sebagai template utama.

2. Mengubah Primary Key menjadi UUID
- Melakukan import uuid dan mendefinisikan field id sebagai UUID yang menjadi primary key untuk model Product
```python
import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
```
UUID membuat string unik (random objek) yang digunakan sebagai identifier untuk objek pada database.
- Migrasi model dengan menjalankan perintah:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

3. Membuat Form Input Data dan Menampilkan Data pada HTML
- Membuat berkas `forms.py` pada direktori `main` untuk membuat struktur form yang menerima Product baru.
```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock", "category", "rating"]
```
- Menambahkan import `redirect` pada berkas `views.py` yang ada di direktori `main`
```python
from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
```
`redirect` mengarahkan pengguna ke URL tertentu setelah melakukan suatu tindakan.
- Menambahkan fungsi `add_product` pada berkas `views.py` di direktori `main` yang menerima parameter `request`. Fungsi ini digunakan untuk menghasilkan form yang dapat menambahkan data Product ke database secara otomatis ketika data yang ada pada form di-submit.
```python
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)
```
- Mengubah fungsi `show_main` pada berkas `views.py` menjadi seperti berikut:
```python
def show_main(request):
    product_entries = Product.objects.all()

    context = {
        'nama': 'Siti Shofi Nadhifa',
        'npm': '2306152172',
        'class': 'PBP D',
        'products': product_entries
    }

    return render(request, "main.html", context)
```
- Menambahkan import dan path URL ke fungsi `add_product` pada berkas `urls.py` di direktori `main`
```python
from django.urls import path
from main.views import show_main, add_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product', add_product, name='add_product'),
]
```
- Membuat berkas HTML baru pada direktori `main/templates` dengan nama `add_product.html`
```html
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
- Menambahkan kode untuk menampilkan product dalam `{% block content %}` pada berkas `main.html` yang ada di direktori `main/templates`
```html
{% extends 'base.html' %}
{% block content %}
<h1>Grab It Now!</h1>
...
<h2>List Produk</h2>

{% if not products %}
<p>Belum ada data produk pada Grab It Now!.</p>
{% else %}
<table>
  <tr>
    <th>Nama Produk</th>
    <th>Harga</th>
    <th>Deskripsi</th>
    <th>Stok</th>
    <th>Kategori</th>
    <th>Rating</th>
  </tr>

  {% for product in products %}
  <tr>
    <td>{{product.name}}</td>
    <td>{{product.price}}</td>
    <td>{{product.description}}</td>
    <td>{{product.stock}}</td>
    <td>{{product.category}}</td>
    <td>{{product.rating}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:add_product' %}">
  <button>Add New Product</button>
</a>
{% endblock content %}
```
- Menjalankan proyek Django dengan perintah `python3 manage.py runserver` untuk melakukan pengecekan web yang saya buat pada `http://localhost:8000/`

4. Mengembalikan data dalam bentuk XML
- Menambahkan import `HttpResponse` dan `Serializer` pada berkas `views.py` di direktori `main`
```python
from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
```
- Membuat sebuah fungsi baru dengan nama `show_xml`, membuat variabel `data` untuk menyimpan hasil query dari data pada Product, serta menambahkan return function `HttpResponse` yang berisi data hasil query yang sudah diserialisasi menjadi XML menggunakan `serializers` dan parameter `content_type="application/xml"`
```python
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
- Menambahkan import dan path URL ke fungsi `show_xml` pada berkas `urls.py` di direktori `main`
```python
from django.urls import path
from main.views import show_main, add_product, show_xml

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'),
]
```

5. Mengembalikan data dalam bentuk JSON
- Membuat sebuah fungsi baru dengan nama `show_json`, membuat variabel `data` untuk menyimpan hasil query dari data pada Product, serta menambahkan return function `HttpResponse` yang berisi data hasil query yang sudah diserialisasi menjadi JSON menggunakan `serializers` dan parameter `content_type="application/json"`
```python
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- Menambahkan import dan path URL ke fungsi `show_json` pada berkas `urls.py` di direktori `main`
```python
from django.urls import path
from main.views import show_main, add_product, show_xml, show_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]
```

6. Mengembalikan data berdasaekan ID dalam bentuk XML dan JSON
- Membuat dua fungsi baru, yaitu `show_xml_by_id` dan `show_json_by_id` yang menerima parameter `request` dan `id` pada berkas `views.py` di direktori `main`
- Menambahkan variabel `data` yang menyimpan hasil query dari data dengan id tertentu pada `Product`
```python
data = Product.objects.filter(pk=id)
```
- Menambahkan return function `HttpResponse` yang berisi data hasil query yang sudah diserialisasi menjadi XML dan JSON menggunakan `serializers` dan parameter `content_type="application/xml"`untuk XML dan `content_type="application/json"`untuk JSON
XML:
```python
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
JSON:
```python
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- Menambahkan import dan path ke URL fungsi `show_xml_by_id` dan `show_json_by_id` pada berkas `urls.py` di direktori `main`
```python
from django.urls import path
from main.views import show_main, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

7. (Tambahan) Menambahkan fungsi untuk menghapus produk
- Menambahkan import `get_object_or_404` pada berkas `views.py` di direktori `main` untuk mendapatkan objek dari database dengan parameter tertentu
```python
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
```
- Membuat fungsi baru bernama `delete_project` yang menerima parameter `request` dan `id` pada berkas `views.py` di direktori `main`
```python
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('main:show_main')
```
- Menambahkan import dan path ke URL fungsi `delete_project` pada berkas `urls.py` di direktori `main`
```python
from django.urls import path
from main.views import show_main, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id, delete_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('delete-product/<uuid:id>/', delete_product, name='delete_product'),
]
```
- Menambahkan kode untuk menghapus product dalam `{% block content %}` pada berkas `main.html` yang ada di direktori `main/templates`
```html
...
{% if not products %}
<p>Belum ada data produk pada Grab It Now!.</p>
{% else %}
<table>
  <tr>
    <th>Nama Produk</th>
    <th>Harga</th>
    <th>Deskripsi</th>
    <th>Stok</th>
    <th>Kategori</th>
    <th>Rating</th>
    <th>Aksi</th>
  </tr>

  {% for product in products %}
  <tr>
    <td>{{product.name}}</td>
    <td>{{product.price}}</td>
    <td>{{product.description}}</td>
    <td>{{product.stock}}</td>
    <td>{{product.category}}</td>
    <td>{{product.rating}}</td>
    <td>
        <a href="{% url 'main:delete_product' product.id %}">
          <button>Delete</button>
        </a>
      </td>
  </tr>
  {% endfor %}
</table>
{% endif %}
...
```

## Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.
`http://localhost:8000/xml/`
![/xml/](/images/xml.png)

`http://localhost:8000/xml/[id]`
![/xml_by_id/](/images/xml_by_id.png)

`http://localhost:8000/json/`
![/json/](/images/json.png)

`http://localhost:8000/json/[id]`
![/json_by_id/](/images/json_by_id.png)

</details>

<details>
<summary>Tugas 2</summary>

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
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "siti-shofi-grabitnow1.pbp.cs.ui.ac.id"]
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
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "siti-shofi-grabitnow1.pbp.cs.ui.ac.id"]
```
- Menjalankan perintah-perintah yang ada pada informasi `Project Command` pada PWS. Ganti perintah `git remote add pws <link>` menjadi `git remote set-url pws <link>` jika sebelumnya sudah pernah membuat projek pada PWS.
- Menjalankan perintah `git branch -M main` untuk kembali mengubah branch utama menjadi `main`.
- Menggunakan perintah `git push pws main::master` untuk melakukan push pada setiap perubahan yang dilakukan.

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![User Request Flow](/images/user_request_flow.png)

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
</details>
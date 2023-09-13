# Tugas 2
Untuk Tugas 2 PBP, saya membuat aplikasi *inventory* bertemakan sebuah tas. Aplikasi berjudul *My Bag* dapat dilihat pada [link ini](https://my-bag.adaptable.app/).

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Membuat sebuah proyek Django baru.

    Sebelum membuat proyek Django, ada beberapa hal yang perlu dipersiapkan terlebih dahulu. Pertama, saya membuat sebuah direktori baru, yang saya namakan `pbp-assignment`. Kemudian saya buat sebuah *virtual environment* dengam menjalankan perintah `python -m venv env` pada terminal dan mengaktifkannya dengan perintah `env\Scripts\activate.bat`.
    
    Lalu dalam direktori yang sama saya buat kumpulan *dependencies* dalam suatu *Text Document* . *Dependencies* tersebut yaitu

    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```

    Kembali lagi ke terminal yang sudah diaktifkan *virtual environment*, saya jalankan perintah `pip install -r requirements.txt` untuk menginstall semua *dependencies*-nya. 
    
    Setelah itu baru saya membuat proyek Django dengan nama `pbp_assignment` dengan menjalankan perintah 

    ```
    django-admin startproject pbp_assignment .
    ```

    setelah perintah dijalankan, akan muncul direktori proyek dalam direktori utama serta berkas-berkas yang diperlukan proyek.

    Untuk memastikan proyek bekerja dengan baik, dijalankan server Django dengan perintah `python manage.py runserver` dan membuka http://localhost:8000, karena ada animasi roket maka aplikasi berhasil dibuat.

    Sebelum melanjutkan pembuatan aplikasi, saya menginisiasi direktori utama dan mengubahnya menjadi suatu repositori Git. Setelah itu, saya sambugkan repositori lokal ini dengan repositori baru pada GitHub.

- Membuat aplikasi dengan nama main pada proyek tersebut.

    Dalam direktori utama, saya buka terminal dan menjalankan virtual environment. Lalu saya jalankan perintah
    ```
    python manage.py startapp main
    ```

    akan muncul subdirektori baru dengan nama main berisi file-file yang diperlukan aplikasi. Setelah itu saya daftarkan aplikasi main dalam direktori proyek, dengan menambahkan `'main'` pada list `INSTALLED_APPS` di berkas settings.py.

    Kemudian saya buat subdirektori baru, yaitu templates, dalam direktori aplikasi main. Di dalam subdirektori tersebut saya buat sebuah berkas HTML bernama main.html yang akan digunakan nantinya.

- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

    Routing dilakukan dengan mengimpor fungsi include dan menambahkan rute URL pada list yang disediakan.
    ```
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls'))
    ]
    ```
    untuk melihat aplikasi, dapat dijalankan perintah  `python manage.py runserver` pada *virtual environment* dan membuka  http://localhost:8000

- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    - name sebagai nama item dengan tipe CharField.
    - amount sebagai jumlah item dengan tipe IntegerField.
    - description sebagai deskripsi item dengan tipe TextField.
    
    Pada direktori main terdapat berkas models.py. Dalam berkas tersebut saya tambahkan suatu model bernama `Item` dengan atribut yang diperlukan.
    ```
    class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    ```
    setelah itu saya migrasi model ini untuk mengubah struktur tabel basis data dengan menjalankan perintah
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

    Pada views.py saya impor fungsi render untuk me-render file HTML serta menambahkan fungsi `show_main` sebagai berikut

    ```
    from django.shortcuts import render

    def show_main(request):
        context = {
            'nama_aplikasi': "My Bag",
            'nama': "Puti Raissa",
            'kelas': "PBP E"
        }

        return render(request, "main.html", context)
    ```
    Fungsi tersebut akan mengembalikan suatu *dictionary* ke template HTML sehingga key dari dictionary tersebut dapat bertindak menyerupai sebuah variabel dan dapat digunakan seperti demikian,
    ```
    <body>
        <h1>{{nama_aplikasi}}</h1>
        <h4>{{nama}}</h4>
        <h4>{{kelas}}</h4>
    </body>
    ```

- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    
    Routing pada urls.py aplikasi main dijalankan dengan menulis kode berikut

    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

    fungsi `show_main` yang sudah diimpor dari views.py akan menjadi tampilan ketika URL diakses.

- Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet

    Setelah aplikasi jadi dilakukan deployment dengan cara memilih `NEW APP` dan menyambungkannya ke repositori yang ada pada GitHub.

    Pilih branch master, template *Python App Template*, *PostgreSQL*, lalu sesuaikan versi *python* menjadi 3.10 dan memasukkan *Start Command* `python manage.py migrate && gunicorn pbp_assignment.wsgi`

    Terakhir, centang bagian `HTTP Listener on PORT` dan *deploy app*. Aplikasi pun berhasil dideploy. :D

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan](bagan.jpg)

Ketika *browser/user* melakukan *request* ke URL, dicek pada `urls.py` dan memanggil *view* yang sesuai dengan URL. *View* yang terletak pada `views.py` kemudian mengecek model yang sesuai dan diambil dari `models.py`. Lalu `views.py` mengembalikan data dari model ke *template* HTML. Data dimasukkan ke `main.html` dan setelah itu web dikembalikan sebagai respons untuk *browser/user*.

### Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

*Virtual environment* digunakan untuk membentuk suatu lingkungan baru yang terpisah dan terisolasi untuk proyek python. Hal ini dilakukan untuk mengelola *dependencies*, menghindari konflik antar versi aplikasi, memastikan kompabilitas, dan menjaga lingkungan pengembangan aplikasi tetap teratur.

Pembuatan aplikasi Django tanpa menggunakan virtual environment masih memungkinkan tetapi tidak direkomendasikan. Karena adanya kemungkinan muncul masalah/error. 

### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya

**MVC** (Model View Controller)

Aplikasi dipisah menjadi tiga komponen:

- Model

    Model mendefinisikan object ke dalam tabel database dan mengatur relasi antar object. 

- View

    View mengatur tampilan antarmuka pengguna dan cara data dari Model ditampilkan kepada pengguna.

- Controller

    Controller menjadi penghubung model dan view serta mengatur alur kontrol dalam aplikasi dan menangani permintaan dari pengguna.

**MVT** (Model View Template)

Aplikasi dipisah menjadi tiga komponen:

- Model

    Model bertanggung jawab untuk mengelola data dan melakukan operasi terhadap data tersebut. 

- View

    View mengatur logika dan alur program serta data yang dikirimkan oleh pengguna ke dalam database maupun dari database ke pengguna.

- Template

    Template menampilkan halaman website ke user yang diproses lewat browser.

**MVVM** (Model View ViewModel)

MVVM berfokus pada pemisahan antara kode untuk logika bisnis dan tampilan aplikasi. Aplikasi dipisah menjadi tiga komponen:

- Model

    Model mengelola data yang digunakan untuk logika bisnis. 

- View

    View mengatur tampilan aplikasi (UI). View hanya menampilkan data yang diberikan oleh ViewModel dan mengirimkan tindakan pengguna ke ViewModel

- ViewModel

    ViewModel menjadi perantara antara Model dan View. ViewModel mengambil data dari model dan diteruskan ke view.

Perbedaan utama terletak pada hubungan antara komponen. Pada MVC Controller bertindak sebagai penghubung antara Model dan View. Sementara itu, MVT adalah perkembangan dari MVC yang lebih erat menghubungkan Model dan View dan menggunakan Template untuk merender tampilan. Di sisi lain, MVVM memisahkan Model, View, dan ViewModel, dengan ViewModel berperan sebagai perantara antara Model dan View.
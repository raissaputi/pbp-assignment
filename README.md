# Tugas Individu PBP

Proyek Django *Inventory* - __My Bag__

Puti Raissa - 2206830391 - PBP E

## Tugas 3

### Apa perbedaan antara form POST dan form GET dalam Django?

Form POST dalam Django merupakan *method* HTTP yang mengembalikan *form login* Django. Secara sederhana, browser mengemas data dari *form*, mengenkripsinya untuk pengiriman, mengirimkannya ke server dan menerima responsnya kembali. Sebaliknya, form GET adalah suatu *method* HTTP yang mengemas data ke dalam sebuah *string*, dan menggunakannya untuk menyusun URL. URL tersebut berisi alamat tempat data harus dikirimkan, serta *keys* dan *value* data.

Perbedaan yang signifikan antara keduanya terdapat dalam keamanannya. 

|POST|GET|
|:---|:--|
|Nilai variabel tidak ditampilkan di URL|Nilai variabel ditampilkan di URL|
|Lebih Aman|Tidak seaman POST|
|Biasa digunakan untuk *request* yang membuat perubahan dalam basis data|Digunakan untuk *request* yang tidak memengaruhi sistem|

### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

__XML__ (Extensible Markup Language) adalah bahasa markup serbaguna yang dirancang terutama untuk menyimpan, mengirimkan, dan mengatur data. XML menawarkan fleksibilitas dengan menggunakan tag dan atribut yang dibuat user untuk merepresentasikan data. Dokumen XML terstruktur secara hierarkis, membentuk struktur dengan elemen yang bersarang. XML digunakan secara luas dalam skenario pertukaran data, file konfigurasi, dan merepresentasikan informasi terstruktur di berbagai domain.

__JSON__ (JavaScript Object Notation) merepresentasikan data dengan format sederhana yang mudah dibaca mesin dan manusia. Data disajikan dalam pasangan *key-value* di dalam suatu *array*. JSON banyak digunakan untuk mentransmisikan data antara server dan klien, terutama dalam aplikasi web. Secara keseluruhan, JSON lebih sederhana dan efisien.

__HTML__ (HyperText Markup Language) mempunyai tujuan yang sepenuhnya berbeda dibandingkan XML dan JSON. HTML fokus pada pembuatan dokumen terstruktur untuk web, seperti halaman web. Ini mendefinisikan tata letak, konten, dan visual halaman web, mencakup elemen seperti judul, paragraf, daftar, tautan, dan komponen multimedia. Dokumen HTML menggunakan elemen-elemen yang telah ditentukan sebelumnya yang dikelilingi oleh tag. Penggunaan utama HTML adalah dalam pengembangan web yang memungkinkan pembuatan *interface* web yang *user-friendly* dan interaktif.

### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena lebih ringkas dan padat, sehingga lebih cepat dalam parsing dan generasi. Ini mengurangi ukuran dan bandwidth transfer data, serta meningkatkan kinerja dan efisiensi pemrosesan data. JSON juga mudah dibaca oleh manusia dan mesin, sehingga memudahkan pemeliharaan kode. JSON juga sangat kompatibel dengan aplikasi/teknologi web, sehingga mudah untuk mengembangkan serta mengintegrasikan aplikasi web dan API.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Membuat input form untuk menambahkan objek model pada app sebelumnya.

    Dalam suatu file python baru, `forms.py`, import kelas ModelForm dari modul form yang disediakan Django serta model Item dari aplikasi main. Kemudian dibuat class ItemForm yang meng-inherit kelas ModelForm Django. Dengan class ini kita membuat form yang sesuai dengan model Item. Di dalam ItemForm ada class Meta. Di dalamnya kita menentukan model yang akan digunakan oleh form ini (Item) dan fields dari model yang akan ditampilkan dalam form (name, amount, description).

    ```
    from django.forms import ModelForm
    from main.models import Item

    class ItemForm(ModelForm):
        class Meta:
            model = Item
            fields = ["name", "amount", "description"]
    ```

    Selanjutnya dalam file `views.py` dibuat fungsi create_product,

    ```
    def create_product(request):
        form = ItemForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_product.html", context)
    ```
    Fungsi ini menangani input baru dari form. Akan dibuat sebuah objek ItemForm berdasarkan data yang diterima dari `request.POST` (data yang dikirimkan melalui form). Kemudian, diperiksa apakah form tersebut valid dengan menggunakan `form.is_valid()`. Jika valid dan metode request adalah POST, data produk baru akan disimpan ke database melalui `form.save()`, dan pengguna akan diarahkan kembali ke halaman utama dengan HttpResponseRedirect.

    Kemudian di dalam file urls.py ditambahkan path URL yang mengarahkan permintaan ke create_product view saat pengguna ingin menambahkan produk baru.

    Setelah itu dibuat file HTML baru, `create_product.html`, yang akan menampilkan halaman form untuk menambah item baru. File ini mencakup form dengan token CSRF, bidang-bidang form, dan tombol "Add Item" yang mengirimkan data form ke view create_product.

    Terakhir pada file `main.html` ditambahkan potongan kode,
    ```
    {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.description}}</td>
            </tr>
        {% endfor %}
    ```
    untuk menampilkan data produk yang diterima dari view show_main dalam bentuk tabel, serta
    ```
    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Item
        </button>
    </a>
    ```
    sebagai tombol yang akan mengarahkan user pada halaman form penambahan item.


- Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

    Berikut 5 fungsi views yang dibuat, 

    __Format HTML__

    ```
    def show_main(request):
        items = Item.objects.all()

        context = {
            'nama_aplikasi': "My Bag",
            'nama': "Puti Raissa",
            'kelas': "PBP E",
            'items': items
        }

        return render(request, "main.html", context)
    ```
    `items = Item.objects.all()` mengambil semua objek Item dari database dengan Item.objects.all() dan menyimpannya dalam variabel items. Data item kemudian disertakan dalam konteks dan akan ditampilkan dalam template HTML main.html.

    __Format XML__
    ```
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    __Format JSON__
    ```
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    Kedua fungsi fungsi ini mengambil semua data dari model Item menggunakan `Item.objects.all()`. Selanjutnya, data tersebut diubah menjadi format XML/JSON menggunakan *serializer*. Akhirnya, respons HTTP yang berisi data sesuai format dikembalikan.
 
    __Format XML by ID__
    ```
    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    __Format JSON by ID__
    ```
    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    Dua fungsi ini kurang-lebih sama dengan dua fungsi sebelumnya, hanya saja data dari model Item diambil dan difilter berdasarkan ID.

- Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

    Di dalam file urls.py yang terdapat di direktori main, diimpor kelima fungsi dan ditambahkan path url nya ke dalam list `urlpatterns` untuk dapat mengakses fungsi-fungsi tersebut. 
    ```
    ...
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    ... 
    ```
    Untuk melihat aplikasi, dapat dijalankan perintah `python manage.py runserver` pada *virtual environment* dan membuka http://localhost:8000/[format(xml, json, xml/[id], json/[id])]

### Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

![html](images/html.jpg)
![xml](images/xml.jpg)
![json](images/json.jpg)
![xml-id](images/xml-id.jpg)
![json-id](images/json-id.jpg)

### Arsip tugas
<details>
<summary>Tugas 2</summary>

## Tugas 2
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
</details>
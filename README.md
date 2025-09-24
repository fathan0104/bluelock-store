Fathan Alfahrezi
2406496284
PBP E
Tugas 2

web : https://fathan-alfahrezi-blueelockstore.pbp.cs.ui.ac.id/
repo : https://github.com/fathan0104/bluelock-store.git


1. Dalam membangun proyek ini, langkah awal yang saya lakukan adalah membuat project Django baru. Tahapan ini sebenarnya sudah pernah saya coba sebelumnya ketika mengikuti tutorial, dimulai dengan instalasi git lalu membuat direktori khusus yang nantinya dipakai sebagai tempat project. Direktori tersebut kemudian dihubungkan dengan GitHub melalui perintah git remote add (link). Setelah itu saya melakukan proses commit dan push agar project dapat tersimpan di GitHub.

Setelah repository siap, saya melanjutkan dengan instalasi Django dan membuat berkas requirements.txt sebagaimana disarankan pada tutorial 0. Berkas tersebut berisi daftar package yang dibutuhkan untuk menjalankan Django. Proses instalasinya cukup sederhana dan tidak memakan banyak waktu. Selanjutnya saya membuat project menggunakan perintah django-admin startproject (namaProject) ..

Tahap berikutnya adalah menambahkan file .env. File ini berfungsi untuk menyimpan environment variables di luar kode utama, seperti konfigurasi database, API Key, maupun pengaturan mode aplikasi. Dengan begitu, project bisa dijalankan di berbagai environment tanpa harus mengubah kode program. Di sini saya juga membuat .env.prod yang berisi pengaturan PRODUCTION = True, sehingga aplikasi nantinya bisa menggunakan database PostgreSQL di production. Agar Django dapat membaca file .env, saya menyesuaikan konfigurasi pada settings.py.

Langkah ketiga setelah project terkoneksi dengan GitHub adalah menghubungkannya ke PWS sesuai arahan pada tutorial 0. Pada tahap ini saya menambahkan domain project ke dalam ALLOWED_HOSTS, sehingga project bisa diakses melalui PWS.

Setelah semua setup selesai, barulah saya membuat aplikasi dengan nama main di dalam project bluelock_store, yang di sini saya gunakan untuk membuat toko bernama SP Sportswear. Tidak seperti project football-news sebelumnya, aplikasi ini difokuskan pada penjualan produk olahraga. Karena itu saya mengubah model menjadi Product agar sesuai dengan konteks toko. Field-field yang digunakan antara lain:

name: nama barang

price: harga barang

description: deskripsi produk

thumbnail: gambar produk

category: kategori (jersey, sepatu, sweater, celana, tas, sleeve, kaos kaki, dll)

is_featured: penanda barang unggulan

stock: Jumlah stok

Rating : Rating dari tiap produk

Pemilihan tipe data juga disesuaikan dengan kebutuhan:

CharField-> teks pendek (misalnya nama & kategori)

TextField-> teks panjang (deskripsi produk)

IntegerField -> angka bulat (harga)

URLField -> menyimpan URL gambar

BooleanField -> kondisi biner (featured atau tidak)

PositiveIntegerField -> menyimpan bilangan bulat positif

DecimalField -> menyimpan bilangan desmal

Setelah model dibuat, saya melanjutkan ke template. Saya menyiapkan file main.html sebagai tampilan awal yang berisi teks sederhana, termasuk nama dan kelas saya. Untuk menghubungkannya, saya membuat routing pada urls.py serta fungsi view pada views.py. 

Jika konfigurasi routing tidak dilakukan, tentu main.html tidak bisa ditampilkan dengan benar. Karena itu saya juga menyesuaikan urls.py di dalam direktori main serta urls.py utama agar saling terhubung.

Setelah aplikasi berjalan dengan baik, saya melakukan deployment ke PWS yang sebelumnya sudah dikonfigurasi.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Client --REQUEST--> --Urls--> --View--> --Model--> --View--> --Template--> Response 

Alurnya dapat dijelaskan sebagai berikut:

Client: pengguna yang mengirim request ke server

URL: melakukan pencocokan request dengan fungsi view yang tepat

Views: mengolah request, berinteraksi dengan model bila diperlukan, lalu memilih template untuk respon

Model: representasi struktur data/database (misalnya tabel produk)

Template: file HTML yang memuat markup statis sekaligus data dinamis dari views

3. Jelaskan peran settings.py dalam proyek Django!
File settings.py adalah pusat konfigurasi Django. Di sinilah kita bisa mengatur berbagai hal seperti daftar aplikasi, konfigurasi database, daftar host yang diizinkan, penggunaan environment variables, hingga lokasi file statis. Modifikasi pada settings.py menentukan bagaimana project Django akan berjalan, baik di mode development maupun production.

4. Bagaimana cara kerja migrasi database di Django?
Migrasi digunakan untuk menyinkronkan model Django dengan skema database. Prosesnya terdiri dari:
-> python manage.py makemigrations: membuat file migrasi berdasarkan perubahan pada models.py
-> python manage.py migrate: menerapkan migrasi tersebut ke database dengan menjalankan perintah SQL yang sesuai
Dengan cara ini, setiap perubahan model (misalnya menambah field baru) bisa tercermin di database tanpa harus menulis query SQL manual.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django merupakan salah satu framework web yang direkomendasikan, terutama bagi pemula yang ingin cepat membangun aplikasi. Django hadir dengan fitur bawaan lengkap sehingga tidak perlu repot mencari library tambahan untuk kebutuhan dasar. Dari sisi keamanan pun, Django sudah memiliki perlindungan terhadap ancaman umum seperti SQL Injection dan XSS.
Selain itu, Django menggunakan pola arsitektur MTV (Model-Template-View) yang serupa dengan MVC. Struktur ini memisahkan komponen logika, tampilan, dan data, sehingga kode lebih terorganisir. Pola ini membantu developer — khususnya pemula — agar terbiasa menulis kode dengan prinsip separation of concerns.


6. Feedback
Tutorial cukup jelas dan mudah dipahami


Tugas 3
1. Mengapa Kita Memerlukan Data Delivery dalam Implementasi Sebuah Platform? 
Data delivery (pengiriman data) sangat penting dalam implementasi platform karena memastikan bahwa data yang tepat sampai ke pengguna atau sistem yang tepat, pada waktu yang tepat, dan dalam format yang benar. Tanpa proses ini, data tidak akan bisa digunakan secara efektif, bahkan jika data tersebut sudah dikumpulkan dan diproses dengan baik.

2. Mana yang Lebih Baik antara XML dan JSON? Mengapa JSON Lebih Populer?
Secara umum, JSON (JavaScript Object Notation) dianggap lebih baik dan lebih populer daripada XML (Extensible Markup Language) untuk sebagian besar aplikasi web modern.
alasan utama json lebih populer adalah
    - Sintaks lebih ringkas
    - Ukuran file lebih kecil
    - Mudah diuraikan
    - Kompatibilitas dengan web API

3. Fungsi dari Method is_valid() pada Form Django dan Mengapa Kita Membutuhkannya?
Method is_valid() pada Django Forms berfungsi untuk memvalidasi data yang dikirimkan melalui form. Ketika Anda memanggil form.is_valid(), Django akan melakukan beberapa hal:
    -Validasi Otomatis: Memeriksa apakah setiap field pada form (misalnya, teks, email, tanggal) telah diisi dengan format yang benar.
    -Validasi Khusus: Menjalankan metode validasi khusus yang mungkin Anda definisikan pada form (misalnya, memeriksa apakah password dan konfirmasi password cocok).
    -Mengisi cleaned_data: Jika validasi berhasil, Django akan menyimpan data yang sudah divalidasi dan dibersihkan dalam atribut form.cleaned_data. Atribut ini aman untuk digunakan karena sudah melewati semua pemeriksaan. 

4. Mengapa Kita Membutuhkan csrf_token saat Membuat Form di Django? Apa yang Terjadi jika Tidak Ditambahkan? Bagaimana Hal Tersebut Dapat Dimanfaatkan oleh Penyerang?
Kita membutuhkan csrf_token untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery).
Apa yang terjadi jika tidak ada?: Jika csrf_token tidak ditambahkan, form Anda akan rentan terhadap serangan CSRF. Ini berarti penyerang dapat membuat halaman web palsu dan "memaksa" 
pengguna yang sedang login di situs Anda untuk melakukan tindakan yang tidak mereka sadari (misalnya, mengubah password, mentransfer uang, atau menghapus data).
Bagaimana dimanfaatkan oleh penyerang?: Penyerang akan membuat halaman web yang berisi form tersembunyi. Ketika korban (yang sudah login di situs Anda) mengunjungi halaman web palsu tersebut, 
kode JavaScript atau form tersembunyi akan otomatis mengirimkan permintaan ke situs Anda. Karena browser korban menyertakan cookie sesi yang valid, server Anda akan menganggap permintaan itu sah dan menjalankan tindakan tersebut tanpa sepengetahuan korban. csrf_token mencegah hal ini karena server akan menolak permintaan yang tidak memiliki token yang sesuai.

5. Bagaimana Cara Mengimplementasikan Checklist di Atas secara Step-by-step?
    - Menambahkan 4 Fungsi views Baru seperti get_xml,get_json,get_xml_by_id,get_json_by_id
    - Setelah menambahkan views lalu memetakannya ke url pada urls.py
    - Menambah isi main.html yang akan menampilkan daftar objek. Di dalam template ini, tambahkan tombol "Add" dan "Detail" untuk setiap objek.
    - Membuat halaman forms.py untuk menambahkan objek model dan tambahkan csrf token di dalamnya
    - Membuat halaman yang menampilkan detail setiap objek

6. Apakah Ada Feedback untuk Asdos di Tutorial 2 yang Sudah Kalian Kerjakan?
Untuk tutorial 2 ini sudah cukup jelas dibuat oleh asdosnya

TUGAS 4
1. Apa Perbedaan antara HttpResponseRedirect() dan redirect()?
Perbedaan utamanya terletak pada level abstraksi dan kemudahannya. HttpResponseRedirect() adalah kelas dari django.http yang secara eksplisit membuat objek response HTTP dengan status kode 302 (atau 301), yang memberitahu browser untuk memuat URL baru. Sementara itu, redirect() adalah fungsi shortcut dari django.shortcuts yang lebih direkomendasikan dan fleksibel; ia dapat menerima nama view, URL absolut, atau bahkan objek model, dan secara otomatis menghasilkan HttpResponseRedirect() yang benar di belakang layar.

2. Jelaskan Cara Kerja Penghubungan Model Product dengan User!
Penghubungan ini diimplementasikan melalui mekanisme Foreign Key (models.ForeignKey). Ketika user = models.ForeignKey(User, on_delete=models.CASCADE) didefinisikan di model Product, Django membuat kolom user_id di tabel database main_product. Kolom user_id ini menyimpan Primary Key (id) dari tabel auth_user. Dengan kata lain, setiap baris di tabel main_product memiliki pointer yang menunjuk secara langsung ke pemiliknya di tabel auth_user. Atribut on_delete=models.CASCADE memastikan integritas data, di mana jika seorang pengguna dihapus, semua produk yang terasosiasi dengannya juga akan terhapus.

3. Apa Perbedaan antara Authentication dan Authorization, dan Apa yang Dilakukan saat Pengguna Login?
Authentication (Otentikasi) menjawab pertanyaan "Siapa Anda?" Ini adalah proses verifikasi identitas (misalnya, mencocokkan username dan password).
Authorization (Otorisasi) menjawab pertanyaan "Apa yang boleh Anda lakukan?" Ini adalah proses penentuan hak akses atau izin bagi pengguna yang sudah terotentikasi.
Saat pengguna login, yang terjadi adalah proses Authentication. Sistem memanggil authenticate() untuk memverifikasi kredensial dan kemudian menggunakan login() untuk membangun sesi pengguna, secara efektif membuktikan identitas pengguna tersebut.

Bagaimana Django Mengimplementasikan Kedua Konsep Tersebut?
Authentication: Django mengimplementasikannya melalui modul django.contrib.auth. Setelah pengguna diverifikasi oleh authenticate(), fungsi login() membuat Sesi (Session) yang disimpan di backend (database atau cache). Objek pengguna yang logged in kemudian dapat diakses di request berikutnya melalui request.user.
Authorization: Django menyediakan sistem Permissions (izin) yang dapat dikaitkan dengan user dan group (misalnya, can_add_product). Dalam kasus aplikasi sederhana seperti ini, otorisasi diimplementasikan secara implisit melalui filtering data (Product.objects.filter(user=request.user)), di mana view secara hardcoded hanya mengizinkan pengguna untuk mengambil data yang mereka miliki.

4. Bagaimana Django Mengingat Pengguna yang Telah Login? Jelaskan Kegunaan Lain dari Cookies dan Apakah Semua Cookies Aman Digunakan?
Django mengingat pengguna melalui kombinasi Session dan Cookies. Setelah login berhasil, Django membuat entri Session di backend (tabel django_session) yang berisi detail otentikasi pengguna. Kemudian, Django mengirimkan Cookie khusus bernama sessionid ke browser pengguna. Cookie ini hanya berisi ID unik yang merujuk pada session di backend. Pada setiap request berikutnya, browser mengirimkan sessionid kembali ke server, yang kemudian digunakan oleh Django untuk mencari sesi yang sesuai dan mengidentifikasi request.user.
Kegunaan Lain Cookies: Cookies memiliki kegunaan luas, seperti menyimpan preferensi user (bahasa, tema), melacak item di keranjang belanja, dan digunakan oleh layanan pihak ketiga untuk pelacakan perilaku (iklan bertarget).
Keamanan Cookies: Tidak, tidak semua cookies aman. Cookies yang ditandai dengan flag keamanan seperti HttpOnly (mencegah akses melalui JavaScript, melindungi dari XSS) dan Secure (hanya dikirim melalui koneksi HTTPS) dianggap lebih aman. Namun, cookies pihak ketiga (third-party cookies) yang digunakan untuk pelacakan sering kali menimbulkan masalah privasi dan dianggap berisiko.

5. Jelaskan Bagaimana Cara Kamu Mengimplementasikan Checklist di Atas secara Step-by-Step
Definisi Relasi: Menambahkan user = models.ForeignKey(User, ...) di model Product pada models.py.
Migrasi Awal Gagal (IntegrityError): Menjalankan makemigrations dan gagal karena data lama tidak memiliki user_id. Saya memilih opsi one-off default tetapi ID yang saya masukkan tidak ada di database.
Perbaikan Database: Saya keluar dari shell, menjalankan python manage.py createsuperuser untuk memastikan ada user dengan ID 1 yang valid di database.
Migrasi Ulang Sukses: Saya menghapus file migrasi yang gagal, menjalankan ulang makemigrations, dan memasukkan ID 1 sebagai default. Kemudian menjalankan python manage.py migrate untuk menerapkan user_id di tabel main_product.
Perbaikan views.py (NameError & UnboundLocalError): Saya mengimpor model Product (from .models import Product) di views.py dan memperbaiki logika query dari product = product... menjadi products = Product.objects.filter(user=request.user) untuk menghilangkan error binding dan memastikan filtering data.
Implementasi Fitur: Saya menambahkan fungsi register, login, dan logout dan menggunakan decorator @login_required pada show_main.
Cookies: Saya menambahkan logic untuk mengatur dan mengambil cookie last_login di fungsi login dan show_main menggunakan response.set_cookie() dan request.COOKIES.get().
Pembuatan Data Lokal: Melalui antarmuka admin atau shell, saya membuat dua akun pengguna dan mengaitkan masing-masing tiga dummy data produk, memvalidasi bahwa filtering data di halaman utama berjalan dengan benar.

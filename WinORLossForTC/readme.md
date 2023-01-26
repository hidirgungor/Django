Django'da bir web sitesi oluşturmak için aşağıdaki adımlar izlenmelidir:

Proje oluşturulur: django-admin startproject proje_adi
Uygulama oluşturulur: python manage.py startapp uygulama_adi
Veritabanı oluşturulur ve modeller yazılır: models.py dosyasına veritabanı tablosu için gerekli modeller yazılır.
Veritabanına modeller yansıtılır: python manage.py makemigrations ve python manage.py migrate komutları ile veritabanına modeller yansıtılır.
Formlar oluşturulur: forms.py dosyasına TC kimlik numarası arama için gerekli form yazılır.
View oluşturulur: views.py dosyasına TC kimlik numarasına göre veritabanından bilgi çekme işlemi yapacak view yazılır.
URL yapılandırılır: urls.py dosyasına arama sayfası için gerekli URL yapılandırması yapılır.
Tema oluşturulur: templates klasörüne arama sayfası için gerekli HTML dosyası oluşturulur.
Django'da TC kimlik numarasına göre arama yapacak bir web sitesi oluşturulması için aşağıdaki kodlar kullanılabilir:
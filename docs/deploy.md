# Wdrożenie projektu na serwer

### Wgrywamy pliki na serwer
- ręcznie:
  
  wszystkie pliki oprócz 'media' i 'static' z roota projektu  

- z repozytorium:

> git clone adres_repo

**UWAGA** Jeżeli repo jest prywatne to prawdopodobnie plik ***.env*** nie jest dodany do ***.gitignore***. W innym wypadku należy dodać ***.env*** ręcznie do roota projektu.

### Instalacja środowiska i wymaganych zalezności

- ręcznie: 
 - instalujemy środowisko wirtualne: 
   > mkvirtualenv --python=/usr/bin/python3.7 nazwasrodowiska
 -  instalujemy Django: 
   > pip install django=2.2.5
 - dalej instalujemy w ten sam sposób wszystkie moduły z pliku requirements.txt:
   > pip install nazwa_modułu==wersja

- automatycznie:
 - komenda automatycznie zainstaluje wszystko co znajdzie w pliku reqiruements:
  > pip install -r requirements.txt

***UWAGA*** Problem z ckeditor_upload rozwiązujemy przez odinstalowanie django-ckeditor i ponowną instalację tego modułu (tak, dziwna sprawa ale działa :) )

### Konfiguracja Django

- w ***manage.py*** zmieniamy wersję developerską:

 > os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic.settings.development')
 na produkcyjną:

 > os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic.settings.production')

- w ***settings/production.py*** ustawiamy adres domeny:

 > ALLOWED_HOSTS = ['nazwadomeny.pl']

- w ***.env*** wpisujemy odpowiednie dane

- nie mamy bazy danych z localhosta dlatego musimy od nowa utworzyć userów, zrobić migracje i podpiąć pliki statyczne:
  > python manage.py makemigrations
  >
  > python manage.py migrate
  >
  > python manage.py createsuperuser
  >
  > python manage.py collectstatic

**UWAGA:** jeżeli jakieś pliki statyczne chcemy update'ować za pomocą panelu admina (np własne style css) to zmieniamy url takiego pliku ze STATIC na ścieżkę STATIC_ROOT - inaczej musielibyśmy przy każdej zmianie pliku wywoływać collectstatic 
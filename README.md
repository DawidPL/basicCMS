# BASIC CMS

CMS for building and managing multiple sites simultaneously. It allows you to switch between projects and display the selected/active one in the browser. When adding individual elements, we can choose which project to change. The system is built in classic Django without DRF (although I added a basic version if needed). It is also possible to generate a static version of the site for servers that do not support Python.

![alt text](https://github.com/DawidPL/basicCMS/blob/master/screen1.jpg)
![alt text](https://github.com/DawidPL/basicCMS/blob/master/screen2.jpg)
![alt text](https://github.com/DawidPL/basicCMS/blob/master/screen2a.jpg)

Wersja 2.2.0

1. Dodano podstawowe REST API.
2. Drobne poprawki w defaultowych templatkach.
3. Rozbudowa dokumentacji.

Wersja 2.1.1

1. Każda podstrona ma swoje unikalne ID.
2. Naprawiono problem z miniaturkami grafik.
3. Dodano dodatkowe pola dla podstron i strony głównej.
4. Dodano generowanie statyczne z panelu admina.

Wersja 2.1

1. Pole wyboru numeru templatki wskazuje na aktualną liczbę gotowych motywów (nie jest dodana na sztywno jak wcześniej).
2. Dodano model 'Projekt'. Teraz budując strony określamy do którego projektu dana strona należy i na tej podstawie Django renderuję odpowiedni template.
3. Dodano zmienne w dokumentacji
4. Poprawiono nazewnictwo
5. Zmieniono widoki funkcyjne na klasy.


Wersja 2.0

1. Poprawiono plik requirements.
2. Poprawiono ładowanie poszczególnych sekcji w całym projekcie.
3. Zmieniono stukturę styli (teraz mamy po prostu styles -> template_1 -> i tutaj od razu dajemy base.scss z całą resztą includów (wg Waszego upodobania), bez podziału na homepage...subpage itd. 
4. Dodano CDN z font awesome w base.html.
5. Dodano opcjonalne linki do boksów.
6. Zwiększono liczbę templatek w polu wyboru do 100.
7. Przywrócono opcjonalnie formularz kontaktowy.
8. Dodano logo strony we wpisach blogowych.
9. Dodano sortowanie drag&drop w panelu.
10. Dodano custom.js dla każdej templatki
11. Dodano Lightbox.
12. Dodano opcjonalną recaptche dla formularza kontaktowego.
13. Rozdzielono ustawienia na wersje developerską i produkcyjną.
14. Generowanie wersji statycznej za pomocą jednej komendy (nie dwóch jak dotychczas).
15. Poprawiono generowanie dropdown menu.
15. Poprawki w dokumentacji.


Depends on which database you prefer, install:
- PostgreSQL : psycopg2 2.8.3
- MySQL: mySQLclient 1.4.4

**********************************************
 Cygwin - sometimes needed for gettext tool:
 https://mlocati.github.io/articles/gettext-iconv-windows.html
 http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/

 How to : https://docs.djangoproject.com/en/1.7/topics/i18n/translation/#gettext-on-windows
 **********************************************


 Problem with polish encoding:
 Open gettext.py in Python -> Lib directory and replace 'ASCII' to 'UTF-8': 'charset = self._charset or 'UTF-8'


## Zmienne w templatkach

### Strona główna

 - ##### Menu 
  ***site_settings.logo_text*** - logo strony

  ***site_settings.logo_img.url*** - tekst do logo

  ***site_settings.site_url*** - url strony

  ***multilanguage_prefix*** - prefik dodatkowego języka

   ***multilanguage_marker*** - checkbox sprawdzający czy język ma być wyświetlany

  ***{% for parent, children in parents.items %}*** - pętla po podstronach, gdzie ***parent*** to strona rodzic a ***children*** dziecko które wyświetla się w rozwijanym menu

 - ##### Karuzela 
  ***slide.display*** - checkbox sprawdzający czy slider ma być wyświetlany

  ***slide.img.url*** - grafika slidera

  ***slide.title*** - tytuł slidera

  ***slide.subtitle*** - tekst pod tytułem slidera

  ***slide.button_name*** - nazwa przycisku na sliderze

  ***slide.button_url*** - url przycisku slidera

 - ##### Main
  ***homepage.sort_active*** - sprawdza czy wybrane jest ręczne sortowanie sekcji 

  ***image.display*** - checkbox sprawdzający czy grafika ma być wyświetlona w galerii

  ***image.img.url*** - wyświetla grafikę

  ***box.is_active*** - checkbox sprawdzający czy box ma być wyświetlany

  ***box.link*** - url boxa

  ***box.image.url*** - grafika boxa

  ***box.title_tag*** - tag nagłowka boxa

  ***box.title*** - tytuł nagłowka boxa

  ***box.subtitle_tag*** - tag tekstu pod nagłowkiem boxa

  ***box.sub_title*** - treść pod nagłówkiem boxa

  ***homepage.content|safe, homepage.content2|safe*** itd - wyświetlają zawartość poszczególnych sekcji 

### Podstrony

 ***unique_subpage.title*** - tytuł podstrony

 ***unique_subpage.content|safe*** - treść podstrony

 ***image.img.url*** - wyświetla grafikę z galerii

 ***box.title*** - tytuł boxa

 ***box.image.url*** - grafika boxa

### Blog

 - ##### Lista wpisów
  ***single_content.title*** - tytuł wpisu

  ***single_content.img.url*** - grafika główna wpisu

  ***single_content.pre_content*** - krótki tekst 

 - ##### Pojedynczy wpis:

  ***blog.img.url*** - grafika także we wpisie 

  ***blog.content|safe*** - treść wpisu 

  ***blog.created*** - data dodania wpisu 

### Kontakt

 ***contact.content*** - tekst pod tytułem

 ***contact.company_name*** - nazwa firmy

 ***contact.company_address_first_line*** - pierwszy wiersz z adresem

 ***contact.comapany_address_second_line*** - drugii wiersz z adresem

 ***contact.company_phone_number*** - nr telefonu

 ***contact.company_phone_number_second*** - opcjonalny drugi nr telefonu

 ***contact.company_email*** - mail

 ***contact.company_email_second*** - opcjonalny drugi mail 

 ***site_settings.google_map_iframe|safe*** - mapa google
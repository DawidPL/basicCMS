# Admin

##### W pliku ***admin.py*** możemy wykonywać wiele dodatkowych operacji na modelach.

- Aby model był w ogóle widoczny w panelu admina musimy go najpierw zarejestrować:
 > admin.site.register(NazwaModelu)

- Możemy także ukryć niechciane (najcześciej domyślne) modele, np Group:

 >admin.site.unregister(Group)

- Główny tytuł panelu ustawimy za pomocą:
> admin.site.site_header = f'Panel administracyjny strony {settings.PAGE_NAME}'

- Jeżeli chcemy dodatkowo zmodyfikować dany model tworzymy klasę, która dziedziczy z modelu admina i ją także rejestrujemy:

```python
class NazwaModeluAdmin(admin.ModelAdmin):
     
admin.site.register(NazwaModelu, NazwaModeluAdmin)
```

- W klasie mamy dostęp do szeregu przydatnych opcji:
 - Brak możliwości utworzenia kolejnego obiektu jeżeli jeden już istnieje:

    ```python

    def has_add_permission(self, request):
        return not NazwaModelu.objects.exists()

    ```

 - Określenie które kolumny wyświetlą się w widoku modelu. W tym celu przekazujemy do krotki pola modelu. Możemy także zdefiniować własną zmienną bezpośrednio w modelu - to również zadziała, jeżeli potrzebujemy tylko opisu (stringa):
  > list_display = ('title', 'display', 'updated', 'created')

 - Dodatkowe style i skrypty dla Modelu dodamy za pomocą klasy ***Media*** :

 ```python

 class Media:
        js = ('pages/scripts/admin.js',)
        css = {
            'all': ('pages/styles/admin.css',)
        }

 ```

 - Wyszukiwanie obiektów na podstawie konkrentego pola/wielu pól:

 > search_fields = ('img',)


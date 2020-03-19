# Modele,

##### czyli wszystko co znajdziemy w panelu admina i zapisujemy do bazy 

- w modelu **Project** znajduje się lista developerów którą można edytować w razie potrzeby

```python
 class Project(models.Model):

    dev_list = ['Dawid', 'Łukasz', 'Damian', 'Karol']

```

- za pomocą klasy ***Meta*** zmieniamy wyświetlaną domyślnie nazwę dla modelu:

```python

 class Meta:
        verbose_name = 'Narzędzia SEO'
        verbose_name_plural = verbose_name

```

- dzięki metodzie ```__str__ ``` nadpisujemy domyślną nazwę obiektu klasy (reprezentuje i zwraca obiekt w formie stringu) 

```python

def __str__(self):
        return f'Ustawienia strony'

```

- jeżeli obiektów jest więcej możemy skorzystać z ***id*** który ma domyślnie przypisany każdy obiekt, np:

```python

def __str__(self):
        return f'id: {self.id}'

```

##### Z modelami ścisle powiązany jest plik ***admin.py*** w którym rejestrujemy i dodatkowo edytujemy parametry modeli.  
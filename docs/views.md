# Widoki

##### Jedynym widokiem wartym krótkiego wyjaśnienia jest ***generated_page*** w którym generują się wszystkie podstrony.

```python

def generated_page(request, slug):
    models_repository = ProjectRepository()
    multilanguage = Multilanguage.objects.exclude(multilanguage_marker=False)
    unique_subpage = get_object_or_404(Subpage, slug=slug)
    homepage = models_repository.get_homepage()
    site_settings = models_repository.get_site_setting()
    social_media = models_repository.get_social_media()
    contact_page = models_repository.get_contact_page()
    subpage_sorted = models_repository.get_active_subpages()

    context = {
        'unique_subpage': unique_subpage,
        'multilanguage': multilanguage,
        'site_settings': site_settings,
        'subpage_sorted': subpage_sorted,
        'homepage': homepage,
        'social_media': social_media,
        'contact': contact_page,
    }

    if unique_subpage.is_active or unique_subpage.slug == 'admin':
        return render(request, 'subpage.html', context)
    else:
        return render(request, '404.html', context)

```

- ***models_repository*** - wszystkie obiekty są filtrowane na bazie ten instancji, tj. Projektu który ustawimy w panelu dla konkretnej strony
- ***Slug***, czyli przyjazny url w panelu admina. Na jego podstawie Django "wie" którą podstronę załadować

- ***'gallery__graphics__display_order'*** - podwójny znak podkreślenia używamy gdy odwołujemy się do klucza obcego w bazie
- ***subpage_sorted*** - obiekt używany przez ***header*** templatek do sortowania podstron w menu
- ***unique_subpage_gallery*** - obiekty wyświetla posortowane grafiki (jeżeli nie używamy gotowej templatki podstrony)

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.deconstruct import deconstructible

from optimized_image.fields import OptimizedImageField
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from .utils.template_counter import template_counter
from .utils.list_of_choices_generator import choice_generator


@deconstructible
class UploadLocation:

    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        return f'{instance.project.title}/{self.path}/{filename}'

upload_location_blog = UploadLocation('blog')
upload_location_favicon = UploadLocation('favicon')
upload_location_logo = UploadLocation('logo')
upload_location_images= UploadLocation('images')
upload_location_box = UploadLocation('boxes')
upload_location_slide = UploadLocation('slides')

class Project(models.Model):

    dev_list = ['Dawid', 'Łukasz', 'Damian', 'Karol', 'Kamila', 'Ewelina']

    title = models.CharField('Nazwa projektu', max_length=100)
    author = models.CharField('Autor', choices=choice_generator.choices_list_generator(dev_list),
                              max_length=100, blank=True)
    comment = models.TextField('Komentarze/uwagi do projektu', blank=True)
    created = models.DateTimeField('Utworzono', auto_now_add=True)
    updated = models.DateTimeField('Zmodyfikowano', auto_now=True)
    is_active = models.BooleanField('Aktywny', null=False, default=False)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Projekt'
        verbose_name_plural = 'Projekty'

    def __str__(self):
        return self.title



class BaseModel(models.Model):
    project = models.ForeignKey('Project', verbose_name='Projekt', on_delete=models.CASCADE)
    template = models.IntegerField('Wybierz template',
                                   choices=choice_generator.choices_list_generator(template_counter.get_count()),
                                   null=True, blank=True)
    created = models.DateTimeField('Utworzono', auto_now_add=True)
    updated = models.DateTimeField('Zmodyfikowano', auto_now=True)
    objects = models.Manager()

    class Meta:
        abstract = True

    # choice_dict is using in template to iterate over all projects and load the choosen one 
    choice_dict = choice_generator.choices_dict_generator(template_counter.get_count())


class MultiField(models.Model):
    sort_active = models.BooleanField('Ustaw ręcznie kolejność wyświetlania wszystkich sekcji', default=False)
    gallery = models.ForeignKey('Gallery', verbose_name='Galeria', on_delete=models.SET_NULL,
                                   null=True, blank=True)                    
    display_gallery_order = models.IntegerField('Kolejność wyświetlania:', default=1)
    boxes = models.ManyToManyField('Box', verbose_name='Boxy', blank=True)
    display_boxes_order = models.IntegerField('Kolejność wyświetlania:', default=2)
    content = RichTextUploadingField('Sekcja 1', null=True, blank=True)
    display_content_order = models.IntegerField('Kolejność wyświetlania:', default=3)
    content_2 = RichTextUploadingField('Sekcja 2', null=True, blank=True)
    display_content_2_order = models.IntegerField('Kolejność wyświetlania:', default=4)
    content_3 = RichTextUploadingField('Sekcja 3', null=True, blank=True)
    display_content_3_order = models.IntegerField('Kolejność wyświetlania:', default=5)
    content_4 = RichTextUploadingField('Sekcja 4', null=True, blank=True)
    display_content_4_order = models.IntegerField('Kolejność wyświetlania:', default=6)
    content_5 = RichTextUploadingField('Sekcja 5', null=True, blank=True)
    display_content_5_order = models.IntegerField('Kolejność wyświetlania:', default=7)

    class Meta:
        abstract = True

class Homepage(BaseModel, MultiField):
    carousel = models.ManyToManyField('Carousel', verbose_name='Slajdy', blank=True)
    display_carousel = models.BooleanField('wyświetl slider', default=True)       

    class Meta:
        verbose_name = 'Strona główna'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'strona główna'

    edit_string = 'Edycja strony głównej'


class Subpage(BaseModel, MultiField):
    title = models.CharField('Nazwa podstrony', max_length=254)
    slug = models.SlugField('Przyjazny url', unique=True)
    is_active = models.BooleanField('Jest aktywna', default=True)
    my_order = models.PositiveIntegerField(verbose_name='Sortowanie drag&drop', default=0, blank=False, null=False)
    parent = models.ForeignKey('self', verbose_name='Jest dzieckiem:', on_delete=models.CASCADE, null=True, blank=True)
    meta_title = models.CharField('Meta title', max_length=100, null=True, blank=True)
    meta_description = models.TextField('Meta description', null=True, blank=True)


    class Meta:
        verbose_name = 'Podstrony'
        verbose_name_plural = 'Podstrony'
        ordering = ['my_order']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}'


class ContactPage(BaseModel):
    meta_title = models.CharField('Meta title', max_length=100, blank=True)
    meta_description = models.TextField('Meta description', blank=True)
    form_is_active = models.BooleanField('Formularz aktywny', default=True)
    content = models.TextField('Tekst pod tytułem', blank=True)
    company_name = models.CharField('Nazwa firmy', max_length=100, blank=True)
    company_address_first_line = models.CharField('Adres firmy - pierwszy wiersz', max_length=250, blank=True)
    comapany_address_second_line = models.CharField('Adres firmy - drugi wiersz', max_length=250, blank=True)
    company_phone_number = models.CharField('Numer telefonu', max_length=25, blank=True)
    company_phone_number_second = models.CharField('Drugi numer telefonu', max_length=25, blank=True)
    company_email = models.EmailField('Adres email firmy', max_length=100, blank=True)
    company_email_second = models.EmailField('Drugi adres email', max_length=100, blank=True)


    class Meta:
        verbose_name = "Kontakt"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'Kontakt'


class BlogPost(BaseModel):
    title = models.CharField('Tytuł wpisu', max_length=255, blank=False)
    slug = models.SlugField('Przyjazny url', unique=True)
    is_active = models.BooleanField('Wyświetl', default=True)
    blog_order = models.PositiveIntegerField(verbose_name='Sortowanie drag&drop', default=0, blank=False, null=False)
    meta_title = models.CharField('Meta title', max_length=100, blank=True)
    meta_description = models.TextField('Meta description', blank=True)
    img = OptimizedImageField('Główna grafika', upload_to=upload_location_blog, blank=True)
    img_in_single_blog = models.BooleanField('Dodaj grafikę do wpisu', default=True)
    pre_content = models.TextField('Krótki tekst', max_length=1000, blank=True)
    content = RichTextUploadingField('Treść wpisu', blank=True)

    class Meta:
        verbose_name = 'Wpis'
        verbose_name_plural = 'Wpisy'
        ordering = ['blog_order']

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/{self.slug}'
    


class SiteSettings(models.Model):
    project = models.ForeignKey('Project', verbose_name='Projekt', on_delete=models.CASCADE)
    site_url = models.CharField('Adres url witryny', max_length=200, default='localhost:8000')
    site_name = models.CharField('Nazwa witryny', max_length=255, blank=False)
    meta_title = models.CharField('Meta title strony głównej', max_length=100, blank=True)
    meta_description = models.TextField('Meta description strony głównej', blank=True)
    is_blog_active = models.BooleanField('Blog jest aktywny', default=False)
    template = models.IntegerField('Wybierz template podstrony Blog',
                                   choices=choice_generator.choices_list_generator(template_counter.get_count()),
                                   null=False, blank=False)
    meta_title_blog = models.CharField('Meta title podstrony Blog', max_length=100, blank=True)
    meta_description_blog = models.TextField('Meta description podstrony Blog', blank=True)
    site_favicon = models.ImageField('Favicon', upload_to=upload_location_favicon, blank=True)
    logo_text = models.CharField('Tekst logo', max_length=100, blank=True)
    logo_img = OptimizedImageField('Logo', upload_to=upload_location_logo, blank=True)
    google_map_iframe = models.TextField('Iframe mapy Google', blank=True)
    head_widgets = models.TextField('Przed tagiem </head>', blank=True)
    body_widgets = models.TextField('Przed tagiem </body>', blank=True)

    class Meta:
        verbose_name = 'Ustawienia strony'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'Ustawienia strony'


class Multilanguage(models.Model):
    EN = 'en'
    DE = 'de'
    FR = 'fr'
    RU = 'ru'

    LANGUAGES = [
        (EN, 'angielski'),
        (DE, 'niemiecki'),
        (FR, 'francuski'),
        (RU, 'rosyjski'),
    ]

    project = models.ForeignKey('Project', verbose_name='Projekt', on_delete=models.CASCADE)
    multilanguage_prefix = models.CharField('wybierz dodatkowy język', max_length=2,
                                            choices=LANGUAGES, blank=True)
    multilanguage_marker = models.BooleanField('Wyświetl język', default=False)

    class Meta:
        verbose_name = 'Dodatkowy język'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.multilanguage_prefix}'


class Gallery(models.Model):

    project = models.ForeignKey('Project', verbose_name='Projekt', on_delete=models.CASCADE)
    title = models.CharField('Nazwa galerii', max_length=100)
    display = models.BooleanField('Wyświetl', default=True)
    graphics = models.ManyToManyField('Image', verbose_name='grafiki', through='GalleryPanel')
    created = models.DateTimeField('Utworzono', auto_now_add=True)
    updated = models.DateTimeField('Zmodyfikowano', auto_now=True)

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerie'

    def __str__(self):
        return f'{self.title}'


class GalleryPanel(models.Model):
    gallery_panel = models.ForeignKey('Gallery', on_delete=models.CASCADE)
    image = models.ForeignKey('Image', verbose_name='Wybrane grafiki', on_delete=models.CASCADE)
    my_order = models.PositiveIntegerField(verbose_name='Sortowanie drag&drop', default=0, editable=True, blank=False,
                                           null=False)

    class Meta:
        verbose_name = 'Grafikę'
        verbose_name_plural = 'Grafiki'
        ordering = ['my_order']

    def __str__(self):
        return f'Ogólne'


class Image(models.Model):
    '''

    Default models.ImageField replaced with OptimizedImageField which is TinyPNG API object

    '''

    project = models.ForeignKey('Project', verbose_name='Projekt', on_delete=models.CASCADE)
    title = models.CharField('Tytuł', max_length=255, blank=True)
    img = OptimizedImageField('wybrana grafika', upload_to=upload_location_images)
    img_thumbnail = ImageSpecField(source='img',
                                   processors=[ResizeToFill(50, 50)],
                                   format='JPEG',
                                   options={'quality': 90})
    display = models.BooleanField('wyświetl', default=True)
    created = models.DateTimeField('Utworzono', auto_now_add=True)
    updated = models.DateTimeField('Zmodyfikowano', auto_now=True)

    class Meta:
        verbose_name = 'Plik graficzny'
        verbose_name_plural = 'Pliki graficzne'
        ordering = ['gallerypanel__my_order']

    def replace_url_string(self):
        replace_image_name = self.img.url.replace("/media/images/", " ")
        return replace_image_name

    def __str__(self):
        return f'id: {self.id} | nazwa pliku: {self.replace_url_string()}'


class Box(models.Model):
    h1 = 'h1'
    h2 = 'h2'
    h3 = 'h3'
    h4 = 'h4'
    h5 = 'h5'
    p = 'p'

    TAG_TYPE = [
        (h1, h1),
        (h2, h2),
        (h3, h3),
        (h4, h4),
        (h5, h5),
        (p, p),
    ]

    project = models.ForeignKey('Project', verbose_name='Projekt', on_delete=models.CASCADE)
    title = models.CharField('Tytuł', max_length=150, blank=True)
    title_tag = models.CharField('Tag tytułu', max_length=2, default=h1, choices=TAG_TYPE)
    sub_title = models.TextField('Treść boxa', blank=True)
    subtitle_tag = models.CharField('Tag tekstu pod tytułem', max_length=2, default=p, choices=TAG_TYPE)
    image = OptimizedImageField('Grafika', upload_to=upload_location_box)
    link = models.CharField('Jest linkiem do:(podaj tylko przyjazny url np. "podstrona1")', max_length=250,
                            blank=True)
    is_active = models.BooleanField('Aktywny', default=True)
    my_order = models.PositiveIntegerField(verbose_name='Sortowanie drag&drop', default=0, blank=False, null=False)
    created = models.DateTimeField('Utworzono', auto_now_add=True)
    updated = models.DateTimeField('Zmodyfikowano', auto_now=True)

    class Meta:
        verbose_name = 'Box'
        verbose_name_plural = 'Boxy'
        ordering = ['my_order']

    def __str__(self):
        return f'{self.title}'


class Carousel(models.Model):
    project = models.ForeignKey('Project', verbose_name='Projekt', on_delete=models.CASCADE)
    title = models.CharField('Tytuł', max_length=100, blank=True)
    subtitle = models.TextField('tekst pod tytułem', blank=True)
    is_active = models.BooleanField('wyświetl', default=True)
    my_order = models.PositiveIntegerField(verbose_name='Sortowanie drag&drop', default=0, blank=False, null=False)
    img = OptimizedImageField('Plik', upload_to=upload_location_slide)
    button_name = models.CharField('Nazwa przycisku', max_length=25, blank=True)
    button_url = models.CharField('URL przycisku', max_length=200, blank=True)
    created = models.DateTimeField('Utworzono', auto_now_add=True)
    updated = models.DateTimeField('Zmodyfikowano', auto_now=True)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slide\'y'
        ordering = ['my_order']

    def __str__(self):
        if self.title:
            return self.title
        else:
            return f'{self.id}'


class SocialMedia(models.Model):
    project = models.ForeignKey('Project', verbose_name='Projekt', on_delete=models.CASCADE)
    fb_url = models.CharField('Adres profilu Facebooka', max_length=250, blank=True)
    fb_is_active = models.BooleanField('Wtyczka Facebook aktywna', default=False)
    tw_url = models.CharField('Adres profilu Twittera', max_length=250, blank=True)
    tw_is_active = models.BooleanField('Wtyczka Twitter aktywna', default=False)
    ins_url = models.CharField('Adres profilu Instagrama', max_length=250, blank=True)
    ins_is_active = models.BooleanField('Wtyczka Instagram aktywna', default=False)

    class Meta:
        verbose_name = 'Social media'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'Edytuj ikony social media'


class CustomCss(models.Model):
    custom_css = models.TextField('Dodaj własne style', blank=True)

    class Meta:
        verbose_name = 'Własne style'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'Dodatkowe style css'


@receiver(post_save, sender=CustomCss)
def save_css_file_signal(sender, instance, **kwargs):
    field_name = 'custom_css'
    css = CustomCss.objects.first()
    field_value = getattr(css, field_name)
    formatted_field_value = field_value.replace('\n', '')
    filename = f'{settings.STATIC_ROOT}/pages/styles/custom.css'
    try:
        with open(filename, 'w+') as f:
            f.write(formatted_field_value)
    except:
        print(f'Could not open {filename}')

from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import Group
from django.forms import Textarea, TextInput
from django.db import models
from django.core.management import call_command

from imagekit.admin import AdminThumbnail
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import (Gallery,
                     Carousel,
                     SiteSettings,
                     Multilanguage,
                     Subpage,
                     BlogPost,
                     CustomCss,
                     Image,
                     Homepage,
                     Box,
                     ContactPage,
                     SocialMedia,
                     GalleryPanel,
                     Project,
                     )
from .repository.models_repository import ModelsRepository

admin.site.unregister(Group)

admin.site.site_header = f'BASIC CMS'
admin.site.index_title = f'Panel administracyjny strony {settings.PAGE_NAME}'
admin.site.site_title = ''


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('project', 'site_url')
    list_filter = (('project_id'),)


# @admin.register(Multilanguage)
# class MultilanguageAdmin(admin.ModelAdmin):
#     list_display = ('multilanguage_prefix', 'multilanguage_marker')


@admin.register(CustomCss)
class CustomCssAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 40, 'cols': 200})},
    }


class ImageTabularInline(SortableInlineAdminMixin, admin.TabularInline):
    model = GalleryPanel
    extra = 1
    ordering = ('my_order',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'thumbnail_display', 'img',
                    'display', 'updated', 'created')
    search_fields = ('img',)
    list_filter = (('project_id'),)
    actions = ['display_selected', 'hide_selected']

    thumbnail_display = AdminThumbnail(image_field='img')

    def display_selected(self, request, queryset):
        queryset.update(display=True)

    def hide_selected(self, request, queryset):
        queryset.update(display=False)

    display_selected.short_description = 'wyświetl wybrane pliki graficzne'
    hide_selected.short_description = 'schowaj wybrane pliki graficzne'



@admin.register(GalleryPanel)
class GalleryPanelAdmin(admin.ModelAdmin):
    list_display = ('image',)
    search_fields = ('image',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'display', 'updated', 'created')
    list_filter = (('project_id'),)
    inlines = (ImageTabularInline,)


@admin.register(Carousel)
class CarouselAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'thumbnail_display', 'title', 'is_active', 'updated', 'created')
    list_filter = (('project_id'),)
    thumbnail_display = AdminThumbnail(image_field='img')


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    fields = ('project', 'template', 'sort_active', 'carousel', 'display_carousel',
            'gallery', 'display_gallery_order', 'boxes', 'display_boxes_order', 
            'content', 'display_content_order','content_2', 'display_content_2_order',
            'content_3', 'display_content_3_order', 'content_4', 'display_content_4_order',
            'content_5', 'display_content_5_order',)
    list_display = ('project', 'updated', 'created')
    list_filter = (('project_id'),)

    class Media:
        pass


@admin.register(Subpage)
class SubpageAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ('project', 'template', 'sort_active', 'title', 'slug', 'is_active',
            'parent', 'meta_title', 'meta_description', 'gallery', 'display_gallery_order', 
            'boxes', 'display_boxes_order', 'content', 'display_content_order','content_2', 
            'display_content_2_order', 'content_3', 'display_content_3_order', 'content_4', 
            'display_content_4_order', 'content_5', 'display_content_5_order',)
    list_display = ('project', 'title', 'slug', 'is_active', 'updated', 'created')
    list_filter = (('project_id'),)


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('project', 'created')
    list_filter = (('project_id'),)


@admin.register(Box)
class BoxAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'updated', 'created')
    list_filter = (('project_id'),)


@admin.register(BlogPost)
class BlogPostAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'project', 'title', 'is_active', 'updated', 'created')
    list_filter = (('project_id'),)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('project',)
    list_filter = (('project_id'),)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'updated', 'created', 'is_active')
    readonly_fields = ('is_active',)
    actions = ['activate', 'export_to_static_version']

    def activate(self, request, queryset):
        repository = ModelsRepository()
        if len(queryset) > 0:
            repository.set_project(queryset[0])

    def export_to_static_version(self, request, queryset):
        if len(queryset) > 0:
            project = queryset[0]
            call_command('generate_static_website', id=project.id)

    activate.short_description = 'Aktywuj wybrany projekt'
    export_to_static_version.short_description = 'Eksportuj do wersji statycznej(poczekaj chwilę na zakończenie procesu, nie odświeżaj strony)'

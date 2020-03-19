from mixer.backend.django import mixer

import pytest

from pages.models import Multilanguage
from .fixtures.models_fixtures import (title_list, site_url_list, meta_title_list,
                                       meta_description_list, logo_text_list,
                                       google_map_iframe, head_widgets, body_widgets,
                                       company_name_list, company_adress,
                                       company_phone_list, company_email_list,
                                       box_list, words_list, sentence_list, content_list,
                                       slug_list, css_list)


@pytest.mark.django_db
class TestProject:

    def test_if_project_title_is_correct(self, title_list):
        for title in title_list:
            project = mixer.blend('pages.Project', title=title)
            assert project.title == str(title)


@pytest.mark.django_db
class TestSiteSettings:

    def test_if_site_url_is_correct(self, site_url_list):
        for site in site_url_list:
            site_settings = mixer.blend('pages.SiteSettings', site_url=site)
            assert site_settings.site_url == site

    def test_if_project_id_is_correct(self, title_list):
        for title in title_list:
            project = mixer.blend('pages.Project', title=title)
            site_settings = mixer.blend('pages.SiteSettings', project_id=project)
            assert site_settings.project_id.title == project.title

    def test_if_meta_title_is_correct(self, meta_title_list):
        for meta in meta_title_list:
            site_settings = mixer.blend('pages.SiteSettings', meta_title=meta)
            assert site_settings.meta_title == meta

    def test_if_meta_description_is_correct(self, meta_description_list):
        for meta in meta_description_list:
            site_settings = mixer.blend('pages.SiteSettings', meta_description=meta)
            assert site_settings.meta_description == meta

    def test_if_meta_blog_title_is_correct(self, meta_title_list):
        for meta in meta_title_list:
            site_settings = mixer.blend('pages.SiteSettings', meta_title_blog=meta)
            assert site_settings.meta_title_blog == meta

    def test_if_meta_blog_description_is_correct(self, meta_description_list):
        for meta in meta_description_list:
            site_settings = mixer.blend('pages.SiteSettings', meta_description_blog=meta)
            assert site_settings.meta_description_blog == meta

    def test_if_logo_text_list_is_correct(self, logo_text_list):
        for meta in logo_text_list:
            site_settings = mixer.blend('pages.SiteSettings', logo_text=meta)
            assert site_settings.logo_text == meta

    def test_if_google_map_iframe_is_correct(self, google_map_iframe):
        for meta in google_map_iframe:
            site_settings = mixer.blend('pages.SiteSettings', google_map_iframe=meta)
            assert site_settings.google_map_iframe == meta

    def test_if_body_widgets_is_correct(self, body_widgets):
        for meta in body_widgets:
            site_settings = mixer.blend('pages.SiteSettings', body_widgets=meta)
            assert site_settings.body_widgets == meta

    def test_if_head_widgets_is_correct(self, head_widgets):
        for meta in head_widgets:
            site_settings = mixer.blend('pages.SiteSettings', head_widgets=meta)
            assert site_settings.head_widgets == meta


@pytest.mark.django_db
class TestMultilanguage:

    def test_if_multilanguage_prefix_is_correct(self):
        multilanguage = mixer.blend('pages.Multilanguage', multilanguage_prefix='en')
        assert multilanguage.multilanguage_prefix == 'en'

    def test_if_multilanguage_marker_is_correct(self):
        multilanguage = Multilanguage.objects.create(multilanguage_prefix='en',
                                                     multilanguage_marker=False)
        assert multilanguage.multilanguage_prefix == 'en'
        assert multilanguage.multilanguage_marker == False


@pytest.mark.django_db
class TestGallery:

    def test_if_gallery_title_and_display_is_correct(self, title_list):
        for item in title_list:
            gallery = mixer.blend('pages.Gallery', title=item, display=False)
            assert gallery.title == str(item)
            assert gallery.display == False

    def test_if_gallery_many_to_many_field_is_correct(self, title_list):
        for item in title_list:
            gallery = mixer.blend('pages.Gallery', title=item)
            image = mixer.blend('pages.Image', title=item)
            assert gallery.title == image.title


@pytest.mark.django_db
class TestImage:

    def test_if_image_title_is_correct(self, title_list):
        for item in title_list:
            image = mixer.blend('pages.Image', title=item)
            assert image.title == str(item)

    def test_if_image_display_order_is_correct(self):
        for num in range(1, 500):
            image = mixer.blend('pages.Image', display_order=num)
            assert image.display_order == num

    def test_if_image_display_is_correct(self):
        image = mixer.blend('pages.Image', display=False)
        assert image.display == False


@pytest.mark.django_db
class TestBox:

    def test_if_box_title_and_subtitle_are_correct(self, words_list):
        for item in words_list:
            box = mixer.blend('pages.Box', title=item, subtitle=item)
            assert box.title == str(item)
            assert box.subtitle == str(item)

    def test_if_box_tags_are_correct(self, box_list):
        for item in box_list:
            box = mixer.blend('pages.Box', title_tag=item, subtitle_tag=item)
            assert box.title_tag == item
            assert box.subtitle_tag == item

    def test_if_box_display_order_is_correct(self):
        for num in range(1, 500):
            box = mixer.blend('pages.Box', display_order=num)
            assert box.display_order == num

    def test_if_box_display_is_correct(self):
        box = mixer.blend('pages.Box', display=False)
        assert box.display == False


@pytest.mark.django_db
class TestCarouselImage:

    def test_if_carousel_title_and_subtitle_are_correct(self, words_list):
        for item in words_list:
            carousel = mixer.blend('pages.Carousel', title=item, subtitle=item)
            assert carousel.title == item
            assert carousel.subtitle == item

    def test_if_carousel_display_is_correct(self):
        box = mixer.blend('pages.Box', display=False)
        assert box.display == False

    def test_if_carousel_button_name_and_url_are_correctt(self, words_list, site_url_list):
        for item in words_list:
            carousel = mixer.blend('pages.Carousel', button_name=item)
            assert carousel.button_name == item
        for item in site_url_list:
            carousel = mixer.blend('pages.Carousel', button_url=item)
            assert carousel.button_url == item


@pytest.mark.django_db
class TestHomepage:

    def test_if_homepage_choosen_template_is_correct(self):
        for num in range(100):
            homepage = mixer.blend('pages.Homepage', template=num)
            assert homepage.template == num

    def test_if_homepage_sort_is_active(self):
        homepage = mixer.blend('pages.Homepage', sort_active=False)
        assert homepage.sort_active == False

    def test_if_homepage_choosen_and_display_carousel_is_correct(self):
        carousel = mixer.blend('pages.Carousel', title='test')
        homepage = mixer.blend('pages.Homepage', display_carousel=False, carousel=carousel)
        assert homepage.display_carousel == False
        assert homepage.carousel.first().title == carousel.title

    def test_if_homepage_choosen_gallery_is_correct(self):
        image = mixer.blend('pages.Image', title='img name')
        gallery = mixer.blend('pages.Gallery', title='gallery name', graphics=image)
        homepage = mixer.blend('pages.Homepage', gallery=gallery)
        assert homepage.gallery.title == gallery.title
        assert gallery.graphics.first().title == image.title

    def test_if_homepage_choosen_boxes_are_correct(self):
        box = mixer.blend('pages.Box', title='box title', is_active=False)
        homepage = mixer.blend('pages.Homepage', boxes=box)
        assert homepage.boxes.first().title == box.title
        assert homepage.boxes.first().is_active == box.is_active

    def test_if_homepage_content_fields_data_are_correct(self, content_list):
        for item in content_list:
            homepage = mixer.blend('pages.Homepage',
                                   content=item, content_2=item,
                                   content_3=item, content_4=item,
                                   content_5=item)
            assert homepage.content == item
            assert homepage.content_2 == item
            assert homepage.content_3 == item
            assert homepage.content_4 == item
            assert homepage.content_5 == item

    def test_if_homepage_display_elements_order_are_correct(self):
        order_list = [1, 2, 3, 4, 5, 6, 7]
        homepage = mixer.blend('pages.Homepage',
                               display_gallery_order=order_list[4],
                               display_boxes_order=order_list[0],
                               display_content_order=order_list[5],
                               display_content_2_order=order_list[6],
                               display_content_3_order=order_list[3],
                               display_content_4_order=order_list[2],
                               display_content_5_order=order_list[1],
                               )
        assert homepage.display_gallery_order == order_list[4]
        assert homepage.display_boxes_order == order_list[0]
        assert homepage.display_content_order == order_list[5]
        assert homepage.display_content_2_order == order_list[6]
        assert homepage.display_content_3_order == order_list[3]
        assert homepage.display_content_4_order == order_list[2]
        assert homepage.display_content_5_order == order_list[1]


@pytest.mark.django_db
class TestSubpage:

    def test_if_subpage_choosen_template_is_correct(self):
        for num in range(100):
            subpage = mixer.blend('pages.Subpage', template=num)
            assert subpage.template == num

    def test_if_subpage_title_is_correct(self, title_list):
        for item in title_list:
            subpage = mixer.blend('pages.Subpage', title=item)
            assert subpage.title == str(item)

    def test_if_subpage_slug_is_correct(self, slug_list):
        for item in slug_list:
            subpage = mixer.blend('pages.Subpage', slug=item)
            assert subpage.slug == item

    def test_if_subpage_display_is_active(self):
        subpage = mixer.blend('pages.Subpage', is_active=False)
        subpage_2 = mixer.blend('pages.Subpage', is_active=True)
        assert subpage.is_active == False
        assert subpage_2.is_active == True

    def test_if_subpage_display_order_is_correct(self):
        for num in range(30):
            subpage = mixer.blend('pages.Subpage', display_order=num)
            assert subpage.display_order == num

    def test_if_subpage_parent_is_correct(self):
        pass

    def test_if_subpage_meta_title_and_meta_description_is_correct(self, meta_title_list, meta_description_list):
        for item in meta_title_list:
            subpage = mixer.blend('pages.Subpage', meta_title=item)
            assert subpage.meta_title == item
        for item in meta_description_list:
            subpage = mixer.blend('pages.Subpage', meta_description=item)
            assert subpage.meta_description == item

    def test_if_subpage_choosen_gallery_is_correct(self):
        gallery = mixer.blend('pages.Gallery', title='subpage gallery')
        subpage = mixer.blend('pages.Subpage', gallery=gallery)
        assert subpage.gallery.title == gallery.title

    def test_if_subpage_choosen_box_is_correct(self):
        box = mixer.blend('pages.Box', title='subpage box title')
        subpage = mixer.blend('pages.Subpage', box=box)
        assert subpage.box.first().title == box.title


@pytest.mark.django_db
class TestContactPage:

    def test_if_contant_page_meta_title_and_meta_description_is_correct(self, meta_title_list, meta_description_list):
        for item in meta_title_list:
            contact_page = mixer.blend('pages.ContactPage', meta_title=item)
            assert contact_page.meta_title == item
        for item in meta_description_list:
            contact_page = mixer.blend('pages.ContactPage', meta_description=item)
            assert contact_page.meta_description == item

    def test_if_contat_page_form_active_is_correct(self):
        contact_page = mixer.blend('pages.ContactPage', form_is_active=False)
        contact_page_2 = mixer.blend('pages.ContactPage', form_is_active=True)
        assert contact_page.form_is_active == False
        assert contact_page_2.form_is_active == True

    def test_if_contact_page_content_is_correct(self, content_list):
        for item in content_list:
            contact_page = mixer.blend('pages.ContactPage', content=item)
            assert contact_page.content == item

    def test_if_company_name_is_correct(self, company_name_list):
        for item in company_name_list:
            site_owner_identity = mixer.blend('pages.ContactPage', company_name=item)
            assert site_owner_identity.company_name == item

    def test_if_company_adress_is_correct(self, company_adress):
        for item in company_adress:
            site_owner_identity = mixer.blend('pages.ContactPage', company_adress_first_line=item,
                                              company_adress_second_line=item)
            assert site_owner_identity.company_adress_first_line == item
            assert site_owner_identity.company_adress_second_line == item

    def test_if_company_phone_number_is_correct(self, company_phone_list):
        for item in company_phone_list:
            site_owner_identity = mixer.blend('pages.ContactPage', company_phone_number=item,
                                              company_phone_number_second=item)
            assert site_owner_identity.company_phone_number == item
            assert site_owner_identity.company_phone_number_second == item

    def test_if_company_email_adresss_is_correct(self, company_email_list):
        for item in company_email_list:
            site_owner_identity = mixer.blend('pages.ContactPage', company_email=item,
                                              company_email_second=item)
            assert site_owner_identity.company_email == item
            assert site_owner_identity.company_email_second == item


@pytest.mark.django_db
class TestBlog:

    def test_if_blog_title_is_correct(self, title_list):
        for item in title_list:
            blog = mixer.blend('pages.BlogPost', title=item)
            assert blog.title == str(item)

    def test_if_blog_slug_is_correct(self, slug_list):
        for item in slug_list:
            blog = mixer.blend('pages.BlogPost', slug=item)
            assert blog.slug == item

    def test_if_blog_display_is_active(self):
        blog = mixer.blend('pages.BlogPost', is_active=False)
        blog_2 = mixer.blend('pages.BlogPost', is_active=True)
        assert blog.is_active == False
        assert blog_2.is_active == True

    def test_if_blog_meta_title_and_meta_description_is_correct(self, meta_title_list, meta_description_list):
        for item in meta_title_list:
            blog = mixer.blend('pages.BlogPost', meta_title=item)
            assert blog.meta_title == item
        for item in meta_description_list:
            blog = mixer.blend('pages.BlogPost', meta_description=item)
            assert blog.meta_description == item

    def test_if_blog_img_in_single_blog_display_is_active(self):
        blog = mixer.blend('pages.BlogPost', img_in_single_blog=False)
        blog_2 = mixer.blend('pages.BlogPost', img_in_single_blog=True)
        assert blog.img_in_single_blog == False
        assert blog_2.img_in_single_blog == True

    def test_if_blog_pre_content_and_content_are_correct(self, sentence_list, content_list):
        for item in sentence_list:
            blog = mixer.blend('pages.BlogPost', pre_content=item)
            assert blog.pre_content == item
        for item in content_list:
            blog = mixer.blend('pages.BlogPost', content=item)
            assert blog.content == item

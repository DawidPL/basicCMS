from django_distill import distill_path
from django.urls import path, include
from rest_framework import routers

from pages import api
from . import views
from .utils import static_generators

router = routers.DefaultRouter()
router.register('homepage', api.HomepageViewSet)
router.register('subpage', api.SubpageViewSet)
router.register('contactpage', api.ContactPageViewSet)
router.register('gallery', api.GalleryViewSet)
router.register('carousel', api.CarouselViewSet)
router.register('image', api.ImageViewSet)
router.register('box', api.BoxViewSet)
router.register('sitesettings', api.SiteSettingsViewSet)
router.register('blogpost', api.BlogPostViewSet)
router.register('socialmedia', api.SocialMediaViewSet)

urlpatterns = [
    distill_path('', views.IndexView.as_view(), name='index',
                 distill_func=static_generators.no_parametr_view, distill_file='index.html'),
    distill_path('kontakt/', views.ContactView.as_view(), name='contact',
                 distill_func=static_generators.no_parametr_view, distill_file='contact.html'),
    distill_path('blog/', views.BlogView.as_view(), name='blog',
                 distill_func=static_generators.no_parametr_view, distill_file='blog.html'),
    distill_path('blog/<slug:slug>/', views.SinglePostView.as_view(), name='single_post',
                 distill_func=static_generators.iter_single_blog_post),
    distill_path('<slug:slug>/', views.SubpageView.as_view(), name='generated_page',
                 distill_func=static_generators.iter_single_subpage),
    path('api/v1/', include(router.urls))             
]



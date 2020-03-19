from rest_framework import viewsets, permissions

from .serializers import (GallerySerializer,
                        CarouselSerializer,
                        SiteSettingsSerializer,
                        SubpageSerializer,
                        BlogPostSerializer,
                        ImageSerializer,
                        HomepageSerializer,
                        BoxSerializer,
                        ContactPageSerializer,
                        SocialMediaSerializer,
                        )

from .models import (Gallery,
                     Carousel,
                     SiteSettings,
                     Subpage,
                     BlogPost,
                     Image,
                     Homepage,
                     Box,
                     ContactPage,
                     SocialMedia,
                     )


class HomepageViewSet(viewsets.ModelViewSet):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly, )

class SubpageViewSet(viewsets.ModelViewSet):
    queryset = Subpage.objects.all()
    serializer_class = SubpageSerializer

class ContactPageViewSet(viewsets.ModelViewSet):
    queryset = ContactPage.objects.all()
    serializer_class = ContactPageSerializer

class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BoxViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class SiteSettingsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer

class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class CarouselViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer

class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class SocialMediaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
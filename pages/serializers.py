from rest_framework import serializers

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

class HomepageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homepage
        fields ='__all__'

class SubpageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subpage
        fields ='__all__'

class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPage
        fields ='__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields ='__all__'

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields ='__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields ='__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields ='__all__'

class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields ='__all__'

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields ='__all__'

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields ='__all__'
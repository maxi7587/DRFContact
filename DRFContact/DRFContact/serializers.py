from rest_framework import serializers
from DRFContact.DRFContact.models import Address, Phone, Web, SocialMedia, Contact

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'url', 'country', 'state', 'city', 'street_name', 'street_number', 'zip', 'detail')
        read_only_fields = ('created_at','updated_at', 'deleted_at')

class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = ('id', 'url', 'country_code', 'area_code', 'phone_number')
        read_only_fields = ('created_at','updated_at', 'deleted_at')

class SocialMediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('id', 'url', 'web_contact', 'social_network', 'link')
        read_only_fields = ('created_at','updated_at', 'deleted_at')

class WebSerializer(serializers.HyperlinkedModelSerializer):
    social_media = SocialMediaSerializer(many=True)

    class Meta:
        model = Web
        fields = ('id', 'url', 'email', 'web_url', 'social_media')
        read_only_fields = ('created_at','updated_at', 'deleted_at')

    def create(self, validated_data):
        social_media_data = validated_data.pop('social_media')
        web = Web.objects.create(**validated_data)
        for social_media in social_media_data:
            SocialMedia.objects.create(web_contact=web, **social_media)
        return web

    def update(self, validated_data):
        social_media_data = validated_data.pop('social_media')
        web = Web.objects.create(**validated_data)
        for social_media in social_media_data:
            SocialMedia.objects.create(web_contact=web, **social_media)
        return web

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'url', 'name', 'address', 'phone', 'web')
        read_only_fields = ('created_at','updated_at', 'deleted_at')

    def to_representation(self, instance):
        self.fields['address'] = AddressSerializer(read_only=True)
        self.fields['phone'] = PhoneSerializer(read_only=True)
        self.fields['web'] = WebSerializer(read_only=True)

        return super(ContactSerializer, self).to_representation(instance)

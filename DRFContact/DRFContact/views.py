from django.shortcuts import render
from rest_framework import viewsets
from DRFContact.DRFContact.serializers import AddressSerializer, PhoneSerializer, WebSerializer, SocialMediaSerializer, ContactSerializer
from DRFContact.DRFContact.models import Address, Phone, Web, SocialMedia, Contact

# Create your views here.

class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows addresses to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows phones to be viewed or edited.
    """
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class WebViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows web contacts to be viewed or edited.
    """
    queryset = Web.objects.all()
    serializer_class = WebSerializer

class SocialMediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows social media contacts to be viewed or edited.
    """
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

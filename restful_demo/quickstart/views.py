# -*- coding: utf-8 -*-
from models import Message
from rest_framework import viewsets
from restful_demo.quickstart.serializers import MessageSerializer
# Create your views here.


class MessageViewSet(viewsets.ReadOnlyModelViewSet):
      queryset = Message.objects.all()
      serializer_class = MessageSerializer
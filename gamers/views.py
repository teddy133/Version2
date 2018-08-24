# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from models import Games
from models import Members
from serializers import GamesSerializer
from serializers import MembersSerializer
from models import StoreCategory
from models import Store
from models import Manager
from models import Region
from serializers import StoreCategorySerializer
from serializers import StoreSerializer
from serializers import ManagerSerializer
from serializers import ManagerRegionSerializer
from django.utils.translation import ugettext



from django.shortcuts import render

# Create your views here.

class GamesList(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    name = 'games-list'

class GamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    name = 'games-detail'

class MembersList(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    name = 'members-list'

class MembersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    name = 'members-detail'









class StoreCategoryList(generics.ListCreateAPIView):
    queryset = StoreCategory.objects.all()
    serializer_class = StoreCategorySerializer
    name = 'storecategory-list'


class StoreCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreCategory.objects.all()
    serializer_class = StoreCategorySerializer
    name = 'storecategory-detail'


class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    name = 'store-list'


class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    name = 'store-detail'


class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    name = 'manager-list'


class ManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    name = 'manager-detail'


class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = ManagerRegionSerializer
    name = 'region-list'


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = ManagerRegionSerializer
    name = 'region-detail'










class GameAdministration(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
        'Games' : reverse(GamesList.name, request=request),
        'Members' : reverse(MembersList.name, request=request),
        'store-categories': reverse(StoreCategoryList.name, request=request),
        'stores': reverse(StoreList.name, request=request),
        'manager': reverse(ManagerList.name, request=request),
        'regions': reverse(RegionList.name, request=request)
        })

from django.conf.urls import url, include
import views
from django.utils.translation import ugettext

urlpatterns = [
    url(r'^Games/$', views.GamesList.as_view(), name=views.GamesList.name),
    url(r'^Games/(?P<pk>[0-9]+)$', views.GamesDetail.as_view(), name=views.GamesDetail.name),
    url(r'^Members/$', views.MembersList.as_view(), name=views.MembersList.name),
    url(r'^Members/(?P<pk>[0-9]+)$', views.MembersDetail.as_view(), name=views.MembersDetail.name),


    url(r'^drone-categories/$', views.StoreCategoryList.as_view(), name=views.StoreCategoryList.name),
    url(r'^drone-categories/(?P<pk>[0-9]+)$', views.StoreCategoryDetail.as_view(), name=views.StoreCategoryDetail.name),
    url(r'^drones/$',views.StoreList.as_view(),name=views.StoreList.name),
    url(r'^drones/(?P<pk>[0-9]+)$',views.StoreDetail.as_view(),name=views.StoreDetail.name),
    url(r'^pilots/$',views.ManagerList.as_view(),name=views.ManagerList.name),
    url(r'^pilots/(?P<pk>[0-9]+)$',views.ManagerDetail.as_view(),name=views.ManagerDetail.name),
    url(r'^competitions/$',views.RegionList.as_view(),name=views.RegionList.name),
    url(r'^competitions/(?P<pk>[0-9]+)$',views.RegionDetail.as_view(),name=views.RegionDetail.name),


    url(r'$', views.GameAdministration.as_view(), name=views.GameAdministration.name)
]

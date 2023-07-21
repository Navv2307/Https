from django.urls import path
from .views import *

urlpatterns = [
    path("create/", Poi_create.as_view(), name='create'),
    path('view/', Poi_list.as_view(), name='view'),
    path('nearest-parents/', NearestParentObjectsAPI.as_view(), name='nearest-parents-api'),

]
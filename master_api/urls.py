from django.urls import path
from .viewsets.masterViewset import (
    MasterCreateViewSet,
    MasterUpdateViewSet,
    MasterDeleteViewSet,
    MasterListViewSet,
    MasterRetrieveViewSet,
)

urlpatterns = [
   
    path("masters/create", MasterCreateViewSet.as_view({"post": "create"})),
    path("masters/update", MasterUpdateViewSet.as_view({"put": "update"})),
    path("masters/delete", MasterDeleteViewSet.as_view({"delete": "delete"})),
    path("masters/list", MasterListViewSet.as_view({"post": "list"})),
    path("masters/get", MasterRetrieveViewSet.as_view({"post": "retrieve"})),
    
]

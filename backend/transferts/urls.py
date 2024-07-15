from django.urls import path, include
from .api import TransfertList, TransfertDetail, search_client

urlpatterns = [
    path('transferts', TransfertList.as_view(), name="get_transferts"),
    path('transfert/<int:pk>', TransfertDetail.as_view(), name="get_post_transfert"),
    path('clients/<str:keywords>', search_client, name="search_client"),
    path('clients/sub/<str:client_id>', search_client, name="search_client_subscription"),
]

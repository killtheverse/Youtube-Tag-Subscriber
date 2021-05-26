from django.urls import path
from .views import (
    query_list, query_detail
    # register_query, get_query_results,
    # get_user_queries, delete_query
)

urlpatterns = [
    path('queries/', query_list),
    path('queries/<str:slug>/', query_detail),
    # path('queries/', register_query),
    # path('get_query_results/', get_query_results),  
    # path('get_user_queries/', get_user_queries),
    # path('delete_query/', delete_query),
]

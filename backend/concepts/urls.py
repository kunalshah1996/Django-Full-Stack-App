from django.urls import path

from . import views

urlpatterns =[
    path('<int:pk>/',views.concept_detail_view),
    path('',views.concept_list_view),
    path('filter',views.concept_filter_list_view),
    path('search/',views.concept_search_view),
]
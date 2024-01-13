from django.urls import path,include
from core_app import views
urlpatterns = [
 path('',views.index,name='index'),
 path('package/<pid>',views.Package_detail,name='package-detail'),
 path('search/',views.search,name="search"),
 path('search_result/',views.search_result,name="search-result"),
]

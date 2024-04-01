
from django.urls import include, path 
from . import views

urlpatterns = [
    path('', views.create_user_view , name='default-view'),
    path('other', views.second_page_view),

    path("api/", include("django.contrib.auth.urls"))
]

from django import views
from django.urls import include, path





urlpatterns = [

    path('',views.job_list),
    path('<int:id>',views.job_detail),
]
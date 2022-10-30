from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), #challanges/
    path("<int:month>", views.monthly_challange_by_number),
    path("<str:month>", views.monthly_challage, name="month-challange")
]
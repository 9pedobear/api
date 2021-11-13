from django.urls import path
from .views import *

urlpatterns = [
    path('v1/laptop/create', LaptopCreateView.as_view()),
    path('v1/laptop/list', LaptopListView.as_view()),
    path('v1/laptop/detail/<int:pk>', LaptopDetailView.as_view())

]
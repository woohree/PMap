from django.urls import path
from . import views

app_name = 'toilets'

urlpatterns = [
    path('<x>/<y>/', views.toilet_index),
    path('<int:toilet_pk>/', views.toilet_detail),
    path('<int:toilet_pk>/review/', views.review_create),
    path('<int:toilet_pk>/review/<int:review_pk>', views.review_update_delete),
]
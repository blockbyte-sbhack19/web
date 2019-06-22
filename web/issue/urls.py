from django.urls import path

from . import views

app_name = 'issue'

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /soil/5/detail/
    path('<int:soil_id>/', views.detail, name='detail'),
    # ex: /soil/5/history/
    path('<int:soil_id>/results/', views.history, name='history'),
    # ex: /soil/5/submit/
    path('<int:soil_id>/submit/', views.submit, name='submit'),
]
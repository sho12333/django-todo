from django.urls import include
from django.urls import path

urlpatterns = [
    # ...
    path('todo/', include('todo_app.urls')),
]
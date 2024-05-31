from django.urls import path
from .views import kotlinQuiz

urlpatterns = [
    path('kotlin/v1',kotlinQuiz)
]

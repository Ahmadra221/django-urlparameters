from django.urls import path
from . import views as appviews

urlpatterns = [

    path('welcome/', appviews.print_hello),
    path('order/<str:dish>/', appviews.print_parameter),
    path('query/', appviews.print_querystring),

]
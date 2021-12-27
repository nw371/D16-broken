from django.urls import path

from board.views import IndexPage

urlpatterns = [
    path('', IndexPage.as_view()), #это путь к представлению главной страницы
]
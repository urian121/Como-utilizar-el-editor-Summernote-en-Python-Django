
from django.urls import path

from . views import inicio, registrar_post, listar_posts

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registrar-post/', registrar_post, name='registrar_post'),
    path('listar-de-posts/', listar_posts, name='listar_posts'),
]

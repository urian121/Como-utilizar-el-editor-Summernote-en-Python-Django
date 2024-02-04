from django.shortcuts import redirect, render
from . models import Post


def inicio(request):
    return render(request, 'index.html')


def registrar_post(request):
    if request.method == 'POST':
        autor = request.POST.get('autor')
        titulo = request.POST.get('title')
        contenido = request.POST.get('content')
        status = request.POST.get('is_active')

        post = Post(
            autor=autor,
            title=titulo,
            content=contenido,
            is_active=status,
        )
        post.save()

        return redirect('inicio')
    return redirect('inicio')


def listar_posts(request):
    posts = Post.objects.all()  # Recupera todos los posts de la base de datos
    return render(request, 'listar_posts.html', {'posts': posts})

### Cómo utilizar el editor Summernote en Django

##### El proyecto "Gestor de Posts con Editor Summernote en Django" se centra en la creación de una aplicación web utilizando el framework Django de Python. El objetivo principal es permitir a los usuarios crear y gestionar publicaciones de manera intuitiva y dinámica mediante el uso del editor de texto enriquecido Summernote.

#### Summernote es un editor WYSIWYG (Lo que ves es lo que obtienes) de código abierto que se puede integrar fácilmente en aplicaciones web Django para permitir a los usuarios crear contenido enriquecido de manera intuitiva.

#### Summernote proporciona una serie de características útiles, como opciones de formato de texto,tipo de letras, tamaño de letras, inserción de imágenes, videos, enlaces, listas, tablas, entre otros elementos de contenido. Su integración en Django permite una experiencia de edición de contenido más intuitiva y flexible para los usuarios finales.

1.  Crear un entorno virtual

        Opción 1: Crear entorno virtual con el paquete virtualenv
        Si no tienes instalado virtualenv puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/
        pip install virtualenv ->Instalar de forma global
        virtualenv env ->Crear entorno
        virtualenv --version ->Ver la versión de virtualenv

        Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
        python -m venv env

2.  Activar entorno virtual

        . env/Script/activate ->para Windows
        . env/bin/activate -> Para Mac
        deactivate -->Para desactivar mi entorno virtual

3.  Instalar django desde el manejador de paquete de Python Pip, ya dentro del entorno virtual.

        pip install Django
        Nota: para instalar Django en una version especifica
        pip install Django==4.2.4

4.  Instalar Driver para conectar Gestor de BD MySQL con Django, con el fin de crear una tabla para almacenar los idiomas disponibles

        pip install mysqlclient

5.  Crear el proyecto con django

        `django-admin startproject project_core .`
        El punto . es crucial le dice al script que instale Django en el directorio actual

        Ya en este punto se puede correr el proyecto que a creado Django,
        python manage.py runserver

6.  Crear mi primera aplicación en Django

        python manage.py startapp blog

7.  Instalar nuestra aplicación (blog) ya creada en el proyecto, en el archivo settings.py

        archivo settings.py
        INSTALLED_APPS = [
        ----,
        'blog',
        ]

8.  Conectar las URLS de mi aplicación con el projecto, para esto vamos al archivo uls.py del projecto

        from django.urls import path, include

        urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('blog.urls')),
        ]

9.  Crear mi Modelo

        class Post(models.Model):
        autor = models.CharField(max_length=200)
        title = models.CharField(max_length=200)
        content = models.TextField()
        is_active = models.IntegerField(default=0)
        created_at = models.DateTimeField(default=timezone.now)
        updated = models.DateTimeField(auto_now=True)

10. Registrar modelos en el panel de administración

        python manage.py createsuperuser

11. Crear las migraciones y correrlas

        python manage.py makemigrations -> Creando migraciones
        python manage.py migrate         -> Correr migraciones

12. Correr el proyecto

        python manage.py runserver
        Revisar la consola y visitar la URL http://127.0.0.1:8000

13. Crear el archivo urls.py en la aplicación (traductor)

        from django.urls import path
        from django.utils import timezone
        from . import views

                urlpatterns = [
                        path('', inicio, name='inicio'),
                        path('registrar-post/', registrar_post, name='registrar_post'),
                        path('listar-de-posts/', listar_posts, name='listar_posts'),
                ]

14. Crear la carpeta 'templates' dentro de la aplicación donde estarán mis archivos.html

15. Crear la carpeta 'static' dentro de mi aplicacion, aqui estaran archivos
    estaticos (css, js, imagenes, etc..)

16. Correr archivo requirement.txt para instalar todas las dependencias del proyecto

        pip install -r requirements.txt

#### Resultado final

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/resultado_final_Summernote.png)

### Documentación oficial

        https://summernote.org

### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍

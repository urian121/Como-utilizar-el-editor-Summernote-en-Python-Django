### Creando un Traductor con Python y Django

##### El proyecto "Traductor Multilingüe" busca crear una aplicación web que permita a los usuarios traducir texto entre varios idiomas de manera rápida y sencilla. Utilizando el poder de Python y el marco de desarrollo web Django, este proyecto ofrece una solución eficiente y accesible para las necesidades de traducción de los usuarios.

1.  Crear un entorno virtual, hay muchas formas

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

4.  Instalar el paquete (django-summernote) el cual nos ayudará a traducir el contenido

        pip install django-summernote

5.  Instalar Driver para conectar Gestor de BD MySQL con Django, con el fin de crear una tabla para almacenar los idiomas disponibles

        pip install mysqlclient

6.  Crear el proyecto con django

        `django-admin startproject project_core .`
        El punto . es crucial le dice al script que instale Django en el directorio actual

        Ya en este punto se puede correr el proyecto que a creado Django,
        python manage.py runserver

7.  Crear mi primera aplicación en Django

        python manage.py startapp blog

8.  Instalar nuestra aplicación (blog) ya creada en el proyecto, en el archivo settings.py

        archivo settings.py
        INSTALLED_APPS = [
        ----,
        'blog',  # blog app mi aplicación
        'django_summernote',  # django-summernote paquete de django para el editor de texto
        ]

9.  Se debe añadir la siguiente configuración a tu archivo settings.py para especificar el directorio donde se almacenarán las imágenes subidas

         import os
         # Configuración para el almacenamiento de imágenes subidas
         MEDIA_URL = '/media/'
         MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

10. Conectar las URLS de mi aplicación con el projecto, para esto vamos al archivo uls.py del projecto
    from django.urls import path, include

        from django.conf import settings  # Nuevo
        from django.conf.urls.static import static  # Nuevo


        urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('blog.urls')),
        path("summernote/", include("django_summernote.urls")), # forma parte del paquete summernote
        ]

        # Nuevo
        if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                                document_root=settings.MEDIA_ROOT)

11. Crear mi Modelo

        class Post(models.Model):
        title = models.CharField(max_length=200)
        content = SummernoteTextField()
        created_at = models.DateTimeField(auto_now_add=True)

12. Registrar modelos en el panel de administración

        python manage.py createsuperuser

13. Crear las migraciones y correrlas

        python manage.py makemigrations -> Creando migraciones
        python manage.py migrate         -> Correr migraciones

14. Correr el proyecto

        python manage.py runserver
        Revisar la consola y visitar la URL http://127.0.0.1:8000

15. Crear el archivo urls.py en la aplicación (traductor)

        from django.urls import path
        from . import views

                urlpatterns = [
                        path('', views.inicio, name='inicio'),
                        path('registrar_empleado/', views.registrar_empleado,
                                name='registrar_empleado'),
                        path('empleados/', views.listar_empleados, name='listar_empleados'),
                ]

16. Crear la carpeta 'templates' dentro de la aplicación donde estarán mis archivos.html

17. Crear la carpeta 'static' dentro de mi aplicacion, aqui estaran archivos
    estaticos (css, js, imagenes, etc..)

18. Correr archivo requirement.txt para instalar todas las dependencias del proyecto

        pip install -r requirements.txt

19. Información de Paquete
    https://pypi.org/project/deep-translator/

### Nota, el path en el archivo settings.py del proyecto significa:

        path("summernote/", include("django_summernote.urls")),

        Esta parte define la URL que utilizarás para acceder a las funcionalidades proporcionadas por django-summernote. En este caso, cuando accedas a http://tu_dominio.com/summernote/, estarás accediendo a las funcionalidades de django-summernote.

        include("django_summernote.urls"): Esta parte incluye las URLs proporcionadas por el paquete django-summernote en tu proyecto. Cuando accedes a la ruta summernote/ en tu aplicación Django, el sistema redirige las solicitudes a las URLs definidas en django_summernote.urls.

###### El paquete deep-translator de Python. Este paquete proporciona una interfaz para traducir texto utilizando varios servicios de traducción en línea, como Google Translate, Microsoft Translator, y otros.

#### Resultado final

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/traductor-con-python.png)

### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍

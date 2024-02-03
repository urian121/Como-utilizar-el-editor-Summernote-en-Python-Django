from django.db import models
from django_summernote.fields import SummernoteTextField  # importando la librería
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = SummernoteTextField()
    is_active = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def es_extension_valida(self):
        extensiones_validas = ['.jpg', '.jpeg', '.png', '.gif']
        return any(self.foto_empleado.name.lower().endswith(ext) for ext in extensiones_validas)

    class Meta:
        db_table = "tbl_posts"
        ordering = ['-created_at']

from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_active = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.title} - {self.is_active} "

    def es_extension_valida(self):
        extensiones_validas = ['.jpg', '.jpeg', '.png', '.gif']
        return any(self.foto_empleado.name.lower().endswith(ext) for ext in extensiones_validas)

    class Meta:
        db_table = "tbl_posts"
        ordering = ['-created_at']

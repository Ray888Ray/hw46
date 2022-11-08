from django.db import models
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
# Create your models here.


class ToDo(models.Model):
    goal = models.CharField(max_length=50, null=False, blank=False, verbose_name='Goal')
    content = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')
    started = models.DateTimeField(auto_now_add=True, verbose_name='Started')
    choice = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name='Choice')

    def __str__(self):
        return f'{self.pk}.{self.goal}'

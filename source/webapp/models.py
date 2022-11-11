from django.db import models
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
# Create your models here.


class ToDo(models.Model):
    goal = models.CharField(max_length=10, null=False, blank=False, verbose_name='Goal')
    content = models.TextField(max_length=300, null=True, blank=True, verbose_name='Description')
    started = models.DateField(auto_now_add=True, verbose_name='Started')
    deadline = models.DateField(null=True, blank=True, verbose_name='Deadline')
    choice = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name='Choice')

    def __str__(self):
        return f'{self.pk}.{self.goal}'

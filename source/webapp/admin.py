from django.contrib import admin
from webapp.models import ToDo


# Register your models here.



class ToDoAdmin(admin.ModelAdmin):
    list_display = ['id', 'goal', 'content', 'started', 'choice']
    list_display_links = ['goal']
    list_filter = ['content']
    search_fields = ['goal', 'content']
    exclude = []
    readonly_fields = ['started', 'choice']


admin.site.register(ToDo, ToDoAdmin)

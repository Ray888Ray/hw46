from django import forms
from django.forms import widgets
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class ToDoForm(forms.Form):
    goal = forms.CharField(max_length=20, required=True, label='Goal')
    content = forms.CharField(max_length=300, required=False, label='Content', widget=widgets.Textarea)
    choice = forms.ChoiceField(choices=STATUS_CHOICES)
    deadline = forms.DateField(required=False, label='Deadline', widget=widgets.SelectDateWidget)



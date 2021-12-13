"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Blog
from django.db import models
from .models import Comment

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
class AnketaForm(forms.Form):
    name = forms.CharField(label='ФИО', min_length=2, max_length=100, required=True)
    address = forms.CharField(label='Адрес', min_length=2, max_length=100, required=False)
    phone = forms.CharField(label='Телефон', min_length=11, max_length=11, required=True)
    email = forms.EmailField(label='E-mail', min_length=7, required=True)
    paymentMethod = forms.ChoiceField(label='Способ оплаты', choices=((1, 'Картой на сайте'), (2, 'Наличными в офисе')), required=True)
    agreement = forms.BooleanField(label='С условиями ознакомлен', required=True)

class CommentForm (forms.ModelForm):
   class Meta:
     model = Comment # используемая модель
     fields = ('text',) # требуется заполнить только поле text
     labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm(forms.ModelForm):
   class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}
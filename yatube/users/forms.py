from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


from posts.models import Post # Импортируем модель, чтобы связать с ней форму


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        help_texts = {
            'text': 'Введите текст сообщения',
            'group': 'Выберите группу',
        }       
        labels = {
            'text': 'Текст сообщения',
            'group': 'Группа',
        }
        
        def clean(self):
            data = self.cleaned_data['text']
            if data == '':
                raise ValidationError('Нет текста в поле поста')
            return data

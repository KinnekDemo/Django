__author__ = 'GKadillak'


from django.forms import ModelForm
from fix_it.models import Post, Annotate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class NewPost(ModelForm):

    class Meta:
        model = Post
        exclude = ('author',)


class NewComment(ModelForm):

    class Meta:
        model = Annotate
        exclude = ('total_votes', 'up_votes', 'down_votes', 'thumb_up', 'thumb_down', 'post', 'author', )
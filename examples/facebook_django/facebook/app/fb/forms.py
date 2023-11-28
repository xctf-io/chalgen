from django.forms import (
    Form, CharField, Textarea, PasswordInput, ChoiceField, DateField,
    ImageField
)

from fb.models import UserProfile

class UserPostForm(Form):
    text = CharField(widget=Textarea(
        attrs={'readonly': True, 'rows': 1, 'cols': 40, 'class': 'form-control','placeholder': "What's on your mind?"}))

class UserPostCommentForm(Form):
    text = CharField(widget=Textarea(
        attrs={'readonly': True, 'rows': 1, 'cols': 50, 'class': 'form-control','placeholder': "Write a comment..."}))


class UserLogin(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class UserProfileForm(Form):
    first_name = CharField(max_length=100, required=False, widget=Textarea(attrs={'readonly': True}))
    last_name = CharField(max_length=100, required=False, widget=Textarea(attrs={'readonly': True}))
    gender = ChoiceField(choices=UserProfile.GENDERS, required=False, widget=Textarea(attrs={'readonly': True}))
    date_of_birth = DateField(required=False, widget=Textarea(attrs={'readonly': True}))
    avatar = ImageField(required=False, widget=Textarea(attrs={'readonly': True}))

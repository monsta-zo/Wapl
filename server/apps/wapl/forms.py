from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'nickname', 'username', 'password1', 'password2']
        labels = {
			'name': '이름',		
			'nickname': '닉네임',		
			'username': '아이디',
		}
        
    def __init__(self, name, nickname, username, password1, password2, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.name = name
        self.nickname = nickname
        self.username = username
        self.password1 = password1
        self.password2 = password2

class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "비밀번호나 이메일이 올바르지 않습니다. 다시 확인해 주세요."
        ),
    }

    def __init__(self, username, password, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '아이디'
        self.fields['password'].label = '비밀번호'
        self.username = username
        self.password = password
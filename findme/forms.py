# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterForm(UserCreationForm):
	email = forms.EmailField(label='E-mail')
	first_name = forms.CharField(label='Primeiro nome')
	last_name = forms.CharField(label='Ultimo nome')


class UpdateDataForm(UserChangeForm):
	email = forms.EmailField(label='E-mail')
	first_name = forms.CharField(label='Primeiro nome')
	last_name = forms.CharField(label='Ultimo nome')

	class Meta:
		model = User
		fields = ['username', 'password', 'email', 'first_name', 'last_name']
from django import forms
from .models import  GuessNumbers
import random
class PostForm(forms.ModelForm):
    class Meta:
        model = GuessNumbers
        fields = ('name', 'text', )
        

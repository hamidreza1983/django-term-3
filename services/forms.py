from django import forms
from .models import Comments


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('user', 'product_name', 'message')
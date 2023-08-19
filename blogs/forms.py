from django import forms
from blogs.models import SharePost,Post,Comment


class SharedPostForm(forms.ModelForm):

    class Meta:
        model = SharePost
        fields = ["name","email_field","to_field","comments"]

class CommentForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = Comment
        fields = ['name','email','text']
from django import forms
from blog.models import Newsletter

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(widget=forms.TextInput)
    message = forms.CharField(widget=forms.TextInput)

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
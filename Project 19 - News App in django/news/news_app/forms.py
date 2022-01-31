from django.forms import ModelForm
from .models import NewsContent

class NewsForm(ModelForm):
    class Meta:
        model= NewsContent
        fields = ['img', 'title', 'description', 'source_link', 'tags']
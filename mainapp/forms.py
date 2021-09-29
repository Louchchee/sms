from django.forms import ModelForm
from . import models

class noticeForm(ModelForm):
    class Meta:
        model = models.Notice
        fields = '__all__'
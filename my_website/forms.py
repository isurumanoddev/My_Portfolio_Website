from my_website.models import Projects
from django.forms import ModelForm


class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ["title","thumbnail","body"]


from my_website.models import Projects
from django.forms import ModelForm


class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ["title","body"]

    def __init__(self, *args, **kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        self.fields["title"].widget.attrs.update({'class':'form-control'})
        self.fields["body"].widget.attrs.update({'class':'form-control'})
        # self.fields["thumbnail"].widget.attrs.update({'class':'form-control'})

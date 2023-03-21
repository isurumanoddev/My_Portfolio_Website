from my_website.models import Projects,Messages
from django.forms import ModelForm


class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ["title","thumbnail","body","github_link"]

    def __init__(self, *args, **kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        self.fields["title"].widget.attrs.update({'class':'form-control'})
        self.fields["body"].widget.attrs.update({'class':'form-control'})
        self.fields["thumbnail"].widget.attrs.update({'class':'form-control'})
        self.fields["github_link"].widget.attrs.update({'class':'form-control'})

class ContactForm(ModelForm):
    class Meta:
        model = Messages
        fields = "__all__"
        exclude = ["is_read"]

    def __init__(self, *args, **kwargs):
        super(ContactForm,self).__init__(*args,**kwargs)

        self.fields["name"].widget.attrs.update({'class':'form-control'})
        self.fields["email"].widget.attrs.update({'class':'form-control'})
        self.fields["subject"].widget.attrs.update({'class':'form-control'})
        self.fields["body"].widget.attrs.update({'class':'form-control'})

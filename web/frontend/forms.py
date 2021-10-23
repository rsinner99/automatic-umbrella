from django import forms

from scripts import models as scripts

class DocForm(forms.ModelForm):
    class Meta:
        model = scripts.Doc
        fields = '__all__'

class PeerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    passphrase = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = scripts.Peer
        fields = '__all__'

class FileForm(forms.Form):
    filename = forms.CharField(error_messages={'required': 'Please enter a filename'})
    content = forms.CharField(widget=forms.Textarea())
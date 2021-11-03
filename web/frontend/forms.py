from django import forms
from celery import current_app 

from scripts import models as scripts

# get a list of availabel tasks and store them in a tuple for a dropdown in frontend
# ignore interal celery tasks
AVAILABLE_TASKS = [tuple([t, t]) for t in current_app.tasks.keys() if not t.startswith('celery')]

class DocForm(forms.ModelForm):
    class Meta:
        model = scripts.Doc
        fields = '__all__'

class PeerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    passphrase = forms.CharField(widget=forms.PasswordInput(), required=False)
    class Meta:
        model = scripts.Peer
        fields = '__all__'

class FileForm(forms.Form):
    filename = forms.CharField(error_messages={'required': 'Please enter a filename'})
    content = forms.CharField(widget=forms.Textarea())

class FileViewForm(forms.Form):
    filename = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    content = forms.CharField(widget=forms.Textarea())

class TaskForm(forms.Form):
    taskname = forms.CharField(label="Choose a task from the list!", widget=forms.Select(choices=AVAILABLE_TASKS))
    kwargs = forms.JSONField(initial={}, required=False)

class TaskResultForm(forms.Form):
    result = forms.CharField(widget=forms.Textarea(attrs={'readonly':'readonly'}))

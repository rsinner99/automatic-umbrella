from django.db import models
from django.utils import timezone

# Create your models here.

OS_CHOICES = [
    ('windows', 'Windows'),
    ('linux', 'Linux'),
]

class Doc(models.Model):
    DOC_TYPES = [
        ('sh', 'Bash'),
        ('py', 'Python'),
    ]

    name = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    type = models.CharField(max_length=3, choices=DOC_TYPES)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(editable=False, auto_now=True)
    os = models.CharField(help_text='Operating System', choices=OS_CHOICES, max_length=7)



class Peer(models.Model):

    ip_address = models.GenericIPAddressField(null=True)
    ssh_port = models.IntegerField(default=22)
    hostname = models.CharField(unique=True, max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    private_key = models.TextField(null=True)
    passphrase = models.CharField(blank=True, default="", max_length=20)
    os = models.CharField(help_text='Operating System', choices=OS_CHOICES, max_length=7)

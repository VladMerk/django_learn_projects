from django.db import models
from .managers import DiscordUserOAuth2Manager


class DiscordUser(models.Model):

    id = models.BigIntegerField(primary_key=True)
    discord_tag = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100, null=True)
    public_flags = models.IntegerField()
    locale = models.CharField(max_length=100)
    mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(auto_now=True)

    objects = DiscordUserOAuth2Manager()

    def __str__(self):
        return self.discord_tag

    def is_authenticated(self, request):
        return True

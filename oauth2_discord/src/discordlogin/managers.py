from django.contrib.auth import models


class DiscordUserOAuth2Manager(models.UserManager):
    def create_new_discord_user(self, user):
        discord_tag = f"{user['username']}#{user['discriminator']}"
        return self.create(
            id=user["id"],
            avatar=user["avatar"],
            public_flags=user["public_flags"],
            locale=user["locale"],
            mfa_enabled=user["mfa_enabled"],
            discord_tag=discord_tag,
        )

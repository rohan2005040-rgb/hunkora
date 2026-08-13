from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    avatar = models.ImageField(
        upload_to="profile_pics/",
        default="profile_pics/default.png",
        blank=True,
        null=True,
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    reward_points = models.PositiveIntegerField(default=150)

    def __str__(self):
        return f"{self.user.username}'s Profile"


# ==========================================================
# Auto-create or save UserProfile whenever a User is created
# ==========================================================
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        UserProfile.objects.get_or_create(user=instance)
        if hasattr(instance, "profile"):
            instance.profile.save()
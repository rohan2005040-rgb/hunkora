from django.db import models

# Create your models here.
class Review(models.Model):

    STAR_CHOICES = (
        (5, "★★★★★ Excellent"),
        (4, "★★★★ Very Good"),
        (3, "★★★ Good"),
        (2, "★★ Fair"),
        (1, "★ Poor"),
    )

    name = models.CharField(max_length=100)

    email = models.EmailField()

    rating = models.IntegerField(
        choices=STAR_CHOICES,
        default=5
    )

    review = models.TextField()

    is_approved = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
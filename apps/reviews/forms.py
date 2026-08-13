from django import forms
from .models import Review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "name",
            "email",
            "rating",
            "review",
        ]

    def clean(self):
        cleaned_data = super().clean()
        print("Form Cleaned:", cleaned_data)
        return cleaned_data
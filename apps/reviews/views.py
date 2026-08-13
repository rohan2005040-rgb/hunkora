from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def reviews(request):

    print("METHOD:", request.method)

    if request.method == "POST":
        print("POST RECEIVED")
        print(request.POST)

        form = ReviewForm(request.POST)

        print("IS VALID:", form.is_valid())
        print("ERRORS:", form.errors)

        if form.is_valid():
            form.save()
            print("Saved Successfully")
            return redirect("reviews")
        else:
            print("Form Invalid")

    else:
        form = ReviewForm()

    reviews = Review.objects.filter(is_approved=True)

    return render(
        request,
        "pages/reviews.html",
        {
            "form": form,
            "reviews": reviews,
        },
    )
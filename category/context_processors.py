from .models import Category

def categories(request):
    cat = Category.objects.all()
    return dict(categories=cat)
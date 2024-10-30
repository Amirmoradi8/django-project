from services.models import Category


def general_context(request):
        context = {
        'Category' : Category.objects.all(),
        }
        return context

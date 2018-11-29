from .models import Link

def context_dictionary(request):
    ctx = {}
    links = Link.objects.all()

    for link in links:
        ctx[link.key] = link.url

    return ctx
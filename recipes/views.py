from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation

html_language = translation.get_language()


def home(request):
    return render(request, "recipes/pages/home.html", context={
        'html_language': html_language,
        'title': 'home',
    })


def recipes(request, id: int):
    title: str = _('Recipe')

    return render(request, "recipes/pages/recipes-view.html", context={
        'html_language': html_language,
        'title': f'{title} {id}',
    })

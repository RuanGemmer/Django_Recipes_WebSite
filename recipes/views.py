from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation
from utils.recipes.factory import make_recipe

html_language = translation.get_language()


def home(request):
    return render(request, "recipes/pages/home.html", context={
        'html_language': html_language,
        'title': 'Home',
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipes(request, id: int):
    title: str = _('Recipe')

    return render(request, "recipes/pages/recipes-view.html", context={
        'html_language': html_language,
        'title': f'{title} {id}',
        'recipe': make_recipe(),
        'is_detail_page': True,
    })

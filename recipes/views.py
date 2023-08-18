from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

html_language = translation.get_language()


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, "recipes/pages/home.html", context={
        'html_language': html_language,
        'title': 'Home',
        'recipes': recipes,
    })


def category(request, id):
    recipes = Recipe.objects.filter(
        category__id=id, is_published=True
    ).order_by('-id')
    return render(request, "recipes/pages/home.html", context={
        'html_language': html_language,
        'title': 'Home',
        'recipes': recipes,
    })


def recipes(request, id: int):
    recipe = Recipe.objects.filter(
        id=id
    ).first()
    title: str = _('Recipe')

    return render(request, "recipes/pages/recipes-view.html", context={
        'html_language': html_language,
        'title': f'{title} {id}',
        'recipe': recipe,
        'is_detail_page': True,
    })

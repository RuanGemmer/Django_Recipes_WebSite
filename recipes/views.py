from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.utils.translation import gettext as _
from django.utils import translation
from recipes.models import Recipe

html_language = translation.get_language()


def home(request):
    recipes = get_list_or_404(
        Recipe.objects.filter(is_published=True).order_by('-id')
    )

    return render(request, "recipes/pages/home.html", context={
        'html_language': html_language,
        'title': 'Home',
        'recipes': recipes,
    })


def category(request, id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=id, is_published=True
        ).order_by('-id')
    )
    title = _('Category')

    return render(request, "recipes/pages/home.html", context={
        'html_language': html_language,
        'title': f'{title} - {recipes[0].category.name}',
        'recipes': recipes,
    })


def recipes(request, id: int):
    recipe = get_object_or_404(
        Recipe.objects.filter(id=id, is_published=True)
    )
    title: str = _('Recipe')

    return render(request, "recipes/pages/recipes-view.html", context={
        'html_language': html_language,
        'title': f'{title}: {recipe.title}',
        'recipe': recipe,
        'is_detail_page': True,
    })

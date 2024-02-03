from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'pancakes': {
        'молоко, л': 0.5,
        'яйца, шт': 3,
        'масло растительное, ст. ложка': 1,
        'мука, г': 250,
        'сахар, ст. ложка': 1,
        'соль, щепотка': 1,
        'масло сливочное, ст. ложка': 1,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
# можете добавить свои рецепты ;)
}

def recipe_view(request, dish):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            ingridient: amount * servings
            for ingridient, amount
            in DATA.get(dish).items()
        }
    }
    return render(request, 'calculator/index.html', context)

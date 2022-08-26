from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

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
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}





def omlet(request):
    d = {}

    context = {'recipe': d}

    persons = int(request.GET.get("servings", '1'))
    for ingredient, amount in DATA['omlet'].items():
        amount = float("{0:.2f}".format(amount * persons))
        context['recipe'][ingredient] = amount

    return render(request, 'calculator/index.html', context)



def pasta(request):
    d = {}
    context = {'recipe': d}
    persons = int(request.GET.get("servings", '1'))
    for ingredient, amount in DATA['pasta'].items():
        amount = float("{0:.2f}".format(amount * persons))
        context['recipe'][ingredient] = amount
    print(context)
    print(DATA)

    return render(request, 'calculator/index.html', context)

def buter(request):
    d = {}
    context = {'recipe': d}
    persons = int(request.GET.get("servings", '1'))
    for ingredient, amount in DATA['buter'].items():
        amount = amount * persons
        context['recipe'][ingredient] = amount
    print(context)
    print(DATA)

    return render(request, 'calculator/index.html', context)


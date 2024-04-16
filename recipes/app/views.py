from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from .models import Category, Recipe
from .forms import RecipeForm, CategoryForm, LoginForm, RegisterForm
# Create your views here.


def index(request):
    """Home page"""

    categories = Category.objects.all()
    recipes = Recipe.objects.all()
    context = {
        "categories": categories,
        "recipes": recipes
    }

    return render(request, 'app/index.html', context=context)


def all_recipes_by_category(request, category):
    """for View recipes by category"""

    categories = Category.objects.all()
    category = Category.objects.get(name=category)
    recipes = Recipe.objects.filter(category=category)

    context = {
        "categories": categories,
        "recipes": recipes
    }

    return render(request, 'app/index.html', context=context)


def recipe_detail(request, pk):
    """for Recipe view detail"""

    recipe = Recipe.objects.get(pk=pk)
    recipe.views_count += 1
    recipe.save()
    context = {
        "recipe": recipe,
    }

    return render(request, 'app/recipe_detail.html', context=context)


def recipe_create(request):
    """for Recipe create """

    recipe_form = RecipeForm(data=request.POST, files=request.FILES)
    if recipe_form.is_valid():
        recipe_form.save()
        messages.success(request, "Content created successfully!")
        return redirect('index')

    recipe_form = RecipeForm()
    context = {
        'recipe_form': recipe_form,
    }
    return render(request, 'app/recipe_form.html', context=context)


def recipe_update(request, pk):
    """for  Recipe update(change)"""

    recipe = Recipe.objects.get(pk=pk)

    recipe_form = RecipeForm(data=request.POST or None, instance=recipe, files=request.FILES or None)
    if recipe_form.is_valid():
        recipe_form.save()
        messages.info(request, "Content edited successfully!")
        return redirect('index')

    context = {
        'recipe_form': recipe_form,
    }
    return render(request, 'app/recipe_form.html', context=context)


def recipe_delete(request, pk):
    """for recipe delete"""

    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        recipe.delete()
        messages.warning(request, "You have deleted the post!")
        return redirect('index')

    return render(request, 'app/recipe_delete.html', {"recipe": recipe})


def all_categories(request):
    """get all category"""

    categories = Category.objects.all()
    return render(request, 'app/categories.html', context={"categories": categories})


def category_create(request):
    """for category create"""

    category_form = CategoryForm(data=request.POST)
    if category_form.is_valid():
        category_form.save()
        messages.success(request, "Category created successfully!")
        return redirect('all_categories')

    category_form = CategoryForm()
    context = {
        'category_form': category_form,
    }
    return render(request, 'app/category_form.html', context=context)


def category_update(request, pk):
    """for category update"""

    category = Category.objects.get(pk=pk)

    category_form = CategoryForm(data=request.POST or None, instance=category)
    if category_form.is_valid():
        category_form.save()
        messages.info(request, "Category edited successfully!")
        return redirect('all_categories')

    context = {
        'category_form': category_form,
    }
    return render(request, 'app/category_form.html', context=context)


def category_delete(request, pk):
    """for category update"""

    category = Category.objects.get(pk=pk)

    if request.method == 'POST':
        category.delete()
        messages.warning(request, "You have deleted the category!")
        return redirect('all_categories')

    return render(request, 'app/category_delete.html', {"category": category})


def user_login(request):
    """This is for login"""

    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f'{user.username.title()}, you have successfully entered the site.')
        return redirect('index')

    if form.errors:
        messages.error(request, "Check that the fields are correct!")

    form = LoginForm()
    context = {
        'form': form,
        'title': 'Sign in'
    }
    return render(request, 'app/login.html', context=context)


def user_logout(request):
    """This is for logout"""

    logout(request)
    messages.warning(request, "You are logged out!")
    return redirect('login')


def user_register(request):
    """This is for sing up"""

    form = RegisterForm(data=request.POST)
    if form.is_valid():
        form.save()
        messages.info(request, "You can log in by entering your username and password.")
        return redirect('login')

    form = RegisterForm()
    context = {
        'form': form,
        'title': 'Sign up'
    }
    return render(request, 'app/register.html', context=context)


def page_not_found(request):
    """This is for page not found"""

    messages.warning(request, "It's page not found!")
    return render(request, 'app/page_not_found.html')


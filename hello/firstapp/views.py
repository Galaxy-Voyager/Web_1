from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import *
from .forms import UserForm
from django.shortcuts import render
from .models import Person

def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})
    """
    if request.method == "POST":
        name = request.POST.get("name") # получить значение поля Имя
        age = request.POST.get("age")  # получить значение поля Возраст
        output = '<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1} </hЗ>'.format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, 'firstapp/index.html', {'form': userform})
    header = 'Персональные данные'                  #обычная переменная
    langs = ['Английский', 'Немецкий', 'Испанский'] #массив
    user = {'name': 'Максим', 'age': 30}            #словарь
    addr = ('Виноградная', 23, 45)                  #кортеж
    """

def create(request):
    if request.method == 'POST':
        klient = Person()
        klient.name = request.POST.get('name')
        klient.age = request.POST.get('age')
        klient.save()
    return HttpResponseRedirect('/')

def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == 'POST':
            person.name = request.POST.get('name')
            person.age = request.POST.get('age')
            person.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html', {'person': person})
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Клиент не найден</h>')

def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect('/')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Клиент не найден</h2>')


def about(request):
    return HttpResponse('About')

def contact(request):
    return HttpResponseRedirect('/about')

def details(request):
    return HttpResponsePermanentRedirect('/')

def products(request, productid):
    category = request.GET.get('cat', '')
    output = '<h2>Продукт № {0} Категория: {1}</h2>'.format(productid, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get('id', 1)
    name = request.GET.get('name', 'Максим')
    output = '<h2>Пользователь</h2><h3>id: {0} Имя:{1}</h3'.format(id, name)
    return HttpResponse(output)

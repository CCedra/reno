from django.shortcuts import render, redirect # redirect - Перенаправление пользователя
from .models import Task, Prod
from .forms import ProdForm


#Переменной такс присваеваем все объекты содержащиеся в модели Task. При вызове функции возвращаем
#render https://djbook.ru/rel1.8/topics/http/shortcuts.html
def index(request):
    return render(request, 'main/index.html')


def about(request):
    tasks = Prod.objects.all()
    return render(request, 'main/about.html', {'title': 'Наши товары', 'tasks': tasks})



def add_product(request):
    error = ''
    if request.method == 'POST':
        form = ProdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верна'
    form = ProdForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/add_product.html', context)

    


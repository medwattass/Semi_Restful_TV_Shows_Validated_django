from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from datetime import datetime
from django.contrib import messages


def root(request):
    return redirect('/shows')


def shows(request):
    context = {
        "shows": Show.objects.all()
        }	
    return render(request, 'shows.html', context)


def new_show(request):
    return render(request, 'new_show.html')


def edit_show(request, id):
    context = {
        "show": Show.objects.get(id=id)
        }
    return render(request, 'edit_show.html', context)


def show_show(request, id):
    context = {
        "show": Show.objects.get(id=id)
        }
    return render(request, 'show_show.html', context)


def create_show(request):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            title = request.POST.get('title')
            network = request.POST.get('network')
            description = request.POST.get('description')
            release_date = request.POST.get('release_date')
            this_show = Show.objects.create(title=title, network=network, description=description, release_date=release_date)
            print(this_show.id)
            return redirect('/shows/show/'+ str(this_show.id))
    else:
        return HttpResponse('Method not allowed', status=405)


def update_show(request):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        id = request.POST.get('id')
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/shows/edit/' + id)
        else:
            to_update = Show.objects.get(id=id)
            to_update.title = request.POST.get('title')
            to_update.network = request.POST.get('network')
            to_update.description = request.POST.get('description')
            to_update.release_date = datetime.strptime(request.POST.get('release_date'), '%Y-%m-%d')
            to_update.save()
            return redirect ('/shows/show/' + id)
    else:
        return HttpResponse('Method not allowed', status=405)


def delete_show(request, id):
    if request.method == 'POST':
        Show.objects.get(id=id).delete()
        return redirect('/shows')
    else:
        return HttpResponse('Method not allowed', status=405)

from django.shortcuts import render, redirect
from . import models, forms
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
import simplejson


def libraries_list(request):
    libraries = models.Library.objects.all().order_by('-date_created')
    query = request.GET.get('q')
    data = models.Library.objects.values_list('latitude', 'longitude')
    json_data = simplejson.dumps(list(data))

    if query:
        lookups = Q(address__contains=query)
        libraries = models.Library.objects.filter(lookups).order_by('-date_created')

    page = request.GET.get('page', 1)
    paginator = Paginator(libraries, 8)

    try:
        all_libraries = paginator.page(page)
    except PageNotAnInteger:
        all_libraries = paginator.page(1)
    except EmptyPage:
        all_libraries = paginator.page(paginator.num_pages)

    context = {
        "libraries": libraries,
        'all_libraries': all_libraries,
        'json_data': json_data
    }

    return render(request, 'libraries_list.html', context)


def add_library(request):
    if request.method == 'POST':
        form = forms.LibraryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('libraries_list')
        else:
            print(form.errors)

    else:
        form = forms.LibraryForm()

    context = {
        "form": form
    }

    return render(request, "add_library.html", context)

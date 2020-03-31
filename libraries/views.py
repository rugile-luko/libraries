from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import simplejson
import requests
from django.contrib import messages


def home(request):
    api_key = settings.MAPS_API_KEY
    return render(request, "home.html", context={"api_key": api_key})


def libraries_list(request):
    libraries = models.Library.objects.all().order_by('-date_created')
    query = request.GET.get('q')
    data = models.Library.objects.values_list('latitude', 'longitude')
    json_data = simplejson.dumps(list(data))
    query_latitude = None
    query_longitude = None
    count_libraries = libraries.count()
    api_key = settings.MAPS_API_KEY

    if query:
        api_response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(query, api_key))
        api_response_dict = api_response.json()
        if api_response_dict['status'] == 'OK':
            latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            longitude = api_response_dict['results'][0]['geometry']['location']['lng']

        query_latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        query_longitude = api_response_dict['results'][0]['geometry']['location']['lng']

        libraries = []
        json_data = []
        for library in models.Library.objects.all():
            if library.measure_distance(longitude, latitude) < 20:
                libraries.append(library)
                json_data.append([
                    library.latitude,
                    library.longitude
                ])

        count_libraries = len(libraries)
        json_data = simplejson.dumps(json_data)

    page = request.GET.get('page', 1)
    paginator = Paginator(libraries, 8)

    try:
        all_libraries = paginator.page(page)
    except PageNotAnInteger:
        all_libraries = paginator.page(1)
    except EmptyPage:
        all_libraries = paginator.page(paginator.num_pages)

    context = {
        "query": query,
        "libraries": libraries,
        "api_key": api_key,
        'all_libraries': all_libraries,
        'json_data': json_data,
        'query_latitude': query_latitude,
        'query_longitude': query_longitude,
        'count_libraries': count_libraries
    }

    return render(request, 'libraries_list.html', context)


def add_library(request):
    api_key = settings.MAPS_API_KEY
    if request.method == 'POST':
        form = forms.LibraryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Library added successfully!')
            return redirect('libraries_list')
        else:
            messages.error(request, "Something went wrong. Please check if you haven't missed any required fields.")

    else:
        form = forms.LibraryForm()

    context = {
        "form": form,
        "api_key": api_key
    }

    return render(request, "add_library.html", context)


def detail_view(request, pk):
    api_key = settings.MAPS_API_KEY
    library = get_object_or_404(models.Library, pk=pk)

    context = {
        "library": library,
        "api_key": api_key
    }

    return render(request, 'detail_view.html', context)

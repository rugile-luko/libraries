from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import simplejson
import requests


def libraries_list(request):
    libraries = models.Library.objects.all().order_by('-date_created')
    query = request.GET.get('q')
    data = models.Library.objects.values_list('latitude', 'longitude')
    json_data = simplejson.dumps(list(data))
    query_latitude = None
    query_longitude = None
    search_radius = request.GET.get('radius_around_selected_destination')
    count_libraries = libraries.count()

    if query:
        api_key = "AIzaSyDHmd_dI3EZ7JwL6xSHYGJnsFMZe5zBYW4"
        api_response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(query, api_key))
        api_response_dict = api_response.json()
        if api_response_dict['status'] == 'OK':
            latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            longitude = api_response_dict['results'][0]['geometry']['location']['lng']
            print(latitude, longitude)

        query_latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        query_longitude = api_response_dict['results'][0]['geometry']['location']['lng']

        libraries = []
        json_data = []
        for library in models.Library.objects.all():
            if library.measure_distance(longitude, latitude) < float(search_radius):
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
        "search_radius": search_radius,
        "libraries": libraries,
        'all_libraries': all_libraries,
        'json_data': json_data,
        'query_latitude': query_latitude,
        'query_longitude': query_longitude,
        'count_libraries': count_libraries
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


def detail_view(request, pk):
    library = get_object_or_404(models.Library, pk=pk)

    context = {
        "library": library
    }

    return render(request, 'detail_view.html', context)

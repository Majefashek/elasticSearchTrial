from django.shortcuts import render
from .documents import CarDocument

# Create your views here.
def home(request):

    
    # Get the search query parameters from the request
    color = 'farida'  # Default to 'red' if not provided
    #description = request.GET.get('description', 'beautiful')  # Default to 'beautiful' if not provided

    # Perform the search
    s = CarDocument.search().filter("term", color=color)

    # Prepare the results
    results = []
    for hit in s:
        results.append({
            'name': hit.name,
            'color': hit.color,
            'description': hit.description,
            'type': hit.type
        })

    # Render the results in the home.html template
    return render(request, 'home.html', {'results': results})
from django.shortcuts import render
from core_app.models import *
# Create your views here.
def index(rq):
    package=Package.objects.filter(package_status='published',status=True)
    context={
        'package':package
    }
    return render(rq,'Main/index.html',context)

def Package_detail(rq,pid):
    package=Package.objects.get(pid=pid)
    packages=Package.objects.filter(category=package.category)
    p_image=package.p_images.all()
    context={
        'package':package,
        'p_image':p_image,
        'packages':packages
    }
    return render(rq,'package/package-detail.html',context)

def search(rq):
    return render(rq,'search/search.html')

def search_result(request):
    title = request.GET.get('t')
    prefecture=request.GET.get('l')
    description=request.GET.get('d')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Start with all products
    packages = Package.objects.all()

    # Filter by title
    if title:
        packages = packages.filter(title__icontains=title)
    if description:
        packages= packages.filter(description__icontains=description)
    if prefecture:
        packages=packages.filter(prefecture__icontains=prefecture)


    # Filter by price range
    if min_price and max_price:
        packages = packages.filter(price__range=(min_price, max_price))

    # Order the results by date
    packages = packages.order_by('-date')

    context = {
        'title': title,
        'min_price': min_price,
        'max_price': max_price,
        'packages': packages,
        'description':description,
        'prefecture':prefecture
    }
    return render(request,'search/search_result.html',context)


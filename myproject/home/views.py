from django.shortcuts import render,redirect
from .models import Blog
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    data={
        'Blog': Blog.objects.all()
    }
    print(data)
    return render(request,"index.html",data)

def about(request):
    return render(request,"about.html")

def recent(request):
    return render(request,"recent_posts.html")

def add(request):
    return render(request, "add_posts.html")  

def insert(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        
        image_file = request.FILES.get('image')
        
        if image_file:  
            new_blog = Blog(title=title, image=image_file, description=description, date=date)
            new_blog.save()
            return redirect("/")
        else:
            
            return HttpResponse("No image uploaded")
    
    
    return render(request, "/")


def find(request, id):
    fd = {
        "data": Blog.objects.get(id=id)
    }
    return render(request, "find.html",fd)


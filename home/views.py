from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples=[{"name":"neeti","age":30},
    {"name":"himanshu","age":20},
    {"name":"sonika","age":22},
    {"name":"naman","age":23},
    {"name":"tripti","age":12}
    
    ]
    vegetables=["pumpkin","tomato","potato"]
    text="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Tempora, voluptas vero placeat sequi, odio quam commodi vel nostrum, similique nesciunt fugiat. Ipsum, est! Iure ducimus, commodi aliquam labore perferendis totam."
    return render(request,"index.html",context={"peoples":peoples,"text":text,"vegetables":vegetables,"page":"Home"})
def success_page(request):
    return HttpResponse("<h1>Success</h1>")
def about(request):
    return render(request,"about.html",context={"page":"About"})
def contact(request):
    return render(request,"contact.html",context={"page":"Contact"})
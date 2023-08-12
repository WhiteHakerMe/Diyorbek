from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    My_link = Link_me.objects.all()
    My_About = About_Me.objects.all() 
    My_Sill_s = My_Sills.objects.all()
    Post_post = Post_Dizayne.objects.all()
    Home_r = HomeTitle.objects.all()
    Category_ss = Category.objects.all()
    ctx = {
        "My_link":My_link,
        "My_About":My_About,
        "My_Sill_s": My_Sill_s,
        "Post_post":Post_post,
        "Home_r":Home_r,
        "Category_ss":Category_ss
    }
    return render(request, "index.html", ctx)

def Portfolios(request, slug=None):
    Category_ss = Category.objects.all()
    Category_s = Category.objects.get(slug=slug)
    Post_post = Post_Dizayne.objects.all().filter(type_id=Category_s.id)
    ctxs = {
        "Post_post":Post_post,
        "Category_s":Category_s,
        "Category_ss":Category_ss
    }
    return render(request, "portfolio-single-2.html", ctxs)


    
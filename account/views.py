from django.shortcuts import render,redirect
from django.views import generic
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

from .models import Post


@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id = post_id).first()
        if post and post.author == request.user:
            post.delete()

    return render(request,'main/home.html',{"posts":posts})



#Переделать это под класс
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return  render(request,'registration/sign_up.html',{"form": form})


class PostCreation(generic.View):

    model = Post
    template_name = 'main/create_post.html'

    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(self.request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = PostForm(self.request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
            return redirect("/home")
        else:
            return render(self.request, self.template_name, {"form": form})















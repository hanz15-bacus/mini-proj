from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .models import Post, Comment, User
from .forms import LoginForm, RegisterForm
from django.core.exceptions import ValidationError

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post_details.html', {'post': post, 'comments': comments})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user=User.objects.get(username=name,password=password)
                posts = Post.objects.all()
                return render(request,'post_list.html',
                    {'posts':posts})
            except:
                form = LoginForm()
                return render(request,'login.html',{'form':LoginForm()})
    form = LoginForm()
    return render(request,'login.html',{'form':LoginForm})


from django.core.exceptions import ValidationError
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confpassword= form.cleaned_data['confpassword']
            if password and confpassword:
                if password != confpassword:
                    raise ValidationError("Passwords do not match.")

            

            if User.objects.filter(username=username).exists():
                form.add_error(None, 'Username already exists.')
                return render(request, 'register.html', {'form': form})

            new_user = User(username=username, age=age, email=email, password=password)
            new_user.save()
            form = LoginForm()
            return render(request, 'login.html', {'form': form})

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
           

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# -------------------
# Page Views
# -------------------

def home(request):
    return render(request, 'index.html')

def clients(request):
    return render(request, 'clients.html')

def about(request):
    return render(request, 'about.html')

def services(request):   
    return render(request, 'services.html')

def contact(request):    
    return render(request, 'contact.html')


# -------------------
# Authentication Views
# -------------------

def login_view(request):
    """
    Handle login functionality.
    If POST: authenticate user and redirect to home.
    If GET: show login page.
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')


def signup(request):
    """
    Handle signup functionality.
    If POST: validate and create new user, then redirect to login.
    If GET: show signup page.
    """
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate passwords
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        # Check if email exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, 'signup.html')

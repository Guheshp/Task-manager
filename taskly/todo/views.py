from django.shortcuts import render, redirect
from  django.http import HttpResponse

from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import CreateTaskform, UpdateUserForm

from . models import Task



# - Create your views here. -

def home(request):

    return render(request, 'index.html')

# - Dashboard. -

@login_required(login_url='my-signin')
def Dashboard(request):
    return render(request, 'profile/dashboard.html')

# - profile. - 

@login_required(login_url='my-signin')
def Profile(request):
    pass

# - signup. -

def Signup(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request, 'username already exist please try another')
            return redirect("my-signup")

        if User.objects.filter(email=email):
            messages.error(request, 'email is already exist please try another ')
            return redirect("my-signup")
        
        # if len(username) >10:
        #     messages.error(request, ' username must be under 10 charecters')

        if not username.isalnum():
            messages.error(request, 'username must be Alph-number')
            return redirect("my-signup")

        if password1 != password2:
            messages.error(request, 'password not matching please try again')
            return redirect("my-signup")
        

        myuser = User.objects.create_user(username, email, password1)

        myuser.save()

        messages.success(request, 'your account has been created successfully')

        return redirect('my-signin')

    return render(request, 'signup.html')

# - signin. - 

def Signin(request):

    if request.method == 'POST':
        username = request.POST['username'] 
        password1 = request.POST['password1']

        user = authenticate(username=username, password = password1)

        if user is not None:
            auth_login(request, user)
            #name = user.username
            #return render(request, 'index.html', {'name':name})
            return redirect('my-dashboard')
        else:
            messages.error(request,'bad credentials')

    return render(request, 'signin.html')


# - profilemanagement. - 
@login_required(login_url='my-signin')
def ProfileManagement(request):
    if request.method == 'POST':
        
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            print("Form is valid. Redirecting to 'my-dashboard'")
            return redirect('my-dashboard')
        else:
             print("Form is not valid. Errors:", user_form.errors)
             print("Submitted data:", request.POST)
    else:
        user_form = UpdateUserForm(instance=request.user)

    context = {'user_form': user_form}
    return render(request, 'profile/profile-management.html', context=context)



# - signout. - 

def Signout(request):
    auth_logout(request)
    messages.success(request, 'logged out successfully ')
    
    return redirect("")

# - CreateTask. -
@login_required(login_url='my-signin')
def CreateTask(request):

    form = CreateTaskform()
    
    if request.method == 'POST':

        form = CreateTaskform(request.POST)

        if form.is_valid():
           
            task = form.save(commit=False)
           
            task.user = request.user
           
            task.save()
            return redirect("my-Viewtask")
        
    context = { 'form':form }
    
    return render(request, 'profile/create-task.html',context=context)
            
# - ViewTask. -
@login_required(login_url='my-signin')
def ViewTask(request):

    current_user = request.user.id

    task = Task.objects.all().filter(user=current_user)

    context = {'task':task}


    return render(request, 'profile/view-task.html',context)

# - UpdateTask. -
@login_required(login_url='my-signin')
def UpdateTask(request, pk):

    task = Task.objects.get(id=pk)

    form = CreateTaskform(instance=task)

    if request.method == 'POST':

        form = CreateTaskform(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect('my-Viewtask')
        
    context= {'form': form }
        
    return render(request, 'profile/update-task.html',context)

# - DeleteTask. -
@login_required(login_url='my-signin')
def DeleteTask(request, pk):

    task = Task.objects.get(id = pk)

    if request.method == 'POST':

        task.delete()

        return redirect('my-Viewtask')
    
    return render(request, 'profile/delete-task.html')
    




    
#-------------------------------xxxxxxxxxx-------------------------------
# def register(request):
#     return render(request, 'register.html')

# def login(request):
#     return render(request, 'login.html')

# create a task ---
# def createTask(request):

#     form = TaskForm()

#     if request.method == 'POST':

#         form = TaskForm(request.POST)

#         if form.is_valid():
#             form.save()

#             return redirect('view-task')
        
#     context = {'form':form }
    
#     return render(request, 'create-form.html', context=context)

# # view task
# def viewTask(request):
#     task = Task.objects.all()

#     context = {'task':task}

#     return render(request, 'view-task.html', context=context )

#registering or creating a user

# def register(request):

#     form = CreateUserForm()

#     if request.method == 'POST':

#         form = CreateUserForm(request.POST)

#         if form.is_valid():
#             form.save()

#             return HttpResponse('user registerd completed')
    
#     context = {'form' : form }

#     return render(request,'register.html',context=context)        

         
# #login a user 
# def my_login(request):

#     form = LoginForm()

#     if request.method == 'POST':

#         form = LoginForm(request, data = request.POST)

#         if form.is_valid():

#             username = form.POST.get['username']
#             password = form.POST.get['password']

#             user = authenticate(request, username=username, password=password)

#             if user is not None:

#                 auth.login(request, user)

#                 return HttpResponse('you have logged in ')
            
#     context = {'form': form}
            
#     return render(request, 'login.html', context=context) 
    
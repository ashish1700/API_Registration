from django.shortcuts import render, HttpResponse , redirect
from app1.models import task
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.





def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        my_user=User.objects.create_user(uname,email,password)
        my_user.save()
        return redirect('login')
   
    return render(request, 'signup.html')
       
       
   
   
   
   
   
   
    # if request.method == 'POST':
    #     nm = request.POST['your_name']
    #     em = request.POST['your_email']
    #     pas = request.POST['your_pass']
    #     print(nm , em, pas )
    #     user = task( uname = nm, email = em, password =pas)
    #     user.save()
    #     return redirect('login')
    # return render(request,'signup.html')



def loginpage(request):
    if request.method == 'POST':
        nm = request.POST.get('uname')
        pas = request.POST.get('pas')
        user = authenticate(request, username = nm, password = pas)
        if user is not None:
            login(request, user)
            return redirect('home')
            # return render(request,'home')
        else:
            return HttpResponse("invalid credentials")
    return render(request,'login.html')

# def loginpage(request):
#     if request.method == 'POST':
#         fm = AuthenticationForm(request=request, data=request.POST)
#         if fm.is_valid():
#             uname = fm.cleaned_data['uname']
#             upas = fm.cleaned_data['pas']
#             user1 = authenticate(uname = uname, pas =upas)
#             if user1 is not None:
#                 login(request, user1)
#                 return redirect('home')
#     else:
#         fm = AuthenticationForm()
#     fm = AuthenticationForm()
#     return render(request, 'login.html', {'form':fm})

@login_required(login_url='login')
def homepage(request):
    return render (request, 'home.html')


def logoutpage(request):
    logout(request)
    return redirect('login')
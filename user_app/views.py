from django.shortcuts import render,redirect,Http404
from user_app.models import Profile
from user_app.forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def signup(rq):
    form=RegisterForm()
    if rq.method=='POST':
        form=RegisterForm(rq.POST or None)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(rq,f'{username},登録完了しました')
            return redirect('signin')
    else:
        form=RegisterForm()
    context={
        'form':form
    }
    return render(rq,'User_Auth/signup.html',context)
def signin(rq):
    if rq.user.is_authenticated:
        messages.warning(rq,'ログイン済み')
        return redirect('index')
    else:
        if rq.method=='POST':
            email=rq.POST.get('email')
            password=rq.POST.get('password')
            user=authenticate(rq,email=email,password=password)
            if user is not None:
                login(rq,user)
                messages.success(rq,f'{email},ログインしました。')
                return redirect('index')
            else:
                messages.error(rq,'メールアドレスとパスワードに誤りがあります。もう一度入力し直してください')
                return redirect('signin')            
    return render(rq,'User_Auth/signin.html')

def singout(rq):
    logout(rq)
    messages.success(rq,'ログアウしました')
    return redirect('signin')

# def Profile_View(rq):
#     try:
#         user_profile = Profile.objects.get(user=rq.user)
#     except Profile.DoesNotExist:
#         raise Http404("Profile does not exist for this user.")

#     context = {
#         'user_profile': user_profile
#     }

#     return render(rq, 'User_Auth/profile.html', context)



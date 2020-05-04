from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from configuration.models import SiteInfo, SocialAccount, Presentation, UserAccount
from forms.formulaire import LoginForm, RegisterForm



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            avatar = form.cleaned_data.get('avatar')
            user = authenticate(username=username, password=password)
            UserAccount.objects.create(user=user, avatar=avatar)
            return redirect('login')
    else:
        form = RegisterForm()

    info_site = SiteInfo.objects.filter(status=True)[0]
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]
    datas = {
        'form': form,
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
    }
    return render(request, "pages/register.html", datas)


def login_page(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')

    info_site = SiteInfo.objects.filter(status=True)[0]
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]
    datas = {
        'form': form,
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
    }
    return render(request, "pages/login.html", datas)


def logout_page(request):
    logout(request)
    return redirect('login')

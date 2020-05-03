from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from configuration.models import SiteInfo, SocialAccount, Temoignage, Presentation, UserAccount, OtherInfo
from commerce.models import Cathegorie, Produit, Panier
from blog.models import Article, CathegorieArticle, Commentaire, Tag, InstagramFeed
from contact.models import Contact, NewsLetter
from formulaire import ContactForm, LoginForm, RegisterForm


def index(request):
    if request.method == 'POST':
        email = request.POST['newsletter']
        if email:
            news_letter = NewsLetter.objects.create(email=email)
            news_letter.save()
    cath1 = Cathegorie.objects.get(status=True, nom='quality')
    cath2 = Cathegorie.objects.get(status=True, nom='trending')
    product_quality = Produit.objects.filter(status=True, cathegorie=cath1).order_by('-date_update')[:4]
    product_trending = Produit.objects.filter(status=True, cathegorie=cath2)[:6]
    temoignage = Temoignage.objects.filter(status=True)
    info_site = SiteInfo.objects.filter(status=True)[0]
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]
    datas = {
        'product_quality_last': product_quality[0],
        'temoignage': temoignage,
        'product_quality': product_quality[1:],
        'product_trending': product_trending,
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
    }
    return render(request, "index.html", datas)


def about(request):
    if request.method == 'POST':
        email = request.POST['newsletter']
        if email:
            news_letter = NewsLetter.objects.create(email=email)
            news_letter.save()
    autresInfo = OtherInfo.objects.filter(status=True)[0]
    temoignage = Temoignage.objects.filter(status=True)
    info_site = SiteInfo.objects.filter(status=True)[0]
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]
    datas = {
        'autresInfo': autresInfo,
        'info_site': info_site,
        'presentation': presentation,
        'temoignage': temoignage,
        'social_account': social_account,
    }
    return render(request, "about.html", datas)


def blog(request, filtre=None, id=None):
    if request.method == 'POST':
        email = request.POST['newsletter']
        if email:
            news_letter = NewsLetter.objects.create(email=email)
            news_letter.save()

    if filtre == 'cath':
        articles = Article.objects.filter(status=True, cathegorie=id)
    elif filtre == 'tag':
        articles = Article.objects.filter(status=True, tague=id)
    else:
        articles = Article.objects.filter(status=True)

    _paginator = Paginator(articles, 5)
    page = request.GET.get('page')

    try:
        articles_page = _paginator.page(page)
    except PageNotAnInteger: # Si le numero de page n'est pas un entier
        articles_page = _paginator.page(1)
    except EmptyPage: # Si la page est vide
        articles_page = _paginator.page(_paginator.num_pages)

    tags = Tag.objects.filter(status=True)
    instagramfeed = InstagramFeed.objects.filter(status=True).order_by('-date_update')
    cathegories = CathegorieArticle.objects.filter(status=True)
    info_site = SiteInfo.objects.filter(status=True)[0]
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]

    datas = {
        'instagramfeeds':instagramfeed,
        'articles': articles_page,
        'tags': tags,
        'cathegories': cathegories,
        'recent_articles': articles.order_by('-date_update')[:4],
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
    }
    return render(request, "blog.html", datas)


@login_required(login_url='login')
def cart(request):
    if request.method == 'POST':
        email = request.POST['newsletter']
        if email:
            news_letter = NewsLetter.objects.create(email=email)
            news_letter.save()
    user = UserAccount.objects.get(user=request.user)
    entrepot = Panier.objects.filter(user=user, status=True)
    info_site = SiteInfo.objects.filter(status=True)[0]
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]

    _subtotal = [p.produit.prix*p.quantite for p in entrepot]
    subtotal = sum(_subtotal) if _subtotal else 0

    datas = {
        'subtotal': subtotal,
        'entrepot': entrepot,
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
    }
    return render(request, "cart.html", datas)


def checkout(request):
    if request.method == 'POST':
        email = request.POST['newsletter']
        if email:
            news_letter = NewsLetter.objects.create(email=email)
            news_letter.save()
    info_site = SiteInfo.objects.filter(status=True)[0]
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]
    datas = {
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
    }
    return render(request, "checkout.html", datas)


def confirmation(request):
    if request.method == 'POST':
        email = request.POST['newsletter']
        if email:
            news_letter = NewsLetter.objects.create(email=email)
            news_letter.save()
    info_site = SiteInfo.objects.filter(status=True)[0]
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]
    datas = {
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
    }
    return render(request, "confirmation.html", datas)


def contact(request):
    contact_form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactForm()
    autresInfo = OtherInfo.objects.filter(status=True)[0]
    info_site = SiteInfo.objects.filter(status=True)[0]
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]
    datas = {
        'autresInfo': autresInfo,
        'contact_form': contact_form,
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
    }
    return render(request, "contact.html", datas)


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
    return render(request, 'register.html', datas)


def login_page(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                # print('\n\n\n***\n OUI \n*\n\n\n')
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
    return render(request, "login.html", datas)


def logout_page(request):
    logout(request)
    return redirect('login')


def product_list(request, limit=6, search=None, filtre=None, idt=None):
    if request.method == 'POST':
        email = request.POST['newsletter']
        if email:
            news_letter = NewsLetter.objects.create(email=email)
            news_letter.save()

    if filtre == 'cath':
        produits_page = Produit.objects.filter(status=True, cathegorie_id=idt)
    else:
        produits = Produit.objects.filter(status=True)
        _paginator = Paginator(produits, limit)
        page = request.GET.get('page')

        try:
            produits_page = _paginator.page(page)
        except PageNotAnInteger: # Si le numero de page n'est pas un entier
            produits_page = _paginator.page(1)
        except EmptyPage: # Si la page est vide
            produits_page = _paginator.page(_paginator.num_pages)

    cathegories = Cathegorie.objects.filter(status=True)
    autresInfo = OtherInfo.objects.filter(status=True)[0]
    temoignage = Temoignage.objects.filter(status=True)
    info_site = SiteInfo.objects.filter(status=True)[0]
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]
    datas = {
        'cathegories': cathegories.order_by('-date_update'),
        'autresInfo': autresInfo,
        'temoignage': temoignage,
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
        'produits_page': produits_page,
        'limit': limit,
    }
    return render(request, "product_list.html", datas)


def single_blog(request, id):
    _article = get_object_or_404(Article, id=id, status=True)
    if request.method == 'POST':
        try:
            email = request.POST['newsletter']
        except:
            if request.user.is_authenticated:
                commentaire = request.POST['comment']
                if commentaire:
                    user = UserAccount.objects.get(status=True, user=request.user)
                    if user:
                        poster_ommentaire = Commentaire.objects.create(
                            article=_article,
                            user=user,
                            commentaire=commentaire
                            )
                        poster_ommentaire.save()
            else:
                return redirect('login')
        else:
            if email:
                news_letter = NewsLetter.objects.create(email=email)
                news_letter.save()
    instagramfeed = InstagramFeed.objects.filter(status=True)
    autresInfo = OtherInfo.objects.filter(status=True)[0]
    tags = Tag.objects.filter(status=True)
    articles = Article.objects.filter(status=True)
    comment = Commentaire.objects.filter(status=True, article=_article)
    cathegories = CathegorieArticle.objects.filter(status=True)
    info_site = SiteInfo.objects.filter(status=True)[0]
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]
    datas = {
        'autresInfo': autresInfo,
        'instagramfeeds': instagramfeed.order_by('-date_update'),
        'commentaires': comment,
        'article': _article,
        'tags': tags,
        'cathegories': cathegories,
        'recent_articles': articles.order_by('-date_update')[:4],
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
    }
    return render(request, "single-blog.html", datas)


def single_product(request, act=None, id=None):
    produit = get_object_or_404(Produit, status=True, id=id)

    if request.method == 'POST':
        try:
            email = request.POST['newsletter']
        except:
            if request.user.is_authenticated:
                nombre = request.POST['quantite']
                user = UserAccount.objects.get(user=request.user)
                if nombre.isdigit() and user:
                    panier = Panier.objects.create(quantite=int(nombre), produit=produit, user=user)
                    panier.save()
                    return redirect('cart')
        else:
            if email:
                news_letter = NewsLetter.objects.create(email=email)
                news_letter.save()
    if act == 'rm':
        if request.user.is_authenticated:
            user = UserAccount.objects.get(user=request.user)
            panier = Panier.objects.get(status=True, produit_id=id, user=user)
            panier.delete()

    try:
        deja_dans_le_panier = Panier.objects.get(produit=produit, status=True)
    except:
        deja_dans_le_panier = None

    info_site = SiteInfo.objects.filter(status=True)[0]
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]
    datas = {
        'deja_dans_le_panier':deja_dans_le_panier,
        'produit': produit,
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
    }
    return render(request, "single-product.html", datas)

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

# Create your views here.
from configuration.models import SiteInfo, SocialAccount, Temoignage, Presentation, UserAccount, OtherInfo
from commerce.models import Cathegorie, Produit, Panier
from contact.models import NewsLetter



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
    return render(request, "pages/cart.html", datas)



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
    return render(request, "pages/checkout.html", datas)



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
    return render(request, "pages/confirmation.html", datas)



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
    return render(request, "pages/product_list.html", datas)



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
    return render(request, "pages/single-product.html", datas)

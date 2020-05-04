from django.shortcuts import render

from configuration.models import SiteInfo, SocialAccount, Temoignage, Presentation, OtherInfo
from commerce.models import Cathegorie, Produit
from contact.models import NewsLetter



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
    return render(request, "pages/index.html", datas)


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
    return render(request, "pages/about.html", datas)

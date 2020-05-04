from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from configuration.models import SiteInfo, SocialAccount, Presentation, UserAccount, OtherInfo
from blog.models import Article, CathegorieArticle, Commentaire, Tag, InstagramFeed
from contact.models import NewsLetter


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
    return render(request, "pages/blog.html", datas)



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
    return render(request, "pages/single-blog.html", datas)

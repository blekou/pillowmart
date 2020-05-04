from django.shortcuts import render

# Create your views here.
from configuration.models import SiteInfo, SocialAccount, OtherInfo, Presentation
from forms.formulaire import ContactForm


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
    return render(request, "pages/contact.html", datas)

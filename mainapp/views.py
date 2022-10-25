from xmlrpc.client import Server
from django.shortcuts import render, redirect
from .models import *
from siteSettings.models import Favicon
from contacts.models import *
from services.models import *
from portfolio.models import *
from aboutUs.models import *
from siteSettings.models import *
from .forms import ApplicationForm

from .bot import send_application

from .models import MetaTag as MainappMetaTag
from services.models import MetaTag as ServiceMetaTag
from portfolio.models import MetaTag as PortfolioMetaTag
from contacts.models import MetaTag as ContactMetaTag
from aboutUs.models import MetaTag as AboutMetaTag


# Create your views here.


def index(request):
    favicons = Favicon.objects.all()

    links = SocialMedia.objects.all()

    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    firsts = FirstBlock.objects.all()
    seconds = SecondBlock.objects.all()
    thirds = ThirdBlock.objects.all()

    metatags = MainappMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'links': links,
        'title': 'Главная',
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'firsts': firsts,
        'seconds': seconds,
        'thirds': thirds,
        'metatags': metatags,
    }

    return render(request, 'index.html', context)


def services(request):
    services = Service.objects.all()

    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()
    links = SocialMedia.objects.all()
    favicons = Favicon.objects.all()

    metatags = ServiceMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'title': 'Услуги',
        'services': services,
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags,
        'links': links,
    }

    return render(request, 'services.html', context)


def portfolio(request):
    portfolios = Portfolio.objects.all()

    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()
    links = SocialMedia.objects.all()
    favicons = Favicon.objects.all()

    metatags = PortfolioMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'title': 'Портфолио',
        'portfolios': portfolios,
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags,
        'links': links
    }

    return render(request, 'portfolio.html', context)


def contacts(request):
    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()
    links = SocialMedia.objects.all()
    favicons = Favicon.objects.all()

    metatags = ContactMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'title': 'Контакты',
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags,
        'links': links
    }
    return render(request, 'contact.html', context)


def about(request):
    teams = Team.objects.all()
    abouts = AboutUs.objects.all()
    links = SocialMedia.objects.all()
    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    favicons = Favicon.objects.all()

    metatags = AboutMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'title': 'О нас',
        'teams': teams,
        'abouts': abouts,
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags,
        'links': links
    }

    return render(request, 'about.html', context)


def services_more(request, id):
    service = Service.objects.get(id=id)
    links = SocialMedia.objects.all()
    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    favicons = Favicon.objects.all()

    metatags = ServiceMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'service': service,
        'title': service.service_ru,
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags,
        'links': links
    }

    return render(request, './pages/interior.html', context)


def application(request):
    form = ApplicationForm

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        send_application(name, phone, email)

        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'index.html', context)


# UZ
def uz_index(request):
    favicons = Favicon.objects.all()

    links = SocialMedia.objects.all()

    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    firsts = FirstBlock.objects.all()
    seconds = SecondBlock.objects.all()
    thirds = ThirdBlock.objects.all()

    metatags = MetaTag.objects.all()

    context = {
        'favicons': favicons,
        'links': links,
        'title': 'Bosh sahifa',
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'firsts': firsts,
        'seconds': seconds,
        'thirds': thirds,
        'metatags': metatags,
    }

    return render(request, 'uz_index.html', context)


def uz_services(request):
    services = Service.objects.all()

    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    links = SocialMedia.objects.all()

    favicons = Favicon.objects.all()

    metatags = ServiceMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'links': links,
        'title': 'Bizning xizmatlarimiz',
        'services': services,
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags
    }

    return render(request, 'uz_services.html', context)


def uz_portfolio(request):
    portfolios = Portfolio.objects.all()
    links = SocialMedia.objects.all()

    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    favicons = Favicon.objects.all()

    metatags = PortfolioMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'links': links,
        'title': 'Portfolio',
        'portfolios': portfolios,
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags
    }

    return render(request, 'uz_portfolio.html', context)


def uz_contacts(request):
    links = SocialMedia.objects.all()
    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    favicons = Favicon.objects.all()

    metatags = ContactMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'links': links,
        'title': 'Biz bilan aloqa',
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags
    }
    return render(request, 'uz_contact.html', context)


def uz_about(request):
    teams = Team.objects.all()
    abouts = AboutUs.objects.all()

    links = SocialMedia.objects.all()
    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    favicons = Favicon.objects.all()

    metatags = AboutMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'links': links,
        'title': 'Kompaniyamiz haqida',
        'teams': teams,
        'abouts': abouts,
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags
    }

    return render(request, 'uz_about.html', context)


def uz_services_more(request, id):
    service = Service.objects.get(id=id)

    links = SocialMedia.objects.all()
    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    favicons = Favicon.objects.all()

    metatags = ServiceMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'service': service,
        'links': links,
        'title': service.service_uz,
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags
    }

    return render(request, './pages/uz_interior.html', context)


# EN
def en_index(request):
    favicons = Favicon.objects.all()

    links = SocialMedia.objects.all()

    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    firsts = FirstBlock.objects.all()
    seconds = SecondBlock.objects.all()
    thirds = ThirdBlock.objects.all()

    metatags = MetaTag.objects.all()

    context = {
        'favicons': favicons,
        'links': links,
        'title': 'Home page',
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'firsts': firsts,
        'seconds': seconds,
        'thirds': thirds,
        'metatags': metatags,
    }

    return render(request, 'en_index.html', context)


def en_services(request):
    services = Service.objects.all()

    links = SocialMedia.objects.all()
    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    favicons = Favicon.objects.all()

    metatags = ServiceMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'title': 'Our services',
        'links': links,
        'services': services,
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags
    }

    return render(request, 'en_services.html', context)


def en_portfolio(request):
    portfolios = Portfolio.objects.all()

    links = SocialMedia.objects.all()
    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    favicons = Favicon.objects.all()

    metatags = PortfolioMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'title': 'Portfolio',
        'links': links,
        'portfolios': portfolios,
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags
    }

    return render(request, 'en_portfolio.html', context)


def en_contacts(request):
    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    links = SocialMedia.objects.all()
    favicons = Favicon.objects.all()

    metatags = ContactMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'title': 'Contacts',
        'links': links,
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags
    }
    return render(request, 'en_contact.html', context)


def en_about(request):
    teams = Team.objects.all()
    abouts = AboutUs.objects.all()

    links = SocialMedia.objects.all()
    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    favicons = Favicon.objects.all()

    metatags = AboutMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'title': 'About us',
        'links': links,
        'teams': teams,
        'abouts': abouts,
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags
    }

    return render(request, 'en_about.html', context)


def en_services_more(request, id):
    service = Service.objects.get(id=id)

    links = SocialMedia.objects.all()
    emails = Email.objects.all()
    phones = Phone.objects.all()
    addresses = Address.objects.all()

    favicons = Favicon.objects.all()

    metatags = ServiceMetaTag.objects.all()

    context = {
        'favicons': favicons,
        'service': service,
        'links': links,
        'title': service.service_en,
        'emails': emails,
        'phones': phones,
        'addresses': addresses,
        'metatags': metatags
    }

    return render(request, './pages/en_interior.html', context)

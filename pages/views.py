# from django.http import HttpResponse
from django.views.generic import TemplateView

# def homePageView(request):
#     return HttpResponse("안녕하세요 :)")

class HomePageView(TemplateView):
    template_name = "home.html"


class LocationPageView(TemplateView):
    template_name = "location.html"


class TermsPageView(TemplateView):
    template_name = "terms.html"
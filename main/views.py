from django.views.generic import TemplateView


class PageIndex(TemplateView):
    template_name='main/index.html'

class PageMain(TemplateView):
    template_name='main/main.html'
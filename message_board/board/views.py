from django.views.generic import TemplateView

#представление главной страницы, чтобы отобразить свпй шаблон
class IndexPage(TemplateView):
    template_name = 'default.html'
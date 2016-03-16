from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_template_names(self):
        prefix = 'desktop'
        if self.request.flavour == 'mobile':
            prefix = 'mobile'
        return ['%s/%s' % (prefix, self.template_name)]

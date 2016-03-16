from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_template_names(self):
        prefix = 'desktop'
        if self.request.flavour == 'mobile':
            prefix = 'mobile'
        return ['%s/%s' % (prefix, self.template_name)]

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['sidebar'] = True
        if 'layout' in self.request.GET:
            if self.request.GET['layout'] == 'topless':
                context_data['topless'] = True
            elif self.request.GET['layout'] == 'body':
                context_data['topless'] = True
                context_data['bottomless'] = True
                context_data['sidebar'] = False

        print(context_data)
        return context_data

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

class FirstTemplateView(LoginRequiredMixin, TemplateView):
    def get_template_names(self):
        template_name = "first.html"
        return template_name

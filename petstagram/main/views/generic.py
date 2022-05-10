from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

from petstagram.main.models import PetPhoto


class HomePageView(TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_adititonal_nav_items'] = True
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')

        return super().dispatch(request, *args, **kwargs)

class DashboardView(ListView):
    model = PetPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pets_photos'



def handle_404(request):
    return render(request, 'main/401_error.html')
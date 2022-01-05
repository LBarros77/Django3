from django.shortcuts import render
from django.utils.formats import date_format
from django.views.generic import ListView, DetailView
from .models import Sale
from .form import SaleSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin

def home_view(request):
    form = SaleSearchForm(request.POST or None)

    # if request.POST:
    #     date_from = request.POST.get('date_from')
    #     date_to = request.POST.get('date_to')
    #     char_type = request.POST.get('char_type')
    #     print(date_from, date_to, char_type)

    context = {
        'form': form,
    }
    return render(request, 'sales/home.html', context)

class SaleListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'sales/main.html'

class SaleDatailView(LoginRequiredMixin, DetailView):
    model = Sale
    template_name = 'sales/detail.html'

def sale_list_view(request):
    qs = Sale.objects.all()
    return render(request, 'sales/main.html', {'qs': qs})

def sale_detail_view(request, **kwargs):
    pk = kwargs.get('pk')
    obj = Sale.objects.get(pk=pk)
    # or
    # obj = get_object_or_404(Sale, pk=pk)
    return render(request, 'sales/detail.html', {'object': obj})
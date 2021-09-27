from django.http.response import HttpResponse
from core.forms import AchadoForm, PerdidoForm
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.generic import ListView
from .models import *
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
# Create your views here.

def relatorio_perdidos(request):
    perdidos = Perdido.objects.all().order_by('-id')

    html_string = render_to_string('core/relatorio_perdidos.html', {'perdidos':perdidos})
    html = HTML(string=html_string)
    result = html.write_pdf()

    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=relatorio_perdidos.pdf'

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb+')
        response.write(output.read())
    
    return response

def index(request):
    categorias = Categoria.objects.all()
    perdidos = Perdido.objects.all()
    achados = Achado.objects.all()
    ultimo_perdido = perdidos.order_by('-data_registro')
    ultimo_achado = achados.order_by('-data_registro')

    context = {
        'categorias': categorias,
        'perdidos': perdidos[:4],
        'achados': achados[:4],
        'ultimo_perdido': ultimo_perdido[0],
        'ultimo_achado': ultimo_achado[0],
        'form_perdido': PerdidoForm(),
        'form_achado': AchadoForm(),
    }
    return render(request, context = context,template_name = "core/index.html")

def perdidos(request):
    categorias = Categoria.objects.all()
    perdidos = Perdido.objects.all().order_by('-data_perdido')
    achados = Achado.objects.all()
    ultimo_perdido = perdidos.order_by('-data_registro')
    ultimo_achado = achados.order_by('-data_registro')

    if request.method == 'POST':
        form = PerdidoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:index')

    context = {
        'categorias': categorias,
        'perdidos': perdidos,
        'ultimo_perdido': ultimo_perdido[0],
        'ultimo_achado': ultimo_achado[0],
    }
    return render(request, context = context,template_name = "core/perdidos.html")

def achados(request):
    categorias = Categoria.objects.all()
    perdidos = Perdido.objects.all().order_by('-data_perdido')
    achados = Achado.objects.all()
    ultimo_perdido = perdidos.order_by('-data_registro')
    ultimo_achado = achados.order_by('-data_registro')
    if request.method == 'POST':
        form = AchadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    context = {
        'categorias': categorias,
        'achados': achados,
        'ultimo_perdido': ultimo_perdido[0],
        'ultimo_achado': ultimo_achado[0],
    }
    return render(request, context = context,template_name = "core/achados.html")

def detalhes_achado(request, pk):        
    achado = Achado.objects.get(pk=pk)
    context = {
        'detalhe': achado
    }
    return render(request, context=context, template_name='core/detalhes.html')

def detalhes_perdido(request, pk):
    perdido = Perdido.objects.get(pk=pk)
    context = {
        'detalhe': perdido
    }
    return render(request, context=context, template_name='core/detalhes.html')


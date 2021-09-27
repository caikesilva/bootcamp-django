from django.core.files.images import ImageFile
from django.db.models import fields
from django.db.models.fields.files import ImageField, ImageFieldFile
from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea
from .models import *
from django import forms

class PerdidoForm(ModelForm):
    class Meta:
        model = Perdido
        fields = '__all__'
        exclude = ['resolvido','data_registro']
    
    nomecompleto = forms.CharField(
        widget = forms.TextInput(
            attrs= {
                'type':'text',
                'class':'form-control',
                'placeholder':'Nome do perdido'
                
            }
        ),
        label='Nome completo*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )

    tipo_item = forms.ModelChoiceField(
        queryset= Categoria.objects.select_related().order_by('nome'),
        widget=forms.Select(attrs={'placeholder':'Categoria','class':'form-control',}),
        label='Categoria',
        empty_label='Selecione uma categoria',
        required=True
    )

    numero = forms.CharField(
        widget = forms.TextInput(
            attrs= {
                'type':'text',
                'class':'form-control',
                'placeholder':'Nº de referencia'
            }
        ),
        label='Nº de referencia*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )

    bairro = forms.CharField(
        widget = forms.DateInput(
            attrs= {
                'type':'text',
                'class':'form-control',
                'placeholder':'Bairro'
            }
        ),
        label='Bairro*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )

    declarante = forms.CharField(
        widget = forms.DateInput(
            attrs= {
                'type':'text',
                'class':'form-control',
                'placeholder':'Quem achou?'
            }
        ),
        label='Declarante*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )

    data_perdido = forms.CharField(
        widget = forms.DateInput(
            attrs= {
                'type':'date',
                'class':'form-control',
                'placeholder':'Data perdido'
            }
        ),
        label='Data perdido*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )

    photo = forms.FileInput(
        attrs={
            'class':'form-control',
        }
    )

    descricao = forms.CharField(
        widget=TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Descrição...',
            }
        ),
        max_length=50,
        label='Descrição'
    )


class AchadoForm(ModelForm):
    class Meta:
        model = Achado
        fields = '__all__'
        exclude = ['resolvido','data_registro']
    
    nomecompleto = forms.CharField(
        widget = forms.TextInput(
            attrs= {
                'type':'text',
                'class':'form-control',
                'placeholder':'Nome do achado'
                
            }
        ),
        label='Nome completo*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )

    tipo_item = forms.ModelChoiceField(
        queryset= Categoria.objects.select_related().order_by('nome'),
        widget=forms.Select(attrs={'placeholder':'Categoria','class':'form-control',}),
        label='Categoria',
        empty_label='Selecione uma categoria',
        required=True
    )

    numero = forms.CharField(
        widget = forms.TextInput(
            attrs= {
                'type':'text',
                'class':'form-control',
                'placeholder':'Nº de referencia'
            }
        ),
        label='Nº de referencia*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )

    bairro = forms.CharField(
        widget = forms.DateInput(
            attrs= {
                'type':'text',
                'class':'form-control',
                'placeholder':'Bairro'
            }
        ),
        label='Bairro*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )

    declarante = forms.CharField(
        widget = forms.DateInput(
            attrs= {
                'type':'text',
                'class':'form-control',
                'placeholder':'Quem achou?'
            }
        ),
        label='Declarante*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )

    data_achado = forms.CharField(
        widget = forms.DateInput(
            attrs= {
                'type':'date',
                'class':'form-control',
                'placeholder':'Data achado'
            }
        ),
        label='Data achado*',
        max_length=50,
        required=True,
        help_text='Obrigatorio'
    )

    photo = forms.ImageField(
        widget=forms.FileInput(
            attrs= {
                'class':'form-control',
            }
        )
    )

    descricao = forms.CharField(
        widget=TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Descrição...',
            }
        ),
        max_length=50,
        label='Descrição'
    )


  
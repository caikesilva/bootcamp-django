from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=255, null=False, verbose_name='Nome categoria')
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

class Perdido(models.Model):
    class Meta:
        verbose_name = 'Perdido'
        verbose_name_plural = 'Perdidos'
        ordering = ['id','nomecompleto']
    
    nomecompleto = models.CharField(max_length=255, verbose_name="Nome completo")
    tipo_item = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    numero = models.CharField(max_length=30, verbose_name="Numero")
    bairro = models.CharField(max_length=30, verbose_name="Bairro")
    declarante = models.CharField(max_length=30, verbose_name="Declarante")
    data_perdido = models.DateField(verbose_name="Data")
    data_registro = models.DateField(default=timezone.now)
    photo = models.ImageField(upload_to="itens_perdidos")
    descricao = models.TextField(max_length=255,verbose_name="Descrição")
    resolvido = models.BooleanField(default=False, verbose_name="Resolvido")
    
    def __str__(self):
        return self.nomecompleto

class Achado(models.Model):
    class Meta:
        verbose_name = 'Achado'
        verbose_name_plural = 'Achados'
        ordering = ['id','nomecompleto']
    
    nomecompleto = models.CharField(max_length=255, verbose_name="Nome completo")
    tipo_item = models.ForeignKey(Categoria, on_delete=models.CASCADE,verbose_name="Categoria")
    numero = models.CharField(max_length=30, verbose_name="Numero")
    bairro = models.CharField(max_length=30, verbose_name="Bairro")
    declarante = models.CharField(max_length=30, verbose_name="Declarante")
    data_achado = models.DateField(verbose_name="Data")
    data_registro = models.DateField(default=timezone.now)
    photo = models.ImageField(upload_to="itens_perdidos")
    descricao = models.TextField(max_length=255,verbose_name="Descrição")
    resolvido = models.BooleanField(default=False, verbose_name="Resolvido")

    def __str__(self):
        return self.nomecompleto
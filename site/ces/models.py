from django.db import models
from django.utils import timezone
from datetime import datetime


class TipoObjeto(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de objeto"
        verbose_name_plural = "Tipos de objeto"


class Objeto(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    codigo = models.CharField(unique=True, max_length=50, blank=False, null=False)
    nome = models.CharField(unique=True, max_length=50, blank=False, null=False)
    tipoObjeto_id = models.ForeignKey(TipoObjeto)

    def __str__(self):
        return self.nome


class PerfilUsuario(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    nome = models.CharField(max_length=50, blank=True, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Perfil de usuário"
        verbose_name_plural = "Perfis de usuário"


class Usuario(models.Model):
    id= models.AutoField(primary_key=True, blank=False, null=False)
    nome = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=50, unique=True, blank=False,)
    senha = models.TextField(blank=False, null=False)
    perfilUsuario_id = models.ForeignKey(PerfilUsuario)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Movimentacao(models.Model):
    id= models.AutoField(primary_key=True, blank=False, null=False)
    retirada = models.DateTimeField(null=True, blank=True)
    devolucao = models.DateTimeField(null=True, blank=True)
    objeto_id = models.ForeignKey(Objeto)
    usuario_id = models.ForeignKey(Usuario)

    def __str__(self):
        return str("{0} para {1}").format(self.objeto_id, self.usuario_id)

    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"


class Permissao_Objeto_x_Usuario(models.Model):
    id= models.AutoField(primary_key=True, blank=False, null=False)
    objeto_id = models.ForeignKey(Objeto)
    usuario_id = models.ForeignKey(Usuario)

    def __str__(self):
        return str(self.id)


class Permissao_Objeto_x_PerfilUsuario(models.Model):
    id= models.AutoField(primary_key=True, blank=False, null=False)
    tipoObjeto_id = models.ForeignKey(TipoObjeto)
    perfilUsuario_id = models.ForeignKey(PerfilUsuario)

    def __str__(self):
        return str(self.id)


class AdminWeb(models.Model):
    id= models.AutoField(primary_key=True, blank=False, null=False)
    tipoObjeto_id = models.ForeignKey(TipoObjeto)
    usuario_id = models.ForeignKey(Usuario)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Admin web"
        verbose_name_plural = "Admins web"

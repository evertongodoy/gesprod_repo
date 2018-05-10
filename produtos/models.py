from django.db import models

# Create your models here.

# Classes que desrevem o modelo do negocio
# upload_to = Caso voce queira salvar em uma  pasta especial dentro da pasta de medias
# file will be uploaded to MEDIA_ROOT/uploads
 # Ex: upload = models.FileField(upload_to='uploads/')

class Produto(models.Model):

    id_produto = models.AutoField(primary_key=True, editable=False)
    descricao = models.CharField(max_length=50)
    preco_custo = models.DecimalField(max_digits=8, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=8, decimal_places=2)
    observacao = models.TextField(null=True, blank=True)
    # Automatically set the field to NOW every time the object is saved. Useful for “last-modified” timestamps
    data_criacao = models.DateField(
    	auto_now=False, auto_now_add=True
    )
    imagem = models.ImageField(upload_to='imagens_produto', null=True, blank=True)

    # define your custom name  https://stackoverflow.com/questions/32657766/how-to-control-table-names-created-by-django-migrate
    class Meta:
        db_table = 'produto' 

    def __str__(self):
        return self.descricao
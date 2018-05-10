from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from produtos.models import Produto
from produtos.forms import ProdutoForm

@login_required
def prod_list(request):
    # prods = Produto.objects.get(id=10)
    prods = Produto.objects.all()

    return render(request, 'lista_produtos.html', {'lst_prod' : prods})


@login_required
def prod_new(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('prod_list')

    return render(request, 'produto_form.html', {'formulario': form})


@login_required
def prod_upd(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('prod_list')

    return render(request, 'produto_form.html', {'formulario': form})


@login_required
def prod_del(request, id):
    produto = get_object_or_404(Produto, pk=id)
    # form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

    if request.method == 'POST':
        produto.delete()
        return redirect('prod_list')

    return render(request, 'produto_del_confirm.html', {'prod': produto})

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from services.mercadopago.mercadopago import get_preference, get_payment
from pagamento.models import PagamentoMercadoPago
from pedido.models import Pedido
from .models import Pedido
from checkout.models import Carrinho
from django.urls import reverse


@login_required
def pedido_finalizado_mercado_pago(request):
    if not 'mercado_pago_id' in request.session:
        pedido_id = int(request.session['pedido'])
        return redirect("pedido:pedido", pk=pedido_id)

    mercado_pago_id = request.session['mercado_pago_id']
    payment_id = request.GET.get('payment_id')

    preference = get_preference(mercado_pago_id)
    payment = get_payment(payment_id)

    # Atualiza os dados do mercado pago na tabela de pagamento
    PagamentoMercadoPago.objects.filter(
        mercado_pago_id=mercado_pago_id).update(
            transaction_amount=payment['transaction_amount'],
            installments=payment['installments'],
            payment_method_id=payment['payment_method_id'],
            mercado_pago_status=payment['status'],
            mercado_pago_status_detail=payment['status_detail'],
            payment_id=payment_id
    )
    pagamento_mp = PagamentoMercadoPago.objects.get(
        mercado_pago_id=mercado_pago_id)

    # Atualiza os dados do pagamento no pedido
    Pedido.objects.filter(pk=pagamento_mp.pedido.id).update(pago=True)
    carrinho_uuid = request.session['carrinho']
    Carrinho.objects.filter(uuid=carrinho_uuid).update(
        abandonado=False, finalizado=True)
    del request.session['carrinho']
    del request.session['mercado_pago_id']

    return redirect("pedido:pedido", pk=pagamento_mp.pedido.id)


class PedidoDetailView(LoginRequiredMixin, DetailView):
    template_name = 'pedido/pedido.html'
    model = Pedido
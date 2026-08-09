import { patch } from "@web/core/utils/patch";
import OrderPaymentValidation from "@point_of_sale/app/utils/order_payment_validation";

patch(OrderPaymentValidation.prototype, {
    /**
     * Toda a venda em Portugal já gera um documento certificado (Fatura Simplificada
     * ou Fatura, série FS/FT) por obrigação legal — `action_pos_order_paid` em
     * pos_order.py força `to_invoice=True` no servidor mesmo quando o operador não
     * pediu fatura explicitamente. Sem esta sobreposição, o core mostraria/descarregaria
     * sempre o PDF A4 (vê `finalizeValidation` em order_payment_validation.js: usa
     * `isToInvoice()`, que reflete esse valor já forçado, não a intenção original do
     * operador). O talão impresso pelo ePOS já traz QR/ATCUD/hash e satisfaz sozinho a
     * obrigação legal — o popup do PDF A4 nunca é necessário aqui, mesmo quando o
     * operador pede fatura a sério com o NIF do cliente (decisão explícita do utilizador).
     */
    shouldDownloadInvoice() {
        if (this.order.l10n_pt_nortelix_atcud) {
            return false;
        }
        return super.shouldDownloadInvoice(...arguments);
    },
});

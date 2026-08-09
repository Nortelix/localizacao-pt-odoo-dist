{
    "name": "Portugal - Certificação Fiscal AT nas Encomendas de Venda (Nortelix)",
    "version": "19.0.1.0.0",
    "category": "Accounting/Localizations",
    "summary": "Assinatura digital de Notas de Encomenda (documento de conferência, WorkingDocuments no SAF-T)",
    "description": """
Estende `l10n_pt_nortelix_cert` às encomendas de venda (`sale.order`): assina
digitalmente (cadeia de hash, Portaria 363/2010) e atribui ATCUD/QR Code a uma
encomenda no momento em que é confirmada — o "documento suscetível de ser entregue ao
cliente para conferência de transmissão de bens ou de prestação de serviços" (Ofício AT
101/2026, ponto 5.3; WorkType "NE" — Nota de Encomenda — no schema SAF-T-PT 1.04_01).

Ao contrário das guias de transporte, este tipo de documento NÃO tem comunicação em
tempo real por webservice próprio — só é reportado no ficheiro SAF-T mensal (secção
WorkingDocuments, ver `l10n_pt_nortelix_cert_saft`, que passa a incluir essa secção
automaticamente quando este módulo está instalado, sem precisar dele como dependência).

Quando uma fatura é criada a partir de uma encomenda confirmada, a Odoo já preenche
`invoice_origin` com o nome da encomenda — o que já alimenta o elemento
Line/OrderReferences existente em `l10n_pt_nortelix_cert_saft` sem trabalho adicional
(ponto 5.4 do ofício).
""",
    "author": "Nortelix",
    "license": "OPL-1",
    "depends": ["l10n_pt_nortelix_cert", "sale"],
    "data": [
        "data/at_series_type_data.xml",
        "views/sale_order_views.xml",
        "report/report_sale_order_at.xml",
    ],
    "installable": True,
    "application": True,
}

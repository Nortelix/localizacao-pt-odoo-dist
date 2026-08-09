{
    "name": "Portugal - Certificação Fiscal AT (Nortelix)",
    "version": "19.0.1.0.0",
    "category": "Accounting/Localizations",
    "summary": "Séries comunicadas, ATCUD, cadeia de hash/assinatura RSA e QR Code para faturação certificável pela AT",
    "description": """
Módulo standalone de suporte técnico à certificação de software de faturação
junto da Autoridade Tributária e Aduaneira (AT) portuguesa.

Este módulo NÃO concede, por si só, um número de certificado AT: implementa os
requisitos técnicos (séries comunicadas, ATCUD, cadeia de hash com assinatura
RSA local, QR Code) necessários para submeter o software a certificação.
A submissão formal é um processo administrativo externo, da responsabilidade
do produtor de software.

Depende apenas de `account`, para funcionar em Odoo Community e Enterprise.
""",
    "author": "Nortelix",
    "license": "OPL-1",
    "depends": ["account", "base_setup"],
    "external_dependencies": {
        "python": ["zeep", "lxml", "cryptography"],
    },
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/at_series_type_data.xml",
        "data/ir_cron_data.xml",
        "wizard/at_series_communicate_wizard_views.xml",
        "views/at_series_views.xml",
        "views/res_company_views.xml",
        "views/account_move_views.xml",
        "views/account_payment_views.xml",
        "views/account_tax_views.xml",
        "views/product_product_views.xml",
        "views/res_config_settings_views.xml",
        "report/report_invoice_at.xml",
        "report/report_payment_receipt_at.xml",
    ],
    "installable": True,
    "application": True,
}

{
    "name": "Portugal - Certificação Fiscal AT no POS (Nortelix)",
    "version": "19.0.1.0.0",
    "category": "Accounting/Localizations",
    "summary": "Fatura Simplificada automática, cliente Consumidor Final e licenciamento por capacidade para o Ponto de Venda",
    "description": """
Estende `l10n_pt_nortelix_cert` ao Ponto de Venda (POS): toda a venda confirmada gera
automaticamente um documento certificado (Fatura Simplificada — série "FS" — quando o
cliente não se identifica, ou Fatura normal — série "FT" — quando um cliente com NIF
próprio é indicado), reaproveitando inteiramente a assinatura/QR/ATCUD já existentes
para faturas.

Inclui um cliente "Consumidor Final" (NIF 999999990) nativo, usado por omissão quando
nenhum cliente é escolhido no POS.

O uso do POS é uma capacidade da licença Nortelix à parte da faturação normal — tem de
estar explicitamente ativada (ver módulo `l10n_pt_nortelix_licensing_admin`).
""",
    "author": "Nortelix",
    "license": "OPL-1",
    "depends": ["l10n_pt_nortelix_cert", "point_of_sale"],
    "data": [
        "data/res_partner_data.xml",
        "views/pos_config_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "l10n_pt_nortelix_cert_pos/static/src/**/*",
        ],
    },
    "installable": True,
    "application": True,
}

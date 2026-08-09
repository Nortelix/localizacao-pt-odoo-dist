{
    "name": "Portugal - Certificação Fiscal AT nos Documentos de Transporte (Nortelix)",
    "version": "19.0.1.0.0",
    "category": "Accounting/Localizations",
    "summary": "Comunicação em tempo real de guias de transporte/remessa à AT (Documentos de Transporte)",
    "description": """
Estende `l10n_pt_nortelix_cert` às guias de transporte/remessa (`stock.picking`):
comunica os elementos das guias à AT em tempo real, logo que a guia é confirmada
("Marcar como a Fazer" — antes da mercadoria sair, não só quando é validada/concluída,
que já é tarde demais para o documento acompanhar o transporte), através do
webservice de Documentos de Transporte (`documentosTransporte.wsdl`, distinto do
e-Fatura), reaproveitando a mesma infraestrutura de séries/ATCUD e de assinatura digital
(cadeia de hash, Portaria 363/2010) já usada para faturas — as guias de transporte estão
sujeitas à mesma obrigação de assinatura de qualquer documento emitido por software
certificado, com ATCUD e QR Code na guia impressa.

Nem toda a movimentação de stock representa um Documento de Transporte: só entregas a
clientes (GR) e transferências internas (GA) são mapeadas automaticamente nesta versão,
e mesmo essas só quando existir uma série AT ativa configurada para o tipo de operação
em causa — sem série configurada, a guia segue o fluxo normal da Odoo sem qualquer
comunicação à AT.
""",
    "author": "Nortelix",
    "license": "OPL-1",
    "depends": ["l10n_pt_nortelix_cert", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/at_cancel_picking_wizard_views.xml",
        "views/at_series_views.xml",
        "views/res_company_views.xml",
        "views/res_config_settings_views.xml",
        "views/stock_picking_views.xml",
        "report/report_delivery_at.xml",
    ],
    "installable": True,
    "application": True,
    "post_init_hook": "post_init_hook",
}

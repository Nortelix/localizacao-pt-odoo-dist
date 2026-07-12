{
    "name": "Portugal - Exportação SAF-T (Nortelix)",
    "version": "19.0.1.0.0",
    "category": "Accounting/Localizations",
    "summary": "Exportação do ficheiro SAF-T (PT) de faturação, schema 1.04_01",
    "description": """
Gera o ficheiro SAF-T (PT) — vertente de Faturação (Portaria n.º 302/2016) — a partir dos
documentos assinados pelo módulo `l10n_pt_nortelix_cert`.

Cobre: Header, MasterFiles (Customer, Product, TaxTable), SourceDocuments/SalesInvoices
e SourceDocuments/Payments (recibos, regime normal — código "RG").
NÃO cobre (fora de âmbito): MovementOfGoods, WorkingDocuments, regime de IVA de caixa
("RC"), SAF-T de Contabilidade (obrigação distinta, com calendário próprio).

Antes de qualquer submissão real à AT, validar o XML gerado contra o XSD oficial
1.04_01 publicado pela Autoridade Tributária.
""",
    "author": "Nortelix",
    "license": "OPL-1",
    "depends": ["l10n_pt_nortelix_cert"],
    "external_dependencies": {
        "python": ["lxml"],
    },
    "data": [
        "security/ir.model.access.csv",
        "wizard/saft_export_wizard_views.xml",
    ],
    "installable": True,
    "application": True,
}

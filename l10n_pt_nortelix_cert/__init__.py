from . import models
from . import services
from . import wizard


def _l10n_pt_nortelix_set_default_signing_service_url(env):
    """Pré-preenche o URL do serviço de assinatura Nortelix nas empresas já existentes
    na base de dados ao instalar este módulo (o `default=` do campo, em
    models/res_company.py, só cobre empresas criadas DEPOIS disto — não há forma de um
    `default=` de campo alcançar registos que já existiam antes de o campo existir).
    Nunca sobrescreve uma empresa que já tenha um valor diferente configurado."""
    companies = env["res.company"].search([("l10n_pt_nortelix_signing_service_url", "=", False)])
    companies.write({"l10n_pt_nortelix_signing_service_url": "https://signature.nortelix.pt"})

# For copyright and license notices, see __manifest__.py file in module root
# directory or check the readme files

{
    "name": "VAT Ledger for Argentina",
    "version": "16.0.1.0.0",
    "category": "Accounting",
    "license": "AGPL-3",
    "summary": "VAT Ledger, VAT Digital Ledger and VAT Reports for Argentina",
    "author": "Odoo Community Association (OCA), Codize, Exemax, ADHOC SA, Moldeo Interactive",
    "website": "https://github.com/OCA/l10n-argentina",
    "depends": ["base", "l10n_ar", "report_xlsx"],
    "external_dependencies": {},
    "data": [
        "views/account_vat_ledger.xml",
        "security/ir.model.access.csv",
        "report/account_vat_ledger.xml",
        "report/account_vat_ledger_xlsx.xml",
    ],
    "maintainers": ["nimarosa", "ibuioli"],
    "installable": True,
}

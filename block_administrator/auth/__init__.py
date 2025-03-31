import frappe


def validate():
    if frappe.session.user == "Administrator":
        block_admin = frappe.get_single("Block Administrator")
        if block_admin.block_administrator_login == 1:
            frappe.throw(
                msg=frappe._("Administrator login is disabled"),
                exc=frappe.PermissionError,
            )

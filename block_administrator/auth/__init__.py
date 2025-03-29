import frappe


def validate():
    if frappe.session.user == "Administrator":
        frappe.throw(
            msg=frappe._("Administrator login is disabled"),
            exc=frappe.PermissionError,
        )
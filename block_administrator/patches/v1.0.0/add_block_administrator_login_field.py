import frappe
from block_administrator.install import get_custom_fields
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.query_builder import DocType


def execute():
    # Add the setting as a Custom Field on System Settings (idempotent).
    create_custom_fields(get_custom_fields())

    # Carry over the setting from the old "Block Administrator" single doctype,
    # which is removed in this release, so existing sites don't lose their config.
    # Note: use the raw query builder - frappe.db.get_value adds an "ORDER BY
    # creation" that doesn't exist on the Singles table.
    singles = DocType("Singles")
    old_value = (
        frappe.qb.from_(singles)
        .select(singles.value)
        .where(singles.doctype == "Block Administrator")
        .where(singles.field == "block_administrator_login")
        .run(pluck=True)
    )

    if not old_value:
        return

    if not frappe.db.get_single_value(
        "System Settings", "block_administrator_login", cache=False
    ):
        frappe.db.set_single_value(
            "System Settings", "block_administrator_login", old_value[0]
        )

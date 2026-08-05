import frappe


def validate_system_settings(doc, method=None):
    """Prevent enabling the Administrator login block if it would lock out all admins.

    Runs on every save of System Settings (``doc_events`` → ``validate``, see
    ``hooks.py``). Enabling the block is only allowed when there is at least one
    other enabled user in the system with the System Manager role, so a
    recovery path always exists. Disabling the block (or saving unrelated
    changes) is always allowed.
    """
    if not doc.block_administrator_login:
        return

    if not doc.has_value_changed("block_administrator_login"):
        return

    other_users = frappe.get_all(
        "User",
        filters={"enabled": 1, "name": ("not in", ["Administrator", "Guest"])},
        pluck="name",
    )

    if not other_users:
        frappe.throw(
            frappe._(
                "Cannot block Administrator login as there are no other enabled users in the system. You would lose all access."
            ),
            frappe.ValidationError,
        )

    system_managers = frappe.get_all(
        "Has Role",
        filters={
            "role": "System Manager",
            "parenttype": "User",
            "parent": ("in", other_users),
        },
        pluck="parent",
    )

    if not system_managers:
        frappe.throw(
            frappe._(
                "Cannot block Administrator login as no other enabled user has the System Manager role. You would lose all admin access."
            ),
            frappe.ValidationError,
        )

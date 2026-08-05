import frappe


def validate_login(login_manager):
    """Block the built-in Administrator account from logging in when enabled.

    Registered via the ``on_login`` session hook (see ``hooks.py``). It runs after
    the credentials have been verified but before the session is created, so a
    blocked login fails cleanly with an ``AuthenticationError`` and no session is
    left behind.
    """
    if login_manager.user != "Administrator":
        return

    # The field is a Custom Field added on System Settings by this app.
    # Bail out gracefully if it hasn't been synced yet (e.g. pre-migrate).
    if not frappe.get_meta("System Settings").has_field("block_administrator_login"):
        return

    if frappe.db.get_single_value("System Settings", "block_administrator_login"):
        frappe.throw(
            msg=frappe._(
                "Administrator login is disabled. Please contact your System Manager."
            ),
            exc=frappe.AuthenticationError,
        )

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

# Anchor fields for placing the checkbox in the System Settings form, in order
# of preference. `insert_after` is only a *placement hint* - the field itself
# and the login-blocking logic never depend on any of these. If
# `disable_user_pass_login` is ever removed/renamed in a future Frappe version,
# we fall back to another field in the same area, and finally to "append",
# which is a special value that always works (field is added at the end of the
# form).
ANCHOR_FIELDS = (
    "disable_user_pass_login",
    "login_methods_section",
    "deny_multiple_sessions",
    "session_expiry",
)


def get_custom_fields():
    """Return the custom field definitions with a resolved `insert_after`.

    The anchor is resolved against the live System Settings metadata at call
    time (install / migrate / patch), so it never points to a field that does
    not exist. Even in the worst case - every anchor field gone - the field is
    still created and rendered at the end of the form, and the login blocking
    keeps working.
    """
    meta = frappe.get_meta("System Settings")
    insert_after = next(
        (field for field in ANCHOR_FIELDS if meta.has_field(field)), "append"
    )

    return {
        "System Settings": [
            {
                "fieldname": "block_administrator_login",
                "label": "Block Administrator Login",
                "fieldtype": "Check",
                "insert_after": insert_after,
                "default": 0,
                "description": "When checked, the built-in Administrator account is blocked from logging in with an email and password.",
            },
        ]
    }


def after_install():
    create_custom_fields(get_custom_fields())

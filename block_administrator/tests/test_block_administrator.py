import frappe
from frappe.tests import IntegrationTestCase

from block_administrator.auth import validate_login
from block_administrator.validations import validate_system_settings


class TestBlockAdministrator(IntegrationTestCase):
    def setUp(self):
        self.created_users = []
        super().setUp()

    def tearDown(self):
        frappe.db.set_single_value("System Settings", "block_administrator_login", 0)
        for email in self.created_users:
            if frappe.db.exists("User", email):
                frappe.delete_doc("User", email, force=True)
        frappe.db.commit()
        super().tearDown()

    def make_user(self, email, roles, enabled=True):
        if frappe.db.exists("User", email):
            frappe.delete_doc("User", email, force=True)
            frappe.db.commit()

        user = frappe.get_doc(
            {
                "doctype": "User",
                "email": email,
                "first_name": email.split("@")[0].replace(".", " ").title(),
                "send_welcome_email": 0,
                "user_type": "System User",
                "enabled": enabled,
                "roles": [{"role": role} for role in roles],
            }
        )
        user.insert(ignore_permissions=True)
        self.created_users.append(email)
        frappe.db.commit()
        return email

    def test_blocks_administrator_login_when_enabled(self):
        frappe.db.set_single_value("System Settings", "block_administrator_login", 1)

        login_manager = frappe._dict(user="Administrator")
        with self.assertRaises(frappe.AuthenticationError):
            validate_login(login_manager)

    def test_allows_administrator_login_when_disabled(self):
        frappe.db.set_single_value("System Settings", "block_administrator_login", 0)

        login_manager = frappe._dict(user="Administrator")
        validate_login(login_manager)

    def test_allows_other_users_when_enabled(self):
        frappe.db.set_single_value("System Settings", "block_administrator_login", 1)

        login_manager = frappe._dict(user="test@example.com")
        validate_login(login_manager)

    def test_rejects_enabling_when_no_other_users(self):
        doc = frappe.get_doc("System Settings")
        doc.block_administrator_login = 1

        with self.assertRaises(frappe.ValidationError):
            validate_system_settings(doc)

    def test_rejects_enabling_when_no_other_system_manager(self):
        self.make_user("tester.no.sm@example.com", ["Translator"])

        doc = frappe.get_doc("System Settings")
        doc.block_administrator_login = 1

        with self.assertRaises(frappe.ValidationError):
            validate_system_settings(doc)

    def test_allows_enabling_when_other_system_manager_exists(self):
        self.make_user("tester.sm@example.com", ["System Manager"])

        doc = frappe.get_doc("System Settings")
        doc.block_administrator_login = 1

        validate_system_settings(doc)

    def test_allows_disabling_always(self):
        doc = frappe.get_doc("System Settings")
        doc.block_administrator_login = 0

        validate_system_settings(doc)

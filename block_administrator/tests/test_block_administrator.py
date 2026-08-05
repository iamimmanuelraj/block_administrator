import frappe
from frappe.tests import IntegrationTestCase

from block_administrator.auth import validate_login


class TestBlockAdministrator(IntegrationTestCase):
    def tearDown(self):
        frappe.db.set_single_value("System Settings", "block_administrator_login", 0)
        super().tearDown()

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

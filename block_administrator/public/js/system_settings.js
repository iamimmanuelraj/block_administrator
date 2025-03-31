// In your_custom_app/public/js/system_settings.js
frappe.ui.form.on("System Settings", {
  refresh: function (frm) {
    // First check if our custom wrapper already exists in the DOM
    if ($(".block-administrator-wrapper").length === 0) {
      // Find an existing field in the form to place our control after
      let target_field = frm.fields_dict["disable_user_pass_login"];

      // Create the wrapper with a custom class for identification
      const field_wrapper = document.createElement("div");
      field_wrapper.className = "frappe-control block-administrator-wrapper";
      target_field.$wrapper[0].insertAdjacentElement("afterend", field_wrapper);

      // Create the field
      const field = frappe.ui.form.make_control({
        df: {
          fieldname: "block_administrator_login",
          fieldtype: "Check",
          label: "Block Administrator Login", // Added label
          description:
            "When checked, the inbuilt frappe's Administrator account is blocked from email-password login. When unchecked, the Administrator account can log in using email and password.",
        },
        parent: field_wrapper,
        frm: frm,
      });

      // Render the complete field with label and description
      field.refresh();

      // Cache value to reduce database queries
      if (!frm.block_administrator_login_cached) {
        frappe.db
          .get_single_value("Block Administrator", "block_administrator_login")
          .then((value) => {
            frm.block_administrator_login_cached = value;

            // Temporarily disable change handler by caching and removing it
            const tempOnChange = field.df.change;
            field.df.change = null;

            // Use proper API to set value to show the checkbox correctly
            field.set_input(value === 1 || value === true);

            // Remove any existing event handlers to prevent multiple bindings
            field.$input.off("change");

            // Add a single change event handler
            field.$input.on("change", function () {
              const currentValue = field.$input.prop("checked") ? 1 : 0;

              frappe.db
                .set_value(
                  "Block Administrator",
                  "Block Administrator",
                  "block_administrator_login",
                  currentValue,
                )
                .then(() => {
                  frappe.show_alert({
                    message: __("Administrator login setting updated"),
                    indicator: "green",
                  });
                });
            });
          })
          .catch((err) => {
            console.error(
              "Error fetching block_administrator_login value:",
              err,
            );
          });
      } else {
        // Use cached value
        const value = frm.block_administrator_login_cached;

        // Temporarily disable change handler by caching and removing it
        const tempOnChange = field.df.change;
        field.df.change = null;

        // Use proper API to set value to show the checkbox correctly
        field.set_input(value === 1 || value === true);

        // Remove any existing event handlers to prevent multiple bindings
        field.$input.off("change");

        // Add a single change event handler
        field.$input.on("change", function () {
          const currentValue = field.$input.prop("checked") ? 1 : 0;

          frappe.db
            .set_value(
              "Block Administrator",
              "Block Administrator",
              "block_administrator_login",
              currentValue,
            )
            .then(() => {
              frappe.show_alert({
                message: __("Administrator login setting updated"),
                indicator: "green",
              });
            });
        });
      }
    }
  },
});

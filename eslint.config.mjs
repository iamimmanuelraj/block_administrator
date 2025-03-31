import { defineConfig } from "eslint/config";
import globals from "globals";
import path from "node:path";
import { fileURLToPath } from "node:url";
import js from "@eslint/js";
import { FlatCompat } from "@eslint/eslintrc";
import { includeIgnoreFile } from "@eslint/compat";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const compat = new FlatCompat({
  baseDirectory: __dirname,
  recommendedConfig: js.configs.recommended,
  allConfig: js.configs.all,
});
const gitignorePath = path.resolve(__dirname, ".gitignore");

export default defineConfig([
  includeIgnoreFile(gitignorePath),
  {
    extends: compat.extends("eslint:recommended"),

    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.node,
        frappe: true,
        Vue: true,
        SetVueGlobals: true,
        __: true,
        repl: true,
        Class: true,
        locals: true,
        cint: true,
        cstr: true,
        cur_frm: true,
        cur_dialog: true,
        cur_page: true,
        cur_list: true,
        cur_tree: true,
        msg_dialog: true,
        is_null: true,
        in_list: true,
        has_common: true,
        posthog: true,
        has_words: true,
        validate_email: true,
        open_web_template_values_editor: true,
        validate_name: true,
        validate_phone: true,
        validate_url: true,
        get_number_format: true,
        format_number: true,
        format_currency: true,
        comment_when: true,
        open_url_post: true,
        toTitle: true,
        lstrip: true,
        rstrip: true,
        strip: true,
        strip_html: true,
        replace_all: true,
        flt: true,
        precision: true,
        CREATE: true,
        AMEND: true,
        CANCEL: true,
        copy_dict: true,
        get_number_format_info: true,
        strip_number_groups: true,
        print_table: true,
        Layout: true,
        web_form_settings: true,
        $c: true,
        $a: true,
        $i: true,
        $bg: true,
        $y: true,
        $c_obj: true,
        refresh_many: true,
        refresh_field: true,
        toggle_field: true,
        get_field_obj: true,
        get_query_params: true,
        unhide_field: true,
        hide_field: true,
        set_field_options: true,
        getCookie: true,
        getCookies: true,
        get_url_arg: true,
        md5: true,
        $: true,
        jQuery: true,
        moment: true,
        hljs: true,
        Awesomplete: true,
        Sortable: true,
        Showdown: true,
        Taggle: true,
        Gantt: true,
        Slick: true,
        Webcam: true,
        PhotoSwipe: true,
        PhotoSwipeUI_Default: true,
        io: true,
        JsBarcode: true,
        L: true,
        Chart: true,
        DataTable: true,
        Cypress: true,
        cy: true,
        it: true,
        describe: true,
        expect: true,
        context: true,
        before: true,
        beforeEach: true,
        after: true,
        qz: true,
        localforage: true,
        extend_cscript: true,
      },

      ecmaVersion: "latest",
      sourceType: "module",
    },

    rules: {
      indent: "off",
      "brace-style": "off",
      "no-mixed-spaces-and-tabs": "off",
      "no-useless-escape": "off",

      "space-unary-ops": [
        "error",
        {
          words: true,
        },
      ],

      "linebreak-style": "off",
      quotes: ["off"],
      semi: "off",
      camelcase: "off",
      "no-unused-vars": "off",
      "no-console": ["warn"],
      "no-extra-boolean-cast": ["off"],
      "no-control-regex": ["off"],
    },
  },
]);

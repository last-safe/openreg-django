JAZZMIN_SETTINGS = {
    "site_title": "OpenReg",
    "site_header": "OpenReg",
    "site_brand": "OpenReg",
    "site_logo": "/img/logo.gif",
    "login_logo": "/img/logo.gif",
    "login_logo_dark": "/img/logo.gif",

    "site_icon": "/img/favicon.ico",
    "welcome_sign": "Добро пожаловать в OpenReg",
    "copyright": "OpenReg",
    "user_avatar": None,

    "topmenu_links": [
        {"name": "To Home", "url": "/", "permissions": ["auth.view_user"]},
        {"model": "app.Users"},
        {"model": "auth.user"},
    ],

    "usermenu_links": [
        {"name": "💬", "url": "https://t.me/nyukhat", "new_window": True},
    ],

    "hide_models": ['auth.Group'],

    "show_sidebar": True,
    "navigation_expanded": True,

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",

    "related_modal_active": True,

    "custom_css": "css/bootstrap-dark.css",
    "custom_js": None,

    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",

    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    }
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-success",
    "accent": "accent-teal",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-info",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    # "theme": "cyborg",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}
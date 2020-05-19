
from openupgradelib import openupgrade


views_to_update = [
    "website_event_filter_selector.filter_type",
    "website_event_filter_selector.filter_country",
    "website_event_filter_selector.filter_city",
]


@openupgrade.migrate()
def migrate(env, version):
    for view_ref in views_to_update:
        view = env.ref(view_ref)
        view.active = False


from openupgradelib import openupgrade
from .common import views_to_update


@openupgrade.migrate()
def migrate(env, version):
    for view_ref in views_to_update:
        view = env.ref(view_ref)
        view.active = True

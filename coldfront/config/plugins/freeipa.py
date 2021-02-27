from coldfront.config.base import INSTALLED_APPS, ENV

INSTALLED_APPS += [
    'coldfront.plugins.freeipa',
]

FREEIPA_KTNAME = ENV.str('COLDFRONT_PLUGIN_FREEIPA_KTNAME')
FREEIPA_SERVER = ENV.str('COLDFRONT_PLUGIN_FREEIPA_SERVER')
FREEIPA_USER_SEARCH_BASE = ENV.str('COLDFRONT_PLUGIN_FREEIPA_USER_SEARCH_BASE')
FREEIPA_ENABLE_SIGNALS = False
ADDITIONAL_USER_SEARCH_CLASSES = ['coldfront.plugins.freeipa.search.LDAPUserSearch',]
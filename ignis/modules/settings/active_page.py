from ignis.variable import Variable
from .elements import SettingsPage

fallback_page = SettingsPage(name="Settings")
active_page = Variable(value=fallback_page)

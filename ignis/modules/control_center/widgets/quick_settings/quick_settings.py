from ignis.widgets import Widget
from .wifi import wifi_control
from .record import RecordButton
from .dnd import DNDButton
from .dark_mode import DarkModeButton
from .ethernet import ethernet_control
from .vpn import vpn_control
from ...qs_button import QSButton
from ignis.services.network import NetworkService

network = NetworkService.get_default()


class QuickSettings(Widget.Box):
    def __init__(self):
        super().__init__(vertical=True, css_classes=["qs-main-box"])
        network.wifi.connect("notify::devices", lambda x, y: self.__refresh())
        network.ethernet.connect("notify::devices", lambda x, y: self.__refresh())
        network.vpn.connect("notify::connections", lambda x, y: self.__refresh())

        self.__refresh()

    def __refresh(self) -> None:
        self.child = []
        self.__configure()

    def __configure(self) -> None:
        self.__qs_fabric(
            *wifi_control(),
            *ethernet_control(),
            *vpn_control(),
            DNDButton(),
            DarkModeButton(),
            RecordButton(),
        )

    def __qs_fabric(self, *buttons: QSButton) -> None:
        for i in range(0, len(buttons), 2):
            self.__add_button(buttons, i)

    def __add_button(self, buttons: tuple[QSButton, ...], i: int) -> None:
        row = Widget.Box(homogeneous=True)
        if len(self.child) > 0:
            row.style = "margin-top: 0.5rem;"

        self.append(row)

        button1 = buttons[i]
        row.append(button1)

        if button1.content:
            self.append(button1.content)

        if i + 1 < len(buttons):
            button2 = buttons[i + 1]
            button2.style = "margin-left: 0.5rem;"
            row.append(button2)

            if button2.content:
                self.append(button2.content)

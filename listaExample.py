from kivy.app import App
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import ScreenManager, Screen
import asyncio
import bleak

class BLEListItem(OneLineListItem):
    def __init__(self, ble_device, **kwargs):
        self.ble_device = ble_device
        super().__init__(text=ble_device.name, **kwargs)

class BLEDeviceList(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list = []
        self.add_widget(self.list)

    async def update_list(self):
        async with bleak.BleakClient("host-device-name") as client:
            devices = await client.discover()
            self.list.clear_widgets()
            for device in devices:
                self.list.add_widget(BLEListItem(device))

class BLEApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(BLEDeviceList(name="devices"))
        return sm

if __name__ == "__main__":
    BLEApp().run()

import asyncio
import bleak
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# bind bleak's python logger into kivy's logger before importing python module using logging
from kivy.logger import Logger
import logging

logging.Logger.manager.root = Logger

class BleApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.devices = []
        self.label = Label(text="Presiona el botón para escanear")

    async def scan_ble_devices(self):
        async with bleak.BleakClient("localhost") as client:
            self.label = Label(font_size="15sp")
            self.devices = await client.discover()

    def update_devices_list(self, *args):
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.label)
        for device in self.devices:
            layout.add_widget(Label(text=device.name))
        self.root.clear_widgets()
        self.root.add_widget(layout)

    def build(self):
        button = Button(text="Escanear")
        button.bind(on_press=self.start_scan)
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def start_scan(self, *args):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.scan_ble_devices())
        self.update_devices_list()

if __name__ == "__main__":
    BleApp().run()

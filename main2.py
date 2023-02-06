import asyncio
from bleak import BleakScanner
from bleak import BleakClient

address = "50:51:A9:8D:F3:98"                   #DEBEN COINCIDIR LA MAC Y EL UUID DEL DISPOSITIVO PARA QUE SE CONECTE
MODEL_NBR_UUID = "0000dfb1-0000-1000-8000-00805f9b34fb"


async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

async def main2(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))



asyncio.run(main())
asyncio.run(main2(address))
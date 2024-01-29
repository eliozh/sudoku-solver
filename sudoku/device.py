from ppadb.client import Client as AdbClient


def connect_device():
    client = AdbClient()
    devices = client.devices()

    if len(devices) == 1:
        return devices[0]
    elif len(devices) == 0:
        raise Exception("No avaiable android devices.")

    for index, device in enumerate(devices):
        print(f"{index + 1}. {device.serial}")
    result = int(input(f"Choose device: "))

    return devices[result - 1]
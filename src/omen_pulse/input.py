import select

from evdev import InputDevice, ecodes, list_devices

from .detector import PressDetector


DEVICE_NAME = "HP WMI hotkeys"
OMEN_KEY = ecodes.KEY_PROG2


def find_omen_device():
    for path in list_devices():
        device = InputDevice(path)

        if device.name == DEVICE_NAME:
            return device

    raise RuntimeError(f"Could not find input device: {DEVICE_NAME}")


def listen():
    device = find_omen_device()
    detector = PressDetector()

    print("⚡ OMEN Pulse")
    print(f"Device: {device.name}")
    print(f"Path:   {device.path}")
    print(f"Key:    KEY_PROG2 ({OMEN_KEY})")
    print("Listening...\n")

    while True:

        readable, _, _ = select.select(
            [device.fd],
            [],
            [],
            0.05,
        )

        if readable:
            for event in device.read():

                if event.type != ecodes.EV_KEY:
                    continue

                if event.code != OMEN_KEY:
                    continue

                if event.value != 1:
                    continue

                detector.press()

        detector.check_timeout()


if __name__ == "__main__":
    listen()

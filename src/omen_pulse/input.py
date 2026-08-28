import select
import time

from evdev import InputDevice, ecodes, list_devices


DEVICE_NAME = "HP WMI hotkeys"
OMEN_KEY = ecodes.KEY_PROG2

DOUBLE_PRESS_WINDOW = 0.40


def find_omen_device():
    for path in list_devices():
        device = InputDevice(path)

        if device.name == DEVICE_NAME:
            return device

    raise RuntimeError(f"Could not find input device: {DEVICE_NAME}")


def listen():
    device = find_omen_device()

    print("⚡ OMEN Pulse")
    print(f"Device: {device.name}")
    print(f"Path:   {device.path}")
    print(f"Key:    KEY_PROG2 ({OMEN_KEY})")
    print("Listening...\n")

    pending_single = False
    first_press_time = 0.0

    while True:

        timeout = DOUBLE_PRESS_WINDOW

        if pending_single:
            elapsed = time.monotonic() - first_press_time
            timeout = max(0, DOUBLE_PRESS_WINDOW - elapsed)

        readable, _, _ = select.select([device.fd], [], [], timeout)

        # Timeout: no second press arrived
        if not readable:
            if pending_single:
                print("⚡ SINGLE PRESS → 🎬 ENTERTAINMENT MODE")
                pending_single = False
                first_press_time = 0.0

            continue

        for event in device.read():

            if event.type != ecodes.EV_KEY:
                continue

            if event.code != OMEN_KEY:
                continue

            # Only react to key-down events
            if event.value != 1:
                continue

            current_time = time.monotonic()

            if (
                pending_single
                and current_time - first_press_time <= DOUBLE_PRESS_WINDOW
            ):
                print("⚡ DOUBLE PRESS → 🔨 FOCUS / BUILD MODE")

                pending_single = False
                first_press_time = 0.0

            else:
                pending_single = True
                first_press_time = current_time


if __name__ == "__main__":
    listen()

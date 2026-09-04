import subprocess
from dataclasses import dataclass


@dataclass
class LaunchedProcess:
    name: str
    process: subprocess.Popen | None
    owned: bool = True


def launch_pwa(name, desktop_file):
    process = subprocess.Popen(
        ["gio", "launch", str(desktop_file)],
        start_new_session=True,
    )

    return LaunchedProcess(
        name=name,
        process=process,
        owned=False,
    )


def launch_command(name, command):
    process = subprocess.Popen(
        command,
        start_new_session=True,
    )

    return LaunchedProcess(
        name=name,
        process=process,
        owned=True,
    )


def launch_flatpak(name, app_id):
    process = subprocess.Popen(
        ["flatpak", "run", app_id],
        start_new_session=True,
    )

    return LaunchedProcess(
        name=name,
        process=process,
        owned=True,
    )


def launch_gapplication(name, app_id, action):
    process = subprocess.Popen(
        ["gapplication", "action", app_id, action],
        start_new_session=True,
    )

    return LaunchedProcess(
        name=name,
        process=process,
        owned=False,
    )


def cleanup_processes(processes):
    for launched in processes:
        if not launched.owned:
            print(
                f"↪️ Leaving {launched.name} open "
                "(shared application)"
            )
            continue

        process = launched.process

        if process is None or process.poll() is not None:
            continue

        print(f"🧹 Closing {launched.name}...")

        try:
            process.terminate()
        except ProcessLookupError:
            pass

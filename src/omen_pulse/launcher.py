import subprocess


def launch_pwa(desktop_file):
    subprocess.Popen(
        ["gio", "launch", desktop_file],
        start_new_session=True,
    )


def launch_command(command):
    subprocess.Popen(
        command,
        start_new_session=True,
    )


def launch_flatpak(app_id):
    subprocess.Popen(
        ["flatpak", "run", app_id],
        start_new_session=True,
    )

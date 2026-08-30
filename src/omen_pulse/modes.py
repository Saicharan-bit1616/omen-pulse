import subprocess
import time


HOME = "/home/chvsaicharan"

APPLICATIONS = {
    "youtube": (
        f"{HOME}/.local/share/applications/"
        "chrome-agimnkijcaahngcdmfeangaknmldooml-Default.desktop"
    ),

    "instagram": (
        f"{HOME}/.local/share/applications/"
        "chrome-akpamiohjfcnimfljfndmaldlcfphjmp-Default.desktop"
    ),

    "whatsapp": (
        f"{HOME}/.local/share/applications/"
        "chrome-hnpfjngllnobngcgfapefoaidbinmjnm-Default.desktop"
    ),
}


def launch_pwa(desktop_file):
    return subprocess.Popen(
        ["gio", "launch", desktop_file],
        start_new_session=True,
    )


def launch_command(command):
    return subprocess.Popen(
        command,
        start_new_session=True,
    )


def launch_flatpak(app_id):
    return subprocess.Popen(
        ["flatpak", "run", app_id],
        start_new_session=True,
    )


def entertainment_mode():
    print("🎬 ENTERTAINMENT MODE ACTIVATED")

    launch_pwa(APPLICATIONS["youtube"])
    time.sleep(0.8)

    launch_pwa(APPLICATIONS["instagram"])
    time.sleep(0.8)

    launch_pwa(APPLICATIONS["whatsapp"])


def focus_mode():
    print("🔨 FOCUS / BUILD MODE ACTIVATED")

    launch_command(["antigravity"])
    time.sleep(0.8)

    launch_command(["ptyxis"])
    time.sleep(0.8)

    launch_flatpak("com.spotify.Client")

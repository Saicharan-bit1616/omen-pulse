from pathlib import Path


HOME = Path.home()
APPLICATIONS = HOME / ".local/share/applications"


FOCUS_APPS = {
    "chatgpt": {
      "type": "desktop",
       "desktop_file": APPLICATIONS
        / "chrome-cadlkienfkclaiaibeoongdcgmdikeeg-Default.desktop",
    },

    "claude": {
        "type": "desktop",
        "desktop_file": APPLICATIONS
        / "chrome-fmpnliohjhemenmnlpbfagaolkdacoja-Default.desktop",
    },

    "antigravity": {
        "type": "command",
        "command": ["/usr/share/antigravity/antigravity"],
    },

    "terminal": {
        "type": "gapplication",
        "app_id": "org.gnome.Ptyxis",
        "action": "new-window",
    },
    "spotify": {
        "type": "flatpak",
        "app_id": "com.spotify.Client",
    },

    "opencode": {
        "type": "command",
        "command": ["/opt/OpenCode/ai.opencode.desktop"],
    },

    "github": {
        "type": "desktop",
        "desktop_file": APPLICATIONS
        / "chrome-mjoklplbddabcmpepnokjaffbmgbkkgg-Default.desktop",
    },

    "text_editor": {
        "type": "command",
        "command": ["/usr/bin/gnome-text-editor"],
    },
}


ENTERTAINMENT_APPS = {
    "youtube": {
        "type": "desktop",
        "desktop_file": APPLICATIONS
        / "chrome-agimnkijcaahngcdmfeangaknmldooml-Default.desktop",
    },

    "instagram": {
        "type": "desktop",
        "desktop_file": APPLICATIONS
        / "chrome-akpamiohjfcnimfljfndmaldlcfphjmp-Default.desktop",
    },

    "whatsapp": {
        "type": "desktop",
        "desktop_file": APPLICATIONS
        / "chrome-hnpfjngllnobngcgfapefoaidbinmjnm-Default.desktop",
    },

    "threads": {
        "type": "desktop",
        "desktop_file": APPLICATIONS
        / "chrome-jhfafgojnlneaffmkkjbcpnadneeocbk-Default.desktop",
    },

    "animesugetv": {
        "type": "desktop",
        "desktop_file": APPLICATIONS
        / "chrome-njjpieepmonlmnpcahkhpkbbkehhkkmp-Default.desktop",
    },
}


MODES = {
    "focus": FOCUS_APPS,
    "entertainment": ENTERTAINMENT_APPS,
}

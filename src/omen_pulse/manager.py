from .config import MODES
from .launcher import (
    LaunchedProcess,
    cleanup_processes,
    launch_command,
    launch_flatpak,
    launch_pwa,
    launch_gapplication,
)

class ModeManager:
    def __init__(self):
        self.current_mode = None
        self.launched_processes: list[LaunchedProcess] = []

    def cleanup(self):
        if not self.launched_processes:
            return

        print("🧹 Cleaning up current mode...")

        cleanup_processes(self.launched_processes)

        self.launched_processes.clear()
        self.current_mode = None

    def activate(self, mode_name: str):
        if mode_name not in MODES:
            raise ValueError(f"Unknown mode: {mode_name}")

        if self.current_mode == mode_name:
            print(f"⚡ {mode_name.upper()} MODE IS ALREADY ACTIVE")
            return

        if self.current_mode is not None:
            self.cleanup()

        print(f"\n⚡ Activating {mode_name.upper()} MODE")

        for name, app in MODES[mode_name].items():
            app_type = app["type"]

            if app_type == "desktop":
                launched = launch_pwa(
                    name,
                    app["desktop_file"],
                )

            elif app_type == "command":
                launched = launch_command(
                    name,
                    app["command"],
                )

            elif app_type == "flatpak":
                launched = launch_flatpak(
                    name,
                    app["app_id"],
                )

            elif app_type == "gapplication":
                launched = launch_gapplication(
                    name,
                    app["app_id"],
                    app["action"],
                )

            else:
                raise ValueError(
                    f"Unknown application type: {app_type}"
                )

            self.launched_processes.append(launched)

        self.current_mode = mode_name

        print(f"✅ {mode_name.upper()} MODE ACTIVE")

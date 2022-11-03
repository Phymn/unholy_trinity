from dataclasses import dataclass


class Settings:
    def __init__(self) -> None:
        ...

    def refresh_settings(self) -> None:
        # Import all settings and populate the dataclasses
        ...

    @dataclass(frozen=True)
    def get_settings(self) -> dataclass:
        ...



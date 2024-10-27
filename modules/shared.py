from dataclasses import dataclass


@dataclass
class opts:
    directml_memory_provider: str = "Performance Counter"


@dataclass
class cmd_opts:
    device_id: str = "0"
    use_ipex: bool = False
    use_directml: bool = True

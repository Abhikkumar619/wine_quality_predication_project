from dataclasses import dataclass
from pathlib import Path

# Creating entity, entity is nothing but it is custom return type of the function.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    status_file : str
    all_schema: dict
from typing import List, TypedDict, Union

# Arguments
class Arguments(TypedDict, total=False):
    level: Union[bool, int]
    auto_level: bool
    min_level: int
    max_level: int
    nocrop: bool
    margin_horizontal: Union[int, float]
    margin_vertical: Union[int, float]
    dpi: Union[int, float]
    sharpen: bool
    dither: bool
    tesseract: bool
    tesseract_lang: str
    assisted_split: bool


# Configuration
class Configuration(TypedDict, total=False):
    scan_folder: str
    scanimage: str
    scanimage_arguments: List[str]
    default_args: 'Arguments'
    viewer: str

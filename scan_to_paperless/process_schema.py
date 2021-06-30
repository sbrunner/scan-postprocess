from typing import Dict, List, TypedDict, Union

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
    append_credit_card: bool
    assisted_split: bool


# Assisted split
#
# Assited split configuration
class AssistedSplit(TypedDict, total=False):
    source: str
    destinations: List[Union[int, str]]
    image: str
    limits: List["Limit"]


# Configuration
class Configuration(TypedDict, total=False):
    images: List[str]
    destination: str
    args: "Arguments"
    steps: List["Step"]
    assisted_split: List["AssistedSplit"]
    transformed_images: List[str]
    intermediate_error: List["IntermediateError"]
    images_config: Dict[str, "_ConfigurationImagesConfigAdditionalproperties"]
    images_status: Dict[str, "_ConfigurationImagesStatusAdditionalproperties"]


# Intermediate error
class IntermediateError(TypedDict, total=False):
    error: str
    traceback: List[str]


# Limit
class Limit(TypedDict, total=False):
    name: str
    type: str
    value: int
    vertical: bool
    margin: int


# Step
class Step(TypedDict, total=False):
    name: str
    sources: List[str]
    process_count: int


class _ConfigurationImagesConfigAdditionalproperties(TypedDict, total=False):
    angle: Union[Union[int, float], None]


class _ConfigurationImagesStatusAdditionalproperties(TypedDict, total=False):
    angle: Union[int, float]
    average_deviation: Union[int, float]
    angles: List[Union[int, float]]
    size: List[Union[int, float]]

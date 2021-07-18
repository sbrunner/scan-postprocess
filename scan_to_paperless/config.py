from typing import List, TypedDict, Union

# Arguments
Arguments = TypedDict(
    "Arguments",
    {
        # true: => do level on 15% - 85% (under 15 % will be black above 85% will be white), false: => 0% - 100%, <number>: => (0 + <number>)% - (100 - number)%
        "level": Union[bool, int],
        # If no level specified, do auto level
        #
        # default: False
        "auto_level": bool,
        # Min level if no level end no autolovel
        #
        # default: 15
        "min_level": int,
        # Max level if no level end no autolovel
        #
        # default: 15
        "max_level": int,
        # Don't do any crop
        #
        # default: False
        "nocrop": bool,
        # The horizontal margin used on autodetect content [mm]
        #
        # default: 9
        "margin_horizontal": Union[int, float],
        # The vertical margin used on autodetect content [mm]
        #
        # default: 6
        "margin_vertical": Union[int, float],
        # The DPI used to convert the mm to pixel
        #
        # default: 300
        "dpi": Union[int, float],
        # Do the sharpen
        #
        # default: False
        "sharpen": bool,
        # Do the dither
        #
        # default: False
        "dither": bool,
        # Use tesseract to to an OCR on the document
        #
        # default: False
        "tesseract": bool,
        # The used language for tesseract
        #
        # default: fra+eng
        "tesseract_lang": str,
        # Do en assited split
        #
        # default: False
        "assisted_split": bool,
        # The minimum box size to find the content on witch one we will crop [mm]
        #
        # default: 3
        "min_box_size_crop": Union[int, float],
        # The minimum box size to find the limits based on content [mm]
        #
        # default: 10
        "min_box_size_limit": Union[int, float],
        # The minimum box size to find the content to determine if the page is empty [mm]
        #
        # default: 20
        "min_box_size_empty": Union[int, float],
        # The minimum black in a box on content find on witch one we will crop [%]
        #
        # default: 2
        "min_box_black_crop": Union[int, float],
        # The minimum black in a box on content find the limits based on content [%]
        #
        # default: 2
        "min_box_black_limit": Union[int, float],
        # The minimum black in a box on content find to determine if the page is empty [%]
        #
        # default: 2
        "min_box_black_empty": Union[int, float],
        # The block size used in a box on content find [mm]
        #
        # default: 1.5
        "box_block_size": Union[int, float],
        # A variable of double type representing the constant used in the both methods (subtracted from the mean or weighted mean, used in a box on content find
        #
        # default: 25
        "box_threshold_value_c": Union[int, float],
    },
    total=False,
)


# Configuration
Configuration = TypedDict(
    "Configuration",
    {
        # This should be shared with the process container in 'source'.
        #
        # required
        "scan_folder": str,
        # The scanimage command
        #
        # default: scanimage
        "scanimage": str,
        # default:
        #   - --format=png
        #   - --mode=color
        #   - --resolution=300
        "scanimage_arguments": List[str],
        # WARNING: The required are not correctly taken in account,
        # See: https://github.com/camptocamp/jsonschema-gentypes/issues/6
        #
        # required
        "default_args": "Arguments",
        # The command used to start the viewer
        #
        # default: eog
        "viewer": str,
    },
    total=False,
)

# Configuration

## Properties

- **`images`** *(array)*: The images.
  - **Items** *(string)*
- **`title`** *(string)*: The tile.
- **`full_name`** *(string)*: The full name.
- **`destination`** *(string)*: The destination file name.
- **`args`**: Refer to *#/definitions/args*.
- **`steps`** *(array)*: The carried out steps description.
  - **Items** *(object)*: Cannot contain additional properties.
    - **`name`** *(string)*: The step name.
    - **`sources`** *(array)*: The images obtain after the current step.
      - **Items** *(string)*
    - **`process_count`** *(integer)*: The step number.
- **`assisted_split`** *(array)*
  - **Items** *(object)*: Assited split configuration. Cannot contain additional properties.
    - **`source`** *(string)*
    - **`destinations`** *(array)*
      - **Items** *(['integer', 'string'])*
    - **`image`** *(string)*
    - **`limits`** *(array)*: The (proposed) limits to do the assisted split, You should keep only the right one.
      - **Items** *(object)*: Cannot contain additional properties.
        - **`name`** *(string)*: The name visible on the generated image.
        - **`type`** *(string)*: The kind of split.
        - **`value`** *(integer)*: The split position.
        - **`vertical`** *(boolean)*: Is vertical?
        - **`margin`** *(integer)*: The margin around the split, can be used to remove a fold.
- **`transformed_images`** *(array)*: The transformed image, if removed the jobs will rag again from start.
  - **Items** *(string)*
- **`intermediate_error`** *(array)*: The ignored errors.
  - **Items** *(object)*: Cannot contain additional properties.
    - **`error`** *(string)*
    - **`traceback`** *(array)*
      - **Items** *(string)*
- **`images_config`** *(object)*: Can contain additional properties.
- **`images_status`** *(object)*: Can contain additional properties.
## Definitions

- **`args`** *(object)*: Cannot contain additional properties.
  - **`level`** *(['boolean', 'integer'])*: true: => do level on 15% - 85% (under 15 % will be black above 85% will be white), false: => 0% - 100%, <number>: => (0 + <number>)% - (100 - number)%.
  - **`auto_level`** *(boolean)*: If no level specified, do auto level. Default: `False`.
  - **`min_level`** *(integer)*: Min level if no level end no autolovel. Default: `15`.
  - **`max_level`** *(integer)*: Max level if no level end no autolovel. Default: `15`.
  - **`nocrop`** *(boolean)*: Don't do any crop. Default: `False`.
  - **`margin_horizontal`** *(number)*: The horizontal margin used on autodetect content [mm]. Default: `9`.
  - **`margin_vertical`** *(number)*: The vertical margin used on autodetect content [mm]. Default: `6`.
  - **`dpi`** *(number)*: The DPI used to convert the mm to pixel. Default: `300`.
  - **`sharpen`** *(boolean)*: Do the sharpen. Default: `False`.
  - **`dither`** *(boolean)*: Do the dither. Default: `False`.
  - **`tesseract`** *(boolean)*: Use tesseract to to an OCR on the document. Default: `False`.
  - **`tesseract_lang`** *(string)*: The used language for tesseract. Default: `fra+eng`.
  - **`append_credit_card`** *(boolean)*: Do an assisted split. Default: `False`.
  - **`assisted_split`** *(boolean)*: Do an assisted split. Default: `False`.

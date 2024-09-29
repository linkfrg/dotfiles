import math


def rgba_to_hex(rgba: list) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgba)


def calculate_optimal_size(width: int, height: int, bitmap_size: int) -> tuple:
    image_area = width * height
    bitmap_area = bitmap_size**2
    scale = math.sqrt(bitmap_area / image_area) if image_area > bitmap_area else 1
    new_width = round(width * scale)
    new_height = round(height * scale)
    if new_width == 0:
        new_width = 1
    if new_height == 0:
        new_height = 1
    return new_width, new_height

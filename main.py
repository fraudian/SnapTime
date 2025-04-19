import os
import re
from PIL import Image, ImageDraw, ImageFont, ExifTags
from colorama import init, Fore, Style

init()

def format_date_from_filename(filename):
    parts = filename.split('_')
    if len(parts) >= 3:
        year, month, day = parts[0], parts[1], parts[2]
        date_str = f"{day}/{month}/{year[2:]}"
        if len(parts) > 3:
            hour, minute = parts[3], parts[4]
            time_str = f"{hour}:{minute}"
            return f"{date_str} {time_str}"
        return date_str
    return None

def is_valid_icloud_filename(filename):
    pattern = r"^\d{4}_\d{2}_\d{2}_\d{2}_\d{2}_IMG_.*\.(jpg|jpeg|png|bmp|gif|heic)$"
    return re.match(pattern, filename, re.IGNORECASE)

def correct_orientation(img):
    try:
        exif = img._getexif()
        if exif:
            orientation_key = next((k for k, v in ExifTags.TAGS.items() if v == 'Orientation'), None)
            if orientation_key and orientation_key in exif:
                orientation = exif[orientation_key]
                if orientation == 2:
                    img = img.transpose(Image.FLIP_LEFT_RIGHT)
                elif orientation == 3:
                    img = img.rotate(180, expand=True)
                elif orientation == 4:
                    img = img.transpose(Image.FLIP_TOP_BOTTOM)
                elif orientation == 5:
                    img = img.transpose(Image.FLIP_LEFT_RIGHT).rotate(270, expand=True)
                elif orientation == 6:
                    img = img.rotate(270, expand=True)
                elif orientation == 7:
                    img = img.transpose(Image.FLIP_LEFT_RIGHT).rotate(90, expand=True)
                elif orientation == 8:
                    img = img.rotate(90, expand=True)
    except:
        pass
    return img

def add_timestamp_to_image(image_path, output_folder="output"):
    img = Image.open(image_path)
    img = correct_orientation(img)
    draw = ImageDraw.Draw(img)

    filename = os.path.basename(image_path)
    name_without_ext = os.path.splitext(filename)[0]
    timestamp = format_date_from_filename(name_without_ext)
    if not timestamp:
        return

    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    try:
        bbox = draw.textbbox((0, 0), timestamp, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    except AttributeError:
        text_width, text_height = draw.textsize(timestamp, font=font)

    padding = 10
    x = img.width - text_width - padding - 5
    y = img.height - text_height - padding - 5

    draw.text((x-1, y-1), timestamp, font=font, fill="black")
    draw.text((x+1, y-1), timestamp, font=font, fill="black")
    draw.text((x-1, y+1), timestamp, font=font, fill="black")
    draw.text((x+1, y+1), timestamp, font=font, fill="black")
    draw.text((x, y), timestamp, font=font, fill="white")

    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, filename)
    img.save(output_path)

def process_all_images(folder="."):
    for file in os.listdir(folder):
        if is_valid_icloud_filename(file):
            print(f"{Fore.WHITE}[{Fore.GREEN}-{Fore.WHITE}] Converting {file}...{Style.RESET_ALL}")
            add_timestamp_to_image(os.path.join(folder, file))

process_all_images()

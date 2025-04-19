# 📸 **Image Timestamp Converter**

This Python script adds a timestamp to images that follow a specific naming pattern, such as those transferred from iCloud. The timestamp is derived from the file name and is added to the **bottom-right corner** of the image, similar to how older cameras used to imprint the date and time on photos.

## ✨ Features

- 🖼️ Converts images with filenames like `2016_11_05_20_42_IMG_1129.JPG`.
- 🕰️ The timestamp format is `DD/MM/YY HH:MM` (or just `DD/MM/YY` if no time is provided).
- 🗂️ Creates an **"output"** folder to store the converted images while preserving the original images.
- ✨ Adds a shadow effect behind the timestamp text to ensure readability.

## 📋 Requirements

- 🐍 Python 3.x
- 🖼️ `Pillow` library (for image processing)
- 🎨 `colorama` library (for colored terminal output)

## 🚀 Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies using pip:

```bash
pip install pillow
```

```bash
pip install colorama
```

### Example Output:
Here is an example of how the image will look before and after running the script:

**Before:**
![Original Image](https://media.discordapp.net/attachments/1363005874112827422/1363006799065645296/2015_11_07_21_14_IMG_0827.JPG?ex=68047680&is=68032500&hm=3a762784acebdac20340fda2f1fc0d7c24374223758a9aa7fe9ad1d7dccdd04f&=&format=webp)

**After:**
![Image with Timestamp](https://media.discordapp.net/attachments/1363005874112827422/1363005956107014355/2015_11_07_21_14_IMG_0827.JPG?ex=680475b7&is=68032437&hm=729fdc3c9578b37330e767f237d3e9cc2e49ee98260983e16b388efbba464043&=&format=webp)

Made with ❤️ by fraudian

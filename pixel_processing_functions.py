import numpy as np
from PIL import Image
from config import colors
from pixel import Pixel

def get_pixels(image_path: str) -> np.ndarray[object] | None:
    try:
        pixel_data = np.array(Image.open(image_path))
        
        pixels = np.array([Pixel(tuple(pixel)) for pixel in pixel_data.reshape(-1, pixel_data.shape[-1])], dtype=object)
        
        return pixels
    
    except Exception as e:
        print(f"Error opening image[{image_path}]: {e}")
        return None

def process_pixels(pixel_array : np.ndarray[object]) -> dict:
    img_colors = colors
    for i in pixel_array:
        img_colors[i.color]+=1
    return img_colors

def display_percentage(color_dict : dict) -> None:
    total = sum((i for i in color_dict.values()))
    print(f"Total Pixels : {total}")
    if total == 0:
        print("No valid pixels to process.")
        return
    
    color_dict = dict(sorted(color_dict.items(), key=lambda item: item[1], reverse=True))

    for color, amount in color_dict.items():
        percentage = round(amount/total * 100, 2)
        if percentage > 0:
            print(f"% of {color} : {percentage}")
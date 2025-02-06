from pixel_processing_functions import get_pixels, process_pixels, display_percentage


if __name__ == "__main__":
    test_img_path = r"test_images\test1.png"
    print("Getting pixels")
    p = get_pixels(test_img_path)
    print("processing pixels")
    a = process_pixels(p)
    print("displaying pixels")
    display_percentage(a)
import os

# Check if the 'PIL' package is installed, if not, install it
try:
    from PIL import Image
except ImportError:
    import os
    os.system('pip install pillow')
    from PIL import Image

def merge_images_horizontally(input_folder, output_folder, output_filename):
    """
    Merges all images in the input folder into a single image arranged horizontally and saves it to the output folder.
    Args:
        input_folder (str): The path to the folder containing the input images.
        output_folder (str): The path to the folder where the merged image will be saved.
        output_filename (str): The filename for the merged image.
    Returns:
        None
    Raises:
        FileNotFoundError: If the input folder does not exist.
        IOError: If there is an error in reading or writing images.
    Example:
        merge_images_horizontally('/path/to/input/folder', '/path/to/output/folder', 'merged_image.jpg')
    Notes:
        - The function supports images with extensions 'png', 'jpg', and 'jpeg'.
        - If the output folder does not exist, it will be created.
        - After merging, all input images will be deleted from the input folder.
    """
    images = [Image.open(os.path.join(input_folder, file)) for file in os.listdir(input_folder) if file.endswith(('png', 'jpg', 'jpeg'))]
    
    if not images:
        print("No images found in the input folder.")
        return

    max_height = max(image.height for image in images)
    total_width = sum(image.width for image in images)

    merged_image = Image.new('RGB', (total_width, max_height))

    current_x = 0
    for image in images:
        merged_image.paste(image, (current_x, 0))
        current_x += image.width

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, output_filename)
    merged_image.save(output_path)
    print(f"Merged image saved as {output_path}")

    ## Delete all input images after merging
    # for file in os.listdir(input_folder):
    #     os.remove(os.path.join(input_folder, file))
    # print("All input images have been deleted.")

if __name__ == "__main__":
    input_folder = 'input_images'
    output_folder = 'output_image'
    output_filename = 'merged_image.jpg'
    merge_images_horizontally(input_folder, output_folder, output_filename)

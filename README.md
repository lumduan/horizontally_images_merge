# horizontally_images_merge

Combine images horizontally, based on the height of the tallest image.

## How to Use

Follow these steps to merge images horizontally:

1. **Install Python**: Make sure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Package**: Open a terminal or command prompt and run the following command to install the required package:
    ```sh
    pip install pillow
    ```

3. **Prepare Your Images**: Place all the images you want to merge in a folder named `input_images`. The images should be in `png`, `jpg`, or `jpeg` format.

4. **Run the Script**:
    - Download the `images_merge.py` script and place it in the same directory where the `input_images` folder is located.
    - Open a terminal or command prompt and navigate to the directory where the script is located.
    - Run the script using the following command:
    ```sh
    python images_merge.py
    ```

5. **Check the Output**: After running the script, a new folder named `output_image` will be created in the same directory. Inside this folder, you will find the merged image named `merged_image.jpg`.

## Notes
- If the `output_image` folder does not exist, it will be created automatically.
- The script will not delete the input images after merging. If you want to delete them, uncomment the relevant lines in the script.

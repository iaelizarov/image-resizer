import pandas as pd
from scipy.ndimage import zoom

def resize_csv_image(file_path, target_width=150):
    """
    Reads a CSV file containing image data, resizes its width, and returns the resized data.

    Args:
        file_path (str): Path to the CSV file.
        target_width (int): Desired width for the resized image.

    Returns:d
        pd.DataFrame: DataFrame containing the resized image data.
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    df = df.dropna() # dropna cus last column of initial df contains trash values

    # Extract depth column and pixel columns
    depth_column = df['depth']
    pixel_columns = df.iloc[:, 1:].to_numpy()

    # Current width of the image
    current_width = pixel_columns.shape[1]

    # Calculate the zoom factor for resizing
    zoom_factor = target_width / current_width

    # Resize the image data along the width axis
    resized_pixels = zoom(pixel_columns, (1, zoom_factor), order=1)  # Linear interpolation

    # Create a new DataFrame with resized data
    resized_df = pd.DataFrame(resized_pixels, columns=[f'col{i+1}' for i in range(target_width)])

    # Add the depth column back
    resized_df.insert(0, 'depth', depth_column)

    return resized_df
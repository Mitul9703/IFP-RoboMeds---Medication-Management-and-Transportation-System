from PIL import Image,ImageDraw

def cut_by_corners(input_image_path, output_image_path, corners):
    """
    Cut out a portion of an image using four corner points.

    Parameters:
        input_image_path (str): Path to the input image.
        output_image_path (str): Path to save the cut-out image.
        corners (tuple of tuples): Four corner points of the rectangle in the format ((x1, y1), (x2, y2), (x3, y3), (x4, y4)).
                                  The corners should be provided in clockwise or counterclockwise order.

    Note: The input image must be a rectangular image. Ensure that the provided corner points form a valid rectangle.
    """
    try:
        # Open the input image
        img = Image.open(input_image_path)

        # Create a mask based on the corner points
        mask = Image.new("L", img.size, 0)
        ImageDraw.Draw(mask).polygon(corners, outline=1, fill=1)

        # Convert the mask to an alpha channel
        cut_out_img = img.copy()
        cut_out_img.putalpha(mask)

        # Save the cut-out image
        cut_out_img.save(output_image_path)

        print("Image cut-out and saved successfully!")
    except Exception as e:
        print("Error while cutting out the image:", e)

# Example usage:
input_image_path = "croptestimg.png"
output_image_path = "otp.png"

# Specify the four corner points in clockwise or counterclockwise order
# For example, ((x1, y1), (x2, y2), (x3, y3), (x4, y4))
# Replace the values below with your actual corner points
corners = ((745,365), (1101,438), (1174,641), (818,714))

cut_by_corners(input_image_path, output_image_path, corners)

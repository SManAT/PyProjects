import base64
from pathlib import Path
import click


class ImageToBase64:
    """
    convert an Image to base64 String
    Usage in Html:
    <img src="data:image/jpeg;base64,/9j/4AAQSkZJRg..." alt="Base64 Image">
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def convert_to_base64(self):
        try:
            # Check if file exists
            if not Path(self.file_path).is_file():
                raise FileNotFoundError(f"File not found: {self.file_path}")

            # Read the image file and convert to base64
            with open(self.file_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                return encoded_string.decode("utf-8")

        except Exception as e:
            raise Exception(f"Error converting image to base64: {str(e)}")

    @staticmethod
    def get_image_format(file_path):
        """Returns the image format/extension"""
        return Path(file_path).suffix[1:].lower()

    def get_base64_uri(self):
        """Returns the complete base64 URI including the data type prefix"""
        try:
            base64_string = self.convert_to_base64()
            image_format = self.get_image_format(self.file_path)
            return f"data:image/{image_format};base64,{base64_string}"
        except Exception as e:
            raise Exception(f"Error creating base64 URI: {str(e)}")


@click.command(no_args_is_help=False)
@click.option(
    "-s",
    "--file",
    type=(str),
    required=true,
    help="Image to convert",
)
def start(file):
    if file:

        try:
            converter = ImageToBase64("path/to/your/image.jpg")
            base64_uri = converter.get_base64_uri()
            print(base64_uri)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    start()

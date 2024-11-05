import os
from werkzeug.utils import secure_filename
import uuid


class ImageUtil:

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    BASE_UPLOAD_FOLDER = 'assets/'

    @staticmethod
    def allowed_file(filename: str) -> bool:
        """Check if the file extension is allowed."""
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ImageUtil.ALLOWED_EXTENSIONS

    @staticmethod
    def create_upload_folder(upload_folder_name: str) -> str:
        """Create the upload folder if it doesn't exist."""
        upload_folder = os.path.join(
            ImageUtil.BASE_UPLOAD_FOLDER, upload_folder_name)
        os.makedirs(upload_folder, exist_ok=True)
        return upload_folder

    @staticmethod
    def save_image(file, upload_folder_name: str) -> str:
        """Save the image file to the specified folder with a unique filename."""
        try:
            # Check if file is a tuple (e.g., from multipart form parsing)
            if isinstance(file, tuple) and len(file) == 2:
                # Assuming the file content is the second element
                file_content = file[1]
                # Assuming the filename is the first element
                filename = file[0]
            else:
                raise ValueError("Invalid file format received")

            upload_folder = ImageUtil.create_upload_folder(upload_folder_name)

            # Validate the filename and file extension
            if filename and ImageUtil.allowed_file(filename):
                # Secure the filename and generate a unique name using UUID
                file_extension = os.path.splitext(secure_filename(filename))[1]
                unique_filename = f"{uuid.uuid4().hex}{file_extension}"
                file_path = os.path.join(upload_folder, unique_filename)

                # Save the file content (file_content should be bytes)
                with open(file_path, 'wb') as f:
                    f.write(file_content)

                return upload_folder + "/" + unique_filename
            else:
                raise ValueError("Invalid file type or no file uploaded")

        except Exception as e:
            raise ValueError(f"Error saving image: {str(e)}")

    @staticmethod
    def delete_image(file_path: str) -> None:
        """Delete the specified image file."""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
            else:
                raise FileNotFoundError("File not found")
        except Exception as e:
            raise ValueError(f"Error deleting image: {str(e)}")

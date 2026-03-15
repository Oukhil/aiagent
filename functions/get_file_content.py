import os

from config import MAX_CHARS

def get_file_content(working_directory, file_path):

    try:
        abs_dir = os.path.abspath(working_directory)
        path_dir = os.path.normpath(os.path.join(abs_dir, file_path))

        # Will be True or False
        valid_target_dir = os.path.commonpath([abs_dir, path_dir]) == abs_dir
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(path_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(path_dir, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read(1):
                file_content_string += f'[...\n\nFile "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string

    except Exception as e:
        return f"Error: {e}"
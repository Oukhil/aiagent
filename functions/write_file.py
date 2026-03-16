import os

def write_file(working_directory, file_path, content):

    try:
        abs_dir = os.path.abspath(working_directory)
        path_dir = os.path.normpath(os.path.join(abs_dir, file_path))

        # Will be True or False
        valid_target_dir = os.path.commonpath([abs_dir, path_dir]) == abs_dir
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(path_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(path_dir), exist_ok=True)

        with open(path_dir, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
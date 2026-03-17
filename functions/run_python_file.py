import os
import subprocess

def run_python_file(working_directory, file_path, args=None):

    try:
        abs_dir = os.path.abspath(working_directory)
        path_dir = os.path.normpath(os.path.join(abs_dir, file_path))

        # Will be True or False
        valid_target_dir = os.path.commonpath([abs_dir, path_dir]) == abs_dir
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(path_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not path_dir.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", path_dir]
        if args:
            command.extend(args)
        
        cp_obj = subprocess.run(command, cwd=abs_dir, capture_output=True, text=True, timeout=30)

        result_str = ""
        if cp_obj.returncode:
            result_str += f"Process exited with code {cp_obj.returncode}\n"
        if cp_obj.stdout:
            result_str += f"STDOUT:\n{cp_obj.stdout}\n"
        if cp_obj.stderr:
            result_str += f"STDERR:\n{cp_obj.stderr}\n"
        if not cp_obj.stdout and not cp_obj.stderr:
            result_str += "No output produced"
        
        return result_str

    except Exception as e:
        return f"Error: {e}"
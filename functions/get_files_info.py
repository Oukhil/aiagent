import os

def get_files_info(working_directory, directory="."):

    try:
        abs_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_dir, directory))

        # Will be True or False
        valid_target_dir = os.path.commonpath([abs_dir, target_dir]) == abs_dir
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        dir_list = os.listdir(target_dir)

        dir_items = ''
        for item in dir_list:
            item_dir = os.path.join(target_dir, item)
            item_size = os.path.getsize(item_dir)
            item_status = os.path.isdir(item_dir)
            dir_items += f'- {item}: file_size={item_size} bytes, is_dir={item_status}\n'
        
        return dir_items
    
    except Exception as e:
        return f"Error: {e}"
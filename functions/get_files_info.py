import os

def get_files_info(working_directory, directory="."):
    
    try:
        absolute_path = os.path.abspath(working_directory)

        target_directory = os.path.join(absolute_path, directory)

        valid_target_directory = os.path.commonpath([absolute_path, target_directory]) == absolute_path

        if not valid_target_directory:
            raise ValueError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
        if not os.path.isdir(target_directory):
            raise ValueError(f'Error: "{directory}" is not a directory')
    
        entries = []

        for entry in os.listdir(target_directory):
            path = os.path.join(target_directory, entry)
            is_dir = os.path.isdir(path)
            size = os.path.getsize(path) if not is_dir else None

            entries.append(f"name: {entry} size={size}, is_dir={is_dir}")

        return "/n".join(entries)
    except Exception as e:
        return f"Error: {str(e)}"
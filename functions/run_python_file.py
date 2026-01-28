import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_path = os.path.normpath(
            os.path.join(working_dir_abs, file_path)
        )

        if os.path.commonpath([working_dir_abs, target_path]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", file_path]
        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output_string = []

        if result.returncode != 0:
            output_string.append("Process exited with code X")

        if not result.stderr or result.stdout:
            output_string.append("No output produced")
        
        if result.stderr:
            output_string.append(f"STDERR:\n{result.stderr}")
        
        if result.stdout:
            output_string.append(f"STDOUT:\n{result.stdout}")

        return "\n".join(output_string)

    except Exception as e:
        return f"Error: executing Python file: {e}"
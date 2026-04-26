import os
import subprocess
from google.genai import types

def run_python_file(working_dir, file_path, args=None):

    clean_file_path = file_path.lstrip('/\\')
    abs_working_dir = os.path.realpath(working_dir)
    abs_file = os.path.realpath(os.path.join(abs_working_dir, clean_file_path))

    if os.path.commonpath([abs_working_dir, abs_file]) != abs_working_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file):
        return f'Error: "{file_path}" is not a file or does not exist'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'


    command = ["python3", abs_file]
    if args:
        command.extend(args)
    try:
        completed_process = subprocess.run(
            command,
            cwd=abs_working_dir,
            timeout=30,
            capture_output=True,
            text = True
        )

        output_str = ""

        if completed_process.returncode != 0:
            output_str += f"Process exited with code {completed_process.returncode}\n"
        if not completed_process.stdout and not completed_process.stderr:
            output_str += "\nNo output produced\n"
        else:
            if completed_process.stdout:
                output_str += f"STDOUT:\n{completed_process.stdout}\n"
            if completed_process.stderr:
                output_str += f"STDERR:\n{completed_process.stderr}\n"
        
        return output_str.strip()
    
    except subprocess.TimeoutExpired:
        return 'Error: Execution timed out after 30 seconds'
    except Exception as e:
        return f'Error in executing Python file: {e}'
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional Array of strings to be used as the CLI arguments for the Python file execution",
                items=types.Schema(
                    type=types.Type.STRING
                ),
            )
        },
        required=["file_path"]
    )
)
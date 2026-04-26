import os
from google.genai import types

def write_file(working_dir, file_path, content):

    clean_file_path = file_path.lstrip('/\\')

    abs_working_dir = os.path.realpath(working_dir)
    abs_file = os.path.realpath(os.path.join(abs_working_dir, clean_file_path))

    if os.path.commonpath([abs_working_dir, abs_file]) != abs_working_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    parent_dir = os.path.dirname(abs_file)
    try:
        os.makedirs(parent_dir, exist_ok=True)
    except Exception as e:
        return f'Error: Could not create parent directories for "{parent_dir}"'

    try:
        with open(abs_file, "w", encoding="utf-8") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Failed to write to "{file_path}"'
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory if exists, otherwise creates a new file and writes the content. Creates parent directories if they do not exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            ),
        },
        required=["file_path", "content"]
    )
)
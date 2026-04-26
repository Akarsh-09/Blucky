import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_dir, file_path):

    clean_file_path = file_path.lstrip('/\\')

    abs_working_dir = os.path.realpath(working_dir)
    abs_file = os.path.realpath(os.path.join(abs_working_dir, clean_file_path))

    if os.path.commonpath([abs_working_dir, abs_file]) != abs_working_dir:
        return f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file):
        return f'Error: "{file_path}" is not a file or does not exist'
    

    try:
        file_content_string = ""
        with open(abs_file, 'r', encoding='utf-8') as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read(1):
                file_content_string += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string
    except Exception as e:
        return f"Error: Exception in reading file: {e}"
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specified file relative to the working directory, with a maximum character limit to prevent excessively long responses",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file relative to the working directory (default is the working directory itself)",
            ),
        },
        required=["file_path"]
    )
)

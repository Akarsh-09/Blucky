import os
from google.genai import types


# - README.md: file_size=1032, bytes, is_dir=False
# - src: file_size=128 bytes, is_dir=True
# - package.json: file_size=1234 bytes, is_dir=False


def get_file_info(working_dir, directory="."):

    clean_dir = directory.lstrip('/\\')

    abs_working_dir = os.path.realpath(working_dir)
    abs_dir = os.path.realpath(os.path.join(abs_working_dir, clean_dir))

    if os.path.commonpath([abs_working_dir, abs_dir]) != abs_working_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_dir):
        return f'Error: "{directory}" is not a directory or does not exist'

    contents = os.listdir(abs_dir)

    final_response = ""
    for content in contents:
        content_path = os.path.join(abs_dir, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)

        final_response += f"- {content}: file_size = {size} bytes, is_dir = {is_dir}\n"

    return final_response


schema_get_file_info = types.FunctionDeclaration(
    name="get_file_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
        required=["directory"]
    )
)
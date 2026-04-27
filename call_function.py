import json
from functions.get_dir_info import get_dir_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

# --------- VERY IMP --------- #
# Carefully specify the working directory that Blucky is allowed to access.

working_dir = "calculator" 

def call_function(tool_call, verbose=False):

    function_name = tool_call.function.name

    try:
        args = json.loads(tool_call.function.arguments)
    except json.JSONDecodeError:
        args = {}

    if verbose:
        print(f" - Calling function: {function_name}({args})")
    else:
        print(f" - Calling function: {function_name}({args})")

    result = None
    try:
        if function_name == "get_dir_info":
            result = get_dir_info(working_dir, **args)
        elif function_name == "get_file_content":
            result = get_file_content(working_dir, **args)
        elif function_name == "write_file":
            result = write_file(working_dir, **args)
        elif function_name == "run_python_file":
            result = run_python_file(working_dir, **args)
        else:
            result = f"Error: Unknown function '{function_name}'"

    except TypeError as e:
        result = f"Error: Missing or invalid parameter: {str(e)}"
    except Exception as e:
        result = f"Error: {str(e)}"
    
    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "name": function_name,
        "content": str(result)
    }
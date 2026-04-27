import os
import sys
import json
import argparse
from dotenv import load_dotenv
import openai
from prompts import system_prompt
from functions.get_file_info import schema_get_file_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from call_function import call_function
from config import MAX_ITERS

def main():

    load_dotenv()

    Model_settings = os.environ.get("MODEL_SETTINGS", "{}")
    settings_dict = json.loads(Model_settings)

    api_key = settings_dict.get("API_KEY")
    base_url = settings_dict.get("BASE_URL")
    model_name = settings_dict.get("MODEL")

    client = openai.OpenAI(api_key=api_key, base_url=base_url)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    user_prompt = args.user_prompt

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt}
    ]

    available_functions = [
        schema_get_file_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]

    for i in range(0, MAX_ITERS):

        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=messages,
                tools=available_functions,
                tool_choice="auto"
            )
        except Exception as e:
            print(f"API Error: {e}")
            break

        message = response.choices[0].message

        messages.append(message)

        if args.verbose:
            print(f"\nPrompt: {user_prompt if i == 0 else 'Auto-Iterating...'}")
            print("\n--- Verbose Output ---\n")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")

        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, args.verbose)
                messages.append(result_message)
        else:
            # No more function calls, agent is done - print response and exit
            if message.content:
                print(message.content)
            break

        if i == MAX_ITERS - 1:
            print("Maximum Iterations Limit Reached. Thus Stopping.")
            sys.exit(1)


if __name__ == "__main__":
    main()
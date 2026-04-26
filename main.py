import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.get_file_info import schema_get_file_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from call_function import call_function
from config import MAX_ITERS

def main():

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")

    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    user_prompt = args.user_prompt

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_file_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file,
        ]
    )

    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
    )

    for i in range(0, MAX_ITERS):

        response = client.models.generate_content(
            model='gemma-4-31b-it',
            contents=messages,
            config=config
        )

        if response is None or response.usage_metadata is None:
            print("Response is flawed")
            break

        if args.verbose:
            print("Prompt:", user_prompt)
            print("\n--- Verbose Output ---")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if response.candidates:
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                        continue
                messages.append(candidate.content)

        if response.function_calls:
            for function_call_part in response.function_calls:
                result = call_function(function_call_part, args.verbose)
                messages.append(result)
        else:
            # No more function calls, agent is done - print response and exit
            if response.text:
                print(response.text)
            break

        if i == MAX_ITERS - 1:
            print("Maximum Iterations Limit Reached. Thus Stopping.")
            exit(1)
            return 
 

main()
import os
from google import genai
from google.genai import types
import re
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()

def run(playwright: Playwright,destination) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(destination)
def going_tob_website(destination):
    with sync_playwright() as playwright:
        run(playwright,destination)

def extract_python_code(text):

    pattern = re.compile(r'```python(.*?)```', re.DOTALL)  
    matches = pattern.findall(text)
    
    return matches
def going_to_website(destination):
    with sync_playwright() as playwright:
        run(playwright, destination)


def generate(user_input_given):

    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(
        api_key=api_key,  
    )
    user_input=user_input_given

    model = "gemini-2.5-pro-exp-03-25"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"Given the following command: {command} generate only the **URL** of the website and get the HTML data of the website and also take the state of website. And convert the instructions given as Playwright code. But give only the python code for headless=False state of the browser and No explaination or No comments."), 
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )
    respnse=""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        respnse=respnse+chunk.text
        
    start='```python\n'
    end='```'
    ans=(respnse.split(start))[1].split(end)[0]
    print(ans)
    exec(ans)
        
    
url_match=""
def execute_playwright_code(playwright_code):
    with sync_playwright() as p:

        print(playwright_code)
        exec(playwright_code, {'playwright': p, 'going_to_website': going_to_website})
        

    

if __name__ == "__main__":
    
    command = input("Enter command to automate browser task: ")
    print("Generated Playwright Code:\n", playwright_code)
    
    playwright_code = generate(command)
    

"""with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch a Chromium browser (headless=False to see it)
        page = browser.new_page()
        
        # Dynamically execute the Playwright code
        exec(playwright_code)  # Be careful, make sure the code is safe
        
        # Close the browser after execution
        browser.close()"""



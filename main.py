import os
import gradio as gr
from dotenv import load_dotenv
from google import genai
from google.genai import types

# -----------------setup---------------
load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel(
#     model_name="gemini-1.5-flash",
#     generation_config={
#         "temperature": 0,
#         "max_output_tokens": 50
#     }
# )

# -----------------utils-----------------
def load_prompt(path:str)->str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

BASE_PROMPT = load_prompt("prompts/level_1.txt")

# -----------------agent-----------------
def generate_cli_command(user_input:str)->str:
    full_prompt=f"""
{BASE_PROMPT}

User instruction:
{user_input}
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    # response = model.generate_content(full_prompt)
    # return response.text.strip()
    # response = client.models.generate_content(
    #      model="gemini-1.5-flash",
    #     contents=full_prompt,
    #     config=types.GenerationConfig(
    #         temperature=0,
    #         max_output_tokens=50,
        # model="gemini-1.5-flash",
        # contents=full_prompt,
        # temperature=0,
        # max_output_tokens=50,
        # model="gemini-1.5-flash",
        # contents=full_prompt,
        # generation_config={
        #     "temperature": 0,
        #     "max_output_tokens": 50,
        # }
    
    return response.text.strip()


# -----------------ui-----------------
def main():
    # print("Hello from !")
    #  gr.Interface(
    #     fn=generate_cli_command,
    #     inputs=gr.Textbox(label="הוראה בשפה טבעית"),
    #     outputs=gr.Textbox(label="פקודת CLI"),
    #     title="Natural Language → CLI Agent (Gemini)",
    #     description="Prompt Engineering MVP – Iteration 1"
    # ).launch()
    gr.Interface(
        fn=generate_cli_command,
        inputs=gr.Textbox(label="הוראה בשפה טבעית"),
        outputs=gr.Textbox(label="פקודת CLI"),
        title="Natural Language → CLI Agent (Gemini)",
        description="Prompt Engineering – Iteration 1"
    ).launch()


if __name__ == "__main__":
    main()


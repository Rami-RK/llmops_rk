import os
import gradio as gr
from langchain_community.llms import HuggingFaceEndpoint
import config


# Authentication for Huggingface API
HF_TOKEN = config.api_key
os.environ["HF_TOKEN"] = HF_TOKEN
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN


# Initialization of LLM

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens = 512,
    top_k = 30,
    temperature = 0.1,
    repetition_penalty = 1.03,
)

title = "My OWN ChatGPT"
description = "Implementation of Open Source LLM"

def quena(question):
    result = llm.invoke(question)
    return result
    
demo=gr.Interface(fn=quena,
                  inputs=gr.Textbox(lines=10,placeholder="Write your question."),
                  outputs="text",
                  title=title,
                  description=description,)
# Launch the demo!
demo.launch(share=True)




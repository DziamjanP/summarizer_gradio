from summary import summarize
from parser import parse_pdf
import gradio as gr

demo = gr.Blocks(title="Summary maker", fill_height=True)

# Model aliases for dropdown and their names in APIs
models = {
  "Mistral Medium": "mistral-medium-2505",
  "Magistral Medium": "magistral-medium-2506",
  "Llama 3.3 70B": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
  "Deepseek R1 Distill Llama 70B": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
}

def make_summary(input, model):
  output = summarize(input, models[model])
  return [gr.update(value=output), gr.update(value=output)]
    
with demo:
    gr.Markdown(
    """
    # Summarizer
    Paste your text below to get a brief summary
    """)
    with gr.Row(equal_height=False):
      
      with gr.Column():
        inp = gr.Textbox(label="Input", placeholder="Your text")
        upload = gr.File(label="File with text", file_types=[".pdf"])
        with gr.Accordion("LLM selection", open=False):
          model_selector = gr.Dropdown(choices=models.keys())
        submit = gr.Button("Summarize!")

      with gr.Column():
        with gr.Tab("Text output"):
          out = gr.Textbox(label="Summary", placeholder="Summary will be here", lines=20)
        with gr.Tab("Markdown"):
          out_md = gr.Markdown(label="Summary")

    submit.click(make_summary, inputs=[inp, model_selector], outputs=[out, out_md])
    
    upload.upload(parse_pdf, inputs=upload, outputs=inp)

demo.launch()

from summary import summarize
from parser import parse_pdf
import gradio as gr

demo = gr.Blocks(title="Summary maker")

with demo:
    gr.Markdown(
    """
    # Summarizer
    Paste your text below to get a brief summary
    """)
    inp = gr.Textbox(label="Input", placeholder="Your text")
    upload = gr.File(label="File with text", file_types=[".pdf"])
    submit = gr.Button("Summarize!")
    out = gr.Textbox(label="Summary")
    submit.click(summarize, inp, out)
    upload.upload(parse_pdf, inputs=upload, outputs=inp)

demo.launch()

from summary import summarize
from parser import parse_pdf
import gradio as gr

demo = gr.Blocks(title="Summary maker", fill_height=True)

def make_summary(input):
  output = summarize(input)
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
        submit = gr.Button("Summarize!")
      with gr.Column():
        with gr.Tab("Text output"):
          out = gr.Textbox(label="Summary", placeholder="Summary will be here", lines=20)
        with gr.Tab("Markdown"):
          out_md = gr.Markdown(label="Summary")
    submit.click(make_summary, inp, outputs=[out, out_md])
    upload.upload(parse_pdf, inputs=upload, outputs=inp)

demo.launch()

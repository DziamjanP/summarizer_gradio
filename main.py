from summary import summarize
import gradio as gr

demo = gr.Blocks()

with demo:
    gr.Markdown(
    """
    # Summarizer
    Paste your text below to get a brief summary
    """)
    
    inp = gr.Textbox(label="Input", placeholder="Your text")
    submit = gr.Button("Summarize!")
    out = gr.Textbox(label="Summary")
    submit.click(summarize, inp, out)

demo.launch()

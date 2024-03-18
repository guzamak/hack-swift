from glob import glob
import pathlib
from fastbook import *
import gradio as gr

def predict(picture):
    return model.predict(picture)[0]

interface = gr.Interface(fn=predict,
             inputs=gr.Image(type="pil"),
             outputs=gr.Textbox(),
             allow_flagging='never'
             )

plt = platform.system()
if plt == 'Windows': pathlib.PosixPath = pathlib.WindowsPath

model = load_learner('./rice_diseases_fastai.pkl')

from flask import Flask, render_template, request, send_file
from diffusers import StableDiffusionXLPipeline
import torch
import uuid
import os
from dotenv import load_dotenv

# Load environment variables from .env (optional for token use)
load_dotenv()

app = Flask(__name__)
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# SDXL model
model_id = "stabilityai/stable-diffusion-xl-base-1.0"
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🚀 Using device: {device}")

# Load pipeline
print("⏳ Loading SDXL model...")
pipe = StableDiffusionXLPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    variant="fp16" if device == "cuda" else None,
    use_safetensors=True
)
pipe.to(device)
pipe.enable_attention_slicing()
print("✅ SDXL loaded.")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt'].strip()
    if not prompt:
        return "Prompt is empty!", 400

    print(f"🎨 Generating image for prompt: {prompt}")
    image = pipe(
        prompt,
        num_inference_steps=30,
        guidance_scale=7.5
    ).images[0]

    filename = f"{uuid.uuid4()}.png"
    path = os.path.join(output_dir, filename)
    image.save(path)

    return send_file(path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
# 🖼️ Image Generation Chatbot 🎨

This project is a Flask-based chatbot that generates images from user prompts using **Stable Diffusion** models. It allows users to enter a text prompt and receive a stunning AI-generated image in response.

---

## 🚀 Features

- 🌈 Text-to-image generation using pre-trained models (e.g., Stable Diffusion).
- 🧠 Local inference using `diffusers` and `transformers`.
- 🎯 Web-based frontend with HTML, CSS, and JS.
- 🔥 CUDA/GPU acceleration supported.

---

## 📦 Requirements

Install dependencies via `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Folder Structure

```
image-chatbot/
├── output/
│   └── stores output of images created till now
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── requirements.txt
└── README.md
```

---

## ▶️ Running the App
```
python app.py
```
Open your browser and visit:
http://localhost:5005/

---

## ⚙️ Notes on torch & GPU
For CUDA (GPU) support:
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
Replace cu118 with your CUDA version (cu117, cu121, etc.).

---

## ✨ Sample Prompt
"A futuristic cityscape at night in neon colors, anime style"

🔽 Generates:

![image](https://github.com/user-attachments/assets/3b3b7381-b314-42ef-bd46-209c17bc8674)


---

## 🚀 Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Backend**: Python, Flask, Flask-CORS
- **AI Model**: Stable Diffusion (via 🤗 Hugging Face `diffusers`)
- **Frameworks & Libraries**: PyTorch, Transformers, Diffusers, Accelerate

---

## 📌 Dependencies
- `flask`
- `flask-cors`
- `torch`
- `diffusers`
- `transformers`
- `accelerate`
- `safetensors`


---

## 🧠 Model
Default model: CompVis/stable-diffusion-v1-4

Make sure to accept license and download it locally if needed.

---

## 📝 License
MIT License

---

✨ **Author**: Made by Jasleen Kaur Matharoo  
📧 Email: [jasleen.matharoo@s.amity.edu](mailto:jasleen.matharoo@s.amity.edu)  
🌐 GitHub: [@Jasleen-05](https://github.com/Jasleen-05)

# Table of project.

1. [Face detection system](#Project-1)
2. [Quiz generator](#Project-2)
3. [Android app for sorting data based on file extensions](#file-sorting-android-app)
4. [Telegram bot](#telegram-bot)

---
# Project 1

## Face detection system.

##### Face Detection(with Noise Handling)

A clear, structured roadmap to learn **face detection**, even under **noisy or poor image conditions**, using the best online courses, books, and tutorials.

---

## 🟢 Stage 1: Foundations (Week 1–2)  
> **Goal:** Understand computer vision basics, CNNs, and get familiar with tools.

### ✅ What to Learn:
- Basics of Image Processing
- OpenCV Library
- Introduction to CNN (Convolutional Neural Networks)

### 📚 Resources:
- 📘 Book: *“Make Your Own Neural Network” by Tariq Rashid*
- 🎓 Course: [Coursera – Deep Learning Specialization (Course 4: CNNs)](https://www.coursera.org/specializations/deep-learning)
- 🎥 YouTube: [freeCodeCamp – Deep Learning Crash Course](https://www.youtube.com/watch?v=aircAruvnKk)
- 🧪 Tool: [OpenCV Docs](https://docs.opencv.org/)

---

## 🟡 Stage 2: Classical Face Detection (Week 3)  
> **Goal:** Learn rule-based and traditional methods like Haar and HOG.

### ✅ What to Learn:
- Haar Cascades (OpenCV)
- HOG + SVM (Dlib)
- Landmark Detection (eyes, nose, etc.)

### 📚 Resources:
- 🎓 Udemy: [Python for Computer Vision with OpenCV and Deep Learning](https://www.udemy.com/course/python-for-computer-vision-with-opencv-and-deep-learning/)
- 📘 Book: *“Programming Computer Vision with Python” by Jan Erik Solem*
- 🎥 YouTube: [Murtaza's Workshop Face Detection Tutorial](https://www.youtube.com/watch?v=PmZ29Vta7Vc)

### 🧪 Project Idea:
- Build a webcam-based face detector using OpenCV Haar cascades

---

## 🟠 Stage 3: Deep Learning Face Detection (Week 4–6)  
> **Goal:** Use modern deep learning models for better performance.

### ✅ What to Learn:
- Deep Face Detectors: MTCNN, SSD, YOLO, BlazeFace
- Pretrained Face Detection models (OpenCV DNN, MTCNN)
- Face Alignment & Bounding Box Refinement

### 📚 Resources:
- 🎓 Coursera: [Deep Learning Specialization - Full](https://www.coursera.org/specializations/deep-learning)
- 🎓 Udemy: [Advanced Computer Vision with Python](https://www.udemy.com/course/face-recognition-with-opencv-in-python/)
- 📘 Book: *“Deep Learning for Vision Systems” by Mohamed Elgendy*
- 🧪 GitHub: [ivclab/face-detection](https://github.com/ivclab/face-detection)

### 🧪 Project Idea:
- Use MTCNN to detect faces in group photos with varied lighting.

---

## 🔵 Stage 4: Robust Face Detection in Noisy Images (Week 7–9)  
> **Goal:** Learn how to detect faces in poor, low-light, blurred, or noisy images.

### ✅ What to Learn:
- Image preprocessing:
  - Denoising (Gaussian Blur, Median Filtering)
  - Histogram Equalization
- Noise augmentation for training
- Robust models: RetinaFace, MTCNN

### 📚 Resources:
- 🎓 Udemy: [Image Processing with Python](https://www.udemy.com/course/image-processing-with-python-opencv/)
- 🎓 Coursera: [Image and Video Processing – Duke University](https://www.coursera.org/learn/image-processing)
- 🎥 YouTube: [Nicholas Renotte – Image Noise + Detection](https://www.youtube.com/@nicholasrenotte)
- 📘 Book: *“Image Processing, Analysis, and Machine Vision” by Sonka*

### 🧪 Project Ideas:
- Face detection in blurry CCTV footage
- Apply denoising autoencoder before face detection

---

## 🟣 Stage 5: Advanced Projects + Optimization (Week 10–12)  
> **Goal:** Combine all knowledge to build real-world applications.

### ✅ What to Do:
- Real-time Face Detection with webcam or video input
- Handle occlusions, motion blur, lighting variations
- Deploy model (Flask, FastAPI, or mobile app)

### 📚 Resources:
- 🧪 GitHub: [RetinaFace PyTorch](https://github.com/serengil/retinaface)
- 📘 Book: *“Deep Learning for Computer Vision” by Rajalingappaa Shanmugamani*
- 🎓 Fast.ai Course: [Practical Deep Learning for Coders](https://course.fast.ai/)
- 🎥 YouTube: [PyImageSearch channel](https://www.youtube.com/@PyImageSearch)

### 🧪 Final Projects:
- Face detection with poor lighting + noise
- Build a noisy image face detector dashboard with Streamlit or Flask

---

## 📁 Datasets for Practice

| Dataset | Description |
|--------|-------------|
| [WIDER FACE](http://shuoyang1213.me/WIDERFACE/) | Faces with occlusion, noise, blur |
| [CelebA](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) | Annotated celebrity faces |
| [FDDB](http://vis-www.cs.umass.edu/fddb/) | Benchmark for face detection |
| [LFW](http://vis-www.cs.umass.edu/lfw/) | Labeled Faces in the Wild |

---

## 📆 Summary Timeline

| Week | Focus | Output |
|------|-------|--------|
| 1–2  | Basics of CV & CNN | Detect faces with OpenCV |
| 3    | Classical Detectors | HOG & Haar in practice |
| 4–6  | Deep Learning Models | MTCNN / YOLO Face Detector |
| 7–9  | Noisy Image Handling | Denoising + Detection |
| 10–12| Final Project & Deployment | Real-world face detection system |

---

---

---

---
# Project 2

**Goal**: Build a system that takes **class notes** and **sample question papers** and creates **custom quizzes** in the same style as the sample papers.

---

## 🧩 Step-by-Step Plan with Resources

---

### 🧱 Step 1: Learn the Fundamentals (Programming, NLP, AI)

**What to Learn:**

- Python basics
- NLP concepts (tokenization, parsing, embeddings)
- Transformers and AI basics

**Resources:**

- **Books:**
    - _"Python Crash Course" by Eric Matthes_
- **Courses:**
    - [Python for Everybody – Coursera](https://www.coursera.org/specializations/python)
    - [NLP with Deep Learning – Udemy](https://www.udemy.com/course/natural-language-processing-with-deep-learning-in-python/)
- **YouTube:**
    - [freeCodeCamp - Python for Beginners](https://www.youtube.com/watch?v=rfscVS0vtbw)
    - [Krish Naik – NLP Playlist](https://www.youtube.com/playlist?list=PLZoTAELRMXVNUL99R4bDlVYsncUNvwUBB)

---

### 🔤 Step 2: Text Processing & Preprocessing

**What to Learn:**

- Extract text from PDF or image
- Clean, tokenize, and chunk text

**Tools:**

- `PyMuPDF`, `pdfminer.six`, `Tesseract OCR`, `SpaCy`, `NLTK`

**Resources:**

- [NLTK Docs](https://www.nltk.org/)
- [SpaCy Usage Guide](https://spacy.io/usage)
- [OCR with Python – Tech with Tim](https://www.youtube.com/watch?v=Zsc3nNfYF6A)

---

### 🤖 Step 3: Question Generation (QG)

**What to Learn:**

- Generate WH-, MCQ, and fill-in-the-blank questions
- Prompt engineering

**Tools:**

- `T5`, `BART`, `GPT`, `OpenAI API`, `Hugging Face Transformers`

**Resources:**

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Transformers for NLP – Udemy](https://www.udemy.com/course/nlp-transformers/)
- [Prompt Engineering – Coursera](https://www.coursera.org/learn/prompt-engineering)
- [LangChain Docs](https://docs.langchain.com/)
- [Question Generation with T5 – YouTube](https://www.youtube.com/watch?v=OhF90xX7j98)

---

### 📄 Step 4: Match Style with Sample Question Papers

**What to Learn:**

- Extract format and tone from sample papers
- Use semantic matching for format mimicry

**Tools:**

- `FAISS`, `OpenAI Embeddings`, `SentenceTransformers`, `LangChain`

**Resources:**

- [Few-Shot Prompting – OpenAI Cookbook](https://cookbook.openai.com/)
- [Semantic Search with SBERT](https://www.sbert.net/)

---

### 🏗 Step 5: Build the Backend Pipeline

**Process:**

- Input: Notes + Sample Paper
- Preprocess
- Extract style
- Generate matching questions
- Output quiz

**Tools:**

- Python, OpenAI/Hugging Face, LangChain, LlamaIndex

**Resources:**

- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [LangChain Docs](https://docs.langchain.com/)

---

### 💻 Step 6: Create Optional User Interface

**Tools:**

- `Streamlit`, `Gradio`, `React`

**Resources:**

- [Streamlit Docs](https://docs.streamlit.io/)
- [Gradio Guide](https://www.gradio.app/guides/creating-an-nlp-demo)

---

### 🔁 Step 7: Train, Test, and Improve

**What to Do:**

- Evaluate question quality
- Improve formatting, filtering, and difficulty

**Datasets:**

- [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/)
- [HotpotQA](https://hotpotqa.github.io/)
- [Hugging Face Datasets](https://huggingface.co/datasets)

---

## 🧰 Tech Stack Summary

|Area|Tool / Framework|
|---|---|
|Programming|Python|
|NLP|SpaCy, NLTK|
|Models|T5, BART, GPT|
|Embeddings|OpenAI, SBERT|
|Prompting|OpenAI API, LangChain|
|PDF Parsing|PyMuPDF, pdfminer.six|
|UI|Streamlit, Gradio|
|Vector DB|FAISS, Chroma|
|Hosting|Streamlit Cloud, Hugging Face|

---

---

---

---
# Project 3

## File sorting android app

---

---

---

---
# Project 4

# Telegram bot

Telegram bot which accept text as input, convert into audio and store in Database and send all stored data to particular platform on specified time and date. This project is good for whose schedule is too busy.

# :books: Through coding
- [Official Telegram Bot API Doc](https://core.telegram.org/bots/api)

- [Python Telegram Bot Library](https://docs.python-telegram-bot.org/)

- [BotFather commands guide](https://core.telegram.org/bots#botfather-commands)

# :books: Without coding

- [Manybot](https://manybot.io)
- [ChatFuel](https://chatfuel.com)
- [Flow XO](https://flowxo.com)

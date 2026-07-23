# 🤖 ProPrompter — AI Prompt Engineer

Convert rough, informal ideas into polished, structured prompts for LLMs — free, no signup required.

## What it does
ProPrompt takes a simple or unstructured idea (a sentence or two) and turns it into 
a clear, well-structured prompt ready to use with ChatGPT, Claude, or other LLMs. 
Output length and detail automatically scale to match the complexity of the input — 
a quick birthday message stays short, while a complex request (like interview prep) 
gets a fuller, structured response.

## Tech stack
- **Gradio** — chat interface
- **Google Gemini API** (gemini-3.1-flash-lite, via the `google-genai` SDK) — prompt generation
- **Render** — free hosting

## Try it live
🔗 [proprompter11.onrender.com](https://proprompter11.onrender.com)

> Note: hosted on a free tier, so the app may take up to a minute to "wake up" 
> if it hasn't been used recently.

## Run it locally
```bash
git clone https://github.com/Vd2006/Proprompter.git
cd Proprompter
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Create a `.env` file with:
GEMINI_API_KEY=your_key_here

Then run:
```bash
python app.py
```

## What I learned
Built end-to-end as a hands-on learning project — from requirement gathering and 
prompt engineering to real-world deployment debugging. Along the way: designed and 
iteratively refined a calibration-aware system prompt, handled API rate limits and 
model deprecations, migrated a deprecated SDK mid-project, learned Git/GitHub from 
scratch, and debugged a live server port-binding issue during deployment.

---
Created by Vidhi Dwivedi | forwork.vidhi@gmail.com
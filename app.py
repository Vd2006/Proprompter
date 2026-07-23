import os
from google import genai
import gradio as gr
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found! Please check your Environment Variables.")

client = genai.Client(api_key=api_key)

def generate_ai_prompt(message, history):
    if not message.strip():
        return "Please enter a topic or idea!"
    
    try:
        system_instruction = (
            "You are an expert AI Prompt Engineer. "
            "Convert the user's idea into a high-quality prompt for use with an LLM or image generator. "
            "Scale your output to match the complexity of the input: "
            "if the idea is simple, small, or low-stakes (e.g., a short message, a casual task), "
            "produce a brief, focused prompt of 1-3 sentences. "
            "If the idea is complex, ambiguous, or open-ended (e.g., building a tool, a creative project, "
            "a multi-step task), produce a fuller, structured prompt with clear sections as needed. "
            "Never add structure or length the input doesn't call for."
        )
        
        full_input = f"{system_instruction}\n\nUser Idea: {message}"
        
        # Valid official model name
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=full_input
        )
        
        return response.text
    except Exception as e:
        error_message = str(e)
        if "429" in error_message or "quota" in error_message.lower():
            return "⚠️ We've hit today's usage limit. Please try again in a few minutes, or come back later!"
        # Return exact error for debugging
        return f"⚠️ API Error Details: {error_message}"

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 AI Prompt Engineer")
    gr.Markdown("Enter a simple concept, and this prompt engineer will convert it into a professional, high-quality prompt.")
    
    gr.ChatInterface(
        fn=generate_ai_prompt,
        chatbot=gr.Chatbot(buttons=["copy", "retry"])
    )
    
    # Custom Footer Section
    gr.Markdown(
        "<div style='text-align: center; color: gray; margin-top: 20px; font-size: 14px;'>"
        "✨ Created by <b>Vidhi Dwivedi</b> &nbsp;|&nbsp; 📩 Contact me: <a href='mailto:forwork.vidhi@gmail.com' style='color: #00adb5; text-decoration: none;'><b>forwork.vidhi@gmail.com</b></a>"
        "</div>"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(
        server_name="0.0.0.0",
        server_port=port,
        footer_links=[]
    )
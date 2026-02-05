# 🦆 The Formal-inator 3000

**BEHOLD, PERRY THE PLATYPUS!**  
Every time you send an angry email, Slack message, or rant to the Homeowner’s Association, you risk fines, awkward silences, or HR meetings.  
It is completely unfair!  

So I built THIS: **The Formal-inator 3000!**  
It takes your pure, unadulterated RAGE and translates it into... *Universal Professional English.*  
Now you can be mean... **POLITELY!** ⚡

---

## 🚀 Features
- 🎤 **Voice Input**: Vent your frustrations directly into the microphone.
- 📝 **Text Input**: Type your angry thoughts into the rage box.
- 🤖 **AI-Powered Translation**: Converts raw emotion into professional, diplomatic language.
- 🗂️ **Caching**: Responses are cached to avoid redundant API calls.

---

## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) – UI framework for interactive apps.
- SpeechRecognition – Converts voice input to text.
- [Google Generative AI](https://ai.google.dev/) – Powers the Formal-inator’s diplomatic rewrites.
- dotenv – Loads environment variables.
- `hashlib` – Used for caching responses with MD5 hashing.

---

## 🔄 Workflow

Here’s how the **Formal-inator 3000** works under the hood:

1. **Input Stage**  
   - User either types a rant into the text box or records audio via microphone.  
   - SpeechRecognition converts spoken words into text if voice is used.

2. **Hashing & Cache Check**  
   - The input text is hashed using `hashlib.md5`.  
   - If the hash exists in the cache, the stored response is returned immediately.

3. **Prompt Construction**  
   - A formalization prompt is built, instructing the AI to:  
     - De-escalate emotional tone  
     - Clarify objective facts  
     - Elevate vocabulary  
     - Maintain polite firmness  

4. **AI Processing**  
   - The prompt is sent to Google Generative AI (`gemini-flash-latest`).  
   - The model generates a polished, professional rewrite of the rant.

5. **Special Cases**  
   - Certain inputs trigger humorous overrides.  
   - Otherwise, the AI’s formal output is used.

6. **Output Stage**  
   - The final text is displayed in a clean code block.  
   - Users can copy and paste the polished message into emails, Slack, or reviews.

---

## ⚠️ Notes
- The microphone feature requires proper audio device permissions.
- API usage depends on your Google Generative AI quota.
- This project is for **fun and productivity**—don’t rely on it for **Formal settings** (unless you’re really brave).

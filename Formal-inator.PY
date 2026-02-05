import streamlit as st
import speech_recognition as sr
from google import genai
import os
from dotenv import load_dotenv
import hashlib

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


@st.cache_data
def get_cached_response(text_hash):
    return None

def run_formal_inator(text):
    text_hash = hashlib.md5(text.encode()).hexdigest()
    
    if text_hash in st.session_state.get('response_cache', {}):
        return st.session_state.response_cache[text_hash]
    
    prompt = f"""
    You are the "Formal-inator 3000," the world's most advanced diplomatic translation engine.
    
    Your Mission: 
    Take the user's raw, impulsive, or angry text and rewrite it into "Universal Professional English."
    
    The output must be suitable for:
    - Corporate Emails
    - Slack/Teams Messages
    - Performance Reviews
    - LinkedIn Comments
    - Face-to-Face Conflict Resolution
    
    RULES:
    1. DE-ESCALATE: Remove all anger, sarcasm, and emotional outbursts.
    2. CLARIFY: Focus on the objective facts and the desired outcome.
    3. ELEVATE: Use precise, high-status vocabulary (e.g., instead of "fix this," use "address this discrepancy").
    4. MAINTAIN FIRMNESS: Do not be weak. Be polite but assertive.
    
    Example 1 (Slack): 
    Input: "Stop tagging me, I'm busy." 
    Output: "I am currently heads-down on a critical task. I will review notifications during my next available window."
    
    Example 2 (In-Person): 
    Input: "You are loud and annoying." 
    Output: "I would appreciate it if we could lower our volume to maintain a focused working environment."

    Input Text: "{text}"
    
    Formal-inator Output:
    """
    try:
        response = client.models.generate_content(
            model='gemini-flash-latest',
            contents=prompt
        )
        result = response.text
        
        if 'response_cache' not in st.session_state:
            st.session_state.response_cache = {}
        st.session_state.response_cache[text_hash] = result
        if text == "Perry the Platypus is the best":
            return "Curse you, Perry the Platypus!, Here too 🕵️‍♂️\nYou've triggered the Doofenshmirtz Easter Egg Protocol.\nInitializing: PlatypusInator v3.1...\nSelf-destruct in T-minus 5 seconds...\n 5....\n4....\n3.... Just kidding 😜"
        elif text == "Candace":
            return "MOM! Phineas and Ferb are Testing a Formal-inator 3000!"
        else:
            return result
    except Exception as e:
        return f"Error: The Inator has malfunctioned! {str(e)}"

def activate_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening... Vent your anger! (10 seconds max)")
        
        r.adjust_for_ambient_noise(source, duration=1)
        
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            st.spinner("Processing audio waves...")
            text = r.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            return "Error: Silence detected."
        except sr.UnknownValueError:
            return "Error: Unintelligible grunting."
        except Exception as e:
            return f"Error: {e}"



st.set_page_config(page_title="The Formal-inator",)

st.title(" The Formal-inator 3000")

st.success("""
**BEHOLD, PERRY THE PLATYPUS!** Every time I send an angry email to the Homeowner's Association, I get a fine! 
It is completely unfair!

So I built THIS! **The Formal-inator!** It takes my pure, unadulterated RAGE and translates it into... *Professional Feedback!* Now I can be mean... **POLITELY!** (Evil Laughter) ⚡
""")

if 'rant' not in st.session_state:
    st.session_state.rant = ""
if 'formal_email' not in st.session_state:
    st.session_state.formal_email = ""

st.markdown("### 1. Insert Rage Here ")
col1, col2 = st.columns([3, 1])

with col1:
    text_input = st.text_area(
        "Type your angry thoughts:", 
        value=st.session_state.rant,
        height=120,
        placeholder="Ex: I hate these stupid meetings, they are a waste of time!"
    )

with col2:
    st.write("Or use Voice:")
    if st.button("🎤 Record"):
        recorded_text = activate_microphone()
        if "Error" not in recorded_text:
            st.session_state.rant = recorded_text
            st.rerun()
        else:
            st.error(recorded_text)

if st.button("⚡ ACTIVATE THE INATOR ⚡", type="primary"):
    if text_input:
        with st.spinner("Draining emotion... Injecting synergy..."):
            result = run_formal_inator(text_input)
            st.session_state.formal_email = result
    else:
        st.warning("You must provide input for the Inator to work!")

if st.session_state.formal_email:
    st.markdown("---")
    st.markdown("### 2. The Result 👔")
    st.code(st.session_state.formal_email, language="text")
    st.caption("Copy this and send it before the effects wear off!")

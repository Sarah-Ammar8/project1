import speech_recognition as sr
from gtts import gTTS
import os
import json
import google.generativeai as genai
from streamlit_option_menu import option_menu
import streamlit as st

# ---------------------------------------------------------------------------------------------------
# Configuration and Initialization
# ---------------------------------------------------------------------------------------------------
# Function to load previous conversations from a JSON file
def load_conversations(file_path='conversations.json'):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            st.warning("تم العثور على ملف محادثات تالف. سيتم إعادة تهيئة المحادثات.")
            return []
    return []

# Function to save conversations to a JSON file
def save_conversations(conversations, file_path='conversations.json'):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(conversations, f, ensure_ascii=False, indent=4)

# Configure the Generative AI model with your API key
genai.configure(api_key='AIzaSyCyqQqV1FIE101Jef2lVfyjfl-aNNRPbvk')  # Replace with your actual API key

# Function to get a response from the GPT model
def get_gpt_response(prompt):
    try:
        model = genai.GenerativeModel(model_name='gemini-pro')
        prompt_ = f'''
            أنت روبوت متخصص في مجال الذكاء الاصطناعي فقط، ولا يمكنك تقديم أي معلومات خارج هذا النطاق.
            إذا كان السؤال يتعلق بالذكاء الاصطناعي، أجب عليه بالتفصيل.
            إذا كان السؤال خارج هذا النطاق، أخبر المستخدم أنك لا تستطيع الإجابة على الأسئلة غير المتعلقة بالذكاء الاصطناعي.

            سؤال المستخدم:
            {prompt}
        '''
        response = model.generate_content(prompt_)
        if response:
            return response.text
        else:
            return "لم أحصل على رد من الشات بوت."

    except Exception as e:
        return f"حدث خطأ: {e}"

# Function to convert text to speech and save the audio file
def text_to_speech(text, filename="response.mp3"):
    try:
        tts = gTTS(text=text, lang='ar')  # Change 'ar' to desired language code
        tts.save(filename)
    except Exception as e:
        st.error(f"Error in text-to-speech: {e}")

# Function to capture and convert speech to text
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("يرجى التحدث الآن...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        st.success("جارٍ التعرف على الصوت...")

    try:
        text = r.recognize_google(audio, language="ar")  # Change language as needed
        st.success("تم تحويل الصوت إلى نص بنجاح!")
        return text
    except sr.UnknownValueError:
        st.error("لم يتم التعرف على الصوت. حاول مرة أخرى.")
    except sr.RequestError:
        st.error("تعذر الاتصال بخدمة التعرف على الصوت.")
    return ""

# ---------------------------------------------------------------------------------------------------
# Initialize Session State
# ---------------------------------------------------------------------------------------------------

if 'conversations' not in st.session_state:
    st.session_state.conversations = load_conversations()

if 'selected_conversation' not in st.session_state:
    st.session_state.selected_conversation = None

if 'session_id' not in st.session_state:
    st.session_state.session_id = len(st.session_state.conversations)

# ---------------------------------------------------------------------------------------------------
# Streamlit Page Configuration
# ---------------------------------------------------------------------------------------------------

st.set_page_config(page_title="شات بوت في الذكاء الاصطناعي", layout="wide")

# ---------------------------------------------------------------------------------------------------
# Custom CSS for Styling
# ---------------------------------------------------------------------------------------------------

st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;  /* Light background */
        color: #333;  /* Dark text for better contrast */
    }
    .chatbox {
        height: 500px;
        overflow-y: scroll;
        padding: 10px;
        background-color: #ffffff;  /* White background for chatbox */
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .sender {
        background-color:  #f8f9fa;
        color: black;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        max-width: 70%;
        align-self: flex-end;
        float: right;
        clear: both;
    }
    .bot {
        background-color: #2E8B57;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        max-width: 70%;
        align-self: flex-start;
        float: left;
        clear: both;
    }
    .input-container {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f8f9fa;
        padding: 10px;
        border-top: 1px solid #ccc;
    }
    .audio-icon {
        cursor: pointer;
        margin-left: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------------
# Display the Title of the App
# ---------------------------------------------------------------------------------------------------

st.title("شات بوت في الذكاء الاصطناعي")

# ---------------------------------------------------------------------------------------------------
# Sidebar for Previous Conversations
# ---------------------------------------------------------------------------------------------------

st.sidebar.title("المحادثات السابقة")
if st.session_state.conversations:
    for i, conv in enumerate(st.session_state.conversations):
        if st.sidebar.button(f"عرض المحادثة {i + 1}"):
            st.session_state.selected_conversation = i

if st.session_state.selected_conversation is not None:
    selected_conv = st.session_state.conversations[st.session_state.selected_conversation]
    st.write(f"### محادثة {st.session_state.selected_conversation + 1}:")
    for message in selected_conv:
        if isinstance(message, dict):
            sender = message.get("sender")
            text = message.get("message")
            if sender == "user":
                st.markdown(f"<div class='sender'>{text}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='bot'>{text}</div>", unsafe_allow_html=True)
                audio_file = f"response_{st.session_state.selected_conversation}_{selected_conv.index(message)}.mp3"
                st.audio(audio_file)  # Replay audio for each bot message
    st.stop()

# ---------------------------------------------------------------------------------------------------
# Option Menu for Input Method: Text or Voice
# ---------------------------------------------------------------------------------------------------

selected_input = option_menu(
    menu_title=None,
    options=["كتابة", "صوت"],
    icons=["keyboard", "mic"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# ---------------------------------------------------------------------------------------------------
# Input Field and Buttons (Moved below the option menu)
# ---------------------------------------------------------------------------------------------------

st.markdown("<div class='input-container'></div>", unsafe_allow_html=True)
input_container = st.container()
with input_container:
    cols = st.columns([7, 1, 1])
    with cols[0]:
        if selected_input == "صوت":
            user_input = ""  # Initialize as empty
        else:
            user_input = st.text_input("اكتب استفسارك هنا:", key='text_input')
    with cols[1]:
        if selected_input == "صوت":
            if st.button("🎤 تسجيل الصوت", key='mic_button'):
                with st.spinner("جارٍ تسجيل الصوت..."):
                    voice_text = speech_to_text()
                    if voice_text:
                        st.session_state.conversations.append([{"sender": "user", "message": voice_text}])

                        with st.spinner("جاري معالجة الطلب..."):
                            response = get_gpt_response(voice_text)

                        if response:
                            st.session_state.conversations[-1].append({"sender": "bot", "message": response})
                            audio_file = f"response_{st.session_state.session_id}_{len(st.session_state.conversations)}.mp3"
                            text_to_speech(response, audio_file)  # Save bot's response as audio
        else:
            pass  # Do nothing for text input
    with cols[2]:
        if selected_input == "كتابة":
            if st.button("✈️ إرسال", key='send_button'):
                if user_input.strip():
                    st.session_state.conversations.append([{"sender": "user", "message": user_input}])

                    with st.spinner("جاري معالجة الطلب..."):
                        response = get_gpt_response(user_input)

                    if response:
                        st.session_state.conversations[-1].append({"sender": "bot", "message": response})
                        audio_file = f"response_{st.session_state.session_id}_{len(st.session_state.conversations)}.mp3"
                        text_to_speech(response, audio_file)  # Save bot's response as audio
                else:
                    st.warning("يرجى إدخال نص قبل الإرسال.")

# ---------------------------------------------------------------------------------------------------
# Display the Conversation (Modified to show newest messages first)
# ---------------------------------------------------------------------------------------------------

# Display the conversation in reverse order (newest messages first)
for conv in reversed(st.session_state.conversations):
    for message in conv:
        if isinstance(message, dict):
            sender = message.get("sender")
            text = message.get("message")
            if sender == "user":
                st.markdown(f"<div class='sender'>{text}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='bot'>{text}</div>", unsafe_allow_html=True)
                audio_file = f"response_{st.session_state.session_id}_{len(st.session_state.conversations)}.mp3"
                st.markdown(f"<audio controls src='{audio_file}' class='audio-icon'></audio>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------------
# Button to Clear All Conversations
# ---------------------------------------------------------------------------------------------------

if st.sidebar.button("مسح المحادثات"):
    st.session_state.conversations = []
    st.sidebar.success("تم مسح المحادثات.")

# ---------------------------------------------------------------------------------------------------
# Save Conversations on Script End
# ---------------------------------------------------------------------------------------------------

save_conversations(st.session_state.conversations)

# ---------------------------------------------------------------------------------------------------
# Scrolling to the Latest Message
# ---------------------------------------------------------------------------------------------------

st.markdown("""
    <script>
    var chatbox = document.getElementById('chatbox');
    if(chatbox){
        chatbox.scrollTop = chatbox.scrollHeight;
    }
    </script>
    """, unsafe_allow_html=True)
import streamlit as st
from utils import load_content, get_random_item

# для размера кнопок

custom_css = """
<style>
    .stButton > button {
        font-size: 40px;
        padding: 30px 60px;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# заголовок

st.title('💕 Улучшатель настроения 💕')

# приветственное сообщение

st.write('''
Привет, коллега!

Иногда нам всем в течение рабочего дня становиться немного грустно, особенно на удаленке, без любимых коллег рядом.
Поэтому мы рады видеть тебя в нашем новом приложении, предназначенном для поднятия настроения! Чуть ниже есть две загадочные кнопки, скорее нажимай! 

*Никакого ИИ, весь контент авторский 😊
        ''')

# загружаем контент

compliments = load_content('compliments.txt')
image_paths = load_content('image_paths.txt')

if "compliments_shown" not in st.session_state:
    st.session_state["compliments_shown"] = []
if "images_shown" not in st.session_state:
    st.session_state["images_shown"] = []

left, right = st.columns(2)

def display_text(text):
    '''Кастомное отображение текста'''
    text_with_emoji = f"{text} ❤️"
    st.markdown(
        f'<p style="font-size: 20px; font-family: Arial, sans-serif; color: #2E62DC; text-align: center; border: 2px solid #2E62DC; padding: 10px; font-weight: bold; font-style: italic;">{text_with_emoji}</p>', 
        unsafe_allow_html=True
    )

if left.button("Приятная кнопка"):
    item = get_random_item(compliments, st.session_state["compliments_shown"])
    if item:
        display_text(item)
    else:
        display_text("Пока это все, возвращайся за новой порцией комплиментов позже!")

if right.button("Веселая кнопка"):
    item = get_random_item(image_paths, st.session_state["images_shown"])
    if item:
        st.image(item, use_column_width=True)
    else:
        st.write("Пока это все, возвращайся за новой порцией картинок позже!")




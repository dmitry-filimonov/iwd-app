import streamlit as st
from utils import load_content, get_random_item

# для размера кнопок

# custom_css = """
# <style>
#     .stButton > button {
#         font-size: 20px;
#         padding: 30px 60px;
#     }
# </style>
# """

# st.markdown(custom_css, unsafe_allow_html=True)

# заголовок

st.title('Место для заголовка')

# приветственное сообщение

st.write('Место для приветственного сообщения')

# загружаем контент

compliments = load_content('compliments.txt')
image_paths = load_content('image_paths.txt')

# Use session state to persist shown_items across reruns
if "compliments_shown" not in st.session_state:
    st.session_state["compliments_shown"] = []
if "images_shown" not in st.session_state:
    st.session_state["images_shown"] = []

# Display buttons for content type selection
if st.button("Сделай мне комплимент!"):
    item = get_random_item(compliments, st.session_state["compliments_shown"])
    if item:
        st.write(item)
    else:
        st.write("Пока это все, возвращайся за новой порцией комплиментов позже!")

if st.button("Покажи мне смешную картинку!"):
    item = get_random_item(image_paths, st.session_state["images_shown"])
    if item:
        st.image(item, use_column_width=True)
    else:
        st.write("Пока это все, возвращайся за новой порцией картинок позже!")




import pandas as pd
import streamlit as st
from PIL import Image
import os



# ID Twojego arkusza Google Sheets
sheet_id = "1jnf8qWCOZ8cIHEgIXHs93s64APoiPmsiAV_1MQJe-Pg"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"


def load_data():
    return pd.read_csv(url)

df = load_data()


st.title("Sprawdź swój urlop")

image_url = "https://d3npyywa6qnolf.cloudfront.net/prod/user/823265/eyJ1cmwiOiJodHRwczpcL1wvcGF0cm9uaXRlLnBsXC91cGxvYWRcL3VzZXJcLzgyMzI2NVwvYXZhdGFyX29yaWcuanBnPzE2OTIyNzU2NDciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjI5MCwib3B0aW9ucyI6eyJxdWFsaXR5Ijo5NX19LCJ0b0Zvcm1hdCI6ImpwZWcifX0%3D/Eu%2Fq%2FhM1o8HfA32iLnH6uBNYVnn1hI1idKxeyZDdcRY%3D"  # Podmień na rzeczywisty URL obrazka
st.markdown(
    f'<div align="center"><img src="{image_url}" width="300"></div>',
    unsafe_allow_html=True
)

# Łączenie kolumn Imię i Nazwisko
df['Nazwisko i Imię'] = df['Nazwisko'] + " " + df['Imię']

names = [""] + df['Nazwisko i Imię'].tolist()
full_name = st.selectbox("Wybierz osobę z listy:", names)

# Wybór użytkownika
full_name = st.selectbox("Wybierz osobę z listy:", df['Nazwisko i Imię'])

# Wpisywanie hasła
password = st.text_input("Wpisz swoje hasło:", type="password")

# Przycisk sprawdzający dane
if st.button("Sprawdź urlop"):
    user = df[df['Nazwisko i Imię'] == full_name]

    if user.empty:
        st.error("Nie znaleziono użytkownika!")
    elif user['Hasło'].values[0] == password:
        vacation_days = user['Dni urlopowe'].values[0]
        st.success(f"Pozostało dni urlopowych: {vacation_days}")
    else:
        st.error("Niepoprawne hasło!")

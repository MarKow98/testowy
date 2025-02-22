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



# Łączenie kolumn Imię i Nazwisko
df['Imię i Nazwisko'] = df['Imię'] + " " + df['Nazwisko']

# Wybór użytkownika
full_name = st.selectbox("Wybierz swoje imię i nazwisko:", df['Imię i Nazwisko'])

# Wpisywanie hasła
password = st.text_input("Wpisz swoje hasło:", type="password")

# Przycisk sprawdzający dane
if st.button("Sprawdź urlop"):
    user = df[df['Imię i Nazwisko'] == full_name]

    if user.empty:
        st.error("Nie znaleziono użytkownika!")
    elif user['Hasło'].values[0] == password:
        vacation_days = user['Dni urlopowe'].values[0]
        st.success(f"Pozostało dni urlopowe: {vacation_days}")
    else:
        st.error("Niepoprawne hasło!")

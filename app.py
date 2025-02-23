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
df['Nazwisko i Imię'] = df['Nazwisko'] + " " + df['Imię']

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

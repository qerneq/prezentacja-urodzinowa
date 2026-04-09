import streamlit as st
from datetime import date
import random

# Ustawienia strony
st.set_page_config(page_title="Wszystkiego Najlepszego!", page_icon="🎂")

st.title("🎂 Niespodzianka Urodzinowa!")

# 1. Licznik "Ile to już dni?" (ze screena nr 2)
st.header("1. Licznik 'Ile to już dni jesteś z Nami?'")
urodziny = date(2012, 4, 10) # Tutaj wpisz właściwą datę
dni = (date.today() - urodziny).days
st.metric("Jesteś z nami już tyle dni:", f"{dni} dni")

# 2. Sekcja z kuponami (ze screena nr 1)
st.header("2. Kupony do wykorzystania")
st.write("Kliknij w kupon, aby go zrealizować!")

with st.expander("🎁 KLIKNIJ, ABY ODEBRAĆ PREZENT NR 1"):
    st.write("-> KUPON NA PIZZĘ 🍕")
    st.write("Ważny do końca roku. Płacę ja, jesz Ty!")

with st.expander("🍻 KLIKNIJ, ABY ODEBRAĆ PREZENT NR 2"):
    st.write("-> KUPON NA WSPÓLNĄ ROZRYWKĘ 🍻")
    st.write("Termin do ustalenia – ja stawiam!")

# 3. Wspomnienia 
st.header("3. Wspomnienia")

# Wyświetlanie zdjęcia nr 1
# 'width=500' zapobiega rozjechaniu się zdjęcia na całą szerokość ekranu
st.image("nell.jpg", caption="❤️", width=500)

st.info("Pamiętasz?")

# Wyświetlanie zdjęcia nr 2
st.image("nell4.jpg", caption="Szybka zmiiana scenerii 😂", width=500)

# Wyświetlanie zdjęcia nr 3
st.image("nell2.jpg", caption="❤️", width=500)

# Wyświetlanie zdjęcia nr 4
st.image("nell6.jpg", caption="❤️", width=500)

# Wyświetlanie zdjęcia nr 5
st.image("nell7.jpg", caption="❤️", width=500)  

# Wyświetlanie zdjęcia nr 6
st.image("nell5.jpg", caption="❤️", width=500)

# Dodanie filmiku z folderu
st.subheader("OBYŚ SZŁA PRZEZ ŻYCIE TAK GŁADKO JAK RADZISZ SOBIE NA TYM VIDEO ❤️ JESTEM Z CIEBIE DUMNY❤️:")
# Wpisz dokładną nazwę pliku wideo, który masz w folderze (np. filmik.mp4)
video_file = open('nellvid.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

# 4. Muzyka tak dla umilenia (ze screena nr 2)
st.header("4. Muzyka tak dla umilenia")
# Przykład dla piosenki "Happy"
st.video("https://www.youtube.com/watch?v=ZbZSe6N_BXs")

# --- SEKCJA 5: CHECKLISTA MARZEŃ ---
st.divider() # To narysuje ładną linię oddzielającą
st.header("5. Nasza lista przygód na ten rok ✈️")
st.write("Co Ty na to, żebyśmy w tym roku odhaczyli te rzeczy?")

cele = [
    "wyjscie na salkę gimnastyczną 🤸‍♀ ️",
    "Wyjście na gokarty 🏎️",
    "Przetestowanie polskiej burgerowni 🍔",
    "Tu jest opcja na Twój pomysł! Co chciałabyś zrobić? 🤔",
    "Maraton filmowy 🍿",
    "Coś bardziej szalonego niż reszta, ale nie wiem jeszcze co 😜"
]

# Tworzymy listę do odhaczania
for cel in cele:
    st.checkbox(cel)

# --- SEKCJA 6: GENERATOR UŚMIECHU ---
st.divider()
st.header("6. Generator uśmiechu 😊")
st.write("Gdybyś miał gorszy dzień, kliknij przycisk poniżej!")

komplementy = [
    "Masz najlepsze poczucie humoru na świecie! ❤️",
    "Gdy się smiejesz, cały swiat się cieszy! MY LITTLE CHAMPION! 🏆",
    "Twoja pozytywna energia jest zaraźliwa! ❤️",
    "Jestem z Ciebie dumny, jak ogarniasz gimnastykę i jaką satysfakcję Ci daje! ❤️ 👏",
    "ŻYJ JAK NAJDŁUŻEJ W ZDRÓWKU, KOCHAM CIĘ ❤️",
]

# Przycisk z niespodzianką
if st.button("Kliknij po dawkę pozytywnej energii!"):
    st.balloons() # Animacja balonów
    
    # Wybieramy losowy tekst
    wybrany_tekst = random.choice(komplementy)
    
    # OPCJA 1: Bardzo duże litery (st.header)
    st.header(f"✨ {wybrany_tekst} ✨")
    
    # OPCJA 2 (Jeśli chcesz, żeby tekst był kolorowy i w ramce, ale nieco mniejszy):
    # st.success(wybrany_tekst)
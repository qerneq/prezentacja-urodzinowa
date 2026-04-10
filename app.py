import streamlit as st
import base64
import random
from datetime import date
from streamlit_extras.let_it_rain import rain

# 1. FUNKCJA DO MUZYKI (musi być na samej górze)
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true" loop="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# Ustawienia strony
st.set_page_config(page_title="Wszystkiego Najlepszego!", page_icon="🎂")

st.title("🎂 Niespodzianka Urodzinowa!")

st.write("### 🎵 Włącz muzykę dla lepszego klimatu!")

try:
    audio_file = open('music.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3', loop=True)
except FileNotFoundError:
    st.warning("Wrzuć plik 'music.mp3' do folderu na GitHubie, aby usłyszeć muzykę! 🎶")

# 1. Licznik "Ile to już dni?" (ze screena nr 2)
st.header("Licznik 'Ile to już dni jesteś z Nami?'")
urodziny = date(2012, 4, 10) # Tutaj wpisz właściwą datę
dni = (date.today() - urodziny).days
st.metric("Jesteś z nami już tyle dni:", f"{dni} dni")

# 2. Sekcja z kuponami (ze screena nr 1)
st.header("Kupony do wykorzystania")
st.write("Kliknij w kupon, aby go zrealizować!")

with st.expander("🎁 KLIKNIJ, ABY ODEBRAĆ PREZENT NR 1"):
    st.write("-> KUPON NA PIZZĘ 🍕")
    st.write("Ważny do końca roku. Płacę ja, jesz Ty!")

with st.expander("🍻 KLIKNIJ, ABY ODEBRAĆ PREZENT NR 2"):
    st.write("-> KUPON NA WSPÓLNĄ ROZRYWKĘ 🍻")
    st.write("Termin do ustalenia – ja stawiam!")

# 3. Wspomnienia 
st.header("Wspomnienia")

# Wyświetlanie zdjęcia nr 1
# 'width=500' zapobiega rozjechaniu się zdjęcia na całą szerokość ekranu
st.image("nell.jpg", caption="❤️", use_container_width=True)

st.info("Pamiętasz?")

# Wyświetlanie zdjęcia nr 2
st.image("nell4.jpg", caption="Szybka zmiiana scenerii 😂", use_container_width=True)

# Wyświetlanie zdjęcia nr 3
st.image("nell2.jpg", caption="❤️", use_container_width=True) # To sprawi, że zdjęcie będzie się dopasowywać do szerokości kontenera, ale nie będzie rozciągnięte na całą szerokość ekranu

# Wyświetlanie zdjęcia nr 4
st.image("nell6.jpg", caption="❤️", use_container_width=True)

# Wyświetlanie zdjęcia nr 5
st.image("nell7.jpg", caption="❤️", use_container_width=True)  

# Wyświetlanie zdjęcia nr 6
st.image("nell5.jpg", caption="❤️", use_container_width=True)

# Wyświetlanie zdjęcia nr 7
st.image("nell8.jpg", caption="❤️", use_container_width=True)

# Dodanie filmiku z folderu
st.subheader("OBYŚ SZŁA PRZEZ ŻYCIE TAK GŁADKO JAK RADZISZ SOBIE NA TYM VIDEO ❤️ JESTEM Z CIEBIE DUMNY❤️:")
# Wpisz dokładną nazwę pliku wideo, który masz w folderze (np. filmik.mp4)
video_file = open('nellvid.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

# 4. Muzyka tak dla umilenia (ze screena nr 2)
st.header("Muzyka tak dla umilenia")
# Przykład dla piosenki "Happy"
st.video("https://www.youtube.com/watch?v=DUa7AX1f05w")

# --- SEKCJA 5: CHECKLISTA MARZEŃ ---
st.divider() # To narysuje ładną linię oddzielającą
st.header("Nasza lista przygód na ten rok ✈️")
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
st.header("Generator uśmiechu 😊")
st.write("Gdybyś miał gorszy dzień, kliknij przycisk poniżej!")

komplementy = [
    "Masz najlepsze poczucie humoru na świecie! ❤️",
    "Gdy się smiejesz, cały swiat się cieszy! MY LITTLE CHAMPION! 🏆",
    "Twoja pozytywna energia jest zaraźliwa! ❤️",
    "Jestem z Ciebie dumny, jak ogarniasz gimnastykę i jaką satysfakcję Ci daje! ❤️ 👏",
    "ŻYJ JAK NAJDŁUŻEJ W ZDRÓWKU, KOCHAM CIĘ ❤️",
]

# Przycisk z niespodzianką
# Przykład użycia konfetti w generatorze uśmiechu:
if st.button("Kliknij po dawkę pozytywnej energii! (KAŻDY KLIK TO COŚ INNEGO 😉)"):
    # To puści konfetti (emoji) na 1 sekundę, w ilości 20 sztuk
    rain(
        emoji="🎉",
        font_size=60,
        falling_speed=4,
        animation_length="2s",
    )
    
    st.balloons() # Możesz zostawić balony, będą lecieć razem z konfetti!
    st.header(f"✨ {random.choice(komplementy)} ✨")
    
    

    
    # OPCJA 2 (Jeśli chcesz, żeby tekst był kolorowy i w ramce, ale nieco mniejszy):
    # st.success(wybrany_tekst)
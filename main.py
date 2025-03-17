import streamlit as st

def ascii_to_number(text):
    return int.from_bytes(text.encode('utf-8'), 'big')

def number_to_ascii(number):
    try:
        return number.to_bytes((number.bit_length() + 7) // 8, 'big').decode('utf-8')
    except:
        return "Errore nella decodifica. Assicurati che il numero sia corretto."

st.title("💌 Messaggi Segreti d'Amore 💌")

st.header("Converti un messaggio in numero")
message = st.text_input("Scrivi il tuo messaggio d'amore:")
if st.button("Converti in numero"):
    if message:
        encoded_number = ascii_to_number(message)
        st.success(f"Ecco il tuo messaggio segreto: {encoded_number}")
    else:
        st.warning("Scrivi un messaggio prima di convertire!")

st.header("Decodifica un numero in messaggio")
number = st.text_input("Inserisci il numero da decodificare:")
if st.button("Decodifica"):
    try:
        decoded_message = number_to_ascii(int(number))
        st.success(f"Il messaggio nascosto è: {decoded_message}")
    except ValueError:
        st.error("Inserisci un numero valido!")

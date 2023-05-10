# Dzień 71 Moduły
import requests

url = 'https://example.com/plik_tekst...'

response = requests.get(url)

# Sprawdź, czy żądanie zakończyło się sukcesem (kod odpowiedzi 200)
if response.status_code == 200:
    # Odczytaj zawartość pliku, uwzględniając odpowiednie kodowanie znaków
    text = response.content.decode('UTF-8', errors='ignore')
    print("Pobrany tekst:")
    print(text)
else:
    print(f"Błąd pobierania pliku: {response.status_code}")

# Zadanie

import requests

url = 'https://zerotojunior.dev/cezar.txt.'

response = requests.get(url)

# Sprawdź, czy żądanie zakończyło się sukcesem (kod odpowiedzi 200)
if response.status_code == 200:
    # Odczytaj zawartość pliku, uwzględniając odpowiednie kodowanie znaków
    text = response.content.decode('UTF-8', errors='ignore')
    print("Pobrany tekst:")
    print(text)
else:
    print(f"Błąd pobierania pliku: {response.status_code}")

def decrypt_caesar_cipher(text, shift):
    lowercase_alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    uppercase_alphabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ"
    decrypted_text = ""

    for letter in text:
        if letter in lowercase_alphabet:
            index = (lowercase_alphabet.index(letter) - shift) % len(lowercase_alphabet)
            decrypted_text += lowercase_alphabet[index]
        elif letter in uppercase_alphabet:
            index = (uppercase_alphabet.index(letter) - shift) % len(uppercase_alphabet)
            decrypted_text += uppercase_alphabet[index]
        else:
            decrypted_text += letter

    return decrypted_text

def most_frequent_letter(text):
    text = text.lower()
    letter_counts = {}
    alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"

    for letter in text:
        if letter in alphabet:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

    most_frequent = max(letter_counts, key=letter_counts.get)
    return most_frequent

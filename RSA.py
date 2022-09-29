import os
from time import sleep
import sounddevice as REC
import sboxtrng
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import numpy as np
import random
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import wave
from scipy.io.wavfile import write


# Channels
MONO    = 1
STEREO  = 2
# Częstotliwość próbkowania
SAMPLE_RATE = 44100  
# Czas trwania nagrania
SECONDS = 15

print("Nagrywanie...")
recording = REC.rec( int(SECONDS * SAMPLE_RATE), samplerate = SAMPLE_RATE, channels = MONO, dtype=np.int16)
REC.wait()
print("Nagrano...")
write('recording.wav', SAMPLE_RATE, recording)
print("Zapisano audio")

trng = sboxtrng.trngVector('recording.wav')

#os.remove("recording.wav") 

#skacze po pliku txt i wybiera sobie bity
with open('probki.txt', 'rb') as f:
   klucz = RSA.generate(1024, f.read)

print(klucz)

wiadomosc = simpledialog.askstring(title="Wiadomosc",
                                  prompt="Podaj swoja wiadomosc: \t\t")
print(wiadomosc)

#haszowanie wiadomosc
hash = hashlib.sha224(wiadomosc.encode('ascii')).hexdigest()
# enkryptor
encryptor = PKCS1_OAEP.new(klucz.public_key())  

 # enkrypcja
encrypted_message = encryptor.encrypt(hash.encode('ascii')) 

#edytkowanie klucza
wiadomosc_edytowany_klucz= simpledialog.askstring(title="Wiadomosc",
                                  prompt="Edytuj klucz prywatny: \t\t\t\t\t\t\t\t\t\t\t\t",initialvalue=klucz.export_key().decode('ascii'))


print(wiadomosc_edytowany_klucz)
print('Oreginalny prywatny klucz:')
print(klucz.export_key().decode('ascii'))
 # Porównanie klucza prywatnego z edytowanym i wyświetlenie odpowiednich wiadomości
 
if wiadomosc_edytowany_klucz != klucz.export_key().decode('ascii'): 
    print('UWAGA! Klucz prywanty uległ zmianie!')
else:
    print('ZGODNOŚĆ! Klucze się zgadzją / nie uległ zmianie! .')
    wiadomosc_edytowany_klucz_V2=simpledialog.askstring(title="Wiadomosc",
                                  prompt="Edytuj wiadomosc : \t\t",initialvalue=wiadomosc)

    print(wiadomosc_edytowany_klucz_V2)
    #  dekryptor
    decryptor = PKCS1_OAEP.new(klucz)  
    # uzycie dekryptora aby zdekryptować wiadomosc
    decrypted_message = decryptor.decrypt(encrypted_message)  
   
    if decrypted_message == hashlib.sha224(wiadomosc_edytowany_klucz_V2.encode('ascii')).hexdigest().encode('ascii'):
        print('Nikt nie ingerował.')
    else:
        print('UWAGA! SHA się różni! Ktoś ingerował!')
    print("SHA wiadomości pierwszej:", decrypted_message, "\nSHA wiadomości która została edytowana:", hashlib.sha224(wiadomosc_edytowany_klucz_V2.encode('ascii')).hexdigest().encode('ascii'))

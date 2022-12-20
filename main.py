import tkinter as tk
import datetime
import smtplib
import re, urllib
import urllib.request, ssl
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import speech_recognition as sr
import webbrowser
import requests
from gtts import gTTS
from playsound import playsound
import os
import cv2
import time
import random
import subprocess
from threading import Thread
from responsive_voice import ResponsiveVoice
import pyautogui
import pygame
from tkinter import *


def mainCommands(gender=ResponsiveVoice.MALE, rate=0.52, pitch=0.50, vol=1):
    engine = ResponsiveVoice()
    engine = ResponsiveVoice(lang=ResponsiveVoice.TURKISH)
    r = sr.Recognizer()
    play_sound()


    def record(ask=False):
        with sr.Microphone() as source:
            if ask:
                print(ask)
            audio = r.listen(source)
            voice = ""
            try:
                voice = r.recognize_google(audio, language="tr-TR")
            except sr.UnknownValueError:
                engine.say("anlayamadım", gender=gender, rate=rate, pitch=pitch, vol=vol)
                engine.say("Lütfen arayüz de bulunan butona tekrar tıklayın ve yeniden konuşun", gender=gender, rate=rate, pitch=pitch, vol=vol)
                exit()

            except sr.UnknownValueError:
                engine.say("sistem çalışmadı", gender=gender, rate=rate, pitch=pitch, vol=vol)

            return voice


    def response(voice):
        global numb, month

        if "merhaba" in voice:
            engine.say("Merhabalar efendim,sizin için ne yapabilirim", gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "merhaba Jack" in voice:
            engine.say("Merhabalar efendim,sizin için ne yapabilirim", gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "nasılsın" in voice:
            engine.say("kendimi çok enerjik hissediyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "jack" in voice:
            reply = ["Emrinizdeyim", "Dinliyorum"]
            r = random.choice(reply)
            engine.say(r, gender=gender, rate=rate, pitch=pitch, vol=vol)

        if "not al" in voice:
            engine.say("Ne yazmamı İstiyorsunuz", gender=gender, rate=rate, pitch=pitch, vol=vol)
            time.sleep(0.2)
            note = record()
            file = open('not.txt','a')

            engine.say("Tarih ve saat eklememi ister misin?", gender=gender, rate=rate, pitch=pitch, vol=vol)
            snfm = record()
            if "evet" in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                file.close()
            if "hayır" in snfm:
                file.writelines(note)
                file.close()
                exit()
        if "notları göster" in voice:
            engine.say("notunu gösteriyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            file = open("not.txt", "r")
            engine.say(file.readline(), gender=gender, rate=rate, pitch=pitch, vol=vol)
            file.close()


        def dolar():
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            URL = "https://www.tcmb.gov.tr/kurlar/today.xml"
            dolar = 0
            body = urllib.request.urlopen(URL, context=ctx)
            data = body.read().decode()
            xml = ET.fromstring(data)
            for currency in xml:
                for child in currency:
                    if (child.tag == "ForexSelling" and currency.get("Kod") == "USD"):
                        dolar = float(child.text)
                    else:
                        continue
            engine.say("Dolar Kuru: {}".format(dolar), gender=gender, rate=rate, pitch=pitch, vol=vol)

        if "dolar ne kadar" in voice:
            dolar()
            exit()
        if "altın ne kadar" in voice:
            liste = ["Kuyumcu Alis", "Kuyumcu Satis"]
            website = urllib.urlopen("http://www.bigpara.com/altin/ceyrek-altin-fiyati")
            htmltext = website.read()
            getinspect = '(.+?)'
            pattern = re.compile(getinspect)
            price = re.findall(pattern, htmltext)
            j = 0
            for i in price:
                
                engine.say([j] + " fiyati: " + i)
                j += 1
        def EU():
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            URL = "https://www.tcmb.gov.tr/kurlar/today.xml"
            euro = 0
            body = urllib.request.urlopen(URL, context=ctx)
            data = body.read().decode()
            xml = ET.fromstring(data)
            for currency in xml:
                for child in currency:
                    if (child.tag == "ForexSelling" and currency.get("Kod") == "EUR"):
                        euro = float(child.text)
                    else:
                        continue

            engine.say("Euro Kuru: {}".format(euro), gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "euro ne kadar" in voice:
            EU()
            exit()

        if "teşekkürler" in voice:
            engine.say("rica ederim.Senin için yapabileceğim başka birşey var mı", gender=gender, rate=rate, pitch=pitch, vol=vol)
            thx = record()
            if "Hayır" in thx:
                engine.say("pekala görüşmek üzere", gender=gender, rate=rate, pitch=pitch, vol=vol)
                exit()
        if "düzenli mailleri kontrol et" in voice:
            engine.say("kontrolleri sağlıyorum ancak göze çarpan bir mail bulunmuyor efendim", gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "hey jack" in voice:
            reply = ["Sizi Dinliyorum", "Efendim"]
            r = random.choice(reply)
            engine.say(r, gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "özlettin" in voice:
            engine.say("bende seni özledim az kalsın aküm bitiyordu.esprilerimi özlemiş olmalısın", gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "özledim" in voice:
             engine.say("bende seni özledim az kalsın aküm bitiyordu.esprilerimi özlemiş olmalısın", gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "tarayıcıyı aç" in voice:
            engine.say("interneti açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            os.startfile("chrome")
            exit()
        if "interneti aç" in voice:
            engine.say("interneti açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            os.startfile("chrome")
            exit()
        if "interneti açar mısın" in voice:
            engine.say("interneti açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            os.startfile("chrome")
            exit()
        if "tarayıcıyı açar mısın" in voice:
            engine.say("interneti açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            os.startfile("chrome")
            exit()
        if "napıyorsun" in voice:
            engine.say("her zamanki işlerle meşgulüm.Aslında pek de birşey yaptığım söylenemez", gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "ne yapıyorsun" in voice:
            engine.say("her zamanki işlerle meşgulüm.Aslında pek de birşey yaptığım söylenemez", gender=gender, rate=rate, pitch=pitch, vol=vol)

        if "okuldan nefret ediyorum" in voice:
            engine.say("okul iyidir bende okula gitmek isterdim ama sadece kodlardan oluşuyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "bilgisayarı kapat" in voice:
            os.system("shutdown /s /t 15")
            engine.say("Bilgisayarınız 15 saniye içinde kapatıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "bilgisayarı kapatır mısın" in voice:
            os.system("shutdown /s /t 15")
            engine.say("Bilgisayarınız 15 saniye içinde kapatıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "sistemi kapat" in voice:
            os.system("shutdown /s /t 15")
            engine.say("Bilgisayarınızı 15 saniye içinde kapatıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "sistemi kapatır mısın" in voice:
            os.system("shutdown /s /t 15")
            engine.say("Bilgisayarınızı 15 saniye içinde kapatıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "hesap makinesini aç" in voice:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            engine.say("hesap makinesini açtım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "hesap makinesini açar mısın" in voice:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            engine.say("hesap makinesini açtım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()

        if "not defterini aç" in voice:
            engine.say("Not Defterini açtım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

            exit()
        if "not defterini açar mısın" in voice:
            engine.say("Not Defterini açtım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

            exit()

        if "sence aşı olmalı mıyım" in voice:
            engine.say(
                "eğer salgın hastalık için bir aşı bulunduysa ve çoğunluk yaptırıyorsa sen de sağlığın için yaptırmalısın", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()

        if "ben de iyiyim teşekkürler" in voice:
            engine.say("İyi olmana sevindim,senin için yapabileceğim birşey var mı?", gender=gender, rate=rate, pitch=pitch, vol=vol)
        elif "ben de iyiyim" in voice:
            engine.say("İyi olmana sevindim,senin için yapabileceğim birşey var mı?", gender=gender, rate=rate, pitch=pitch, vol=vol)
        elif "iyiyim" in voice:
            engine.say("pekala kendine iyi bak seni burada bekliyor olacağım", gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "iyi olmaya çalışıyorum" in voice:
            engine.say("senin için yapabileceğim birşey var mı?", gender=gender, rate=rate, pitch=pitch, vol=vol)



        if "yok" in voice:
            engine.say("pekala kendine iyi bak seni burada bekliyor olacağım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "hayır" in voice:
            engine.say("Pekala Ben burada seni bekliyor olacağım şimdilik görüşmek üzere", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "hayır yok" in voice:
            engine.say("pekala kendine iyi bak seni burada bekliyor olacağım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "şuan yok" in voice:
            engine.say("Pekala Ben burada seni bekliyor olacağım şimdilik görüşmek üzere", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()

        if "peki" in voice:
            engine.say("Tekrar görüşmek üzere", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "pekala görüşürüz" in voice:
            engine.say("görüşmek üzere", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()

        if "koronavirüsten korunma yolları" in voice:
            engine.say(
                "dışarıya çıktığında maskeni tak ve yüzeylere fazla dokunmamaya çalış son olarak insanlarla mesafeni koru", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "özledim seni jack" in voice:
            engine.say("bende seni özledim.senin için yapabileceğim bir şey var mı?", gender=gender, rate=rate, pitch=pitch, vol=vol)

        if "okula gidiyor musun" in voice:
            reply = ["Şuan için asistanlık yapıyorum", "hayır sadece asistanlık yapıyorum", "maalesef gitmiyorum"]
            r = random.choice(reply)
            engine.say(r, gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "kamerayı aç" in voice:
            engine.say("kamerayı açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(1)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
            exit()
        if "ekran görüntüsü " in voice:
            ekran_goruntusu = pyautogui.screenshot()
            dosya_adi = "ekran_goruntusu.jpg"
            dosya_yolu = os.path.join('.', dosya_adi)
            ekran_goruntusu.save(dosya_yolu)
            engine.say("ekran görüntüsü yolda", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "ekran görüntüsü al" in voice:
            ekran_goruntusu = pyautogui.screenshot()
            dosya_adi = "ekran_goruntusu.jpg"
            dosya_yolu = os.path.join('.', dosya_adi)
            ekran_goruntusu.save(dosya_yolu)
            engine.say("ekran görüntüsü yolda", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "ekran görüntüsü alır mısın" in voice:
            ekran_goruntusu = pyautogui.screenshot()
            dosya_adi = "ekran_goruntusu.jpg"
            dosya_yolu = os.path.join('.', dosya_adi)
            ekran_goruntusu.save(dosya_yolu)
            engine.say("ekran görüntüsü yolda", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "hayat nasıl gidiyor" in voice:
            reply = ["Her zaman ki gibi asistanlık yapıyorum", "iyi gidiyor senin hayatın nasıl",
                     "teşekkürler herşey yolunda"]
            r = random.choice(reply)
            engine.say(r, gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "iyi gidiyor" in voice:
            engine.say("iyi olmasına sevindim yardıma ihtiyacın olursa her daim buradayım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "iyi" in voice:
            engine.say("iyi olmasına sevindim yardıma ihtiyacın olursa her daim buradayım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "kötü" in voice:
            engine.say("yardıma ihtiyacın olursa her daim buradayım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "normal" in voice:
            engine.say("yapabileceğim bir şey var mı", gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "ınstagram'ı aç" in voice:
            engine.say("açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            url = "https://www.instagram.com"
            webbrowser.get().open(url)
            exit()
        if "ınstagram'ı açar mısın" in voice:
            engine.say("açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            url = "https://www.instagram.com"
            webbrowser.get().open(url)
            exit()
        if "bugün aşı oldum" in voice:
            engine.say("geçmiş olsun umarım faydasını görürsün.Yavaş yavaş espri yeteneğimi anlayacaksın", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()


        if "facebook'u açar mısın" in voice:
            engine.say("1 Saniye", gender=gender, rate=rate, pitch=pitch, vol=vol)
            url = "https://www.facebook.com"
            webbrowser.get().open(url)
            exit()
        if "facebook'u aç" in voice:
            engine.say("1 Saniye", gender=gender, rate=rate, pitch=pitch, vol=vol)
            url = "https://www.facebook.com"
            webbrowser.get().open(url)
            exit()

        if "youtube aç" in voice:
            engine.say("hemen açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            url = "https://www.youtube.com"
            webbrowser.get().open(url)
            exit()
        if "youtube açar mısın" in voice:
            engine.say("hemen açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            url = "https://www.youtube.com"
            webbrowser.get().open(url)
            exit()
        if "gmail i aç" in voice:
            engine.say("Gmail i Açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            url = "gmail.com"
            webbrowser.get().open(url)
            exit()
        if "gmail i açar mısın" in voice:
            engine.say("Gmail i Açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            url = "gmail.com"
            webbrowser.get().open(url)
            exit()

        def hava_durumu():
            API = "51018b60257b50207fc63de7c53af5e1"
            SEHIR_ISMI = "Gaziantep"
            BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?appid={API}&q={SEHIR_ISMI}"
            gelen_veri = requests.get((BASE_URL))
            gelen_veri_JSON = gelen_veri.json()
            celsius = float(gelen_veri_JSON["main"]["temp"]) - 273
            return engine.say(str(int(celsius))+" santigrat derece",gender=gender, rate=rate, pitch=pitch, vol=vol)

        if "hava durumu" in voice:
            hava_durumu()
            exit()
        def muzikAc():
            reply = ["Keyfini yerine getirmeye hazırım", "senin için birkaç parça çalıyorum",
                     "müzik açıyorum"]
            r = random.choice(reply)
            engine.say(r, gender=gender, rate=rate, pitch=pitch, vol=vol)
            url = "https://www.youtube.com/watch?v=XBBt2q_yKC0&list=RDCLAK5uy_n1j1GACZO4o7U1m708pa7jV1q7zR-cY44&start_radio=1"
            webbrowser.get().open(url)


        if "bunaldım" in voice:
            engine.say("keyfini yerine getirmek için bir müzik açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            muzikAc()
            exit()

        if 'müzik aç' in voice:
            engine.say("Müzik açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            muzikAc()
            exit()
        if 'müzik açar mısın' in voice:
            engine.say("Müzik açıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            muzikAc()
            exit()
        if "sesi aç" in voice:
            pyautogui.press("volumeup")
            engine.say("sesi 2 kademe arttırdım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "sesi açar mısın" in voice:
            pyautogui.press("volumeup")
            engine.say("sesi 2 kademe arttırdım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "sesi kıs" in voice:
            pyautogui.press("volumedown")
            engine.say("sesi 2 kademe azalttım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "sesi kısar mısın" in voice:
            pyautogui.press("volumedown")
            engine.say("sesi 2 kademe azalttım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "sesi kapat" in voice:
            engine.say("sesi kapatıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            time.sleep(4)
            pyautogui.press("volumemute")
            exit()
        if "sesi kapatır mısın" in voice:
            engine.say("sesi kapatıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            time.sleep(4)
            pyautogui.press("volumemute")
            exit()

        if "sen bu işi yapıyorsun" in voice:
            engine.say("teşekkür ederim yapımcım sayesinde her geçen gün bir şeyler öğreniyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()

        if "hangi gün deyim" in voice:
            months = {
                "January": "Ocak",
                "February": "Şubat",
                "March": "Mart",
                "April": "Nisan",
                "May": "Mayıs",
                "June": "Haziran",
                "July": "Temmuz",
                "August": "Ağustos",
                "September": "Eylül",
                "October": "Ekim",
                "November": "Kasım",
                "December": "Aralık"
            }
            days = {
                "Monday": "Pazartesi",
                "Tuesday": "Salı",
                "Wednesday": "Çarşamba",
                "Thursday": "Perşembe",
                "Friday": "Cuma",
                "Saturday": "Cumartesi",
                "Sunday": "Pazar"
            }
            month = time.strftime("%B")
            day = time.strftime("%A")
            numb = time.strftime("%d")
            engine.say(numb + months[month] + days[day], gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "bugün günlerden ne" in voice:
            months = {
                "January": "Ocak",
                "February": "Şubat",
                "March": "Mart",
                "April": "Nisan",
                "May": "Mayıs",
                "June": "Haziran",
                "July": "Temmuz",
                "August": "Ağustos",
                "September": "Eylül",
                "October": "Ekim",
                "November": "Kasım",
                "December": "Aralık"
            }
            days = {
                "Monday": "Pazartesi",
                "Tuesday": "Salı",
                "Wednesday": "Çarşamba",
                "Thursday": "Perşembe",
                "Friday": "Cuma",
                "Saturday": "Cumartesi",
                "Sunday": "Pazar"
            }
            month = time.strftime("%B")
            day = time.strftime("%A")
            numb = time.strftime("%d")
            engine.say(numb + months[month] + days[day], gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "10 kasım" in voice:
            engine.say(
                "1938 günü yaşamını yitiren, Türkiye'nin kurucusu ve ilk Cumhurbaşkanı Mustafa Kemal Atatürk Saygı ve özlemle", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()

        if "basit bir yemek tarifi" in voice:
            reply = ["Tava yı ocağa koy biraz yağ ekle yumurta kır ve ye",
                     "Tencereye su, yağ ve tuz eklemen gerek daha sonra kaynaması için birazcık bekle ardından makarnayı içine at ve piştiğinden emin olana kadar kısık ateşte beklet oldu sana makarna"]
            r = random.choice(reply)
            engine.say(r, gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()


        if "24 kasım" in voice:
            engine.say("Geleceğe ışık tutan tüm öğretmenlerimizin günü.", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()

        if "31 aralık " in voice:
            engine.say("Yılın son günü", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()


        if "8 mart" in voice:
            engine.say("Dünya Kadınlar Günü", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "23 nisan" in voice:
            engine.say("Mustafa Kemalin önderliğinde ki Ulusal Egemenlik ve Çocuk Bayramı kutlu olsun.", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()

        if "zar at" in voice:
            zar = ['1', '2','3','4','5','6']
            zar_secim = random.choice(zar)
            engine.say("zarın sonucu" + zar_secim, gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "zar atar mısın" in voice:
            zar = ['1','2','3','4','5','6']
            zar_secim = random.choice(zar)
            engine.say("zarın sonucu" + zar_secim, gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "yazı tura at" in voice:
            bozukpara = ['yazı', 'tura']
            yazitura = random.choice(bozukpara)
            engine.say(yazitura + "geldi", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "yazı tura atar mısın" in voice:
            bozukpara = ['yazı', 'tura']
            yazitura = random.choice(bozukpara)
            engine.say(yazitura + "geldi", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "saat kaç" in voice:
            engine.say(time.strftime("%H:%M"), gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "saat" in voice:
            engine.say(time.strftime("%H:%M"), gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()

        if "siri'yi tanıyor musun" in voice:
            engine.say("o da benim gibi bir asistan", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()

        if "arama yap" in voice:
            engine.say("ne aramak istiyorsun", gender=gender, rate=rate, pitch=pitch, vol=vol)
            search = record("ne aramak istiyorsun")
            url = "https://google.com/search?q=" + search
            engine.say(search + "için bulduklarım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            webbrowser.get().open(url)
            exit()
        if "arama yapar mısın" in voice:
            engine.say("ne aramak istiyorsun", gender=gender, rate=rate, pitch=pitch, vol=vol)
            search = record("ne aramak istiyorsun")
            url = "https://google.com/search?q=" + search
            engine.say(search + "için bulduklarım", gender=gender, rate=rate, pitch=pitch, vol=vol)
            webbrowser.get().open(url)
            exit()
        if "adın ne" in voice:
            engine.say("Aslında Birçok adım var ama yapımcım bana Jack olarak hitap ediyor", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "ismin ne" in voice:
            engine.say("Aslında Birçok adım var ama yapımcım bana Jack olarak hitap ediyor", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "tesla hakkında ne düşünüyorsun" in voice:
            engine.say(
                "yaptıkları Tesla arabalar Starlink internet altyapısı SpaceX uzay araçları hepsi geleceği kurtarmak için bir çözüm olabilir", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "neredesin" in voice:
            reply = ["Kafanızın bir köşesindeyim", "Nerede olmamı isterseniz oradayım", "Emrinizdeyim",
                     "az önce bir devre kartı tasarlıyordum kısacası uğraş halindeydim",
                     "onun yanında değilim", "heran yanınızdayım",
                     "işlemcinizin soğutucu ile ilgileniyordum.biraz destek gerekli gibi duruyor. buyrun efendim ne demiştiniz"]
            r = random.choice(reply)
            engine.say(r, gender=gender, rate=rate, pitch=pitch, vol=vol)

        if "seni kim yarattı" in voice:
            a = ["Ali Eren tarafından oluşturuldum", "Ali eren tarafından piyasaya giriş yaptım",
                 "Beni yaratan Ali eren",
                 "ismimi Jack olarak belirleyen Ali Eren tarafından sizlere hizmet etmek üzere yaratıldım"]
            s = random.choice(a)
            engine.say(s, gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()

        if "ne yapabilirsin" in voice:
            engine.say("internette arama yapabilir mail gönderebilir seninle tatlı sohbetler edebilirim ayrıca uygulamar açabilirim", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()

        if "hangi tür müzikler seversin" in voice:
            engine.say("Aslında yerine göre diyebilirim sen ne dinlersen bende onları dinliyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "müziği kapat" in voice:
            engine.say("kapatıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            pygame.mixer.music.pause()
        if "müziği kapatır mısın" in voice:
            engine.say("kapatıyorum", gender=gender, rate=rate, pitch=pitch, vol=vol)
            pygame.mixer.music.pause()
        if "naber" in voice:
            engine.say("iyiyim senden naber", gender=gender, rate=rate, pitch=pitch, vol=vol)

        if "tamamdır" in voice:
            engine.say("görüşürüz", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()


        if "görüşürüz" in voice:
            engine.say("kendine iyi bak", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()
        if "anladım" in voice:
            engine.say("peki", gender=gender, rate=rate, pitch=pitch, vol=vol)
            exit()

        sevgili = ["Hayır yok", "Galiba ben sanal birisi olduğum için görüşmemiz zor oluyor", "Sanal Asistanlar yalnız yaşamayı severler en azından benim için öyle"]

        if "nerede" in voice:
            engine.say("Konum Bilgisini söyleyin", gender=gender, rate=rate, pitch=pitch, vol=vol)
            time.sleep(0.35)
            voice = voice.replace("nerede", "")
            location = record()
            engine.say(location + "burada", gender=gender, rate=rate, pitch=pitch, vol=vol)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            exit()
        if "bilgi ver" in voice:
            engine.say("hangi konuda bilgi vermemi istersin ?", gender=gender, rate=rate, pitch=pitch, vol=vol)
            results = record("hangi konuda bilgi vermemi istersin ?")
            engine.say(f"{results} için ufak bir bilgi veriyorum. ", gender=gender, rate=rate, pitch=pitch, vol=vol)

            wikipedia = f"https://tr.wikipedia.org/wiki/{results.capitalize().replace(' ', '_')}"
            r = requests.get(url=wikipedia)
            soup = BeautifulSoup(r.content, "lxml")
            text = ""

            for i in soup.find_all("p"):
                text += i.text
            with open("bilgi.txt", "w", encoding="utf-8") as f:
                f.write(text)
            for j in range(8):
                with open("bilgi.txt", "r", encoding="utf-8") as g:
                    okunacak_bilgi = g.readlines()
                engine.say(okunacak_bilgi[j], gender=gender, rate=rate, pitch=pitch, vol=vol)

            os.remove("bilgi.txt")


        if "sevgilin var mı" in voice:
            engine.say(random.choice(sevgili), gender=gender, rate=rate, pitch=pitch, vol=vol)

        ask = ["bir asistan olarak aşk konularına çok uzak kaldığım için yorum yapamıyorum efendim.Başka bir sorun var mı?"]
        if "aşık olmak nasıl birşey" in voice:
            engine.say(random.choice(ask), gender=gender, rate=rate, pitch=pitch, vol=vol)
        if "hiç aşık oldun mu" in voice:
            engine.say(random.choice(ask), gender=gender, rate=rate, pitch=pitch, vol=vol)

    def speak(string):
        tts = gTTS(string, lang="tr")
        rand = random.randint(1, 10000)
        file = "audio-" + str(rand) + ".mp3"
        tts.save(file)
        playsound(file)
        os.remove(file)
    time.sleep(1)
    while True:
        voice = record()
        voice = voice.lower()
        print(voice)
        response(voice)
        play_sound()
        time.sleep(1)
pygame.mixer.init()
def play_sound():
   pygame.mixer.music.load("dinlemesesi.mp3")
   pygame.mixer.music.play()
def gui(geometry, title):
    root = Tk()
    root.configure(background='white')
    root.geometry(f"{geometry}")
    root.title(f"{title}")
    picture = PhotoImage(file='mikrofon.png')
    speak = Button(root,image=picture,bg="white",borderwidth=0, command=lambda: Thread(target=mainCommands).start())
    speak.image=picture
    speak.pack()
    isim1=tk.Label(root,text="JACK",fg="blue",bg="white",font="Times 20 italic")
    isim1.pack()
if __name__ == "__main__":
    gui("300x200", "Jack Asistan")
    mainloop()

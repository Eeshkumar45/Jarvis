import speech_recognition as sr
lis = sr.Recognizer()

try:
    with sr.Microphone() as source:
        text = lis.listen(source)
        textg = lis.recognize_google(text)
        print(textg)
        #texts = lis.recognize_sphinx(text)
        #print(textg)
        #textgc = lis.recognize_google_cloud(text)
        #print(textgc)
        textw = lis.recognize_wit(text,'KFPTWX23MX22H27Z45QLPPPDLFB7IN6E')
        print(textw)
        #text =  lis.recognize_ibm(text,'eeshkumars45@gmail.com','Eesh()Kumar22')
        lis.recognize_bing()
except:
    print('repeat')

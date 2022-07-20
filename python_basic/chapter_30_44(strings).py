from icecream import ic
text = 'python is a popular programming language.'
print(text.capitalize())



def harf_adedi_bulucu( metin,
                       harf):
    print(f"Girdiginiz metinde {metin.count(harf)} adet '{harf}' harfi var.")
metin="python is a popular programming language."
harf_adedi_bulucu(metin,"p")



code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'

if (code1[-4:]=="2020"):
    print(True)
else:
    print(False)

path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'
harf_adedi_bulucu(path1,"youtube")

path1 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
path2 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer'
path3 = 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'

print(path1.find("scientist"))
print(path2.find("scientist"))
print(path3.find("scientist"))


code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'


ic(code1.isalnum())
ic(code2.isalnum())



text = 'Google Colab'
ic(text.upper())



text = '  Google Colab   '
ic(text)
ic(text.strip())

text = 'Google Colab'
ic(text.lower())

code= 'FVNISJND-XX'
ic(code.replace("-"," "))

text = '340-23-245-235'
ic(text.replace("-",""))

text = 'Open,High,Low,Close'
ic(text.split(","))


text = """Python is a general-purpose language.
Python is popular."""
ic(text.splitlines())


num = 34
ic(str(num).zfill(10))


url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
slas_konum=url[::-1].find("/")
ic(url[-slas_konum:].replace("-"," "))
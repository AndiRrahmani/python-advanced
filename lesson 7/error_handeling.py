

numri1 = 10

numri2 = 2

try:
    rezultati = numri1/numri2

except ZeroDivisionError:
    print("Hejjj nuk munesh me pjestu me 000")


numri4 = 20

numri5 = 0

try:
    rezultati = numri4/numri5

except ZeroDivisionError:
    print("Hejjj nuk munesh me pjestu me 000")
else:
    print("pjestimi eshte i pranueshem")

mesazhi = "hello"
try:
    textToInt = int(mesazhi)
except Exception as e:
    print("ka ndodhe nje error",e)



def divide_numbers(a,b):
    try:
        rezultat = a/b
        print("rezultati eshte :",rezultat)

    except ZeroDivisionError:
        print("hej ke provu me pjestu me 0")

    except TypeError:
        print("Invalid type for division")
    except Exception as a:
        print("Ka ndodh nje error",a)

divide_numbers(10,5)
def readfile(filename):
    with open(filename,'r', encoding='utf-8') as file:
        return file.readlines()

def workingwithfiles(filename1=None, filename2=None):
    try:
        if not filename1:
            filename1=input("podaj nazwe pliku nr 1")
        if not filename2:
            filename2 = input("podaj nazwe pliku nr 2")

        news1= readfile(filename1)
        news2=readfile(filename2)

        outputf='wynik.txt'

        with open(outputf, "w", encoding='utf-8') as outf:
            maxx=max(len(news1),len(news2))
            for i in range(maxx):
                if i < len(news1):
                    outf.write(news1[i])
                if i < len(news2):
                    outf.write(news2 [i])
        print('zapisano do pliku')

    except FileNotFoundError:
        print("nie ma takiego pliku")
    except Exception as e:
        print(e)

workingwithfiles("anita.txt","jakis.txt")

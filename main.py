# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def lei(le: float):
    undiv = le - 20
    LEI = undiv / 65
    return LEI


def ei(mys: float, eys: float):
    def mysi(mys: float):
        MYSI = mys / 15
        return MYSI

    def eysi(eys: float):
        EYSI = eys / 18
        return EYSI

    rei = mysi(mys) + eysi(eys)
    EI = rei / 2
    return EI


def ii(gnipc: float):
    from math import log
    rii = log(gnipc) - log(100)
    II = rii / log(750)
    return II


def hdi(le: float, mys: float, eys: float, gnipc: float):
    LEI = lei(le)
    EI = ei(mys, eys)
    II = ii(gnipc)
    from math import cbrt
    hdisum = LEI + EI + II
    mean = hdisum / 3
    HDI = cbrt(mean)
    return HDI


def truncate(f: float, n: int):
    s = '{}'.format(f)
    if "e" in s or "E" in s:
        return '{0:.{1}f}'.format(f, n)  #
    i, p, d = s.partition('.')
    return '.'.join([i, (d + '0' * n)[:n]])


def output_file(hdi, country, filesans):
    filepth = "%s.csv" % filesans
    nfile = input("Is (%s) a new file? [y/n]\n" % filepth)
    if nfile.lower() == "y":
        header = True
    else:
        header = False

    try:
        with open(filepth, 'a') as fileraw:
            if header:
                fileraw.write("Country, Human Development Index\n")
            else: pass
            fileraw.write("%s, %s\n" % (country, hdi))
        fileraw.close()
    except OSError or IOError as exceptio:
        print("Exception occurred: %s" % exceptio)
        from tkinter import messagebox as MsgBox
        MsgBox.showerror("Error", "An error occurred: %s." % exceptio)



def mainloop():
    le = float(input("Enter Life Expectancy:\n"))
    mys = float(input("Enter mean years of schooling:\n"))
    eys = float(input("Enter expected years of schooling:\n"))
    gnipc = float(input("Enter GNI per capita:\n"))
    HumanDI = hdi(le, mys, eys, gnipc)
    HDITrunc = truncate(HumanDI, 3)
    from tkinter import messagebox as MsgBox
    import NewLine
    NewLine.Run("-", 50, "HDI Calculated: %s" % HDITrunc)
    MsgBox.showinfo("HDI Calculator", "Country's HDI is: %s" % HDITrunc)
    write = input("Write to file? [y/n]\n")
    write = write.lower()
    if "y" in write:
        file = input("Enter path to valid CSV file or desired creation path: (do not include .csv)\n")

        country = input("Enter country name:\n")
        output_file(HDITrunc, country, file)
    else:
        pass

    mainloop()


mainloop()

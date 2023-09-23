# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from math import log

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


def mainloop():
    le = float(input("Enter Life Expectancy:\n"))
    mys = float(input("Enter mean years of schooling:\n"))
    eys = float(input("Enter expected years of schooling:\n"))
    gnipc = float(input("Enter GNI per capita:\n"))
    HumanDI = hdi(le, mys, eys, gnipc)
    from tkinter import messagebox as MsgBox
    MsgBox.showinfo("HDI Calculator", "Country's HDi is: %s" % HumanDI)
    mainloop()


mainloop()







try:
    def Run(Char="", Repeat=int(1), StrTxt=""):
        if Repeat > 0:  #If Repeat is less than 0, return an error(below)
            print("%s%s%s" %(Char*Repeat, StrTxt, Char*Repeat))     #print Char (Repeat) times; print StrTxt if any , then print Char (Repeat) times
            return True
        else:
            print("An error occured in module NewLine(Char as str, Repeat as int, StrTxt as str): Integer (Repeat) cannot be 0 or negative. Use of %s not possible." %(Repeat))
            from tkinter import messagebox as MsgBox
            MsgBox.showerror("Error", "An error occured in module NewLine(Char as str, Repeat as int, StrTxt as str): Integer (Repeat) cannot be 0 or negative. Use of %s not possible." %(Repeat))
            return False
except Exception as error:
    print("An exception occured in module NewLine: %s." %(error))
    from tkinter import messagebox as MsgBox
    MsgBox.showerror("Error.", "An error occured in module NewLine: %s." %(error))
    


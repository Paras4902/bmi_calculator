from tkinter import *

root = Tk()
root.geometry("600x450")
root.title("BMI Calculator by Paras4902")
root.resizable(0, 0)

Label(root, text="BMI Calculator", font=("Times", 35, "bold underline")).pack()

ht_entry = Entry(root, font=("Times", 25), bd=10)
ht_entry. place(x=70, y=160, width=150)

wt_entry = Entry(root, font=("Times", 25), bd=10)
wt_entry. place(x=380, y=160, width=150)

bmi_entry = Entry(root, font=("Times", 25), bd=10)
bmi_entry. place(x=70, y=300, width=150)

ur_entry = Entry(root, font=("Times", 25), bd=10)
ur_entry. place(x=280, y=300, width=300)

Label(root, text="↓Height(in cms)↓", font=("Times", 25)).place(x=30, y=100)
Label(root, text="↓Weight(in kg)↓", font=("Times", 25)).place(x=340, y=100)
Label(root, text="↓BMI↓", font=("Times", 25)).place(x=90, y=250)
Label(root, text="↓You are↓", font=("Times", 25)).place(x=360, y=250)
Label(root, text="Program@Paras4902", font=("Times", 25, "italic underline")).place(x=290, y=400)


def getbmi():
    height = int(ht_entry.get())
    weight = int(wt_entry.get())
    bmi = weight / (height ** 2)
    if bmi < 16:
        k = "Severly Underweight"
    elif 16 < bmi < 18.5:
        k = "Underweight"
    elif 18.5 < bmi < 25:
        k = "Healthy"
    else:
        k = "Overweight"
    bmi_entry.delete(0, END)
    bmi_entry.insert(END, bmi)
    ur_entry.delete(0, END)
    ur_entry.insert(END, str(k))


root.bind("<Return>", lambda pressed_key: getbmi())
root.mainloop()

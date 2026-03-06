import tkinter as t
main = t.Tk()
main.geometry("100x100")
main.minsize(100, 100)
main.maxsize(100, 100)
bg_image = t.PhotoImage(file="img.png")
def start():
    main.destroy()
    import _2048
def reset():
    import mon
start_button = t.Button(main, text='start', command=start, width=120, height=70, image=bg_image, compound="center")
start_button.pack()
reset_button = t.Button(main, text='reset', command=reset, width=120, height=30, compound="center")
reset_button.pack()
main.mainloop()
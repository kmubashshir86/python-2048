import tkinter as t 

main=t.Tk()
def start():
    main.destroy()
    import _2048
start=t.Button(main,text='start',command=start)
start.pack()
main.mainloop()
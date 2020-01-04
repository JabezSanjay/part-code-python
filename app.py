import tkinter as tk


root = tk.Tk()
# changed by Jabez
# Adding widgets
root.option_add("*Button.Background", "black")
root.option_add("*Button.Foreground", "red")


root.title('The game')
# Set the geometry attribute to change the root windows size
root.geometry("1920x1200")  # Size of the window is 1920 x 1200
root.resizable(0, 0)  # Don't allow resizing in the x or y direction

back = tk.Frame(root, bg='black')

# Don't allow the widgets inside to determine the frame's width / height
back.pack_propagate(0)
# Expand the frame to fill the root window
back.pack(fill=tk.BOTH, expand=1)

# Adding variables and pack()

go = tk.Button(master=back, text='Start Game')
go.pack()
close = tk.Button(master=back, text='Quit', command=root.destroy)
close.pack()
option1 = tk.OptionMenu(back, *part1, width=50)
option1.pack()


root.mainloop()

from instruments import *
from tkinter import *

master = Tk()

n = 4

init = np.array([[1, 4], [2, 3]])
# n = int(input("N = "))
rez = init
for i in range(0, n):
    rez = hill(rez)
    pass


print_matrix(rez)
rez = t_flip(rez)
# ==REZ



# Working with the canvas
# can_w = master.winfo_screenheight() * 0.9
n_elem = 2 ** (n + 1)
can_h = 20*n_elem  # 512=2^9
can_w = can_h
w = Canvas(master, width=can_w, height=can_h)
w.pack()

for i in range(0, n_elem):
    for j in range(0, n_elem):
        if i % 2 == 0:
            if not(((rez[i][j] == 1) or (rez[i][j] == 4)) and ((rez[i+1][j] == 1) or (rez[i+1][j] == 4))):
                w.create_line(i*20+10, j*20+10, (i+1)*20+10, j*20+10, fill="#000")
        elif i < n_elem - 1:
            if ((i + 1) % 4 == 0) and ((rez[i][j] == 4) and (rez[i+1][j] == 1 or rez[i+1][j] == 4) or (rez[i][j] == 1 and rez[i+1][j] == 4)):
                pass
            elif ((rez[i][j] == 1) or (rez[i][j] == 4)) and ((rez[i+1][j] == 1) or (rez[i+1][j] == 4)):
                w.create_line(i * 20 + 10, j * 20 + 10, (i + 1) * 20 + 10, j * 20 + 10, fill="#000")
        if j % 2 == 0:
            if not(((rez[i][j] == 1) or (rez[i][j] == 4)) and ((rez[i][j+1] == 1) or (rez[i][j+1] == 4))):
                w.create_line(i * 20 + 10, j * 20 + 10, i * 20 + 10, (j + 1) * 20 + 10, fill="#000")
        elif j < n_elem - 1:
            if ((j + 1) % 4 == 0) and (rez[i][j] == 4) and (rez[i][j+1] == 1 or rez[i][j+1] == 4):
                pass
            elif ((rez[i][j] == 1) or (rez[i][j] == 4)) and ((rez[i][j+1] == 1) or (rez[i][j+1] == 4)):
                w.create_line(i * 20 + 10, j * 20 + 10, i * 20 + 10, (j + 1) * 20 + 10, fill="#000")


        #if j % 2 == 0:
        #    w.create_line(i * 20 + 10, j * 20 + 10, i * 20 + 10, (j + 1) * 20 + 10, fill="#000")
        w.create_text(i*20+15, j*20+15, fill="#000", font="Verdana 10", text=rez[i][j], anchor="center")


mainloop()

# print(can_w, ' ', can_h)

from instruments import *
from tkinter import *

master = Tk()

init = np.array([[1, 4], [2, 3]])
n = int(input("N = "))
rez = init
for i in range(0, n):
    rez = hill(rez)
    pass

# print_matrix(rez)
rez = t_flip(rez)


# Working with the canvas
n_elem = 2 ** (n + 1)
dim = 10
can_h = dim*n_elem  # 512=2^9
can_w = can_h
w = Canvas(master, width=can_w, height=can_h)
w.pack()

for i in range(0, n_elem):
    for j in range(0, n_elem):
        if i+1 < n_elem and abs(rez[i+1][j] - rez[i][j]) == 1:
            w.create_line(i * dim + int(dim/2), j * dim + int(dim/2), (i + 1) * dim + int(dim/2), j * dim + int(dim/2), fill="#000")
        if j+1 < n_elem and abs(rez[i][j+1] - rez[i][j]) == 1:
            w.create_line(i * dim + int(dim/2), j * dim + int(dim/2), i * dim + int(dim/2), (j + 1) * dim + int(dim/2), fill="#000")

mainloop()

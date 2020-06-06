from project_1 import *
import turtle as tr
tr.tracer(0)
tr.hideturtle()

molecule1 = (Molecule(100, 100, 5, 45, 'green'))
molecule1.show()
molecule2 = (Molecule(-100, -100, 5, 40, 'red'))
molecule3 = (Molecule(-150, 100, 7, 35, 'pink'))
molecule4 = (Molecule(100, -150, 7, 33, 'purple'))
molecule5 = (Molecule(100, -10, 4, 37, 'yellow'))
molecule2.show()
lst = [molecule1, molecule2, molecule3, molecule4, molecule5]
while True:
    for i in lst:
        i.move()
        i.random()
        i.show()
    tr.update()

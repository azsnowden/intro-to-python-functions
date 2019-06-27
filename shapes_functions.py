from shapes import triangle, square, pentagon, hexagon, star, circle

def shapesCall(userInput, color, size, fill):
    if userInput == 'triangle':
        triangle()
    if userInput == 'square':
        square()
    if userInput == 'pentagon':
        pentagon()
    if userInput == 'hexagon':
        hexagon()
    if userInput == 'star':
        star()
    if userInput == 'circle':
        circle()

y = input("Which shape would you like to create?")
x = input("which color would you like?")

shapesCall(y)
mainloop()
from tkinter import *
from PIL import ImageTk, Image
from time import sleep
from playsound import playsound
img = [0,0,0]
game = Tk()
game.title("Dragon")
canvas= Canvas(master=game, width=600, height=300, background="white")
canvas.pack()

img[0]=ImageTk.PhotoImage(Image.open("photos/dragon.jpg"))
img[1]=ImageTk.PhotoImage(Image.open("photos/cloud.jpg"))
img[2]=ImageTk.PhotoImage(Image.open("photos/tree.jpg"))

dragon = canvas.create_image(0,250,anchor=NW, image=img[0])
cloud = canvas.create_image(550,50,anchor=NW, image=img[1])
tree = canvas.create_image(550,250,anchor=NW, image=img[2])
canvas.update()

def moveCould():
    global cloud
    canvas.move(cloud, -5, 0)
    if canvas.coords(cloud)[0]<-20: # coords toạ dộ [0] là X [1] là Y
        canvas.delete(cloud)
        cloud = canvas.create_image(550,50,anchor=NW, image=img[1])
    canvas.update()

score = 0
text_core = canvas.create_text(550, 30, text = "SCORE: " + str(score), fill = "red", font=("Times",10))
def moveTree():
    global tree, score
    canvas.move(tree, -5, 0)
    if canvas.coords(tree)[0]<-20:   # coords toạ dộ [0] là X [1] là Y
        canvas.delete(tree)
        tree = canvas.create_image(550,250,anchor=NW, image=img[2])
        score= score + 1
        canvas.itemconfig(text_core, text="SCORE: "+ str(score)) # cập nhật lại điểm số
    canvas.update()
check_Jump = False
def jump():
    global check_Jump
    if check_Jump == False:
        playsound("tick.wav", block=False)
        check_Jump == True
        for i in range(0,30):
            canvas.move(dragon,0,-5)
            canvas.update()
            moveCould()
            moveTree()
            sleep(0.01)
        for i in range(0,30):
            canvas.move(dragon,0,5)
            canvas.update()
            moveCould()
            moveTree()
            sleep(0.01)

def keyPress(event):
    if event.keysym == "space":
        jump()
canvas.bind_all("<KeyPress>", keyPress)
gameover = False

def check_gameOver():
    global gameover
    if canvas.coords(tree)[0]<50 and canvas.coords(dragon)[1]>220:
        gameover = True
        text_gameover = canvas.create_text(250, 150, text = "GAME OVER", fill = "red", font=("Times",50))
        playsound("te.wav", block=False)


    game.after(100,check_gameOver)
check_gameOver()
while not gameover:
    moveCould()
    moveTree()
    sleep(0)
game.mainloop()

import turtle as t

wn=t.Screen()
wn.title("pong be")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#score
score_a=0
score_b=0


#paddle a

paddle_a=t.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b

paddle_b=t.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball

ball=t.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=1
ball.dy=1

#pen
pen=t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player a :0 player b:0",align="center",font=("Courier",24,"normal"))


#function

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)


#keyword binding
wn.listen()
wn.onkeypress(paddle_a_up,"q")
wn.onkeypress(paddle_a_down,"w")
wn.onkeypress(paddle_b_up,"e")
wn.onkeypress(paddle_b_down,"r")

#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking

    #top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1



    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #left and right
    if ball.xcor() > 350:
        score_a+=1
        pen.clear()
        pen.write("player a :{} player b:{}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
        ball.goto(0,0)
        ball.dx *=-1


    if ball.xcor() < -350:
        score_b+=1
        pen.clear()
        pen.write("player a :{} player b:{}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
        ball.goto(0,0)
        ball.dx*= -1

    #paddle and ball collisions
    if (ball.xcor()<-340 and ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
        ball.dx*=-1

    elif (ball.xcor()>340 and ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
        ball.dx*=-1
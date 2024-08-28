import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


right_paddle = Paddle(375, 0)
left_paddle = Paddle(-375, 0)
ball = Ball()
score = Score()
ball_speed = 0


screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "a")
screen.onkeypress(left_paddle.move_down, "z")
screen.listen()


game_is_on = True

while game_is_on:
    if ball.ycor() > 280 or ball.ycor() < -280:                 
        ball.y_bounce()                                         

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340) or (ball.distance(left_paddle) < 50 and ball.xcor() < -340):
        ball.x_bounce()                                         
        if ball.ball_speed >= 0.04:                             
            ball.ball_speed = ball.ball_speed - 0.01            

    if ball.xcor() > 380:                                       
        score.increment_lscore()                                
        ball.goto(0, 0)                                         
    if ball.xcor() < -380:                                      
        score.increment_rscore()                                
        ball.goto(0, 0)                                         

    if score.r_score or score.l_score >=20:
        game_is_on = False


    ball.ball_move()                                           
    score.show_score()                                          
    time.sleep(ball.ball_speed)                                 
    screen.update()
   


screen.exitonclick()                                           

from turtle import Turtle


class Ball(Turtle):                        
    def __init__(self):
        super().__init__()                  
        self.shape("circle")               
        self.color("yellow")                 
        self.penup()                        
        self.x_pos = 10                    
        self.y_pos = 10
        self.ball_speed = 0.1               

    def ball_move(self):                    
        x = self.xcor() + self.x_pos        
        y = self.ycor() + self.y_pos       
        self.goto(x, y)

    def y_bounce(self):                     
        self.y_pos *= -1   
      
    def x_bounce(self):                     
        self.x_pos *= -1                    

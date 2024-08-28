from turtle import Turtle


class Paddle(Turtle):                               
    def __init__(self, x_pos, y_pos):
        super().__init__()                          
        self.shape("square")                        
        self.shapesize(5, 1)                        
        self.color("red")                         
        self.teleport(x_pos, y_pos)                 
        self.penup()                                

    def move_up(self):                             
        if self.ycor() < 240:                      
            y = self.ycor() + 30                    
            self.goto(self.xcor(), y)

    def move_down(self):                            
        if self.ycor() > -230:                      
            y = self.ycor() - 30                    
            self.goto(self.xcor(), y)

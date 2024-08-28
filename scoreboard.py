from turtle import Turtle


class Score(Turtle):                                   
    def __init__(self):
        super().__init__()                             
        self.penup()                                  
        self.ht()                                     
        self.color("white")                           
        self.goto(0, 200)                      
        self.r_score = 0                              
        self.l_score = 0
        self.show_score()

    def increment_rscore(self):                        
        self.r_score += 1

    def increment_lscore(self):                        
        self.l_score += 1


    def show_score(self):                              

        self.clear()
        self.write(f"{"Target Score = 2"} \n {self.l_score} - {self.r_score}", align="center", font=("Courier", 30, "normal"))

        if self.l_score >= 20:
            self.clear()
            self.write(f" {self.l_score} - {self.r_score} \n {"Left Player Won"}", align="center", font=("Courier", 30, "normal"))

        elif self.r_score >= 20:
            self.clear()
            self.write(f" {self.l_score} - {self.r_score} \n {"Right Player Won"}", align="center", font=("Courier", 30, "normal"))


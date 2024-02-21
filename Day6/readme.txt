on day six most of the task on a website called reeborgs world where we have to write function
code for challege call hurdle 1 is-
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump_one():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for i in range(0,6):
    jump_one()


hurdle 2

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump_one():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while(at_goal() != True):
#or while not at_goal():
    jump_one()


hurdle 3


def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while(at_goal() != True):
    if (front_is_clear() == True):
        move()
    else:
        jump()



hurdle 4 my code



def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if (right_is_clear()!= True):
        if(front_is_clear() != True):
            turn_left()
            if front_is_clear():
                move()
        else:
            move()
    else:
        turn_right()
        if front_is_clear():
            move()

after understanding


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    
    while wall_on_right():
        move()
        
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
        
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
    
    
    
maze solver


def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        
    elif front_is_clear():
        move()
    else:
        turn_left()
    
       
    
    
    
    

    
  
    

    

    
  
    

    

    
    
    

    
  
    

    

"""
Drawing a piglet
"""
From turtle import  *


Def  nose ( x , y ):
    """ Draw the nose """
    Penup()
    # Move the turtle to the specified coordinates
    Goto(x,y)
    Pendown()
    # Set the direction of sea turtles (0- east, 90- North, 180 West, 270- South)
    Setheading( - 30 )
    Begin_fill()
    a =  0.4
    For i in  range ( 120 ):
        If  0  <= i <  30  or  60  <= i < 90 :
            a = a +  0.08
            #向左向3度
            Left( 3 )
            #走走
            Forward(a)
        Else :
            a = a -  0.08
            Left( 3 )
            Forward(a)
    End_fill()
    Penup()
    Setheading( 90 )
    Forward( 25 )
    Setheading( 0 )
    Forward( 10 )
    Pendown()
    # Set the brush color (red, green, blue)
    Pencolor( 255 , 155 , 192 )
    Setheading( 10 )
    Begin_fill()
    Circle( 5 )
    Color( 160 , 82 , 45 )
    End_fill()
    Penup()
    Setheading( 0 )
    Forward( 20 )
    Pendown()
    Pencolor( 255 , 155 , 192 )
    Setheading( 10 )
    Begin_fill()
    Circle( 5 )
    Color( 160 , 82 , 45 )
    End_fill()


Def  head ( x , y ):
    """画头"""
    Color(( 255 , 155 , 192 ), " pink " )
    Penup()
    Goto(x,y)
    Setheading( 0 )
    Pendown()
    Begin_fill()
    Setheading( 180 )
    Circle( 300 , - 30 )
    Circle( 100 , - 60 )
    Circle( 80 , - 100 )
    Circle( 150 , - 20 )
    Circle( 60 , - 95 )
    Setheading( 161 )
    Circle( - 300 , 15 )
    Penup()
    Goto( - 100 , 100 )
    Pendown()
    Setheading( - 30 )
    a =  0.4
    For i in  range ( 60 ):
        If  0 <= i <  30  or  60  <= i <  90 :
            a = a +  0.08
            Lt( 3 ) # 3 degrees to the left
            Fd(a) #step forward a step
        Else :
            a = a -  0.08
            Lt( 3 )
            Fd(a)
    End_fill()


Def  ears ( x , y ):
    """ Draw an ear """
    Color(( 255 , 155 , 192 ), " pink " )
    Penup()
    Goto(x, y)
    Pendown()
    Begin_fill()
    Setheading( 100 )
    Circle( - 50 , 50 )
    Circle( - 10 , 120 )
    Circle( - 50 , 54 )
    End_fill()
    Penup()
    Setheading( 90 )
    Forward( - 12 )
    Setheading( 0 )
    Forward( 30 )
    Pendown()
    Begin_fill()
    Setheading( 100 )
    Circle( - 50 , 50 )
    Circle( - 10 , 120 )
    Circle( - 50 , 56 )
    End_fill()


Def  eyes ( x , y ):
    """ Draw an eye """
    Color(( 255 , 155 , 192 ), " white " )
    Penup()
    Setheading( 90 )
    Forward( - 20 )
    Setheading( 0 )
    Forward( - 95 )
    Pendown()
    Begin_fill()
    Circle( 15 )
    End_fill()
    Color( " black " )
    Penup()
    Setheading( 90 )
    Forward( 12 )
    Setheading( 0 )
    Forward( - 3 )
    Pendown()
    Begin_fill()
    Circle( 3 )
    End_fill()
    Color(( 255 , 155 , 192 ), " white " )
    Penup()
    Seth( 90 )
    Forward( - 25 )
    Seth( 0 )
    Forward( 40 )
    Pendown()
    Begin_fill()
    Circle( 15 )
    End_fill()
    Color( " black " )
    Penup()
    Setheading( 90 )
    Forward( 12 )
    Setheading( 0 )
    Forward( - 3 )
    Pendown()
    Begin_fill()
    Circle( 3 )
    End_fill()


Def  cheek ( x , y ):
    """ painting cheeks """
    Color(( 255 , 155 , 192 ))
    Penup()
    Goto(x,y)
    Pendown()
    Setheading( 0 )
    Begin_fill()
    Circle( 30 )
    End_fill()


Def  mouth ( x , y ):
    """画嘴巴"""
    Color( 239 , 69 , 19 )
    Penup()
    Goto(x, y)
    Pendown()
    Setheading( - 80 )
    Circle( 30 , 40 )
    Circle( 40 , 80 )


Def  setting ():
    """ Set parameter """
    Pensize( 4 )
    #躲海龟
    Hideturtle()
    Colormode( 255 )
    Color(( 255 , 155 , 192 ), " pink " )
    Setup( 840 , 500 )
    Speed( 10 )


Def  main ():
    """ main function """
    Setting() 
    Nose( - 100 , 100 )
    Head( - 69 , 167 )
    Ears( 0 , 160 )
    Eyes( 0 , 140 )
    Cheek( 80 , 10 )
    Mouth ( - 20 , 30 )
    Done()


If  __name__  ==  ' __main__ ' :
    Main()


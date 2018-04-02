import turtle
from random import randint

#(x,y)위치에 반지름 radius로 원을 그리는 함수
def draw_circle(turtle, color, x, y, radius):
	turtle.penup()		#펜을 올린다
	turtle.fillcolor(color)	#채우기 색상을 설정
	turtle.goto(x,y)	
	turtle.pendown()
	turtle.begin_fill()		#채우기 시작
	turtle.circle(radius)	#반지름radius로 원 그림
	turtle.end_fill()		#채우기 종료

#(x,y) 위치에 width와 height 크기의 사각형 그리는 함수
def draw_rectangle(turtle, color, x, y, width, height):
	turtle.penup()
	turtle.fillcolor(color)
	turtle.goto(x,y)
	turtle.pendown()
	turtle.begin_fill()
	for i in range(2):
		turtle.forward(width)
		turtle.left(90)
		turtle.forward(height)
		turtle.left(90)
	turtle.end_fill()


#(x,y)위치에 width와 height크기의 마름모꼴을 그리는 함수 
def draw_trepezoid(turtle, color, x, y, width, height):
	turtle.penup()
	turtle.fillcolor(color)
	turtle.goto(x,y)
	turtle.pendown()
	turtle.begin_fill()
	turtle.forward(width)
	turtle.right(60)
	turtle.forward(height)
	turtle.right(120)
	turtle.forward(width+20)
	turtle.right(120)
	turtle.forward(height)
	turtle.right(60)
	turtle.end_fill()

#(x,y)위치에 별모양을 그리는 함수
def draw_star(turtle, color, x, y, size):
	print(color)
	turtle.penup()
	turtle.fillcolor(color)
	turtle.goto(x,y)
	turtle.pendown()
	turtle.begin_fill()
	for i in range(10):
		turtle.forward(size)
		turtle.right(144)
	turtle.end_fill()
 
t=turtle.Turtle()
t.shape("turtle")
t.speed(0)
	
x=0	#현재 그림이 그려지는위치
y=0	#현재 그림이 그려지는위치
width=240	#마름모꼴의 최초 크기

#트리의 줄기
draw_rectangle(t,"brown", x-20, y-50, 30, 50)

#트리의 잎
height=20
for i in range(10):
	width=width-20	#마름모꼴의 폭이 줄어든다
	x=0-width/2		#x좌표는 마름모꼴의 중앙으로
	draw_trepezoid(t, "green", x, y, width, height)	#마름모골 그림
	#랜덤한 위치에 원을 그림
	draw_circle(t, "red", x+randint(0,width), y+randint(0,height), 10)
	y=y+height	#y값을 마름모꼴의 높이만큼 증가

#별 모양의 트리의 꼭대기에 그림
draw_star(t, "yellow", 4, y, 100)
t.penup()
t.color("red")
t.goto(-200,250)
t.write("Merry Christmas",font=("Arial",24,"italic"))
t.goto(-200,220)
t.write("Happy New Year!",font=("Arial",24,"italic"))


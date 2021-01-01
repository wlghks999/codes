from tkinter import *
import time
tk=Tk()
width=1280
height=720
font_size=12
color='blue'
class graph:
    def __init__(self,color):
        
        self.canvas = Canvas(tk,width=width,height=height,bd=0,highlightthickness=0) 
        self.canvas.pack()
        self.color=color
        
    
    
    def draw(self, dim,a,b, c,isequation=False):
        
        
        #가로축
        for i in range(0,int(width/2)):
            if i%40==0 and not i==0:
                self.canvas.create_text(i+width/2+5,height/2+10,fill="darkblue",font=("arial",font_size),text="{}".format(int(i/40)))
                self.canvas.create_rectangle(width/2-1+i,height/2-3.5,width/2+1+i,height/2+3.5,fill='darkblue')
            self.id=self.canvas.create_circle(i+width/2,height/2,1,fill='black')
            
                
                
        for i in range(0,int(width/2)):
            if i%40==0 and not i==0:
                self.canvas.create_text(-i+width/2+5,height/2+10,fill="darkblue",font=("arial",font_size),text="{}".format(int(i/40)))
                self.canvas.create_rectangle(width/2-1-i,height/2-3.5,width/2+1-i,height/2+3.5,fill='darkblue')
            self.id=self.canvas.create_circle(-i+width/2,height/2,1,fill='black')
            
            
            
            
        #세로축
        for i in range(0,int(height/2)):
            if i%40==0 and not i==0:
                self.canvas.create_text(width/2+10,height/2-i+5,fill="darkblue",font=("arial",font_size),text="{}".format(int(i/40)))
                self.canvas.create_rectangle(width/2-3.5,height/2-i+1,width/2+3.5,height/2-i+1,fill='darkblue')
            self.id=self.canvas.create_circle(width/2,-i+height/2,1,fill='black')
            
                
                
        for i in range(0,int(height/2)):
            if i%40==0 and not i==0:
                self.canvas.create_text(width/2+10,height/2+i+5,fill="darkblue",font=("arial",font_size),text="{}".format(int(i/40)))
                self.canvas.create_rectangle(width/2-3.5,height/2+i+1,width/2+3.5,height/2+i+1,fill='darkblue')
            self.id=self.canvas.create_circle(width/2,i+height/2,1,fill='black')
            
            
        #방정식이라면 해 구하기
        if(isequation==True):
            linear_solution=self.solution(dim=1,a=a,b=b,c=c)
            print(linear_solution)
            
            
            
            
            
        #그래프 표시
        for i in range(0,int(width/2)):
            self.id=self.canvas.create_circle(width/2,height/2-40*b,2,fill=color)
            self.canvas.move(self.id,i, -(a*i+b))
            
                
                
        for i in range(0,int(width/2)):
            self.id=self.canvas.create_circle(width/2,height/2-40*b,2,fill=color)
            self.canvas.move(self.id,-i, (a*i+b))
            
            
            
            
            
    #방정식 해 구하기
    def solution(self, dim,a=0,b=0,c=0,d=0,e=0):
        if(dim==0):
            print("Not a Graph!")
        if(dim==1):
            if(a==0):
                print("Not a linear Graph!")
            else:
                c-=b
                return c/a
            
            
            
            
    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    Canvas.create_circle = _create_circle


tk.title("Graph")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)

graph=graph(color=color)
graph.draw(dim=1,a=4,b=1,c=0,isequation=True)
quit_button=Button(tk, text="종료", command=tk.destroy).pack()
tk.mainloop()


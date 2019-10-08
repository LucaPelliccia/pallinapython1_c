x=10
y=20
a=80
b=25
verx=1
very=1
alta=20
larga=20
recx=(600/2)-40
recy=400-25
xcer=x
ycer=(y+(larga/2))

def setup():
            size(600,400)

def draw():
    global x,y,verx,very,larga,alta,a,b,recx,recy
    background(255,255,0)
    x= x+2*(verx)
    y= y+2*(very)
    rect(recx,recy,a,b)
    ellipse(x,y,alta,larga)
    if x < 0:
        verx =1
        fill(random(255),random(255),random(255))

    if y < 0:
        very =1
        fill(random(255),random(255),random(255))
  
    if x > width:
        verx =-1
        fill(random(255),random(255),random(255))

    if y > height:
        very =-1
        fill(random(255),random(255),random(255))
    
    if xcer>=recx and xcer<=(recx+a) and ycer>=recy:
        very=-1
    
        
def keyPressed():
    global recx,recy
    if keyCode==RIGHT and recx<(width-a):
        recx+=15
    
    if keyCode==LEFT and recx>0:
        recx-=15
    
   
    
    
    

        
  
    

#by mubashshir
import tkinter as t
import random
import pickle
try:
  with open("money.bin",'rb') as f:
      money=pickle.load(f)
except FileNotFoundError:
       pass
def monadd(x):
  global money  
  money+=x
  with open("money.bin",'wb') as f:
    money=pickle.dump(money,f)
  with open("money.bin",'rb') as f:
      money=pickle.load(f)
try:
  f=open("score.txt","r")
  f.seek(0)
  hiscore=f.read()
  f.close()
except:
  hiscore=0
root=t.Tk()
root.title("2048 by mubahshsir")
dict=dict()
temp_list=[2,]
import random
state_show=t.Button(root,bg="RED")
state_show.grid(row=0,column=5)
def random_hex_color():
  return f"#{random.randrange(0x1000000):06x}"

color = random_hex_color()



state=0
score=0
power=4
lab=t.Label(root,text="hi: "+str(hiscore))
lab.grid(row=0,column=4)
lab2=t.Label(root,text="score : "+str(score))
lab2.grid(row=0,column=3)
lab3=t.Label(root,text="money : "+str(money))
lab3.grid(row=0,column=1)
up=10
down=100
pow2=100
color_dict={}
for i in range(1,pow2+1):
         tempvar=random_hex_color()
         if tempvar not in color_dict.values():
                  color_dict[2**i]=tempvar

def temp__list():
         global power,temp_list,up,down,pow2
         if score in range(up,down):
                  temp_list+=[2**power,]
                  power+=1
                  up=10*up
                  down=10*down
                  tempvar=random_hex_color()
                  if tempvar not in color_dict.values():
                           color_dict[2**(pow2)]=tempvar
                           pow2+=1
def gen(a,b):
         tmp1=[int(a)-1,a,int(a)+1]
         tmp2=[int(b)-1,b,int(b)+1]
         lis=list()
         for i in tmp1:
                  for j in tmp2:
                           lis+=['a'+str(i)+str(j),]
         return lis
                           
#solve not close clicked problem
def clicked(a,b):
         global state,click1,click2,score
         if state:
                  click2=f'a{a}{b}'
                  col=color_dict[dict[click1]]
                  exec(click1+f".config(bg=f'{col}')")
                  state_show.config(bg="red",text="")
                  
                  if (dict[click2]==dict[click1] and click2!=click1):
                           if click1 in gen(click2[1],click2[2]):
                                    monadd(int(dict[click2]/2))
                                    lab3.config(text="money : "+str(money))
                                    temp=random.choice(temp_list)
                                    a=dict[click2]=dict[click1]*2
                                    dict[click1]=temp
                                    exec(click1+f".config(text=f'{temp}',bg=color_dict[temp])")
                                    exec(click2+f".config(text=f'{a}',bg=color_dict[a])")
                                    score+=a
                                    lab2.config(text="score : "+str(score))
                                    temp__list()
                                    if(int(hiscore)<score):
                                      lab.config(text="hi :"+str(score))
                                      f=open("score.txt","w")
                                      f.write(str(score))
                                      f.close()
                           
                           
         else:
                  
                  click1=f'a{a}{b}'
                  exec(click1+".config(bg='white')")
                  state_show.config(bg="green",text=dict[click1])
         state^=1
for i in range(1,6):
         for j in range(1,6):
                  exec("temp=random.choice([2,4,8])")
                  exec(f"dict[f'a{i}{j}']=temp")
                  exec(f"a{i}{j}=t.Button(root,width=10,height=5,text=temp,bg=color_dict[temp],command=lambda : clicked({i},{j}))")
                  exec(f"a{i}{j}.grid(row={i},column={j})")
root.mainloop()

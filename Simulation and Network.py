import pygame,sys,random
import numpy as np

pygame.init()
font=pygame.font.SysFont('arial',30)
width=800
height=600
vision=300
class nn:
    def __init__(self,ip_n,op_n):
        self.ip=ip_n
        self.op=op_n
        self.l1_size=200
        self.w1=np.random.rand(self.l1_size,self.ip+1).T*0.3-0.15
        self.w2=np.random.rand(self.op,self.l1_size+1).T*0.3-0.15
        
    def sig(self,x):
        return 1/(1+np.exp(-x))
        
    def predict(self,ip):
        ip=vision-ip
        ip=np.append(1,ip)
        l1=self.sig(ip@self.w1)
        l1=np.append(1,l1)
        pred=self.sig(l1@self.w2)
        return np.argmax(pred)
        
class prey(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,10))
        self.rect=self.image.get_rect(center=pos)
        pygame.draw.circle(self.image, "green", (5,5),5)
        self.direction=1
        self.speed=8
        self.state=np.full((36),vision)
        self.net=nn(36,9)
        self.start_time=pygame.time.get_ticks()
        self.fitness=0
            
    def update(self):
        self.direction=self.net.predict(self.state)
        if self.direction==1:
            self.rect.y-=self.speed
        elif self.direction==2:
            self.rect.y-=self.speed/(2**0.5)
            self.rect.x+=self.speed/(2**0.5)
        elif self.direction==3:
            self.rect.x+=self.speed
        elif self.direction==4:
            self.rect.y+=self.speed/(2**0.5)
            self.rect.x+=self.speed/(2**0.5)
        elif self.direction==5:
            self.rect.y+=self.speed
        elif self.direction==6:
            self.rect.y+=self.speed/(2**0.5)
            self.rect.x-=self.speed/(2**0.5)
        elif self.direction==7:
            self.rect.x-=self.speed
        elif self.direction==8:
            self.rect.y-=self.speed/(2**0.5)
            self.rect.x-=self.speed/(2**0.5)
            
        if self.rect.x<0:
            self.rect.x=width
        elif self.rect.x>width:
            self.rect.x=0
        if self.rect.y<0:
            self.rect.y=height
        elif self.rect.y>height:
            self.rect.y=0
            
class predator(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,10))
        self.rect=self.image.get_rect(center=pos)
        pygame.draw.circle(self.image, "red", (5,5),5)
        self.direction=2
        self.speed=8
        self.state=np.full((36),vision)
        self.net=nn(36,9)
        self.start_time=pygame.time.get_ticks()
        self.fitness=0
            
    def update(self):
        self.direction=self.net.predict(self.state)
        if self.direction==1:
            self.rect.y-=self.speed
        elif self.direction==2:
            self.rect.y-=self.speed/(2**0.5)
            self.rect.x+=self.speed/(2**0.5)
        elif self.direction==3:
            self.rect.x+=self.speed
        elif self.direction==4:
            self.rect.y+=self.speed/(2**0.5)
            self.rect.x+=self.speed/(2**0.5)
        elif self.direction==5:
            self.rect.y+=self.speed
        elif self.direction==6:
            self.rect.y+=self.speed/(2**0.5)
            self.rect.x-=self.speed/(2**0.5)
        elif self.direction==7:
            self.rect.x-=self.speed
        elif self.direction==8:
            self.rect.y-=self.speed/(2**0.5)
            self.rect.x-=self.speed/(2**0.5)
            
        if self.rect.x<0:
            self.rect.x=width
        elif self.rect.x>width:
            self.rect.x=0
        if self.rect.y<0:
            self.rect.y=height
        elif self.rect.y>height:
            self.rect.y=0

class game:

    
    def __init__(self):
        self.screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('The Evolution')
        self.clock=pygame.time.Clock()
        self.fps=30
        self.setup()
    
    def setup(self):
        self.prey_alive=pygame.sprite.Group()
        self.pred_alive=pygame.sprite.Group()
        self.best_preys=pygame.sprite.Group()
        self.best_preds=pygame.sprite.Group()
        self.all_prey=[]
        self.all_pred=[]
        self.itr=0
        self.top_prey=[]
        self.top_pred=[]
        self.past_pred=[]
        self.past_prey=[]
        
        for i in range(5):
            prey1=prey((random.randint(1,width),random.randint(1,height)))
            self.prey_alive.add(prey1)
            self.all_prey.append(prey1)
        for i in range(5):
            predator1=predator((random.randint(1,width),random.randint(1,height)))
            self.pred_alive.add(predator1)
            self.all_pred.append(predator1)
        
    def prey_split(self):
        current=pygame.time.get_ticks()
        for i in self.prey_alive:
            if (current-i.start_time)%(240000//self.fps)<self.fps:
                self.prey_birth(i)
                
    def opp_collision(self):
        t=pygame.time.get_ticks()
        for i in self.pred_alive:
            for j in self.prey_alive:
                if i.rect.colliderect(j.rect):
                    self.prey_alive.remove(j)
                    i.fitness+=1
                    if(t-i.start_time<=(60000/self.fps)):
                        self.pred_birth(i)
                    i.start_time=t
                    j.fitness=(t-j.start_time)/100
            if(t-i.start_time>=(240000/self.fps)):
                self.pred_alive.remove(i)
                
    def prey_birth(self,parent):
        x=prey((parent.rect.centerx+10,parent.rect.centery+10))
        x.net=parent.net
        self.prey_alive.add(x)
        self.all_prey.append(x)
        
    def pred_birth(self,parent):
        x=predator((parent.rect.centerx+10,parent.rect.centery+10))
        x.net=parent.net
        self.pred_alive.add(x)
        self.all_pred.append(x)
        
    def same_collision(self,grp):
        dist=3
        for i in grp:
            for j in grp:
                if (i!=j):
                    d=((i.rect.centerx-j.rect.x)**2)+((i.rect.centery-j.rect.y)**2)
                    if d<=10**2:
                        if(i.rect.y>j.rect.y):
                            i.rect.centery-=dist
                            j.rect.centery+=dist
                        else:
                            i.rect.centery+=dist
                            j.rect.centery-=dist
                        if(i.rect.x>j.rect.x):
                            i.rect.centerx+=dist
                            j.rect.centerx-=dist
                        else:
                            i.rect.centerx-=dist
                            j.rect.centerx+=dist
                
    def update_state(self):
        for i in self.prey_alive:
            i.state=np.full((36),vision)
        for i in self.pred_alive:
            i.state=np.full((36),vision)
        for i in self.prey_alive:
            for j in self.pred_alive:
                x=i.rect.centerx
                y=i.rect.centery
                d=((x-j.rect.x)**2)+((y-j.rect.y)**2)
                if d<=vision**2:
                    if(x==j.rect.x):
                        if(j.rect.y<y):angle=90
                        else: angle=-90
                    else:
                        angle=np.arctan((j.rect.y-y)/(x-j.rect.x))*180/np.pi
                    ind=int(((angle+360)%360)//10)
                    ind2=int(((angle+360+180)%360)//10)
                    i.state[ind]=d**0.5
                    j.state[ind2]=d**0.5
                    
    def play(self):
        self.prey_split()
        self.update_state()
        self.prey_alive.update()
        self.pred_alive.update()
        self.opp_collision()
        self.same_collision(self.prey_alive)
        self.same_collision(self.pred_alive)
        #self.plot()
        
    def next_gen(self):
        if self.itr>=10:
            print("______________Top itr________________")
            self.all_pred = self.top_pred
            self.all_prey = self.top_prey
            self.top_pred=[] 
            self.top_prey=[]
            self.itr=0
        else:
            self.itr+=1
            self.all_prey=sorted(self.all_prey,key=lambda x : x.fitness,reverse=True)
            self.all_pred=sorted(self.all_pred,key=lambda x : x.fitness,reverse=True)
            self.best_preys.add(self.all_prey[0])
            self.best_preds.add(self.all_pred[0])
            
            self.top_pred.append(self.all_pred[0])
            self.top_prey.append(self.all_prey[0])
        
            prey_fit=np.array([x.fitness for x in self.all_prey],dtype='float')
            pred_fit=np.array([x.fitness for x in self.all_pred],dtype='float')
            if prey_fit.sum()==0 or pred_fit.sum()==0:
                print("NO fitness!!")
                self.prey_alive.empty()
                self.pred_alive.empty()
                a = []
                for i in range(4):
                    p1=self.all_prey[i]
                    prey1 = prey((random.randint(1, width), random.randint(1, height)))
                    
                for z in range(random.randint(0,len(p1.net.w1))):
                    p1.net.w1[z]*=(1/(100*random.randint(1,9)))
                prey1.net.w1 = p1.net.w1
                
                for z in range(random.randint(0, len(p1.net.w1))):
                    p1.net.w2[z] *= (1 / (10 * random.randint(1, 9)))
                prey1.net.w2 = p1.net.w2

                w = prey1.net.w1.flatten()
                prey1.net.w1 = w.reshape(prey1.net.w1.shape)

                w = prey1.net.w2.flatten()
                prey1.net.w2 = w.reshape(prey1.net.w2.shape)

                self.prey_alive.add(prey1)
                a.append(prey1)

                for i in range(1):
                    self.all_prey[i].fitness = 0
                    a.append(self.all_prey[i])

                self.all_prey = a
                b = []
                for i in range(4):
                    p1 = self.all_pred[i]
                    pred1 = predator((random.randint(1, width), random.randint(1, height)))

                    for z in range(random.randint(0, len(p1.net.w1))):
                        p1.net.w1[z] *= (1 / (100 * random.randint(1, 9)))
                    pred1.net.w1 = p1.net.w1
                    for z in range(random.randint(0, len(p1.net.w1))):
                        p1.net.w2[z] *= (1 / (100 * random.randint(1, 9)))
                    pred1.net.w2 = p1.net.w2

                    w = pred1.net.w1.flatten()
                    pred1.net.w1 = w.reshape(pred1.net.w1.shape)

                    w = pred1.net.w2.flatten()
                    pred1.net.w2 = w.reshape(pred1.net.w2.shape)

                    self.pred_alive.add(pred1)
                    b.append(pred1)

                for i in range(1):
                    self.all_prey[i].fitness = 0
                    b.append(self.all_prey[i])

                self.all_pred = b        
            else:
                self.past_pred.append(np.average(pred_fit))
                self.past_prey.append(np.average(prey_fit))
                print("AVERAGE prey fitness:",np.average(prey_fit),"\nAVERAGE pred fitness:",np.average(pred_fit))
                prey_fit/=prey_fit.sum()
                pred_fit/=pred_fit.sum()
                self.prey_alive.empty()
                self.pred_alive.empty()
                a=[]
                p1 = self.all_prey[0]
                prey1=prey((random.randint(1,width),random.randint(1,height)))
                prey1.net.w1=p1.net.w1.copy()
                prey1.net.w2=p1.net.w2.copy()
                
                w=prey1.net.w1.flatten()
                j=self.rand_index(len(w))
                w[j]=np.array([(np.random.random() - 0.5)+i for i in w[j]]) #mutate
                prey1.net.w1=w.reshape(prey1.net.w1.shape)
                
                w=prey1.net.w2.flatten()
                j=self.rand_index(len(w))
                w[j]=np.array([(np.random.random() - 0.5)+i for i in w[j]]) #mutate
                prey1.net.w2=w.reshape(prey1.net.w2.shape)
                
                self.prey_alive.add(prey1)
                a.append(prey1)
                
                for i in range(9):
                    p1=np.random.choice(self.all_prey,p=prey_fit)
                    prey1=prey((random.randint(1,width),random.randint(1,height)))
                    prey1.net.w1=p1.net.w1.copy()
                    prey1.net.w2=p1.net.w2.copy()
                    
                    w=prey1.net.w1.flatten()
                    j=self.rand_index(len(w))
                    w[j]=np.array([(np.random.random() - 0.5)+i for i in w[j]]) #mutate
                    prey1.net.w1=w.reshape(prey1.net.w1.shape)
                    
                    w=prey1.net.w2.flatten()
                    j=self.rand_index(len(w))
                    w[j]=np.array([(np.random.random() - 0.5)+i for i in w[j]]) #mutate
                    prey1.net.w2=w.reshape(prey1.net.w2.shape)
                    
                    self.prey_alive.add(prey1)
                    a.append(prey1)
                    
                self.all_prey=a
                
                p1=self.all_pred[0]
                pred1=predator((random.randint(1,width),random.randint(1,height)))
                pred1.net.w1=p1.net.w1.copy()
                pred1.net.w2=p1.net.w2.copy()
                
                w=pred1.net.w1.flatten()
                j=self.rand_index(len(w))
                w[j]=np.array([(np.random.random() - 0.5)+i for i in w[j]]) #mutate
                pred1.net.w1=w.reshape(pred1.net.w1.shape)
                
                w=pred1.net.w2.flatten()
                j=self.rand_index(len(w))
                w[j]=np.array([(np.random.random() - 0.5)+i for i in w[j]])
                pred1.net.w2=w.reshape(pred1.net.w2.shape)
                
                self.pred_alive.add(pred1)
                b=[]
                b.append(pred1)
                
                
                for i in range(9):
                    p1=np.random.choice(self.all_pred,p=pred_fit)
                    pred1=predator((random.randint(1,width),random.randint(1,height)))
                    pred1.net.w1=p1.net.w1.copy()
                    pred1.net.w2=p1.net.w2.copy()
                    
                    w=pred1.net.w1.flatten()
                    j=self.rand_index(len(w))
                    w[j]=np.array([(np.random.random() - 0.5)+i for i in w[j]]) #mutate
                    pred1.net.w1=w.reshape(pred1.net.w1.shape)
                    
                    w=pred1.net.w2.flatten()
                    j=self.rand_index(len(w))
                    w[j]=np.array([(np.random.random() - 0.5)+i for i in w[j]])
                    pred1.net.w2=w.reshape(pred1.net.w2.shape)
                    
                    self.pred_alive.add(pred1)
                    b.append(pred1)
                    
                self.all_pred=b            
        
        
    def rand_index(self,size):
        ind=np.arange(size)
        np.random.shuffle(ind)
        return ind[:np.random.randint(size)]
        
    def run(self):
        while(1):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.play()
            self.screen.fill('black')
            self.prey_alive.draw(self.screen)
            self.pred_alive.draw(self.screen)
            if (not self.prey_alive) or (not self.pred_alive):
                print("====****====GENERATION OVER====****===="+str(self.itr))
                if (not self.prey_alive):
                    print("Prey lost")
                else:
                    print("predator lost")
                self.next_gen()
                
            pygame.display.update()
            self.clock.tick(self.fps)
    
main=game()
main.run()
from random import*
class cat:
      def __init__(self, name):
        self.name = name
        self.satiety = 50 #сытость
        self.claws = 100
        self.hostsAnger = 0
        self.boredom = 0
        self.toilet = 0 
        self.sleep = 0
        self.alive = True
        
        
      def satietyy(self):
          print('время поесть')
          self.satiety += 10
          self.toilet += 5
          self.boredom += 10
          self.sleep += 10
    
      
      def clawss(self):
        print('надо подточить ногти об новый диван')
        self.satiety -= 5
        self.claws += 10
        self.boredom -= 30
        self.hostsAnger += 20
        self.sleep += 20
        
        
      def hostsAngerr(self):
        print('Держись, хозяин. мне скучно')
        self.boredom -= 20
        self.hostsAnger += 20
        self.sleep += 20
        
      def sleepp(self):
        print('фууух, пора поспать! скручусь милым комочком')
        self.sleep -= 40
        self.hostsAnger -= 60
        self.satiety -=10
        self.boredom += 30
    
      def toilett(self):
        print('какое облегчение, и тапки у хозяина такие удобные')
        self.toilet -= 10
        self.boredom += 20
        self.sleep += 10
        self.hostsAnger +=20
    
      
        
      def is_alive(self):
       if self.satiety > 120:
          print ('я лопнул')
          self.alive = False
       elif self.hostsAnger >= 150:
          print('ой... меня идут убивать')
          self.alive = False
       elif self.boredom >= 150:
          print('интересно, а сетки у нас на окнах крепкие?')
          self.alive = False
      def end(self):
          print('сытость:', self.satiety)
          print('ногти:', self.claws)
          print('злость хозяина:', self.hostsAnger )
          print('скука:', self.boredom)
          print('туалет:', self.toilet)
          print('сон:', self.sleep )
          if self.alive == True :
            print('живой')
          elif self.alive == False :
            print('упс')
      def live(self, day):
        print('День:',day)
        live_cube = randint(1,5)
        if self.satiety > 0:
          print('сытость:', self.satiety)
          print('ногти:', self.claws)
          print('злость хозяина:', self.hostsAnger )
          print('скука:', self.boredom)
          print('туалет:', self.toilet)
          print('сон:', self.sleep )
          if self.alive == True :
            print('живой')
          elif self.alive == False :
            print('упс')
         
        
        
          if live_cube == 1:
              self.satietyy()
              
          elif live_cube == 2:
              self.sleepp ()
             
          elif live_cube == 3:
              self.clawss()
             
          elif live_cube == 4:
              self.hostsAngerr() 
          elif live_cube == 5:
              self.toilett()

        if self.satiety <= 0:
          print('голодный как собака')
          self.satiety += 30          
        if self.toilet <= 0:
            print('ХОЗЯИН, БЫСТРЕЕ! ТУТ ОЧЕРЕДЬ!')
            self.toilet += 20
            print('сытость:', self.satiety)
            print('ногти:', self.claws)
            print('злость хозяина:', self.hostsAnger )
            print('скука:', self.boredom)
            print('туалет:', self.toilet)
            print('сон:', self.sleep )
            if self.alive == True :
              print('живой')
            elif self.alive == False :
              print('упс')
          
          
          
            
          


 
    

    
      
obj = cat('barsik')

for day in range(17):
  
	if obj.alive == False:
    
		break
    
	obj.live(day)
 


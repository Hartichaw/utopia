import kivy
import random
from functools import partial
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color

import time

NAMES =["jean", "hubert", "louis"]
SEX = ["male", "female", "apache helicopter"]
RACES = ["human", "orc", "elf"]

class TestWidget(Widget):
    def on_touch_down(self, touch):
        if True:
            self.background_color = (0.0, 1.0, 0.0, 1.0)
            return True
        else:
            return super(MyWidget, self).on_touch_down(touch)
        

class BuildArea(GridLayout):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        for i in range(12):
            self.add_widget(TestWidget())

#===========		
class settler():
	def __init__(self, name = "jean",
									sex = "male",
									race = "human",
									happyness = 100):
		self._name = name
		self._sex = sex
		self._race = race
		self._happyness = happyness
		
	def randomize_infos(self):
	       self._name = NAMES[random.randint(0, 2)]
	       self._sex = SEX[random.randint(0, 2)]
	       self._race = RACES[random.randint(0, 2)]
        
	def __repr__(self):
		return self._name + ": \n" +\
												"sex: " + self._sex + "\n" +\
												"race: " + self._race + "\n" +\
												"happyness: " + str(self._happyness) + "\n"
												
class colonScreen(GridLayout):
 	   def __init__(self, colony, **kwargs):
 	   	super(colonScreen, self).__init__(**kwargs)

 	   	for i in range(0, len(colony)-1):
 	   		self.add_widget(Label(text=repr(colony[i])))	   			 
 	   		
class Room(Button):
    def __init__(self, **kwargs):
        super(Room, self).__init__(**kwargs)
        self.locked = False
        self.background_color = (0.0, 1.0, 0.0, 1.0)
    def on_press(self):
        if not self.locked:
            self.lock_room()
            Clock.schedule_once(lambda dt:self.unlock_room(),  3)
            
    def lock_room(self):
          self.locked = True
          self.background_color = (1.0, 0.0, 0.0, 1.0)
      
    def unlock_room(self):
          self.locked = False
          self.background_color = (0.0, 1.0, 0.0, 1.0) 	   			
 	   					
class Cafeteria(Room):
    def __init__(self, **kwargs):
        super(Cafeteria, self).__init__(**kwargs)
class Well(Room):
    def __init__(self, **kwargs):
        super(Well, self).__init__(**kwargs)
class Generator(Room):
    def __init__(self, **kwargs):
        super(Generator, self).__init__(**kwargs)
                      		
class deprecated_Room(Button):
        def __init__(self, **kwargs):
            super().__init__( **kwargs)
            self.count = 0
        
        def add_count(self):
             self.count += 1
             self.text= str(self.count)
        		   		
class GameArea(GridLayout):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        for i in range(0, 4):
            self.add_widget(Cafeteria())
            self.add_widget(Well())
            self.add_widget(Generator())
            
class BuildArea(GridLayout):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)        
        
class TopBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        self.food_count = 0
        self.water_count = 0
        self.magic_count = 0
        
        Clock.schedule_interval(lambda dt:self.add_food(-1),  2)
        Clock.schedule_interval(lambda dt:self.add_water(-1), 2)
        
        
    def add_food(self, food_amount):
        self.food_count += food_amount
        self.food_lbl.text = "Food = " + str(self.food_count)
        
    def add_water(self,  water_amount):
        self.water_count += water_amount
        self.water_lbl.text = "Water = " + str(self.water_count)
        
    def add_magic(self, magic_amount):
        self.magic_count += magic_amount
        self.magic_lbl.text = "Magic = " + str(self.magic_count)
 
class UtopiaGame(BoxLayout):
        pass
        
class UtopiaApp(App):
        
        colony = []
        layout = GridLayout(cols=3)
        for i in range(0, 7):
        	settler_c = settler()
        	settler_c.randomize_infos()
        	colony.append(settler_c)
        #return colonScreen(cols=1, colony = colony)
       
        

if __name__ == '__main__':
    UtopiaApp().run()
    
# TODO: Building feature:
# - scroll view at bottom with dif room types
# - scroll view hidden untill button pressed
# - genrate rooms
# - generate specific rooms with scrollbar

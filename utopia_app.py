import kivy
import random
from functools import partial
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color

import time

NAMES =["jean", "hubert", "louis"]
SEX = ["male", "female", "apache helicopter"]
RACES = ["human", "orc", "elf"]

class room_manager():
    def __init__(self, room_nb):
        self.rooms = []      
        self.room_nb = room_nb
        for i in range(0, room_nb):
            self.rooms.append('EmptyRoom')
            
    def  set_room(self, room_idx, room_type):
        self.rooms[room_idx] = room_type
        
    def get_rooms(self):
        return self.rooms
    
    def get_room_nb(self):
        return self.room_nb
        
class RoomSelection(ScrollView):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
    
class BuildArea(GridLayout):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        self.build_list = []
        self.manager = room_manager(40)
        self.update_rooms()
            
    def update_rooms(self):
        self.clear_widgets()
        room_list = self.manager.get_rooms()
        for i in range(0, self.manager.get_room_nb() -1):
            if room_list[i] == 'EmptyRoom':
                self.add_widget(EmptyRoom(i))
            if room_list[i] == "Cafeteria":
                self.add_widget(Cafeteria(i))
            if room_list[i] == "Well":
                self.add_widget(Well(i))
            if room_list[i] == "Generator":
                self.add_widget(Generator(i))  
        
    def build(self, room_type):
            self.clear_widgets()
            for idx in self.build_list:
                self.manager.set_room(idx, room_type)
            self.update_rooms()     
            self.build_list = []
                    
            

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
  	   		
class EmptyRoom(Button):
    def __init__(self, coord_room, **kwargs):
        super(EmptyRoom, self).__init__(**kwargs)
        #self.background_color = (0.0, 0.0, 1.0, 1.0)
        self.default_background = self.background_color
        self.coord_room = coord_room
        self.selected = False
    def on_press(self):
        if self.selected:
            self.selected = False
            self.parent.build_list.remove(self.coord_room)
            self.background_color = self.default_background
        else:
            self.selected = True
            self.parent.build_list.append(self.coord_room)
            self.background_color = (0.0, 0.0, 1.0, 1.0)
        	   		
class Room(Button):
    def __init__(self, coord_room, **kwargs):
        super(Room, self).__init__(**kwargs)
        self.locked = False
        self.background_color = (0.0, 1.0, 0.0, 1.0)
        self.coord_room = coord_room
        
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
    def __init__(self, coord_room, **kwargs):
        super(Cafeteria, self).__init__(coord_room, **kwargs)
class Well(Room):
    def __init__(self, coord_room, **kwargs):
        super(Well, self).__init__(coord_room, **kwargs)
class Generator(Room):
    def __init__(self, coord_room, **kwargs):
        super(Generator, self).__init__(coord_room, **kwargs)
                      	
            
#class BuildArea(ScrollView):
#    def __init__(self, **kwargs):
 #       super().__init__( **kwargs)        
        
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

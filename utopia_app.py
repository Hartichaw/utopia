import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

NAMES =["jean", "hubert", "louis"]
SEX = ["male", "female", "apache helicopter"]
RACES = ["human", "orc", "elf"]

		
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
 	   		
class UtopiaGame(Widget):
    pass
class UIWidget(Widget):
    pass
class MapWidget(Widget):
	pass

class UtopiaApp(App):

    def build(self):
        colony = []
        layout = GridLayout(cols=3)
        for i in range(0, 7):
        	settler_c = settler()
        	settler_c.randomize_infos()
        	colony.append(settler_c)
        #return colonScreen(cols=1, colony = colony)
        for i in range(0, 12):
    	    button = Button()
    	    layout.add_widget(button)
        return UtopiaGame()

if __name__ == '__main__':
    UtopiaApp().run()

# Program to create a calculator  
    
import kivy      
from kivy.app import App  
  
 
from kivy.uix.gridlayout import GridLayout 
  
# for the size of window 
from kivy.config import Config 
  
# Setting size to resizable 
Config.set('graphics', 'resizable', 1) 
  
# Creating Layout class 
class CalcGridLayout(GridLayout):    
    # Function called when equals is pressed 
    def calculate(self, calculation): 
        if calculation: 
            try: 
                self.display.text = str(eval(calculation))
                print(self.display.text)
            except Exception: 
                self.display.text = "Error"
   
 # Creating App class 
class CalculatorApp(App): 
   
    def build(self): 
        return CalcGridLayout() 
   
# creating object and running it  
if __name__ == "__main__":
	calcApp = CalculatorApp() 
	calcApp.run() 

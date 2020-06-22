from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.utils import get_color_from_hex

#Setting the window width and height
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 700)

# Menu Screen class
class MenuScreen(Screen):
    pass

# Player Screen Class
class TwoPlayerScreen(Screen):
    #Getting widgets
    btn0 = ObjectProperty(None)
    btn1 = ObjectProperty(None)
    btn2 = ObjectProperty(None)
    btn3 = ObjectProperty(None)
    btn4 = ObjectProperty(None)
    btn5 = ObjectProperty(None)
    btn6 = ObjectProperty(None)
    btn7 = ObjectProperty(None)
    btn8 = ObjectProperty(None)
    winner_label = ObjectProperty(None)
    red_score = ObjectProperty(None)
    green_score = ObjectProperty(None)
    turn_label = ObjectProperty(None)

    # Path for the images
    cross = "images/Cross.jpg"
    circle = "images/Circle.jpg"
    black = "images/black.jpg"

    #Counters to determine player (X or O) and changing them
    player_counter = 0
    game_counter = 0


    def on_pre_enter(self):
        self.reset()
        self.game_counter = 0
        self.red_score.text = "0"
        self.green_score.text = "0"
        self.turn_label.text = "Red"
        self.turn_label.color = (1, 0, 0, 1)

    #Function that gets called after each turn with a index value
    def do(self, index):
        # A list of widgets
        buttons = [self.btn0, self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8]

        # Logic for playing the game
        if (self.game_counter%2 == 0):
            if (self.player_counter%2 == 0):
                self.player_counter += 1
                buttons[index].background_normal = self.cross
                buttons[index].background_disabled_normal = self.cross
                buttons[index].disabled = True
                self.turn_label.text = "Green"
                self.turn_label.color = (0, 1, 0, 1)
            else:
                self.player_counter += 1
                buttons[index].background_normal = self.circle
                buttons[index].background_disabled_normal = self.circle
                buttons[index].disabled = True
                self.turn_label.text = "Red"
                self.turn_label.color = (1, 0, 0, 1)
        else:
            if (self.player_counter%2 != 0):
                self.player_counter += 1
                buttons[index].background_normal = self.cross
                buttons[index].background_disabled_normal = self.cross
                buttons[index].disabled = True
                self.turn_label.text = "Green"
                self.turn_label.color = (0, 1, 0, 1)
            else:
                self.player_counter += 1
                buttons[index].background_normal = self.circle
                buttons[index].background_disabled_normal = self.circle
                buttons[index].disabled = True
                self.turn_label.text = "Red"
                self.turn_label.color = (1, 0, 0, 1)

        # Calls the showWinner function after every move/turn
        self.showWinner()

        
    # Function to check for winner
    def showWinner(self):
        buttons = [self.btn0, self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8]

        
        if (buttons[0].background_disabled_normal == self.cross and buttons[1].background_disabled_normal == self.cross and buttons[2].background_disabled_normal == self.cross) or (buttons[3].background_disabled_normal == self.cross and buttons[4].background_disabled_normal == self.cross and buttons[5].background_disabled_normal == self.cross) or (buttons[6].background_disabled_normal == self.cross and buttons[7].background_disabled_normal == self.cross and buttons[8].background_disabled_normal == self.cross) or (buttons[0].background_disabled_normal == self.cross and buttons[3].background_disabled_normal == self.cross and buttons[6].background_disabled_normal == self.cross) or (buttons[1].background_disabled_normal == self.cross and buttons[4].background_disabled_normal == self.cross and buttons[7].background_disabled_normal == self.cross) or (buttons[2].background_disabled_normal == self.cross and buttons[5].background_disabled_normal == self.cross and buttons[8].background_disabled_normal == self.cross) or (buttons[0].background_disabled_normal == self.cross and buttons[4].background_disabled_normal == self.cross and buttons[8].background_disabled_normal == self.cross) or (buttons[2].background_disabled_normal == self.cross and buttons[4].background_disabled_normal == self.cross and buttons[6].background_disabled_normal == self.cross):
            self.winner_label.text = "Red Wins"
            self.winner_label.color = (1,0,0,1)
            self.winner_label.opacity = 1
            self.red_score.text = str(int(self.red_score.text) + 1)
            self.turn_label.opacity = 0

            for button in buttons:
                if (button.background_normal == self.black):
                    button.background_disabled_normal = self.black
                button.disabled = True

        elif (buttons[0].background_disabled_normal == self.circle and buttons[1].background_disabled_normal == self.circle and buttons[2].background_disabled_normal == self.circle) or (buttons[3].background_disabled_normal == self.circle and buttons[4].background_disabled_normal == self.circle and buttons[5].background_disabled_normal == self.circle) or (buttons[6].background_disabled_normal == self.circle and buttons[7].background_disabled_normal == self.circle and buttons[8].background_disabled_normal == self.circle) or (buttons[0].background_disabled_normal == self.circle and buttons[3].background_disabled_normal == self.circle and buttons[6].background_disabled_normal == self.circle) or (buttons[1].background_disabled_normal == self.circle and buttons[4].background_disabled_normal == self.circle and buttons[7].background_disabled_normal == self.circle) or (buttons[2].background_disabled_normal == self.circle and buttons[5].background_disabled_normal == self.circle and buttons[8].background_disabled_normal == self.circle) or (buttons[0].background_disabled_normal == self.circle and buttons[4].background_disabled_normal == self.circle and buttons[8].background_disabled_normal == self.circle) or (buttons[2].background_disabled_normal == self.circle and buttons[4].background_disabled_normal == self.circle and buttons[6].background_disabled_normal == self.circle):
            self.winner_label.text = "Green Wins"
            self.winner_label.color = (0,1,0,1)
            self.winner_label.opacity = 1
            self.green_score.text = str(int(self.green_score.text) + 1)
            self.turn_label.opacity = 0
            
            for button in buttons:
                if (button.background_normal == self.black):
                    button.background_disabled_normal = self.black
                button.disabled = True

        elif (self.player_counter == 9):
            self.winner_label.text = "Tie"
            self.winner_label.opacity = 1
            self.winner_label.color = (0, 1, 1, 1)
            self.turn_label.opacity = 0

    #Function to reset the game on pressing Play Again Button
    def reset(self):
        buttons = [self.btn0, self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8]

        self.winner_label.opacity = 0
        self.player_counter = 0
        self.turn_label.opacity = 1

        for button in buttons:
            button.background_normal = self.black
            button.background_disabled_normal = self.black
            button.disabled = False

        self.game_counter += 1


#Loading the external kv file
GUI = Builder.load_file("main.kv")

# App class
class mainApp(App):
    def build(self):
        return GUI

    # Function to change screen
    def changescreen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name

    # function called on pressing quit on menuscreen
    def quitbtn(self):
        quit()

#Running the app
mainApp().run()
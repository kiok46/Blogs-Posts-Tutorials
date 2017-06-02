from kivy.uix.button import Button

class CustomButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.background_down = 'atlas://textures/red-lightgrey/myatlas/button_pressed'
        self.background_normal = 'atlas://textures/red-lightgrey/myatlas/button_pressed'

from kivy.uix.checkbox import CheckBox


class CustomCheckBox(CheckBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_down = 'atlas://textures/red-lightgrey/myatlas/button_pressed'
        self.background_checkbox_normal = 'atlas://textures/red-lightgrey/myatlas/checkbox_off'
        self.background_checkbox_down = 'atlas://textures/red-lightgrey/myatlas/checkbox_on'
        self.background_checkbox_disabled_normal = 'atlas://textures/red-lightgrey/myatlas/checkbox_disabled_off'
        self.background_checkbox_disabled_down = 'atlas://textures/red-lightgrey/myatlas/checkbox_disabled_on'

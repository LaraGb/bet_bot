from PySide6.QtWidgets import QPushButton


class BaseButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
       


class HighlightedButton(BaseButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("background-color: yellow;")
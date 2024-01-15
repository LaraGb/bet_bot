from PySide6.QtWidgets import QPushButton


class BaseButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("height: 39.861px; border-radius: 5.486px; background: #1D1D1D;color:white")
       


class PrimaryHighlightedButton(BaseButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("background-color: yellow;")


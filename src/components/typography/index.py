from PySide6.QtWidgets import QLabel


class BaseTypography(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
       
       
class Title(BaseTypography):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("background-color: yellow;")

class SubTitle(BaseTypography):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("background-color: yellow;")

class Paragraph(BaseTypography):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("background-color: yellow;")

class H3Bold(BaseTypography):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("font-size: 14.698px; font-style: semibold; font-weight: 700;")
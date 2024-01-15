from pyside6.QtWidgets import QFrame

class StyledFrame(QFrame):
    def __init__(self):
        super().__init__()

        # Estilo da borda
        border_style = "border-radius: 8px; border: 0.784px solid rgba(77, 76, 76, 0.38);"

        # Aplicar estilo
        self.setStyleSheet(border_style)
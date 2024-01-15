from PySide6.QtWidgets import QWidget, QDoubleSpinBox, QVBoxLayout, QRadioButton

class CustomDoubleSpinBox(QDoubleSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        # Adicione configurações adicionais conforme necessário
        self.setRange(0, 10000.0)  # Substitua pelos valores desejados
        self.setValue(0.0)
        self.setStyleSheet("padding:8px 12px; border-radius: 8.486px; border: 1.212px solid #D6D6D6; QDoubleSpinBox { background-color: red; } ")
        pass

    # Métodos adicionais podem ser adicionados conforme necessário
    def get_values(self):
        return self.value()
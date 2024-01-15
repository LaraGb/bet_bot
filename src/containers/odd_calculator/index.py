from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QRadioButton, QDoubleSpinBox, QSizePolicy
from PySide6.QtCore import Qt 
from src.components.input.double_spin import CustomDoubleSpinBox


class OddCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        gridLayout = QGridLayout()


        header_column_1 = QLabel("Casa:")
        header_column_1.setAlignment(Qt.AlignCenter)
        header_column_1.setStyleSheet("border-radius: 8.486px; border: 1.212px solid #E2E2E2; background: #EFEFEF;padding:8px 12px; ")

        header_column_2 = QLabel("ODD:")
        header_column_2.setAlignment(Qt.AlignCenter)
        header_column_2.setStyleSheet("color:#613CEA; font-weight: 500; border-radius: 8.486px; border: 1.212px solid rgba(97, 60, 234, 0.50); background: rgba(97, 60, 234, 0.10);padding:8px 12px; ")

        header_column_3 = QLabel("teste")
        header_column_3.setAlignment(Qt.AlignCenter)
        header_column_3.setStyleSheet("border-radius: 8.486px; border: 1.212px solid #E2E2E2; background: #EFEFEF;padding:8px 12px; ")

        header_column_4 = QLabel("Lucro")
        header_column_4.setAlignment(Qt.AlignCenter)
        header_column_4.setStyleSheet("color:#613CEA;font-weight: 500; border-radius: 8.486px; border: 1.212px solid rgba(97, 60, 234, 0.50); background: rgba(97, 60, 234, 0.10);padding:8px 12px; ")

        gridLayout.addWidget(header_column_1, 0, 0)
        gridLayout.addWidget(header_column_2, 0, 1)
        gridLayout.addWidget(header_column_3, 0, 2)
        gridLayout.addWidget(header_column_4, 0, 3)

        # 2 Row
        radioBtn = QRadioButton("Radio")
        spin_box = CustomDoubleSpinBox()
        spin_box_2 = CustomDoubleSpinBox()
        spin_box_3 = CustomDoubleSpinBox()

        gridLayout.addWidget(radioBtn, 1, 0)
        gridLayout.addWidget(spin_box, 1, 1)
        gridLayout.addWidget(spin_box_2, 1, 2)
        gridLayout.addWidget(spin_box_3, 1, 3)

        # 3 Row
        radioBtn = QRadioButton("Radio")
        spin_box = QDoubleSpinBox()
        spin_box_2 = QDoubleSpinBox()
        spin_box_3 = QDoubleSpinBox()

        gridLayout.addWidget(radioBtn, 2, 0)
        gridLayout.addWidget(spin_box, 2, 1)
        gridLayout.addWidget(spin_box_2, 2, 2)
        gridLayout.addWidget(spin_box_3, 2, 3)

        # 4 Row
        radioBtn = QRadioButton("Radio")
        spin_box = QDoubleSpinBox()
        spin_box_2 = QDoubleSpinBox()
        spin_box_3 = QDoubleSpinBox()

        gridLayout.addWidget(radioBtn, 3, 0)
        gridLayout.addWidget(spin_box, 3, 1)
        gridLayout.addWidget(spin_box_2, 3, 2)
        gridLayout.addWidget(spin_box_3, 3, 3)

        gridLayout.setVerticalSpacing(20)
        self.setLayout(gridLayout)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

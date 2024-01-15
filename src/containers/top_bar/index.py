from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QMainWindow, QSizePolicy

class MyTopBar(QWidget):
    def __init__(self):
        super(MyTopBar, self).__init__()

        self.initUI()

    def initUI(self):
        left_frame = QWidget(self)
        left_layout = QHBoxLayout(left_frame)

        for i in range(4):
            btn = QPushButton(f"Button {i + 1}")
            left_layout.addWidget(btn)

        right_frame = QWidget(self)
        right_layout = QHBoxLayout(right_frame)

        right_btn = QPushButton("Right Button")
        right_layout.addWidget(right_btn)

        main_layout = QHBoxLayout(self)
        main_layout.addWidget(left_frame)
        main_layout.addStretch(1)
        main_layout.addWidget(right_frame)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

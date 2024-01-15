from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QHBoxLayout, QPushButton, QGridLayout, QRadioButton, QDoubleSpinBox, QSizePolicy
from PySide6.QtCore import Qt
from src.components.button.index import BaseButton
from src.components.cards.game_info_row.index import GameInfoRow
from src.containers.odd_calculator.index import OddCalculator

class SidebarContainer(QFrame):
    def __init__(self):
        super().__init__()

        # Defina um estilo para o QFrame que representa o SidebarContainer
        container_layout = QVBoxLayout()

        # Adicione a Sidebar ao SidebarContainer
        sidebar = Sidebar()
        container_layout.addWidget(sidebar)

        self.setLayout(container_layout)

class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
       

        #  ------ Primeiro frame -------
        first_frame = QWidget()
        first_frame_layout = QVBoxLayout()

        title_label = QLabel("UEFA Champions League")
        title_label.setStyleSheet("font-size: 24px; font-style: normal; font-weight: 700; line-height: 18.396px;")

        subtitle_label = QLabel("Groupe stage - Matchday 2 of 6")

        first_frame_layout.addWidget(title_label)
        first_frame_layout.addWidget(subtitle_label)

        first_frame.setLayout(first_frame_layout)

        second_frame = QWidget()
        second_frame_layout = QHBoxLayout()

        for i in range(3):
            team_frame = QWidget()
            team_frame_layout = QVBoxLayout()
            team_label = QLabel("Team")
            team_frame_layout.addWidget(team_label)
            team_frame.setLayout(team_frame_layout)
            second_frame_layout.addWidget(team_frame)

        second_frame.setLayout(second_frame_layout)

        third_frame = QWidget()
        third_frame_layout = QHBoxLayout()

        button1 = BaseButton("7.59%")
        button2 = BaseButton("Star")
        button3 = BaseButton("Futebol")
        button1.setStyleSheet("width: 92.787px; height: 39.861px; border-radius: 5.486px; background: #1D1D1D;color:white")

        third_frame_layout.addWidget(button1)
        third_frame_layout.addWidget(button2)
        third_frame_layout.addWidget(button3)

        third_frame.setLayout(third_frame_layout)

        # Adicionando os frames ao frame principal
        initial_sidebar_data = QWidget()
        initial_sidebar_layout = QVBoxLayout()
        initial_sidebar_layout.addWidget(first_frame)
        initial_sidebar_layout.addWidget(second_frame)
        initial_sidebar_layout.addWidget(third_frame)
        initial_sidebar_data.setLayout(initial_sidebar_layout)

        main_layout.addWidget(initial_sidebar_data)

        # -------- Segundo frame do sidebar ------------
        second_sidebar_frame = QWidget()
        second_sidebar_layout = QVBoxLayout()
       
       # TITULO
        second_title_label = QLabel("Detalhes:")
        second_sidebar_layout.addWidget(second_title_label)
     
        info_1 = GameInfoRow("Shelbourne - UC Dublin 1")
        second_sidebar_layout.addWidget(info_1)
        info_2 = GameInfoRow("Shelbourne - UC Dublin 2")
        second_sidebar_layout.addWidget(info_2)
        info_3 = GameInfoRow("Shelbourne - UC Dublin 3")
        second_sidebar_layout.addWidget(info_3)
        info_4 = GameInfoRow("Shelbourne - UC Dublin 4")
        second_sidebar_layout.addWidget(info_4)
       
        second_sidebar_frame.setLayout(second_sidebar_layout)
        main_layout.addWidget(second_sidebar_frame)

        # ------------ Terceiro frame --------------
        third_frame_grid = QWidget()
        third_frame_grid_layout = QGridLayout()

        header_column_1 = QLabel("Casa 1:")
        header_column_1.setAlignment(Qt.AlignCenter)
        header_column_1.setStyleSheet("border-radius: 8.486px; border: 1.212px solid #E2E2E2; background: #EFEFEF;padding:8px 12px; ")
        header_column_2 = QLabel("Casa 2:")
        header_column_2.setAlignment(Qt.AlignCenter)
        header_column_2.setStyleSheet("border-radius: 8.486px; border: 1.212px solid #E2E2E2; background: #EFEFEF;padding:8px 12px; ")

        third_frame_grid_layout.addWidget(header_column_1, 0, 0)
        third_frame_grid_layout.addWidget(header_column_2, 0, 1)

        # ROWS

        item_column_1 = QLabel("1 - Escanteio")
        item_column_1.setAlignment(Qt.AlignCenter)
        item_column_1.setStyleSheet("border-radius: 8.486px; border: 1.212px solid #E2E2E2; background: #EFEFEF;padding:8px 12px; ")
        third_frame_grid_layout.addWidget(item_column_1, 1, 0)


        third_frame_grid.setLayout(third_frame_grid_layout)
        main_layout.addWidget(third_frame_grid)

        # Último frame
        odd_calculator = OddCalculator()
        main_layout.addWidget(odd_calculator)
        
    
    
        self.setFixedWidth(380)
        self.setLayout(main_layout)


    
    
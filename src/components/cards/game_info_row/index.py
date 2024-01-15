from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class GameInfoRow(QWidget):
    def __init__(self, info):
        super().__init__()

        # Criar o layout vertical
        layout = QVBoxLayout(self)

        # Criar o contêiner para definir o plano de fundo
        container = QWidget(self)
        container.setStyleSheet("background:red ")  # Substitua pela cor desejada

        # Criar o rótulo com o nome da equipe
        team_label = QLabel(info, container)

        # Adicionar o rótulo ao contêiner
        container_layout = QVBoxLayout(container)
        container_layout.addWidget(team_label)

        # Adicionar o contêiner ao layout vertical principal
        layout.addWidget(container)

        self.setLayout(layout)

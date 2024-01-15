from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy,QHeaderView
from src.components.table.main_table import TabelaPersonalizada

class MainContent(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Main Content Area")
        self.layout.addWidget(self.label)
        dados = [
        {'Idade': '22:10', 'Data do Evento': '12/04 - 13:00', 'Porcentagem': '3.4%', 'Esporte': 'Futebol',
         'Casa de Apostas 1': 'Nome 1', 'Casa de Apostas 2': 'Nome Casa 2', 'Mercado 1': 'Nome Mercado 1', 'Mercado 2': 'Nome Mercado 2'},
         {'Idade': '22:10', 'Data do Evento': '12/04 - 13:00', 'Porcentagem': '3.4%', 'Esporte': 'Futebol',
         'Casa de Apostas 1': 'Nome 1', 'Casa de Apostas 2': 'Nome Casa 2', 'Mercado 1': 'Nome Mercado 1', 'Mercado 2': 'Nome Mercado 2'}
        ]

        self.tabela = TabelaPersonalizada() 
        # Configurando dados na tabela
        self.tabela.setData(dados)
        self.tabela.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.tabela)

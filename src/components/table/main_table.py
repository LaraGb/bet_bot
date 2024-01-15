from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PySide6.QtGui import QColor, QBrush, QPalette

class TabelaPersonalizada(QTableWidget):
    def __init__(self):
        super(TabelaPersonalizada, self).__init__()

        # Configurando o cabeçalho
        headers = ['Idade', 'Data do Evento', 'Porcentagem', 'Esporte', 'Casa de Apostas 1', 'Casa de Apostas 2', 'Mercado 1', 'Mercado 2']
        self.setHorizontalHeaderLabels(headers)
        self.horizontalHeader().setStyleSheet("QHeaderView::section { background: #F9FAFA; border: 1px solid #EFEFEF; padding:10px}")


        self.verticalHeader().setVisible(False)
        self.setEditTriggers(QTableWidget.NoEditTriggers)

        # Desativando a seleção de colunas
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setSelectionMode(QTableWidget.SingleSelection)

        # Desativando a borda da célula
        self.setStyleSheet("QTableWidget { border:  1.052px solid #EFEFEF; border-radius:12px } QTableWidget::item { border: 0px; }")
      

        # Remover a borda pontilhada e ajustar a cor da seleção da célula
        palette = QPalette()
        palette.setColor(QPalette.Highlight, QColor('lightblue'))
        palette.setColor(QPalette.HighlightedText, QColor('black'))
        self.setPalette(palette)

        # Conectando o sinal cellClicked à função que altera a cor da linha
        self.cellClicked.connect(self.selecionarLinha)

    def setRowColor(self, row, color):
        for col in range(self.columnCount()):
            item = self.item(row, col)
            if item:
                item.setBackground(QBrush(color))

    def limparSelecoes(self):
        for row in range(self.rowCount()):
            self.setRowColor(row, QColor('white'))

    def selecionarLinha(self, row, col):
        # Limpar seleções anteriores
        self.limparSelecoes()

        # Definir cor da linha selecionada
        self.setRowColor(row, QColor('lightblue'))

    def setData(self, data):
        self.setRowCount(len(data))
        self.setColumnCount(len(data[0]))

        headers = list(data[0].keys())
        self.setHorizontalHeaderLabels(headers)

        for i, row_data in enumerate(data):
            for j, (key, value) in enumerate(row_data.items()):
                item = QTableWidgetItem(str(value))
                self.setItem(i, j, item)

if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()

    # Criando a tabela personalizada
    tabela = TabelaPersonalizada(1, 8)  # 1 linha, 8 colunas

    # Dados para popular a tabela
    dados = [
        {'Idade': '22:10', 'Data do Evento': '12/04 - 13:00', 'Porcentagem': '3.4%', 'Esporte': 'Futebol',
         'Casa de Apostas 1': 'Nome 1', 'Casa de Apostas 2': 'Nome Casa 2', 'Mercado 1': 'Nome Mercado 1', 'Mercado 2': 'Nome Mercado 2'},
         {'Idade': '22:10', 'Data do Evento': '12/04 - 13:00', 'Porcentagem': '3.4%', 'Esporte': 'Futebol',
         'Casa de Apostas 1': 'Nome 1', 'Casa de Apostas 2': 'Nome Casa 2', 'Mercado 1': 'Nome Mercado 1', 'Mercado 2': 'Nome Mercado 2'}
    ]

    # Configurando dados na tabela
    tabela.setData(dados)

    # Configurando o layout
    layout = QVBoxLayout()
    layout.addWidget(tabela)
    window.setLayout(layout)

    window.show()
    app.exec()

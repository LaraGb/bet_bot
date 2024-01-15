import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout
from src.containers.side_bar.index import SidebarContainer
from src.containers.main_table.index import MainContent
from src.containers.top_bar.index import MyTopBar

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.sidebar = SidebarContainer()
        self.main_content = MainContent()
        self.topbar = MyTopBar()

      
        main_layout = QVBoxLayout()
        self.setStyleSheet("background-color:white;")

       
        main_layout.addWidget(self.topbar)

       
        sidebar_and_content_layout = QHBoxLayout()

        sidebar_and_content_layout.addWidget(self.sidebar)

        
        sidebar_and_content_layout.addWidget(self.main_content, 1)

       
        main_layout.addLayout(sidebar_and_content_layout)

    
        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)
        self.setWindowTitle("PySide6 App")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())

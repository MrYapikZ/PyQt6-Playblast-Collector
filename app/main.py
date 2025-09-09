import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from app.ui.main_widget_ui import Ui_MainWindow
from app.modules.main.handle_collector import CollectorHandler

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Playblast Collector")
        self.ui.label_version.setText("v0.1.0")

        self.ui.tabWidget_main.addTab(CollectorHandler(), "Collector")
        # Additional UI setup can be done here

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec())

# pyinstaller --clean --noconsole --onefile -n ShotFolderGenerator main.py

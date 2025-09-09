import os
from PyQt6.QtWidgets import QWidget, QMessageBox
from app.ui.collector_widget_ui import Ui_Form
from app.services.file_manager import FileManager

class CollectorHandler(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.toolButton_projectPath.clicked.connect(lambda: self.on_select_project_path(is_project=True))
        self.ui.toolButton_exportPath.clicked.connect(lambda: self.on_select_project_path(is_project=False))
        self.ui.pushButton_execute.clicked.connect(self.on_execute)

    def on_execute(self):
        try:
            # Validate paths
            if not self.ui.lineEdit_projectPath.text():
                QMessageBox.warning(self, "Warning", "Project path is empty.")
                raise ValueError("Project path is empty.")
            if not self.ui.lineEdit_exportPath.text():
                QMessageBox.warning(self, "Warning", "Export path is empty.")
                raise ValueError("Export path is empty.")

            # Scan for latest files
            files = FileManager(self.ui.lineEdit_projectPath.text(),
                                              self.ui.lineEdit_fileExtension.text()).scan()
            # scanner = FileManager("path/to/root", "mov")
            # latest_files = scanner.scan()


            # Copy files and update UI
            self.ui.listWidget_fileList.clear()
            for key, file in files.items():
                ep, seq, shot, div = key

                print(f"{div.upper()} latest: {file}")
                copy_file = FileManager(self.ui.lineEdit_projectPath.text(),
                                              self.ui.lineEdit_fileExtension.text()).copy_file(src=file, destination=self.ui.lineEdit_exportPath.text(), division=div)
                if copy_file == "NOT_EXIST":
                    QMessageBox.warning(self, "Warning", f"Export path does not exist: {self.ui.lineEdit_exportPath.text()}")
                    raise FileNotFoundError(f"Export path does not exist: {self.ui.lineEdit_exportPath.text()}")
                self.ui.listWidget_fileList.addItem(os.path.basename(file))

        except Exception as e:
            print(f"Error setting paths: {e}")
            return

    def on_select_project_path(self, is_project: bool):
        from PyQt6.QtWidgets import QFileDialog
        directory = QFileDialog.getExistingDirectory(self, "Select Project Directory")
        if directory:
            if is_project:
                self.ui.lineEdit_projectPath.setText(directory)
            else:
                self.ui.lineEdit_exportPath.setText(directory)
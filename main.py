from PySide6.QtWidgets import QApplication
import sys
from app import SDDatasetEditorApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SDDatasetEditorApp()
    w.resize(1200, 800)
    w.show()
    sys.exit(app.exec())
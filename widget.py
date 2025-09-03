# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget, QMessageBox
)

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToDoリスト")
        self.resize(400, 300)

        # ウィジェット作成
        self.input = QLineEdit()
        self.input.setPlaceholderText("タスクを入力...")
        self.add_button = QPushButton("追加")
        self.delete_button = QPushButton("削除")
        self.list_widget = QListWidget()

        # ボタンと入力欄のレイアウト
        hbox = QHBoxLayout()
        hbox.addWidget(self.input)
        hbox.addWidget(self.add_button)
        hbox.addWidget(self.delete_button)

        # 全体レイアウト
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.list_widget)
        self.setLayout(vbox)

        # シグナル接続
        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)

    def add_task(self):
        task = self.input.text().strip()
        if task:
            self.list_widget.addItem(task)
            self.input.clear()
        else:
            QMessageBox.warning(self, "エラー", "タスクを入力してください。")

    def delete_task(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            self.list_widget.takeItem(self.list_widget.row(selected_item))
        else:
            QMessageBox.warning(self, "エラー", "削除するタスクを選んでください。")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec())

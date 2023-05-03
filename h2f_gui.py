from PyQt5.QtWidgets import QApplication,QWidget, QTextEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class GUI():

    def __init__(self, translatorH, translatorF):
        self.translatorH = translatorH
        self.translatorF = translatorF

        self.app = QApplication([])
        self.window = QWidget()

        self.window.resize(1000,500)
        self.window.setWindowTitle("Fish Translator")

        self.text_Humans = QLabel("Human")
        self.text_Fishes = QLabel("Fish")

        self.tb_human = QTextEdit()
        self.tb_fish = QTextEdit()
        self.tb_human.setText("Here")
        self.tb_fish.setText("Or here")

        self.but_to_H = QPushButton("Для Людей")
        self.but_to_F = QPushButton("Для Рыб")
        self.but_to_H.clicked.connect(self.to_humans)
        self.but_to_F.clicked.connect(self.to_fishes)

        self.lay_main = QHBoxLayout()
        self.lay_left = QVBoxLayout()
        self.lay_mid = QVBoxLayout()
        self.lay_right = QVBoxLayout()

        self.lay_left.addWidget(self.text_Humans, alignment = Qt.AlignLeft)
        self.lay_left.addWidget(self.tb_human)
        self.lay_mid.addWidget(self.but_to_H)
        self.lay_mid.addWidget(self.but_to_F)
        self.lay_right.addWidget(self.text_Fishes, alignment = Qt.AlignLeft)
        self.lay_right.addWidget(self.tb_fish)

        self.lay_main.addLayout(self.lay_left, stretch = 45)
        self.lay_main.addLayout(self.lay_mid, stretch = 10)
        self.lay_main.addLayout(self.lay_right, stretch = 45)

        self.window.setLayout(self.lay_main)


    def start(self):
        self.window.show()
        self.app.exec_()


    def to_humans(self):
        ans = self.translatorH(self.tb_fish.toPlainText())
        self.tb_human.setText(ans)


    def to_fishes(self):
        ans = self.translatorF(self.tb_human.toPlainText())
        self.tb_fish.setText(ans)





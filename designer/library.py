from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QAbstractTableModel
from data_func import *


class Library(QWidget):

    # constructor
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()

        # 첫번째 줄, 검색하는 타입, 검색창, 검색 버튼
        # 검색 타입 콤보 박스
        self.search_box = QComboBox()
        self.search_box.setMaximumWidth(70)
        self.search_box.addItem('Title')
        self.search_box.addItem('Author')
        self.search_box.addItem('Publisher')
        self.search_box.addItem('Lender')
        # 검색 창
        self.search_bar = QLineEdit("")
        # 검색 버튼
        self.search_btn = QPushButton("검색")
        self.search_btn.setMaximumWidth(70)
        self.hbox1.addWidget(self.search_box)
        self.hbox1.addWidget(self.search_bar)
        self.hbox1.addWidget(self.search_btn)

        # 두번째 줄 반납하기 버튼, 대여 가능 책들 보기, 대여기간 콤보박스, 대여하기 버튼
        # 반납하기 버튼
        self.return_btn = QPushButton("반납하기")

        # 대여하기 버튼
        self.lend_btn = QPushButton("대여하기")

        # 책 리스트를 보여주는 콤보박스
        self.show_box = QComboBox()
        self.show_button = QPushButton("보기")

        self.show_box.addItem("모든 책들")
        self.show_box.addItem("대여 가능한 책들")
        self.show_box.addItem("대여 중인 책들")


        self.hbox2.addWidget(self.show_box)
        self.hbox2.addWidget(self.show_button)

        self.hbox5.addWidget(self.lend_btn)
        self.hbox5.addWidget(self.return_btn)

        # 세번째 줄 데이터 라벨
        self.hbox3.addWidget(QLabel('Title'))
        self.hbox3.addWidget(QLabel('Author'))
        self.hbox3.addWidget(QLabel('Publisher'))

        # 네번째 줄 데이터 창
        self.result_text = QTableWidget(self)
        self.result_text.setMinimumWidth(400)
        self.result_text.setSelectionMode(QAbstractItemView.SingleSelection)
        self.result_text.setColumnCount(3)
        self.setResult_textData("모든 책들")


        self.hbox4.addWidget(self.result_text)

        self.show_lender = QTextEdit()
        self.show_lender.setReadOnly(True)
        self.show_lender.setMaximumHeight(200)
        self.hbox6.addWidget(self.show_lender)

        self.hbox = QHBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.vbox1.addLayout(self.hbox4)
        self.vbox2.addLayout(self.hbox1)
        self.vbox2.addLayout(self.hbox2)
        self.vbox2.addLayout(self.hbox5)
        self.vbox2.addLayout(self.hbox6)
        self.hbox.addLayout(self.vbox1)
        self.hbox.addLayout(self.vbox2)

        self.setLayout(self.hbox)

        # 버튼 누르기 구현
        self.search_btn.clicked.connect(self.buttonClicked)
        self.show_button.clicked.connect(self.buttonClicked)
        self.return_btn.clicked.connect(self.buttonClicked)
        self.lend_btn.clicked.connect(self.buttonClicked)

        self.setGeometry(600, 200, 600, 800)
        self.setWindowTitle('KCC_Library')
        self.show()

    def setResult_textData(self, str):
        column_headers = ['title', 'author', 'publisher']
        self.result_text.setHorizontalHeaderLabels(column_headers)
        if str == "모든 책들":
            show_All(self)
        elif str == "대여 가능한 책들":
            show_Available(self)
        elif str == "대여 중인 책들":
            show_NotAvailable(self)

    def buttonClicked(self):
        sender = self.sender()

        if sender.text() == "검색":
            key = self.search_box.currentText()
            ser = self.search_box.currentText()
            if key == 'Title':
                pass

        elif sender.text() == "보기":
            key = self.show_box.currentText()
            if key == "모든 책들":
                self.setResult_textData("showAll")
            elif key == "대여 가능한 책들":
                self.setResult_textData("showAvailables")
            elif key == "대여 중인 책들":
                self.setResult_textData("showNotAvailables")


    # destructor
    def __del__(self):
        return

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Graph(object):
    def setupUi(self, Dialog_Graph):
        Dialog_Graph.setObjectName("Dialog_Graph")
        Dialog_Graph.resize(300, 430)
        Dialog_Graph.setStyleSheet("background-color: rgb(89, 101, 214);")
        self.label_3 = QtWidgets.QLabel(Dialog_Graph)
        self.label_3.setGeometry(QtCore.QRect(19, 10, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setLineWidth(3)
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog_Graph)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 360, 75, 23))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setAutoRepeat(False)
        self.pushButton_4.setAutoExclusive(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(Dialog_Graph)
        self.label_4.setGeometry(QtCore.QRect(10, 400, 191, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog_Graph)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 60, 120, 23))
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Dialog_Graph)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Graph)

    def retranslateUi(self, Dialog_Graph):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Graph.setWindowTitle(_translate("Dialog_Graph", "Graph"))
        self.label_3.setText(_translate("Dialog_Graph", "                     Graph"))
        self.pushButton_4.setText(_translate("Dialog_Graph", "Exit"))
        self.label_4.setText(_translate("Dialog_Graph", "?????????????????????? ???????? ?????? 1-7"))
        self.pushButton_5.setText(_translate("Dialog_Graph", "???????????? ??? 1"))
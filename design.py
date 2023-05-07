from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 850)
        MainWindow.setMinimumSize(QtCore.QSize(1150, 850))
        MainWindow.setMaximumSize(QtCore.QSize(1150, 850))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formFrame = QtWidgets.QFrame(self.centralwidget)
        self.formFrame.setGeometry(QtCore.QRect(60, 90, 471, 161))
        self.formFrame.setStyleSheet("#formFrame{\n"
                                    "background-color: rgb(121, 195, 208);\n"
                                    "border-radius : 15px;\n"
                                    "}")
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setContentsMargins(13, 13, 13, 13)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_Value = QtWidgets.QLineEdit(self.formFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_Value.setFont(font)
        self.lineEdit_Value.setStyleSheet("")
        self.lineEdit_Value.setObjectName("lineEdit_Value")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Value)
        self.label = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_Date = QtWidgets.QLineEdit(self.formFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_Date.setFont(font)
        self.lineEdit_Date.setStyleSheet("")
        self.lineEdit_Date.setObjectName("lineEdit_Date")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Date)
        self.label_2 = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox_Algo = QtWidgets.QComboBox(self.formFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_Algo.setFont(font)
        self.comboBox_Algo.setStyleSheet("")
        self.comboBox_Algo.setObjectName("comboBox_Algo")
        self.comboBox_Algo.addItem("")
        self.comboBox_Algo.addItem("")
        self.comboBox_Algo.addItem("")
        self.comboBox_Algo.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_Algo)
        self.comboBox_test = QtWidgets.QComboBox(self.formFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_test.setFont(font)
        self.comboBox_test.setStyleSheet("background-color: rgb(121, 194, 208);")
        self.comboBox_test.setObjectName("comboBox_test")
        self.comboBox_test.addItem("")
        self.comboBox_test.addItem("")
        self.comboBox_test.addItem("")
        self.comboBox_test.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.comboBox_test)
        self.pushButton_test = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_test.setGeometry(QtCore.QRect(310, 270, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_test.setFont(font)
        self.pushButton_test.setStyleSheet("#pushButton_test{\n"
                                            "background-color: rgb(121, 195, 208);\n"
                                            "border-radius : 15px;\n"
                                            "}\n"
                                            "#pushButton_test:hover{\n"
                                            "background-color: rgb(121, 195, 255);\n"
                                            "}")
        self.pushButton_test.setObjectName("pushButton_test")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 40, 541, 321))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("#label_3{\n"
                                    "background-color: rgb(121, 195, 208);\n"
                                    "border-radius : 20px;\n"
                                    "}")
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.label_Result = QtWidgets.QLabel(self.centralwidget)
        self.label_Result.setGeometry(QtCore.QRect(590, 80, 481, 281))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Result.setFont(font)
        self.label_Result.setStyleSheet("#label_Result{\n"
                                        "background-color: rgb(202, 202, 202);\n"
                                        "border-radius : 10px;\n"
                                        "}")
        self.label_Result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Result.setObjectName("label_Result")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 400, 1041, 431))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("#label_4{\n"
                                    "background-color: rgb(121, 195, 208);\n"
                                    "border-radius : 20px;\n"
                                    "}")
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(100, 440, 961, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_save_data = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_data.setGeometry(QtCore.QRect(80, 270, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save_data.setFont(font)
        self.pushButton_save_data.setStyleSheet("#pushButton_save_data{\n"
                                                "background-color: rgb(121, 195, 208);\n"
                                                "border-radius : 15px;\n"
                                                "}\n"
                                                "#pushButton_save_data:hover{\n"
                                                "background-color: rgb(121, 195, 255);\n"
                                                "}")
        self.pushButton_save_data.setObjectName("pushButton_save_data")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tarih :"))
        self.lineEdit_Date.setPlaceholderText(_translate("MainWindow", "(yyyy-mm-dd)"))
        self.label_2.setText(_translate("MainWindow", "Algoritma :"))
        self.comboBox_Algo.setItemText(0, _translate("MainWindow", "Prophet Algoritması"))
        self.comboBox_Algo.setItemText(1, _translate("MainWindow", "Gaussian Distribution"))
        self.comboBox_Algo.setItemText(2, _translate("MainWindow", "OpenSVM Methodu"))
        self.comboBox_Algo.setItemText(3, _translate("MainWindow", "Twitter Algoritması"))
        self.comboBox_test.setItemText(0, _translate("MainWindow", "pH"))
        self.comboBox_test.setItemText(1, _translate("MainWindow", "Oksijen"))
        self.comboBox_test.setItemText(2, _translate("MainWindow", "Clor"))
        self.comboBox_test.setItemText(3, _translate("MainWindow", "Bulanıklık"))
        self.pushButton_test.setText(_translate("MainWindow", "TEST"))
        self.label_3.setText(_translate("MainWindow", "Sonuç :"))
        self.label_Result.setText(_translate("MainWindow",
                                             "Son güne ait pH verisinde"
                                             " anomaly tespit edilmedi"))
        self.label_4.setText(_translate("MainWindow", "Grafik :"))
        self.pushButton_save_data.setText(_translate("MainWindow", "KAYDET"))
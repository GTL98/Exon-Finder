# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\tela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 240)
        Form.setMinimumSize(QtCore.QSize(780, 240))
        Form.setMaximumSize(QtCore.QSize(800, 240))
        Form.setStyleSheet("QLineEdit#linha_caminho, #linha_nome_arquivo, #linha_id_seq{\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: black\n"
"}\n"
"QLineEdit#linha_caminho:hover, #linha_nome_arquivo:hover, #linha_id_seq:hover{\n"
"background-color: rgba(147, 207, 230, 100)\n"
"}\n"
"\n"
"QPushButton#botao_ajuda{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border-radius: 10px\n"
"}\n"
"QPushButton#botao_ajuda:hover{\n"
"background-color: rgba(145, 207, 230, 100);\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"border-color:  rgba(147, 207, 230, 255)\n"
"}\n"
"QPushButton#botao_ajuda:pressed{\n"
"background-color: rgba(145, 207, 230, 150);\n"
"border-width: 2px;\n"
"border-style: inset;\n"
"border-color: rgba(145, 207, 230, 255)\n"
"}\n"
"\n"
"QPushButton#botao_escolher, #botao_salvar, #botao_pesquisar, #botao_pasta{\n"
"background-color: rgba(200, 200, 200, 100);\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"border-color: rgba(145, 207, 230, 255)\n"
"}\n"
"QPushButton#botao_escolher:hover, #botao_salvar:hover, #botao_pesquisar:hover,\n"
"#botao_pasta:hover{\n"
"background-color: rgba(147, 207, 230, 100)\n"
"}\n"
"QPushButton#botao_escolher:pressed, #botao_salvar:pressed, #botao_pesquisar:pressed,\n"
"#botao_pasta:pressed{\n"
"background-color: rgba(145, 207, 230, 150);\n"
"border-width: 2px;\n"
"border-style: inset;\n"
"border-color: rgba(145, 207, 230, 255)\n"
"}")
        self.botao_ajuda = QtWidgets.QPushButton(Form)
        self.botao_ajuda.setGeometry(QtCore.QRect(760, 5, 31, 31))
        self.botao_ajuda.setMinimumSize(QtCore.QSize(31, 31))
        self.botao_ajuda.setMaximumSize(QtCore.QSize(31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.botao_ajuda.setFont(font)
        self.botao_ajuda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_ajuda.setStyleSheet("")
        self.botao_ajuda.setObjectName("botao_ajuda")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(665, 210, 123, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.botao_versao = QtWidgets.QPushButton(Form)
        self.botao_versao.setGeometry(QtCore.QRect(660, 210, 131, 23))
        self.botao_versao.setMinimumSize(QtCore.QSize(131, 23))
        self.botao_versao.setMaximumSize(QtCore.QSize(131, 23))
        self.botao_versao.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_versao.setStyleSheet("background-color:rgba(0, 0, 0, 0)")
        self.botao_versao.setText("")
        self.botao_versao.setObjectName("botao_versao")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 161, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo/2770972_png.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 20, 605, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.linha_id_seq = QtWidgets.QLineEdit(self.layoutWidget1)
        self.linha_id_seq.setMinimumSize(QtCore.QSize(0, 31))
        self.linha_id_seq.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.linha_id_seq.setFont(font)
        self.linha_id_seq.setObjectName("linha_id_seq")
        self.horizontalLayout.addWidget(self.linha_id_seq)
        self.botao_pesquisar = QtWidgets.QPushButton(self.layoutWidget1)
        self.botao_pesquisar.setMinimumSize(QtCore.QSize(121, 41))
        self.botao_pesquisar.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.botao_pesquisar.setFont(font)
        self.botao_pesquisar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icones/active-search-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_pesquisar.setIcon(icon)
        self.botao_pesquisar.setObjectName("botao_pesquisar")
        self.horizontalLayout.addWidget(self.botao_pesquisar)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.linha_caminho = QtWidgets.QLineEdit(self.layoutWidget1)
        self.linha_caminho.setMinimumSize(QtCore.QSize(301, 31))
        self.linha_caminho.setMaximumSize(QtCore.QSize(301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.linha_caminho.setFont(font)
        self.linha_caminho.setObjectName("linha_caminho")
        self.horizontalLayout_2.addWidget(self.linha_caminho)
        self.botao_pasta = QtWidgets.QPushButton(self.layoutWidget1)
        self.botao_pasta.setMinimumSize(QtCore.QSize(41, 41))
        self.botao_pasta.setMaximumSize(QtCore.QSize(41, 41))
        self.botao_pasta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_pasta.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icones/folder-horizontal-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_pasta.setIcon(icon1)
        self.botao_pasta.setObjectName("botao_pasta")
        self.horizontalLayout_2.addWidget(self.botao_pasta)
        self.botao_salvar = QtWidgets.QPushButton(self.layoutWidget1)
        self.botao_salvar.setMinimumSize(QtCore.QSize(121, 41))
        self.botao_salvar.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.botao_salvar.setFont(font)
        self.botao_salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icones/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_salvar.setIcon(icon2)
        self.botao_salvar.setObjectName("botao_salvar")
        self.horizontalLayout_2.addWidget(self.botao_salvar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.botao_ajuda.setText(_translate("Form", "?"))
        self.label_5.setText(_translate("Form", "Vers??o 2.0.0"))
        self.label_2.setText(_translate("Form", "Exon\n"
"Finder"))
        self.label_6.setText(_translate("Form", "ID sequ??ncia:"))
        self.botao_pesquisar.setText(_translate("Form", "Pesquisar"))
        self.label_3.setText(_translate("Form", "Salvar em:"))
        self.botao_salvar.setText(_translate("Form", "Salvar"))

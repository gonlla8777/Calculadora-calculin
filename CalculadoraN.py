# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(341, 462)
        Form.setStyleSheet("background-color: rgb(117, 172, 255);")
        self.boton_uno = QtWidgets.QPushButton(Form)
        self.boton_uno.setGeometry(QtCore.QRect(6, 110, 75, 23))
        self.boton_uno.setObjectName("boton_uno")
        self.boton_dos = QtWidgets.QPushButton(Form)
        self.boton_dos.setGeometry(QtCore.QRect(90, 110, 75, 23))
        self.boton_dos.setObjectName("boton_dos")
        self.boton_tres = QtWidgets.QPushButton(Form)
        self.boton_tres.setGeometry(QtCore.QRect(174, 110, 75, 23))
        self.boton_tres.setObjectName("boton_tres")
        self.boton_parentesis_iz = QtWidgets.QPushButton(Form)
        self.boton_parentesis_iz.setGeometry(QtCore.QRect(257, 110, 75, 23))
        self.boton_parentesis_iz.setObjectName("boton_parentesis_iz")
        self.boton_parentesis_de = QtWidgets.QPushButton(Form)
        self.boton_parentesis_de.setGeometry(QtCore.QRect(257, 166, 75, 23))
        self.boton_parentesis_de.setObjectName("boton_parentesis_de")
        self.boton_cuatro = QtWidgets.QPushButton(Form)
        self.boton_cuatro.setGeometry(QtCore.QRect(6, 166, 75, 23))
        self.boton_cuatro.setObjectName("boton_cuatro")
        self.boton_seis = QtWidgets.QPushButton(Form)
        self.boton_seis.setGeometry(QtCore.QRect(174, 166, 75, 23))
        self.boton_seis.setObjectName("boton_seis")
        self.boton_cinco = QtWidgets.QPushButton(Form)
        self.boton_cinco.setGeometry(QtCore.QRect(90, 166, 75, 23))
        self.boton_cinco.setObjectName("boton_cinco")
        self.boton_decimal = QtWidgets.QPushButton(Form)
        self.boton_decimal.setGeometry(QtCore.QRect(257, 222, 75, 23))
        self.boton_decimal.setObjectName("boton_decimal")
        self.boton_siete = QtWidgets.QPushButton(Form)
        self.boton_siete.setGeometry(QtCore.QRect(6, 222, 75, 23))
        self.boton_siete.setObjectName("boton_siete")
        self.boton_nueve = QtWidgets.QPushButton(Form)
        self.boton_nueve.setGeometry(QtCore.QRect(174, 222, 75, 23))
        self.boton_nueve.setObjectName("boton_nueve")
        self.boton_ocho = QtWidgets.QPushButton(Form)
        self.boton_ocho.setGeometry(QtCore.QRect(90, 222, 75, 23))
        self.boton_ocho.setObjectName("boton_ocho")
        self.boton_suma = QtWidgets.QPushButton(Form)
        self.boton_suma.setGeometry(QtCore.QRect(6, 278, 75, 23))
        self.boton_suma.setObjectName("boton_suma")
        self.boton_borrar_todo = QtWidgets.QPushButton(Form)
        self.boton_borrar_todo.setGeometry(QtCore.QRect(174, 278, 75, 23))
        self.boton_borrar_todo.setObjectName("boton_borrar_todo")
        self.boton_cero = QtWidgets.QPushButton(Form)
        self.boton_cero.setGeometry(QtCore.QRect(90, 278, 75, 23))
        self.boton_cero.setObjectName("boton_cero")
        self.boton_igual = QtWidgets.QPushButton(Form)
        self.boton_igual.setGeometry(QtCore.QRect(257, 276, 75, 81))
        self.boton_igual.setObjectName("boton_igual")
        self.boton_multiplicar = QtWidgets.QPushButton(Form)
        self.boton_multiplicar.setGeometry(QtCore.QRect(6, 334, 75, 23))
        self.boton_multiplicar.setObjectName("boton_multiplicar")
        self.boton_borrar_2 = QtWidgets.QPushButton(Form)
        self.boton_borrar_2.setGeometry(QtCore.QRect(174, 334, 75, 23))
        self.boton_borrar_2.setObjectName("boton_borrar_2")
        self.boton_dividir = QtWidgets.QPushButton(Form)
        self.boton_dividir.setGeometry(QtCore.QRect(90, 334, 75, 23))
        self.boton_dividir.setObjectName("boton_dividir")
        self.boton_salir = QtWidgets.QPushButton(Form)
        self.boton_salir.setGeometry(QtCore.QRect(174, 390, 151, 61))
        self.boton_salir.setObjectName("boton_salir")
        self.boton_resta = QtWidgets.QPushButton(Form)
        self.boton_resta.setGeometry(QtCore.QRect(6, 390, 75, 23))
        self.boton_resta.setObjectName("boton_resta")
        self.boton_porcentaje = QtWidgets.QPushButton(Form)
        self.boton_porcentaje.setGeometry(QtCore.QRect(90, 390, 75, 23))
        self.boton_porcentaje.setObjectName("boton_porcentaje")
        self.valor = QtWidgets.QLabel(Form)
        self.valor.setGeometry(QtCore.QRect(20, 20, 311, 61))
        self.valor.setStyleSheet("background-color: rgb(141, 141, 141);\n"
"border-top-color: rgb(255, 255, 255);")
        self.valor.setText("")
        self.valor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.valor.setObjectName("valor")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 311, 61))
        self.label_2.setStyleSheet("background-color: rgb(141, 141, 141);\n"
"border-top-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.boton_potencia = QtWidgets.QPushButton(Form)
        self.boton_potencia.setGeometry(QtCore.QRect(90, 430, 75, 23))
        self.boton_potencia.setObjectName("boton_potencia")
        self.boton_raiz = QtWidgets.QPushButton(Form)
        self.boton_raiz.setGeometry(QtCore.QRect(6, 430, 75, 23))
        self.boton_raiz.setObjectName("boton_raiz")
        self.label_2.raise_()
        self.boton_uno.raise_()
        self.boton_dos.raise_()
        self.boton_tres.raise_()
        self.boton_parentesis_iz.raise_()
        self.boton_parentesis_de.raise_()
        self.boton_cuatro.raise_()
        self.boton_seis.raise_()
        self.boton_cinco.raise_()
        self.boton_decimal.raise_()
        self.boton_siete.raise_()
        self.boton_nueve.raise_()
        self.boton_ocho.raise_()
        self.boton_suma.raise_()
        self.boton_borrar_todo.raise_()
        self.boton_cero.raise_()
        self.boton_igual.raise_()
        self.boton_multiplicar.raise_()
        self.boton_borrar_2.raise_()
        self.boton_dividir.raise_()
        self.boton_salir.raise_()
        self.boton_resta.raise_()
        self.boton_porcentaje.raise_()
        self.valor.raise_()
        self.boton_potencia.raise_()
        self.boton_raiz.raise_()

        self.retranslateUi(Form)
        self.boton_borrar_todo.clicked.connect(self.valor.clear)
        self.boton_salir.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.boton_uno.setText(_translate("Form", "1"))
        self.boton_uno.setShortcut(_translate("Form", "1"))
        self.boton_dos.setText(_translate("Form", "2"))
        self.boton_dos.setShortcut(_translate("Form", "2"))
        self.boton_tres.setText(_translate("Form", "3"))
        self.boton_tres.setShortcut(_translate("Form", "3"))
        self.boton_parentesis_iz.setText(_translate("Form", "("))
        self.boton_parentesis_iz.setShortcut(_translate("Form", "("))
        self.boton_parentesis_de.setText(_translate("Form", ")"))
        self.boton_parentesis_de.setShortcut(_translate("Form", ")"))
        self.boton_cuatro.setText(_translate("Form", "4"))
        self.boton_cuatro.setShortcut(_translate("Form", "4"))
        self.boton_seis.setText(_translate("Form", "6"))
        self.boton_seis.setShortcut(_translate("Form", "6"))
        self.boton_cinco.setText(_translate("Form", "5"))
        self.boton_cinco.setShortcut(_translate("Form", "5"))
        self.boton_decimal.setText(_translate("Form", "."))
        self.boton_decimal.setShortcut(_translate("Form", "."))
        self.boton_siete.setText(_translate("Form", "7"))
        self.boton_siete.setShortcut(_translate("Form", "7"))
        self.boton_nueve.setText(_translate("Form", "9"))
        self.boton_nueve.setShortcut(_translate("Form", "9"))
        self.boton_ocho.setText(_translate("Form", "8"))
        self.boton_ocho.setShortcut(_translate("Form", "8"))
        self.boton_suma.setText(_translate("Form", "+"))
        self.boton_suma.setShortcut(_translate("Form", "+"))
        self.boton_borrar_todo.setText(_translate("Form", "C"))
        self.boton_borrar_todo.setShortcut(_translate("Form", "Esc, Backspace"))
        self.boton_cero.setText(_translate("Form", "0"))
        self.boton_cero.setShortcut(_translate("Form", "0"))
        self.boton_igual.setText(_translate("Form", "="))
        self.boton_igual.setShortcut(_translate("Form", "Enter, Return"))
        self.boton_multiplicar.setText(_translate("Form", "X"))
        self.boton_multiplicar.setShortcut(_translate("Form", "*"))
        self.boton_borrar_2.setText(_translate("Form", "AC"))
        self.boton_dividir.setText(_translate("Form", "/"))
        self.boton_dividir.setShortcut(_translate("Form", "/"))
        self.boton_salir.setText(_translate("Form", "SALIR"))
        self.boton_resta.setText(_translate("Form", "-"))
        self.boton_resta.setShortcut(_translate("Form", "-"))
        self.boton_porcentaje.setText(_translate("Form", "%"))
        self.boton_porcentaje.setShortcut(_translate("Form", "%"))
        self.boton_potencia.setText(_translate("Form", "^"))
        self.boton_potencia.setShortcut(_translate("Form", "P"))
        self.boton_raiz.setText(_translate("Form", "???"))
        self.boton_raiz.setShortcut(_translate("Form", "R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

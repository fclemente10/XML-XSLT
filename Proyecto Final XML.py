#!/usr/bin/python
# -*- coding: latin-1 -*-
import os
import webbrowser
from hashlib import new
from builtins import str
import xmlschema
import easygui
import lxml.etree as ET

from PyQt5 import QtWidgets

'''
dom = ET.parse('Rangers.xml')
xslt = ET.parse('StiloSoccer.xslt')
transform = ET.XSLT(xslt)
newdom = transform(dom)
print(ET.tostring(newdom, pretty_print=True))
f = open('Rangers.html', 'w')
print >> f, (ET.tostring(newdom, pretty_print=True))
'''

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog, QFileDialog, QFormLayout, QLabel, \
    QLineEdit, QGroupBox, QComboBox, QSpinBox, QVBoxLayout, QWidget, QRadioButton
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QtWidgets.QMainWindow):

    def __init__(self, dom='', xslt='', Namefile='...', Namefile2='...', type='xml'):

        super().__init__()

        self.dom = dom
        self.xslt = xslt
        self.Namefile = Namefile
        self.Namefile2 = Namefile2
        self.type = type

        self.top = 100
        self.left = 100
        self.wigth = 1200
        self.hight = 600
        self.title = "Proyecto Final XML - Universidad de Alicante"

        self.labelXMLFile = QLabel(self)
        self.labelXMLFile.setText(self.Namefile)
        self.labelXMLFile.setStyleSheet('QLabel {font:bold;font-size:20px}')
        self.labelXMLFile.move(300, 47)
        self.labelXMLFile.resize(1000, 60)

        self.labelXSLTFile = QLabel(self)
        self.labelXSLTFile.setText(self.Namefile2)
        self.labelXSLTFile.setStyleSheet('QLabel {font:bold;font-size:20px}')
        self.labelXSLTFile.move(300, 145)
        self.labelXSLTFile.resize(1000, 60)

        self.btnLoadXML = QPushButton('Cargar XML', self)
        self.btnLoadXML.move(50, 25)
        self.btnLoadXML.resize(180, 60)
        self.btnLoadXML.setStyleSheet('QPushButton {background-color:#0FB328;font:bold;font-size:20px}')
        self.btnLoadXML.clicked.connect(self.btnLoadXML_click)

        self.btnLoadXSLT = QPushButton('Cargar XSLT', self)
        self.btnLoadXSLT.move(50, 125)
        self.btnLoadXSLT.resize(180, 60)
        self.btnLoadXSLT.setStyleSheet('QPushButton {background-color:#20ABFA;font:bold;font-size:20px}')
        self.btnLoadXSLT.clicked.connect(self.btnLoadXSLT_click)

        self.btnConvert = QPushButton('Procesar Archivos', self)
        self.btnConvert.move(440, 300)
        self.btnConvert.resize(200, 60)
        self.btnConvert.setStyleSheet('QPushButton {background-color:#D2A1F0;font:bold;font-size:20px}')
        self.btnConvert.clicked.connect(self.btnConvert_click)

        self.labelXML = QLabel('File: ', self)
        self.labelXML.setStyleSheet('QLabel {font:bold;font-size:20px}')
        self.labelXML.move(250, 60)

        self.labelXSLT = QLabel('File: ', self)
        self.labelXSLT.setStyleSheet('QLabel {font:bold;font-size:20px}')
        self.labelXSLT.move(250, 160)

        self.radioXML = QRadioButton(self)
        self.radioXML.setText("XML")
        self.radioXML.setStyleSheet('QRadioButton {font:bold;font-size:20px}')
        self.radioXML.setChecked(True)
        self.radioXML.toggled.connect(lambda: self.btnstate(self.radioXML))
        self.radioXML.setGeometry(300, 225, 120, 40)

        self.radioHTML = QRadioButton(self)
        self.radioHTML.setText("HTML")
        self.radioHTML.setStyleSheet('QRadioButton {font:bold;font-size:20px}')
        self.radioHTML.setChecked(False)
        self.radioHTML.toggled.connect(lambda: self.btnstate(self.radioHTML))
        self.radioHTML.setGeometry(500, 225, 120, 40)

        self.radioTXT = QRadioButton(self)
        self.radioTXT.setText("TXT")
        self.radioTXT.setStyleSheet('QRadioButton {font:bold;font-size:20px}')
        self.radioTXT.setChecked(False)
        self.radioTXT.toggled.connect(lambda: self.btnstate(self.radioTXT))
        self.radioTXT.setGeometry(700, 225, 120, 40)

        self.LoadWindow()

    def LoadWindow(self):
        self.setGeometry(self.left, self.top, self.wigth, self.hight)
        self.setWindowTitle(self.title)
        self.show()

    def btnLoadXML_click(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "XML Files (*.xml);;All Files (*)", options=options)
        if fileName:
            print(fileName)
            self.Namefile = fileName
            self.labelXMLFile.setText(self.Namefile)
            self.dom = ET.parse(fileName)

        buttonReply = QMessageBox.question(self, 'Verificacion', "Le gustaria validar el Documento con su XSD?", QMessageBox.Yes |
                                           QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileNameXSD, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                      "XSD Files (*.xsd);;All Files (*)", options=options)
            if fileNameXSD:
                print(fileNameXSD)
            try:
                xmlschema.validate(self.dom, fileNameXSD)
                print('You gotta Dude!!')
                QMessageBox.about(self, "Valido", "El Documento está Validado con su XSD")
            except:
                print('So Close, but NOT')
                QMessageBox.about(self, "NO Valido", "El Documento NO está Validado con su XSD")
        else:
            print('No clicked.')

    def btnLoadXSLT_click(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName2, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "XSLT Files (*.xslt *.xsl);;All Files (*)", options=options)
        if fileName2:
            print(fileName2)
            self.Namefile2 = fileName2
            self.labelXSLTFile.setText(self.Namefile2)
            self.xslt = ET.parse(fileName2)

    def btnstate(self, b):

        if b.text() == "XML":
            self.type = 'xml'
            print(" XML Selecionado")

        if b.text() == "HTML":
            self.type = 'html'
            print(" HTML Selecionado")

        if b.text() == "TXT":
            self.type = 'txt'
            print(" TXT Selecionado")

    def btnConvert_click(self):
        try:
            if isinstance(self.Namefile, str) and isinstance(self.Namefile2, str):
                try:
                    transform = ET.XSLT(self.xslt)
                    newdom = transform(self.dom)
                    if self.type == 'html':
                        print(newdom, file=open("Salida.html", "w"))
                        b = os.path.getsize("Salida.html")
                        print(b)

                        if b > 300:
                            url = "Salida.html"
                            webbrowser.open(url, new=new)
                        else:
                            easygui.msgbox("Los archivos no son compatibles", title="Error")

                    if self.type == 'xml':
                        print(newdom, file=open("Salida.xml", "w"))
                        b = os.path.getsize("Salida.xml")
                        print(b)

                        if b > 300:
                            url = "Salida.xml"
                            webbrowser.open(url, new=new)
                        else:
                            easygui.msgbox("Los archivos no son compatibles", title="Error")
                    if self.type == 'txt':
                        print(newdom, file=open("Salida.txt", "w"))
                        b = os.path.getsize("Salida.txt")
                        print(b)

                        if b > 300:
                            url = "Salida.txt"
                            webbrowser.open(url, new=new)
                        else:
                            easygui.msgbox("Los archivos no son compatibles", title="Error")

                except:
                    easygui.msgbox("Los archivos no son compatibles", title="Error")

        except NameError:
            easygui.msgbox("Es necesario anadir los archivos XML y XSL", title="Error")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Window(dom='', xslt='', Namefile='...', Namefile2='...', type='xml')

    sys.exit(app.exec())

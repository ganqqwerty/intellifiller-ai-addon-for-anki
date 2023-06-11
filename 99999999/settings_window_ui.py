# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.setWindowModality(QtCore.Qt.NonModal)
        SettingsWindow.resize(805, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWindow.sizePolicy().hasHeightForWidth())
        SettingsWindow.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelApiKey = QtWidgets.QLabel(SettingsWindow)
        self.labelApiKey.setObjectName("labelApiKey")
        self.verticalLayout.addWidget(self.labelApiKey)
        self.apiKey = QtWidgets.QLineEdit(SettingsWindow)
        self.apiKey.setObjectName("apiKey")
        self.verticalLayout.addWidget(self.apiKey)
        self.labelEmulate = QtWidgets.QLabel(SettingsWindow)
        self.labelEmulate.setObjectName("labelEmulate")
        self.verticalLayout.addWidget(self.labelEmulate)
        self.emulate = QtWidgets.QComboBox(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emulate.sizePolicy().hasHeightForWidth())
        self.emulate.setSizePolicy(sizePolicy)
        self.emulate.setObjectName("emulate")
        self.emulate.addItem("")
        self.emulate.addItem("")
        self.verticalLayout.addWidget(self.emulate)
        self.addPromptButton = QtWidgets.QPushButton(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addPromptButton.sizePolicy().hasHeightForWidth())
        self.addPromptButton.setSizePolicy(sizePolicy)
        self.addPromptButton.setObjectName("addPromptButton")
        self.verticalLayout.addWidget(self.addPromptButton)
        self.scrollArea = QtWidgets.QScrollArea(SettingsWindow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 605))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.promptsLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.promptsLayout.setObjectName("promptsLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.saveButton = QtWidgets.QPushButton(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton, 0, QtCore.Qt.AlignRight)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "IntelliFiller Settings"))
        self.labelApiKey.setText(_translate("SettingsWindow", "API Key:"))
        self.apiKey.setPlaceholderText(_translate("SettingsWindow", "API key"))
        self.labelEmulate.setText(_translate("SettingsWindow", "Emulate:"))
        self.emulate.setItemText(0, _translate("SettingsWindow", "yes"))
        self.emulate.setItemText(1, _translate("SettingsWindow", "no"))
        self.addPromptButton.setText(_translate("SettingsWindow", "Add Prompt"))
        self.saveButton.setText(_translate("SettingsWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QDialog()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'csv2vector_dialog_view.ui'
#
# Created: Tue Sep 03 16:30:06 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(511, 406)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setAcceptDrops(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 50))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.attrXCoordComboBox = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attrXCoordComboBox.sizePolicy().hasHeightForWidth())
        self.attrXCoordComboBox.setSizePolicy(sizePolicy)
        self.attrXCoordComboBox.setObjectName(_fromUtf8("attrXCoordComboBox"))
        self.gridLayout.addWidget(self.attrXCoordComboBox, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.attrYCoordComboBox = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attrYCoordComboBox.sizePolicy().hasHeightForWidth())
        self.attrYCoordComboBox.setSizePolicy(sizePolicy)
        self.attrYCoordComboBox.setObjectName(_fromUtf8("attrYCoordComboBox"))
        self.gridLayout.addWidget(self.attrYCoordComboBox, 0, 4, 1, 1)
        self.attrDistCoordComboBox = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attrDistCoordComboBox.sizePolicy().hasHeightForWidth())
        self.attrDistCoordComboBox.setSizePolicy(sizePolicy)
        self.attrDistCoordComboBox.setObjectName(_fromUtf8("attrDistCoordComboBox"))
        self.gridLayout.addWidget(self.attrDistCoordComboBox, 1, 4, 1, 1)
        self.attrAzCoordComboBox = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attrAzCoordComboBox.sizePolicy().hasHeightForWidth())
        self.attrAzCoordComboBox.setSizePolicy(sizePolicy)
        self.attrAzCoordComboBox.setObjectName(_fromUtf8("attrAzCoordComboBox"))
        self.gridLayout.addWidget(self.attrAzCoordComboBox, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 4, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.delimiterSpaceRadioButton = QtGui.QRadioButton(self.groupBox_3)
        self.delimiterSpaceRadioButton.setObjectName(_fromUtf8("delimiterSpaceRadioButton"))
        self.gridLayout_5.addWidget(self.delimiterSpaceRadioButton, 2, 0, 1, 1)
        self.delimiterTabRadioButton = QtGui.QRadioButton(self.groupBox_3)
        self.delimiterTabRadioButton.setCheckable(True)
        self.delimiterTabRadioButton.setChecked(False)
        self.delimiterTabRadioButton.setObjectName(_fromUtf8("delimiterTabRadioButton"))
        self.gridLayout_5.addWidget(self.delimiterTabRadioButton, 1, 0, 1, 1)
        self.delimiterCommaRadioButton = QtGui.QRadioButton(self.groupBox_3)
        self.delimiterCommaRadioButton.setObjectName(_fromUtf8("delimiterCommaRadioButton"))
        self.gridLayout_5.addWidget(self.delimiterCommaRadioButton, 1, 1, 1, 1)
        self.delimiterSemicolonRadioButton = QtGui.QRadioButton(self.groupBox_3)
        self.delimiterSemicolonRadioButton.setObjectName(_fromUtf8("delimiterSemicolonRadioButton"))
        self.gridLayout_5.addWidget(self.delimiterSemicolonRadioButton, 2, 1, 1, 1)
        self.delimiterColonRadioButton = QtGui.QRadioButton(self.groupBox_3)
        self.delimiterColonRadioButton.setObjectName(_fromUtf8("delimiterColonRadioButton"))
        self.gridLayout_5.addWidget(self.delimiterColonRadioButton, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 8, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.selectCSVFileButton = QtGui.QPushButton(Dialog)
        self.selectCSVFileButton.setObjectName(_fromUtf8("selectCSVFileButton"))
        self.gridLayout_2.addWidget(self.selectCSVFileButton, 0, 2, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.csvFileEdit = QtGui.QLineEdit(Dialog)
        self.csvFileEdit.setReadOnly(True)
        self.csvFileEdit.setObjectName(_fromUtf8("csvFileEdit"))
        self.gridLayout_2.addWidget(self.csvFileEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.shpFileEdit = QtGui.QLineEdit(Dialog)
        self.shpFileEdit.setReadOnly(True)
        self.shpFileEdit.setObjectName(_fromUtf8("shpFileEdit"))
        self.gridLayout_2.addWidget(self.shpFileEdit, 1, 1, 1, 1)
        self.selectSHPFileButton = QtGui.QPushButton(Dialog)
        self.selectSHPFileButton.setObjectName(_fromUtf8("selectSHPFileButton"))
        self.gridLayout_2.addWidget(self.selectSHPFileButton, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "CSV2Vector", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "The found attributes:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Parameters:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Latitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Bearing:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Distance:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Longitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "Delimiter:", None, QtGui.QApplication.UnicodeUTF8))
        self.delimiterSpaceRadioButton.setText(QtGui.QApplication.translate("Dialog", "Space", None, QtGui.QApplication.UnicodeUTF8))
        self.delimiterTabRadioButton.setText(QtGui.QApplication.translate("Dialog", "Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.delimiterCommaRadioButton.setText(QtGui.QApplication.translate("Dialog", "Comma", None, QtGui.QApplication.UnicodeUTF8))
        self.delimiterSemicolonRadioButton.setText(QtGui.QApplication.translate("Dialog", "Semicolon", None, QtGui.QApplication.UnicodeUTF8))
        self.delimiterColonRadioButton.setText(QtGui.QApplication.translate("Dialog", "Colon", None, QtGui.QApplication.UnicodeUTF8))
        self.selectCSVFileButton.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "CSV File:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Output shp:", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSHPFileButton.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))


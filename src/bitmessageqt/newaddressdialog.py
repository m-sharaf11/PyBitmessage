# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newaddressdialog.ui'
#
# Created: Sun Sep 15 23:53:31 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NewAddressDialog(object):
    def setupUi(self, NewAddressDialog):
        NewAddressDialog.setObjectName(_fromUtf8("NewAddressDialog"))
        NewAddressDialog.resize(723, 704)
        self.formLayout = QtGui.QFormLayout(NewAddressDialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(NewAddressDialog)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label)
        self.label_5 = QtGui.QLabel(NewAddressDialog)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.label_5)
        self.line = QtGui.QFrame(NewAddressDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(100, 2))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.line)
        self.radioButtonRandomAddress = QtGui.QRadioButton(NewAddressDialog)
        self.radioButtonRandomAddress.setChecked(True)
        self.radioButtonRandomAddress.setObjectName(_fromUtf8("radioButtonRandomAddress"))
        self.buttonGroup = QtGui.QButtonGroup(NewAddressDialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.radioButtonRandomAddress)
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.radioButtonRandomAddress)
        self.radioButtonDeterministicAddress = QtGui.QRadioButton(NewAddressDialog)
        self.radioButtonDeterministicAddress.setObjectName(_fromUtf8("radioButtonDeterministicAddress"))
        self.buttonGroup.addButton(self.radioButtonDeterministicAddress)
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.radioButtonDeterministicAddress)
        self.checkBoxEighteenByteRipe = QtGui.QCheckBox(NewAddressDialog)
        self.checkBoxEighteenByteRipe.setObjectName(_fromUtf8("checkBoxEighteenByteRipe"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.SpanningRole, self.checkBoxEighteenByteRipe)
        self.groupBoxDeterministic = QtGui.QGroupBox(NewAddressDialog)
        self.groupBoxDeterministic.setObjectName(_fromUtf8("groupBoxDeterministic"))
        self.gridLayout = QtGui.QGridLayout(self.groupBoxDeterministic)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_9 = QtGui.QLabel(self.groupBoxDeterministic)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBoxDeterministic)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 3)
        self.spinBoxNumberOfAddressesToMake = QtGui.QSpinBox(self.groupBoxDeterministic)
        self.spinBoxNumberOfAddressesToMake.setMinimum(1)
        self.spinBoxNumberOfAddressesToMake.setProperty("value", 8)
        self.spinBoxNumberOfAddressesToMake.setObjectName(_fromUtf8("spinBoxNumberOfAddressesToMake"))
        self.gridLayout.addWidget(self.spinBoxNumberOfAddressesToMake, 4, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBoxDeterministic)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBoxDeterministic)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(73, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBoxDeterministic)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 6, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(42, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBoxDeterministic)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEditPassphraseAgain = QtGui.QLineEdit(self.groupBoxDeterministic)
        self.lineEditPassphraseAgain.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassphraseAgain.setObjectName(_fromUtf8("lineEditPassphraseAgain"))
        self.gridLayout.addWidget(self.lineEditPassphraseAgain, 3, 0, 1, 4)
        self.lineEditPassphrase = QtGui.QLineEdit(self.groupBoxDeterministic)
        self.lineEditPassphrase.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.lineEditPassphrase.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassphrase.setObjectName(_fromUtf8("lineEditPassphrase"))
        self.gridLayout.addWidget(self.lineEditPassphrase, 1, 0, 1, 4)
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.groupBoxDeterministic)
        self.groupBox = QtGui.QGroupBox(NewAddressDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)
        self.newaddresslabel = QtGui.QLineEdit(self.groupBox)
        self.newaddresslabel.setObjectName(_fromUtf8("newaddresslabel"))
        self.gridLayout_2.addWidget(self.newaddresslabel, 1, 0, 1, 2)
        self.radioButtonMostAvailable = QtGui.QRadioButton(self.groupBox)
        self.radioButtonMostAvailable.setChecked(True)
        self.radioButtonMostAvailable.setObjectName(_fromUtf8("radioButtonMostAvailable"))
        self.gridLayout_2.addWidget(self.radioButtonMostAvailable, 2, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 3, 1, 1, 1)
        self.radioButtonExisting = QtGui.QRadioButton(self.groupBox)
        self.radioButtonExisting.setChecked(False)
        self.radioButtonExisting.setObjectName(_fromUtf8("radioButtonExisting"))
        self.gridLayout_2.addWidget(self.radioButtonExisting, 4, 0, 1, 2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 5, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 6, 0, 1, 1)
        self.comboBoxExisting = QtGui.QComboBox(self.groupBox)
        self.comboBoxExisting.setEnabled(False)
        self.comboBoxExisting.setEditable(True)
        self.comboBoxExisting.setObjectName(_fromUtf8("comboBoxExisting"))
        self.gridLayout_2.addWidget(self.comboBoxExisting, 6, 1, 1, 1)
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(NewAddressDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QtCore.QSize(160, 0))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(NewAddressDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewAddressDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewAddressDialog.reject)
        QtCore.QObject.connect(self.radioButtonExisting, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.comboBoxExisting.setEnabled)
        QtCore.QObject.connect(self.radioButtonDeterministicAddress, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBoxDeterministic.setShown)
        QtCore.QObject.connect(self.radioButtonRandomAddress, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox.setShown)
        QtCore.QMetaObject.connectSlotsByName(NewAddressDialog)
        NewAddressDialog.setTabOrder(self.radioButtonRandomAddress, self.radioButtonDeterministicAddress)
        NewAddressDialog.setTabOrder(self.radioButtonDeterministicAddress, self.newaddresslabel)
        NewAddressDialog.setTabOrder(self.newaddresslabel, self.radioButtonMostAvailable)
        NewAddressDialog.setTabOrder(self.radioButtonMostAvailable, self.radioButtonExisting)
        NewAddressDialog.setTabOrder(self.radioButtonExisting, self.comboBoxExisting)
        NewAddressDialog.setTabOrder(self.comboBoxExisting, self.lineEditPassphrase)
        NewAddressDialog.setTabOrder(self.lineEditPassphrase, self.lineEditPassphraseAgain)
        NewAddressDialog.setTabOrder(self.lineEditPassphraseAgain, self.spinBoxNumberOfAddressesToMake)
        NewAddressDialog.setTabOrder(self.spinBoxNumberOfAddressesToMake, self.checkBoxEighteenByteRipe)
        NewAddressDialog.setTabOrder(self.checkBoxEighteenByteRipe, self.buttonBox)

    def retranslateUi(self, NewAddressDialog):
        NewAddressDialog.setWindowTitle(_translate("NewAddressDialog", "Create new Address", None))
        self.label.setText(_translate("NewAddressDialog", "Here you may generate as many addresses as you like. Indeed, creating and abandoning addresses is encouraged. You may generate addresses by using either random numbers or by using a passphrase. If you use a passphrase, the address is called a \"deterministic\" address.\n"
"The \'Random Number\' option is selected by default but deterministic addresses have several pros and cons:", None))
        self.label_5.setText(_translate("NewAddressDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Pros:<br/></span>You can recreate your addresses on any computer from memory. <br/>You need-not worry about backing up your keys.dat file as long as you can remember your passphrase. <br/><span style=\" font-weight:600;\">Cons:<br/></span>You must remember (or write down) your passphrase if you expect to be able to recreate your keys if they are lost. <br/>You must remember the address version number and the stream number along with your passphrase. <br/>If you choose a weak passphrase and someone on the Internet can brute-force it, they can read your messages and send messages as you.</p></body></html>", None))
        self.radioButtonRandomAddress.setText(_translate("NewAddressDialog", "Use a random number generator to make an address", None))
        self.radioButtonDeterministicAddress.setText(_translate("NewAddressDialog", "Use a passphrase to make addresses", None))
        self.checkBoxEighteenByteRipe.setText(_translate("NewAddressDialog", "Spend several minutes of extra computing time to make the address(es) 1 or 2 characters shorter", None))
        self.groupBoxDeterministic.setTitle(_translate("NewAddressDialog", "Make deterministic addresses", None))
        self.label_9.setText(_translate("NewAddressDialog", "Address version number: 4", None))
        self.label_8.setText(_translate("NewAddressDialog", "In addition to your passphrase, you must remember these numbers:", None))
        self.label_6.setText(_translate("NewAddressDialog", "Passphrase", None))
        self.label_11.setText(_translate("NewAddressDialog", "Number of addresses to make based on your passphrase:", None))
        self.label_10.setText(_translate("NewAddressDialog", "Stream number: 1", None))
        self.label_7.setText(_translate("NewAddressDialog", "Retype passphrase", None))
        self.groupBox.setTitle(_translate("NewAddressDialog", "Randomly generate address", None))
        self.label_2.setText(_translate("NewAddressDialog", "Label (not shown to anyone except you)", None))
        self.radioButtonMostAvailable.setText(_translate("NewAddressDialog", "Use the most available stream", None))
        self.label_3.setText(_translate("NewAddressDialog", " (best if this is the first of many addresses you will create)", None))
        self.radioButtonExisting.setText(_translate("NewAddressDialog", "Use the same stream as an existing address", None))
        self.label_4.setText(_translate("NewAddressDialog", "(saves you some bandwidth and processing power)", None))


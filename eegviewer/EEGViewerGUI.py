# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EEGViewer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(685, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_4 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.fileLineEdit1_2 = QtGui.QLineEdit(self.dockWidgetContents)
        self.fileLineEdit1_2.setReadOnly(True)
        self.fileLineEdit1_2.setObjectName(_fromUtf8("fileLineEdit1_2"))
        self.gridLayout_5.addWidget(self.fileLineEdit1_2, 0, 2, 1, 1)
        self.fileLabel1_2 = QtGui.QLabel(self.dockWidgetContents)
        self.fileLabel1_2.setObjectName(_fromUtf8("fileLabel1_2"))
        self.gridLayout_5.addWidget(self.fileLabel1_2, 0, 0, 1, 1)
        self.eeg_channel_combo_box = QtGui.QComboBox(self.dockWidgetContents)
        self.eeg_channel_combo_box.setObjectName(_fromUtf8("eeg_channel_combo_box"))
        self.gridLayout_5.addWidget(self.eeg_channel_combo_box, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionLoad_File = QtGui.QAction(MainWindow)
        self.actionLoad_File.setObjectName(_fromUtf8("actionLoad_File"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionLoad_File)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.fileLineEdit1_2.setText(_translate("MainWindow", "Load a raw EEG file", None))
        self.fileLineEdit1_2.setPlaceholderText(_translate("MainWindow", "Load a .smr file.", None))
        self.fileLabel1_2.setText(_translate("MainWindow", "File 1:", None))
        self.label_2.setText(_translate("MainWindow", "EEG Channel", None))
        self.actionLoad_File.setText(_translate("MainWindow", "Load File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

from pyqtgraph import GraphicsLayoutWidget

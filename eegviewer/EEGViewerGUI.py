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
        MainWindow.resize(877, 839)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.graphicsView = GraphicsLayoutWidget(self.tab)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.graphicsView_2 = GraphicsLayoutWidget(self.tab_2)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.gridLayout_8.addWidget(self.graphicsView_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 19))
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
        self.groupBox_2 = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.fileLineEdit1_3 = QtGui.QLineEdit(self.groupBox_2)
        self.fileLineEdit1_3.setReadOnly(True)
        self.fileLineEdit1_3.setObjectName(_fromUtf8("fileLineEdit1_3"))
        self.gridLayout_6.addWidget(self.fileLineEdit1_3, 0, 2, 1, 1)
        self.fileLabel1_3 = QtGui.QLabel(self.groupBox_2)
        self.fileLabel1_3.setObjectName(_fromUtf8("fileLabel1_3"))
        self.gridLayout_6.addWidget(self.fileLabel1_3, 0, 0, 1, 1)
        self.eeg_channel_combo_box = QtGui.QComboBox(self.groupBox_2)
        self.eeg_channel_combo_box.setObjectName(_fromUtf8("eeg_channel_combo_box"))
        self.gridLayout_6.addWidget(self.eeg_channel_combo_box, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_6.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_7.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_7.addWidget(self.label_6, 1, 0, 1, 1)
        self.fileLineEdit1_4 = QtGui.QLineEdit(self.groupBox_3)
        self.fileLineEdit1_4.setReadOnly(True)
        self.fileLineEdit1_4.setObjectName(_fromUtf8("fileLineEdit1_4"))
        self.gridLayout_7.addWidget(self.fileLineEdit1_4, 0, 2, 1, 1)
        self.fileLabel1_4 = QtGui.QLabel(self.groupBox_3)
        self.fileLabel1_4.setObjectName(_fromUtf8("fileLabel1_4"))
        self.gridLayout_7.addWidget(self.fileLabel1_4, 0, 0, 1, 1)
        self.epoch_tmin_spinbox = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.epoch_tmin_spinbox.setMinimum(-1.0)
        self.epoch_tmin_spinbox.setMaximum(1.0)
        self.epoch_tmin_spinbox.setSingleStep(0.01)
        self.epoch_tmin_spinbox.setProperty("value", -0.2)
        self.epoch_tmin_spinbox.setObjectName(_fromUtf8("epoch_tmin_spinbox"))
        self.gridLayout_7.addWidget(self.epoch_tmin_spinbox, 2, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_7.addWidget(self.label_7, 3, 0, 1, 1)
        self.epoch_tmax_spinbox = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.epoch_tmax_spinbox.setMinimum(-1.0)
        self.epoch_tmax_spinbox.setMaximum(5.0)
        self.epoch_tmax_spinbox.setSingleStep(0.01)
        self.epoch_tmax_spinbox.setProperty("value", 0.5)
        self.epoch_tmax_spinbox.setObjectName(_fromUtf8("epoch_tmax_spinbox"))
        self.gridLayout_7.addWidget(self.epoch_tmax_spinbox, 3, 2, 1, 1)
        self.epoch_channel_combo_box = QtGui.QComboBox(self.groupBox_3)
        self.epoch_channel_combo_box.setObjectName(_fromUtf8("epoch_channel_combo_box"))
        self.gridLayout_7.addWidget(self.epoch_channel_combo_box, 1, 2, 1, 1)
        self.epoch_number_spinbox = QtGui.QSpinBox(self.groupBox_3)
        self.epoch_number_spinbox.setObjectName(_fromUtf8("epoch_number_spinbox"))
        self.gridLayout_7.addWidget(self.epoch_number_spinbox, 4, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_7.addWidget(self.label, 4, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.create_epochs_button = QtGui.QPushButton(self.groupBox_3)
        self.create_epochs_button.setObjectName(_fromUtf8("create_epochs_button"))
        self.gridLayout_5.addWidget(self.create_epochs_button, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 1)
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
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Raw EEG Data", None))
        self.fileLineEdit1_3.setText(_translate("MainWindow", "Load a raw EEG file", None))
        self.fileLineEdit1_3.setPlaceholderText(_translate("MainWindow", "Load a .smr file.", None))
        self.fileLabel1_3.setText(_translate("MainWindow", "File 1:", None))
        self.label_3.setText(_translate("MainWindow", "EEG Channel", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Epochs", None))
        self.label_5.setText(_translate("MainWindow", "Epoch TMin: ", None))
        self.label_6.setText(_translate("MainWindow", "EEG Channel", None))
        self.fileLineEdit1_4.setText(_translate("MainWindow", "Load epochs data", None))
        self.fileLineEdit1_4.setPlaceholderText(_translate("MainWindow", "Load a .smr file.", None))
        self.fileLabel1_4.setText(_translate("MainWindow", "File 2:", None))
        self.label_7.setText(_translate("MainWindow", "Epoch TMax: ", None))
        self.label.setText(_translate("MainWindow", "Epoch #:", None))
        self.create_epochs_button.setText(_translate("MainWindow", "Create Epochs", None))
        self.actionLoad_File.setText(_translate("MainWindow", "Load File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

from pyqtgraph import GraphicsLayoutWidget

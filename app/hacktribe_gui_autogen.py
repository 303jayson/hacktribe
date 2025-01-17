# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hacktribe-gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 786)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.patch_tab = QtWidgets.QWidget()
        self.patch_tab.setObjectName("patch_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.patch_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.patch_tab)
        self.label.setMaximumSize(QtCore.QSize(16777215, 256))
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_src_path = QtWidgets.QLabel(self.patch_tab)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.label_src_path.setFont(font)
        self.label_src_path.setObjectName("label_src_path")
        self.horizontalLayout.addWidget(self.label_src_path)
        self.edit_src_path = QtWidgets.QLineEdit(self.patch_tab)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.edit_src_path.setFont(font)
        self.edit_src_path.setText("../SYSTEM.VSB")
        self.edit_src_path.setObjectName("edit_src_path")
        self.horizontalLayout.addWidget(self.edit_src_path)
        self.browse_src_path = QtWidgets.QPushButton(self.patch_tab)
        self.browse_src_path.setObjectName("browse_src_path")
        self.horizontalLayout.addWidget(self.browse_src_path)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_patch_path = QtWidgets.QLabel(self.patch_tab)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.label_patch_path.setFont(font)
        self.label_patch_path.setObjectName("label_patch_path")
        self.horizontalLayout_2.addWidget(self.label_patch_path)
        self.edit_patch_path = QtWidgets.QLineEdit(self.patch_tab)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.edit_patch_path.setFont(font)
        self.edit_patch_path.setText("../patch/hacktribe-2.patch")
        self.edit_patch_path.setObjectName("edit_patch_path")
        self.horizontalLayout_2.addWidget(self.edit_patch_path)
        self.browse_patch_path = QtWidgets.QPushButton(self.patch_tab)
        self.browse_patch_path.setObjectName("browse_patch_path")
        self.horizontalLayout_2.addWidget(self.browse_patch_path)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_dest_path = QtWidgets.QLabel(self.patch_tab)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.label_dest_path.setFont(font)
        self.label_dest_path.setObjectName("label_dest_path")
        self.horizontalLayout_3.addWidget(self.label_dest_path)
        self.edit_dest_path = QtWidgets.QLineEdit(self.patch_tab)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.edit_dest_path.setFont(font)
        self.edit_dest_path.setText("..")
        self.edit_dest_path.setObjectName("edit_dest_path")
        self.horizontalLayout_3.addWidget(self.edit_dest_path)
        self.browse_dest_path = QtWidgets.QPushButton(self.patch_tab)
        self.browse_dest_path.setObjectName("browse_dest_path")
        self.horizontalLayout_3.addWidget(self.browse_dest_path)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.check_edit_header = QtWidgets.QCheckBox(self.patch_tab)
        self.check_edit_header.setObjectName("check_edit_header")
        self.verticalLayout.addWidget(self.check_edit_header)
        self.check_prefix_filename = QtWidgets.QCheckBox(self.patch_tab)
        self.check_prefix_filename.setChecked(True)
        self.check_prefix_filename.setObjectName("check_prefix_filename")
        self.verticalLayout.addWidget(self.check_prefix_filename)
        self.patch_firmware = QtWidgets.QPushButton(self.patch_tab)
        self.patch_firmware.setObjectName("patch_firmware")
        self.verticalLayout.addWidget(self.patch_firmware)
        self.log_text = QtWidgets.QTextEdit(self.patch_tab)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.log_text.setFont(font)
        self.log_text.setObjectName("log_text")
        self.verticalLayout.addWidget(self.log_text)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.patch_tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuFile.addAction(self.actionExit_2)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hacktribe"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p><p>1. Select source file. This must be Electribe 2 <span style=\" font-weight:600;\">Sampler</span> firmware version <span style=\" font-weight:600;\">2.02</span>.</p><p>2. Select patch file. This must be \'hacktribe-2.patch\' from the hacktribe repo</p><p>3. Select destination path. This is where the patched firmware will be saved.</p><p>4. If installing to synth hardware for the first time, select \'Modify file header...\'. </p><p>5. Click \'Patch Firmware\' button.</p><p><br/></p></body></html>"))
        self.label_src_path.setText(_translate("MainWindow", "Source file:"))
        self.browse_src_path.setText(_translate("MainWindow", "Browse..."))
        self.label_patch_path.setText(_translate("MainWindow", "Patch file: "))
        self.browse_patch_path.setText(_translate("MainWindow", "Browse..."))
        self.label_dest_path.setText(_translate("MainWindow", "Dest path:  "))
        self.browse_dest_path.setText(_translate("MainWindow", "Browse..."))
        self.check_edit_header.setText(_translate("MainWindow", "Modify file header for synth hardware"))
        self.check_prefix_filename.setText(_translate("MainWindow", "Prefix destination filename"))
        self.patch_firmware.setText(_translate("MainWindow", "Patch Firmware"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.patch_tab), _translate("MainWindow", "Patch"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



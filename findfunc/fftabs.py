################################################################################
## Form generated from reading UI file 'fftabs.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_fftabs(object):
    def setupUi(self, fftabs):
        if not fftabs.objectName():
            fftabs.setObjectName(u"fftabs")
        fftabs.resize(1015, 630)
        self.verticalLayout = QVBoxLayout(fftabs)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(fftabs)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnloadsess = QPushButton(fftabs)
        self.btnloadsess.setObjectName(u"btnloadsess")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnloadsess.sizePolicy().hasHeightForWidth())
        self.btnloadsess.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.btnloadsess)
        self.btnsavesess = QPushButton(fftabs)
        self.btnsavesess.setObjectName(u"btnsavesess")
        sizePolicy.setHeightForWidth(self.btnsavesess.sizePolicy().hasHeightForWidth())
        self.btnsavesess.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.btnsavesess)
        self.btnexportcsv = QPushButton(fftabs)
        self.btnexportcsv.setObjectName(u"btnexportcsv")
        sizePolicy.setHeightForWidth(self.btnexportcsv.sizePolicy().hasHeightForWidth())
        self.btnexportcsv.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.btnexportcsv)
        self.linklabel = QLabel(fftabs)
        self.linklabel.setObjectName(u"linklabel")
        self.linklabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.linklabel.setOpenExternalLinks(True)
        self.horizontalLayout.addWidget(self.linklabel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(fftabs)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(fftabs)

    def retranslateUi(self, fftabs):
        fftabs.setWindowTitle(QCoreApplication.translate("fftabs", u"Filter Signatures", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("fftabs", u"Tab 1", None))
        self.btnloadsess.setText(QCoreApplication.translate("fftabs", u"Load session", None))
        self.btnsavesess.setText(QCoreApplication.translate("fftabs", u"Save session", None))
        self.btnexportcsv.setText(QCoreApplication.translate("fftabs", u"Export CSV", None))
        self.linklabel.setText(QCoreApplication.translate("fftabs", u"ff", None))


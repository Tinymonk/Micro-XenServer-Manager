# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\python\Micro-XenServer-Manager\App\ui_main.ui'
#
# Created: Sat Feb 22 22:52:10 2014
#      by: PyQt4 UI code generator 4.10.1
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
        MainWindow.resize(1024, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/resource/favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        MainWindow.setDockOptions(QtGui.QMainWindow.AnimatedDocks|QtGui.QMainWindow.ForceTabbedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 4))
        self.progressBar.setStyleSheet(_fromUtf8("QProgressBar::chunk {\n"
"    border: 1px solid grey;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    border-radius: 5px;\n"
"    background-color: #b91f1f;\n"
"}\n"
"QProgressBar{\n"
"    border: 0px;\n"
"    background: transparent;\n"
"}"))
        self.progressBar.setTextVisible(False)
        self.progressBar.setFormat(_fromUtf8(""))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeView = QtGui.QTreeView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMaximumSize(QtCore.QSize(250, 16777215))
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.horizontalLayout.addWidget(self.treeView)
        spacerItem = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabInformation = QtGui.QWidget()
        self.tabInformation.setObjectName(_fromUtf8("tabInformation"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabInformation)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelInformation = QtGui.QLabel(self.tabInformation)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelInformation.sizePolicy().hasHeightForWidth())
        self.labelInformation.setSizePolicy(sizePolicy)
        self.labelInformation.setMinimumSize(QtCore.QSize(0, 30))
        self.labelInformation.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelInformation.setFont(font)
        self.labelInformation.setStyleSheet(_fromUtf8("QLabel {\n"
"    color: white;\n"
"    background-color: rgb(0, 90, 171);\n"
"}"))
        self.labelInformation.setMargin(5)
        self.labelInformation.setObjectName(_fromUtf8("labelInformation"))
        self.verticalLayout_3.addWidget(self.labelInformation)
        self.frame = QtGui.QFrame(self.tabInformation)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout_2 = QtGui.QFormLayout(self.frame)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_name_label = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_name_label.setFont(font)
        self.lineEdit_name_label.setFrame(False)
        self.lineEdit_name_label.setReadOnly(True)
        self.lineEdit_name_label.setObjectName(_fromUtf8("lineEdit_name_label"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_name_label)
        self.label_8 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_name_description = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_name_description.setFont(font)
        self.lineEdit_name_description.setFrame(False)
        self.lineEdit_name_description.setReadOnly(True)
        self.lineEdit_name_description.setObjectName(_fromUtf8("lineEdit_name_description"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_name_description)
        self.label_2 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_uuid = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_uuid.setFont(font)
        self.lineEdit_uuid.setFrame(False)
        self.lineEdit_uuid.setReadOnly(True)
        self.lineEdit_uuid.setObjectName(_fromUtf8("lineEdit_uuid"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_uuid)
        self.label_3 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_OpaqueRef = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_OpaqueRef.setFont(font)
        self.lineEdit_OpaqueRef.setFrame(False)
        self.lineEdit_OpaqueRef.setReadOnly(True)
        self.lineEdit_OpaqueRef.setObjectName(_fromUtf8("lineEdit_OpaqueRef"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_OpaqueRef)
        self.label_5 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_power_state = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_power_state.setFont(font)
        self.lineEdit_power_state.setFrame(False)
        self.lineEdit_power_state.setReadOnly(True)
        self.lineEdit_power_state.setObjectName(_fromUtf8("lineEdit_power_state"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_power_state)
        self.label_6 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_VCPUs_at_startup = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_VCPUs_at_startup.setFont(font)
        self.lineEdit_VCPUs_at_startup.setFrame(False)
        self.lineEdit_VCPUs_at_startup.setReadOnly(True)
        self.lineEdit_VCPUs_at_startup.setObjectName(_fromUtf8("lineEdit_VCPUs_at_startup"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEdit_VCPUs_at_startup)
        self.label_7 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_memory_target = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_memory_target.setFont(font)
        self.lineEdit_memory_target.setFrame(False)
        self.lineEdit_memory_target.setReadOnly(True)
        self.lineEdit_memory_target.setObjectName(_fromUtf8("lineEdit_memory_target"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.lineEdit_memory_target)
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_is_control_domain = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_is_control_domain.setFont(font)
        self.lineEdit_is_control_domain.setFrame(False)
        self.lineEdit_is_control_domain.setReadOnly(True)
        self.lineEdit_is_control_domain.setObjectName(_fromUtf8("lineEdit_is_control_domain"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_is_control_domain)
        self.label_10 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_tags = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_tags.setFont(font)
        self.lineEdit_tags.setFrame(False)
        self.lineEdit_tags.setReadOnly(True)
        self.lineEdit_tags.setObjectName(_fromUtf8("lineEdit_tags"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_tags)
        self.verticalLayout_3.addWidget(self.frame)
        self.tabWidget.addTab(self.tabInformation, _fromUtf8(""))
        self.tabLog = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabLog.sizePolicy().hasHeightForWidth())
        self.tabLog.setSizePolicy(sizePolicy)
        self.tabLog.setObjectName(_fromUtf8("tabLog"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabLog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelLog = QtGui.QLabel(self.tabLog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLog.sizePolicy().hasHeightForWidth())
        self.labelLog.setSizePolicy(sizePolicy)
        self.labelLog.setMinimumSize(QtCore.QSize(0, 30))
        self.labelLog.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelLog.setFont(font)
        self.labelLog.setStyleSheet(_fromUtf8("QLabel {\n"
"    color: white;\n"
"    background-color: rgb(0, 90, 171);\n"
"}"))
        self.labelLog.setMargin(5)
        self.labelLog.setObjectName(_fromUtf8("labelLog"))
        self.verticalLayout_2.addWidget(self.labelLog)
        self.plainTextLog = QtGui.QPlainTextEdit(self.tabLog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextLog.setFont(font)
        self.plainTextLog.setFrameShape(QtGui.QFrame.StyledPanel)
        self.plainTextLog.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.plainTextLog.setReadOnly(True)
        self.plainTextLog.setObjectName(_fromUtf8("plainTextLog"))
        self.verticalLayout_2.addWidget(self.plainTextLog)
        self.pushButtonSaveLog = QtGui.QPushButton(self.tabLog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSaveLog.setFont(font)
        self.pushButtonSaveLog.setObjectName(_fromUtf8("pushButtonSaveLog"))
        self.verticalLayout_2.addWidget(self.pushButtonSaveLog)
        self.tabWidget.addTab(self.tabLog, _fromUtf8(""))
        self.tabWatch = QtGui.QWidget()
        self.tabWatch.setObjectName(_fromUtf8("tabWatch"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabWatch)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setMargin(9)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.tabWatch)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("QLabel {\n"
"    color: white;\n"
"    background-color: rgb(0, 90, 171);\n"
"}"))
        self.label.setMargin(5)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.scrollArea_2 = QtGui.QScrollArea(self.tabWatch)
        self.scrollArea_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.scrollArea_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 690, 800))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(690, 800))
        self.scrollAreaWidgetContents_2.setMaximumSize(QtCore.QSize(690, 800))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.tabWatch, _fromUtf8(""))
        self.tabStatistic = QtGui.QWidget()
        self.tabStatistic.setObjectName(_fromUtf8("tabStatistic"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tabStatistic)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 5)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_Form = QtGui.QLabel(self.tabStatistic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Form.sizePolicy().hasHeightForWidth())
        self.label_Form.setSizePolicy(sizePolicy)
        self.label_Form.setObjectName(_fromUtf8("label_Form"))
        self.gridLayout.addWidget(self.label_Form, 0, 2, 1, 1)
        self.dateTimeEditFrom = QtGui.QDateTimeEdit(self.tabStatistic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEditFrom.sizePolicy().hasHeightForWidth())
        self.dateTimeEditFrom.setSizePolicy(sizePolicy)
        self.dateTimeEditFrom.setObjectName(_fromUtf8("dateTimeEditFrom"))
        self.gridLayout.addWidget(self.dateTimeEditFrom, 0, 3, 1, 1)
        self.doubleSpinBoxK = QtGui.QDoubleSpinBox(self.tabStatistic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBoxK.sizePolicy().hasHeightForWidth())
        self.doubleSpinBoxK.setSizePolicy(sizePolicy)
        self.doubleSpinBoxK.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.doubleSpinBoxK.setDecimals(3)
        self.doubleSpinBoxK.setProperty("value", 1.0)
        self.doubleSpinBoxK.setObjectName(_fromUtf8("doubleSpinBoxK"))
        self.gridLayout.addWidget(self.doubleSpinBoxK, 0, 1, 1, 1)
        self.dateTimeEditTo = QtGui.QDateTimeEdit(self.tabStatistic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEditTo.sizePolicy().hasHeightForWidth())
        self.dateTimeEditTo.setSizePolicy(sizePolicy)
        self.dateTimeEditTo.setObjectName(_fromUtf8("dateTimeEditTo"))
        self.gridLayout.addWidget(self.dateTimeEditTo, 0, 5, 1, 1)
        self.label_To = QtGui.QLabel(self.tabStatistic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_To.sizePolicy().hasHeightForWidth())
        self.label_To.setSizePolicy(sizePolicy)
        self.label_To.setObjectName(_fromUtf8("label_To"))
        self.gridLayout.addWidget(self.label_To, 0, 4, 1, 1)
        self.pushButtonAnalyze = QtGui.QPushButton(self.tabStatistic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAnalyze.sizePolicy().hasHeightForWidth())
        self.pushButtonAnalyze.setSizePolicy(sizePolicy)
        self.pushButtonAnalyze.setObjectName(_fromUtf8("pushButtonAnalyze"))
        self.gridLayout.addWidget(self.pushButtonAnalyze, 0, 6, 1, 1)
        self.label_Formula = QtGui.QLabel(self.tabStatistic)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_Formula.setFont(font)
        self.label_Formula.setObjectName(_fromUtf8("label_Formula"))
        self.gridLayout.addWidget(self.label_Formula, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 7, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.scrollArea = QtGui.QScrollArea(self.tabStatistic)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 650, 400))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(650, 400))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(650, 400))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_7.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_Total = QtGui.QLabel(self.tabStatistic)
        self.label_Total.setObjectName(_fromUtf8("label_Total"))
        self.horizontalLayout_2.addWidget(self.label_Total)
        self.labelTotalEnergy = QtGui.QLabel(self.tabStatistic)
        self.labelTotalEnergy.setObjectName(_fromUtf8("labelTotalEnergy"))
        self.horizontalLayout_2.addWidget(self.labelTotalEnergy)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.textBrowser = QtGui.QTextBrowser(self.tabStatistic)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_7.addWidget(self.textBrowser)
        self.verticalLayout_7.setStretch(1, 5)
        self.tabWidget.addTab(self.tabStatistic, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setToolTip(_fromUtf8(""))
        self.statusBar.setStatusTip(_fromUtf8(""))
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menuBar.setAcceptDrops(False)
        self.menuBar.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuMain = QtGui.QMenu(self.menuBar)
        self.menuMain.setTitle(_fromUtf8(""))
        self.menuMain.setObjectName(_fromUtf8("menuMain"))
        self.menuRunningVM = QtGui.QMenu(self.menuBar)
        self.menuRunningVM.setEnabled(True)
        self.menuRunningVM.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.menuRunningVM.setAcceptDrops(False)
        self.menuRunningVM.setTitle(_fromUtf8(""))
        self.menuRunningVM.setObjectName(_fromUtf8("menuRunningVM"))
        self.menuVMMigrate = QtGui.QMenu(self.menuRunningVM)
        self.menuVMMigrate.setObjectName(_fromUtf8("menuVMMigrate"))
        self.menuHaltedVM = QtGui.QMenu(self.menuBar)
        self.menuHaltedVM.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.menuHaltedVM.setTitle(_fromUtf8(""))
        self.menuHaltedVM.setObjectName(_fromUtf8("menuHaltedVM"))
        self.menuHost = QtGui.QMenu(self.menuBar)
        self.menuHost.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.menuHost.setTitle(_fromUtf8(""))
        self.menuHost.setObjectName(_fromUtf8("menuHost"))
        self.menuSuspendedVM = QtGui.QMenu(self.menuBar)
        self.menuSuspendedVM.setTitle(_fromUtf8(""))
        self.menuSuspendedVM.setObjectName(_fromUtf8("menuSuspendedVM"))
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionConnect = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/resource/connect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnect.setIcon(icon1)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionQuit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/resource/quit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionDisconnect = QtGui.QAction(MainWindow)
        self.actionDisconnect.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/resource/disconnect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDisconnect.setIcon(icon3)
        self.actionDisconnect.setObjectName(_fromUtf8("actionDisconnect"))
        self.actionVMSuspend = QtGui.QAction(MainWindow)
        self.actionVMSuspend.setObjectName(_fromUtf8("actionVMSuspend"))
        self.actionVMShutdown = QtGui.QAction(MainWindow)
        self.actionVMShutdown.setObjectName(_fromUtf8("actionVMShutdown"))
        self.actionVMStart = QtGui.QAction(MainWindow)
        self.actionVMStart.setObjectName(_fromUtf8("actionVMStart"))
        self.actionHostStart = QtGui.QAction(MainWindow)
        self.actionHostStart.setObjectName(_fromUtf8("actionHostStart"))
        self.actionHostShutdown = QtGui.QAction(MainWindow)
        self.actionHostShutdown.setObjectName(_fromUtf8("actionHostShutdown"))
        self.actionHostReboot = QtGui.QAction(MainWindow)
        self.actionHostReboot.setObjectName(_fromUtf8("actionHostReboot"))
        self.actionVMReboot = QtGui.QAction(MainWindow)
        self.actionVMReboot.setObjectName(_fromUtf8("actionVMReboot"))
        self.actionVMResume = QtGui.QAction(MainWindow)
        self.actionVMResume.setObjectName(_fromUtf8("actionVMResume"))
        self.menuMain.addAction(self.actionConnect)
        self.menuMain.addAction(self.actionDisconnect)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionQuit)
        self.menuRunningVM.addAction(self.actionVMShutdown)
        self.menuRunningVM.addAction(self.actionVMSuspend)
        self.menuRunningVM.addAction(self.actionVMReboot)
        self.menuRunningVM.addAction(self.menuVMMigrate.menuAction())
        self.menuHaltedVM.addAction(self.actionVMStart)
        self.menuHost.addAction(self.actionHostStart)
        self.menuHost.addAction(self.actionHostShutdown)
        self.menuHost.addAction(self.actionHostReboot)
        self.menuSuspendedVM.addAction(self.actionVMResume)
        self.menuBar.addAction(self.menuMain.menuAction())
        self.menuBar.addAction(self.menuRunningVM.menuAction())
        self.menuBar.addAction(self.menuHaltedVM.menuAction())
        self.menuBar.addAction(self.menuHost.menuAction())
        self.menuBar.addAction(self.menuSuspendedVM.menuAction())
        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addAction(self.actionDisconnect)
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Micro XenServer Manager", None))
        self.labelInformation.setText(_translate("MainWindow", "基本信息", None))
        self.label_4.setText(_translate("MainWindow", "名称", None))
        self.label_8.setText(_translate("MainWindow", "描述", None))
        self.label_2.setText(_translate("MainWindow", "uuid", None))
        self.label_3.setText(_translate("MainWindow", "状态", None))
        self.label_5.setText(_translate("MainWindow", "内部引用", None))
        self.label_6.setText(_translate("MainWindow", "CPU数量", None))
        self.label_7.setText(_translate("MainWindow", "分配内存", None))
        self.label_9.setText(_translate("MainWindow", "控制主机", None))
        self.label_10.setText(_translate("MainWindow", "标签", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInformation), _translate("MainWindow", "虚拟机", None))
        self.labelLog.setText(_translate("MainWindow", "资源池日志", None))
        self.pushButtonSaveLog.setText(_translate("MainWindow", "输出日志到log.txt", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLog), _translate("MainWindow", "日志", None))
        self.label.setText(_translate("MainWindow", "动态视图", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWatch), _translate("MainWindow", "数据监测", None))
        self.label_Form.setText(_translate("MainWindow", "时间从", None))
        self.label_To.setText(_translate("MainWindow", "到", None))
        self.pushButtonAnalyze.setText(_translate("MainWindow", "分析", None))
        self.label_Formula.setText(_translate("MainWindow", "k=", None))
        self.label_Total.setText(_translate("MainWindow", "总能耗：", None))
        self.labelTotalEnergy.setText(_translate("MainWindow", "0", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600;\">表达式参考</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e<span style=\" vertical-align:sub;\">c</span> = E<span style=\" vertical-align:sub;\">c</span>t∫f<span style=\" vertical-align:sub;\">c</span>(x) = E<span style=\" vertical-align:sub;\">c</span>∑Tf<span style=\" vertical-align:sub;\">c</span>(nT/t) </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e<span style=\" vertical-align:sub;\">m</span> = E<span style=\" vertical-align:sub;\">m</span>t∫f<span style=\" vertical-align:sub;\">m</span>(x) = E<span style=\" vertical-align:sub;\">m</span>∑Tf<span style=\" vertical-align:sub;\">m</span>(nT/t) </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">E<span style=\" vertical-align:sub;\">c</span>/E<span style=\" vertical-align:sub;\">m</span> = 1/k </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e = e<span style=\" vertical-align:sub;\">c</span> + e<span style=\" vertical-align:sub;\">m</span> = E<span style=\" vertical-align:sub;\">c</span>∑Tf<span style=\" vertical-align:sub;\">c</span>(nT/t) + E<span style=\" vertical-align:sub;\">m</span>∑Tf<span style=\" vertical-align:sub;\">m</span>(nT/t) </p>\n"
"<table border=\"1\" style=\" margin-top:5px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"0\" cellpadding=\"2\"><thead>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">符号</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">描述</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">单位</span></p></td></tr></thead>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">E<span style=\" vertical-align:sub;\">c</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CPU能耗 </p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">W/prec*s </p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">E<span style=\" vertical-align:sub;\">m</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">内存能耗 </p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">W/MB*s </p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e<span style=\" vertical-align:sub;\">c</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CPU总能耗 </p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">W </p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e<span style=\" vertical-align:sub;\">m</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">内存总能耗 </p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">W </p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">t </p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">运行总时间 </p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">s </p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">T </p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">以5s为间隔的测量时间 </p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">s </p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e </p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">总能耗 </p></td>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">W </p></td></tr></table></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStatistic), _translate("MainWindow", "能耗分析", None))
        self.menuVMMigrate.setTitle(_translate("MainWindow", "迁移", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionConnect.setText(_translate("MainWindow", "连接", None))
        self.actionQuit.setText(_translate("MainWindow", "退出", None))
        self.actionDisconnect.setText(_translate("MainWindow", "断开", None))
        self.actionVMSuspend.setText(_translate("MainWindow", "停止", None))
        self.actionVMShutdown.setText(_translate("MainWindow", "关闭", None))
        self.actionVMStart.setText(_translate("MainWindow", "启动", None))
        self.actionHostStart.setText(_translate("MainWindow", "启动", None))
        self.actionHostShutdown.setText(_translate("MainWindow", "关闭", None))
        self.actionHostReboot.setText(_translate("MainWindow", "重启", None))
        self.actionVMReboot.setText(_translate("MainWindow", "重启", None))
        self.actionVMResume.setText(_translate("MainWindow", "恢复", None))

import resource_rc

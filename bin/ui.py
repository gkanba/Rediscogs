# Form implementation generated from reading ui file '.\rediscogs.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_WidgetSearch(object):
    def setupUi(self, WidgetSearch):
        WidgetSearch.setObjectName("WidgetSearch")
        WidgetSearch.resize(1200, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetSearch.sizePolicy().hasHeightForWidth())
        WidgetSearch.setSizePolicy(sizePolicy)
        WidgetSearch.setStyleSheet("QCheckBox::indicator:checked{\n"
"    width: 36px;\n"
"    height: 36px;\n"
"    image: url(:/images/icons/Toggle_On.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"    width: 36px;\n"
"    height: 36px;\n"
"    image: url(:/images/icons/Toggle_Off.png);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border-radius: 10px;\n"
"}")
        self.GBox_Search = QtWidgets.QGroupBox(parent=WidgetSearch)
        self.GBox_Search.setGeometry(QtCore.QRect(5, 0, 275, 370))
        self.GBox_Search.setObjectName("GBox_Search")
        self.GBox_E = QtWidgets.QGroupBox(parent=self.GBox_Search)
        self.GBox_E.setGeometry(QtCore.QRect(10, 260, 255, 60))
        self.GBox_E.setObjectName("GBox_E")
        self.CBox_E = QtWidgets.QCheckBox(parent=self.GBox_E)
        self.CBox_E.setGeometry(QtCore.QRect(20, 15, 40, 40))
        self.CBox_E.setStyleSheet("")
        self.CBox_E.setText("")
        self.CBox_E.setIconSize(QtCore.QSize(30, 30))
        self.CBox_E.setObjectName("CBox_E")
        self.LEdit_E = QtWidgets.QLineEdit(parent=self.GBox_E)
        self.LEdit_E.setGeometry(QtCore.QRect(70, 20, 175, 30))
        self.LEdit_E.setStyleSheet("")
        self.LEdit_E.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LEdit_E.setObjectName("LEdit_E")
        self.GBox_A = QtWidgets.QGroupBox(parent=self.GBox_Search)
        self.GBox_A.setGeometry(QtCore.QRect(10, 20, 255, 60))
        self.GBox_A.setObjectName("GBox_A")
        self.CBox_A = QtWidgets.QCheckBox(parent=self.GBox_A)
        self.CBox_A.setGeometry(QtCore.QRect(20, 15, 40, 40))
        self.CBox_A.setStyleSheet("")
        self.CBox_A.setText("")
        self.CBox_A.setIconSize(QtCore.QSize(30, 30))
        self.CBox_A.setObjectName("CBox_A")
        self.LEdit_A = QtWidgets.QLineEdit(parent=self.GBox_A)
        self.LEdit_A.setGeometry(QtCore.QRect(70, 20, 175, 30))
        self.LEdit_A.setStyleSheet("")
        self.LEdit_A.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LEdit_A.setObjectName("LEdit_A")
        self.GBox_B = QtWidgets.QGroupBox(parent=self.GBox_Search)
        self.GBox_B.setGeometry(QtCore.QRect(10, 80, 255, 60))
        self.GBox_B.setObjectName("GBox_B")
        self.CBox_B = QtWidgets.QCheckBox(parent=self.GBox_B)
        self.CBox_B.setGeometry(QtCore.QRect(20, 15, 40, 40))
        self.CBox_B.setStyleSheet("")
        self.CBox_B.setText("")
        self.CBox_B.setIconSize(QtCore.QSize(30, 30))
        self.CBox_B.setObjectName("CBox_B")
        self.LEdit_B = QtWidgets.QLineEdit(parent=self.GBox_B)
        self.LEdit_B.setGeometry(QtCore.QRect(70, 20, 175, 30))
        self.LEdit_B.setStyleSheet("")
        self.LEdit_B.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LEdit_B.setObjectName("LEdit_B")
        self.GBox_D = QtWidgets.QGroupBox(parent=self.GBox_Search)
        self.GBox_D.setGeometry(QtCore.QRect(10, 200, 255, 60))
        self.GBox_D.setObjectName("GBox_D")
        self.CBox_D = QtWidgets.QCheckBox(parent=self.GBox_D)
        self.CBox_D.setGeometry(QtCore.QRect(20, 15, 40, 40))
        self.CBox_D.setStyleSheet("")
        self.CBox_D.setText("")
        self.CBox_D.setIconSize(QtCore.QSize(30, 30))
        self.CBox_D.setObjectName("CBox_D")
        self.LEdit_D = QtWidgets.QLineEdit(parent=self.GBox_D)
        self.LEdit_D.setGeometry(QtCore.QRect(70, 20, 175, 30))
        self.LEdit_D.setStyleSheet("")
        self.LEdit_D.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LEdit_D.setObjectName("LEdit_D")
        self.GBox_C = QtWidgets.QGroupBox(parent=self.GBox_Search)
        self.GBox_C.setGeometry(QtCore.QRect(10, 140, 255, 60))
        self.GBox_C.setObjectName("GBox_C")
        self.CBox_C = QtWidgets.QCheckBox(parent=self.GBox_C)
        self.CBox_C.setGeometry(QtCore.QRect(20, 15, 40, 40))
        self.CBox_C.setStyleSheet("")
        self.CBox_C.setText("")
        self.CBox_C.setIconSize(QtCore.QSize(30, 30))
        self.CBox_C.setObjectName("CBox_C")
        self.LEdit_C = QtWidgets.QLineEdit(parent=self.GBox_C)
        self.LEdit_C.setGeometry(QtCore.QRect(70, 20, 175, 30))
        self.LEdit_C.setStyleSheet("")
        self.LEdit_C.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LEdit_C.setObjectName("LEdit_C")
        self.Button_Search = QtWidgets.QPushButton(parent=self.GBox_Search)
        self.Button_Search.setGeometry(QtCore.QRect(10, 330, 255, 31))
        self.Button_Search.setStyleSheet("#Button_Search{\n"
"    background-color: rgba(128, 128, 128, 255);\n"
"    border-radius: 10px;\n"
"    border: 2px;\n"
"    border-color: rgb(244, 255, 255);\n"
"    padding: 5px;\n"
"    margin: 1px;\n"
"    image: url(:/images/icons/Search.png);\n"
"}\n"
"\n"
"#Button_Search:hover{\n"
"    background-color: rgba(192, 192, 192, 192);\n"
"    border-radius: 10px;\n"
"    border: 2px;\n"
"    padding: 5px;\n"
"    border-color: #5af2e9;\n"
"    margin: 1px;\n"
"    image: url(:/images/icons/Search.png);\n"
"}\n"
"\n"
"#Button_Search:pressed{\n"
"    background-color: rgba(255, 255, 255, 192);\n"
"    border-radius: 10px;\n"
"    border: 2px;\n"
"    padding: 5px;\n"
"    border-color: #5af2e9;\n"
"    margin: 1px;\n"
"    image: url(:/images/icons/Search.png);\n"
"}")
        self.Button_Search.setText("")
        self.Button_Search.setObjectName("Button_Search")
        self.GBox_List = QtWidgets.QGroupBox(parent=WidgetSearch)
        self.GBox_List.setGeometry(QtCore.QRect(5, 370, 275, 345))
        self.GBox_List.setObjectName("GBox_List")
        self.LView_Releases = QtWidgets.QListView(parent=self.GBox_List)
        self.LView_Releases.setGeometry(QtCore.QRect(10, 20, 255, 315))
        self.LView_Releases.setStyleSheet("")
        self.LView_Releases.setObjectName("LView_Releases")
        self.GBox_Release = QtWidgets.QGroupBox(parent=WidgetSearch)
        self.GBox_Release.setGeometry(QtCore.QRect(290, 0, 905, 715))
        self.GBox_Release.setObjectName("GBox_Release")
        self.Label_Artwork = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_Artwork.setGeometry(QtCore.QRect(30, 60, 200, 200))
        self.Label_Artwork.setStyleSheet("#Label_Artwork{\n"
"    image: {\n"
"            filter: drop-shadow(5px 5px 10px #000000);\n"
"    };\n"
"}")
        self.Label_Artwork.setText("")
        self.Label_Artwork.setPixmap(QtGui.QPixmap(":/images/icons/Artwork_Sample.jpg"))
        self.Label_Artwork.setScaledContents(True)
        self.Label_Artwork.setObjectName("Label_Artwork")
        self.Label_Title = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_Title.setGeometry(QtCore.QRect(260, 130, 591, 71))
        font = QtGui.QFont()
        font.setFamily("Iosevka NFM SemiBold")
        font.setPointSize(49)
        font.setBold(True)
        self.Label_Title.setFont(font)
        self.Label_Title.setStyleSheet("#Label_Title\n"
"{\n"
"    color: rgba(255, 255 ,255 ,255);\n"
"}")
        self.Label_Title.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Label_Title.setScaledContents(True)
        self.Label_Title.setObjectName("Label_Title")
        self.Label_MainArtist = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_MainArtist.setGeometry(QtCore.QRect(300, 230, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Iosevka NFM SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.Label_MainArtist.setFont(font)
        self.Label_MainArtist.setStyleSheet("#Label_MainArtist\n"
"{\n"
"    color: rgba(255, 255 ,255 ,255);\n"
"}")
        self.Label_MainArtist.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Label_MainArtist.setScaledContents(True)
        self.Label_MainArtist.setObjectName("Label_MainArtist")
        self.Label_MainArtistImage = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_MainArtistImage.setGeometry(QtCore.QRect(270, 230, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Iosevka NFM SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.Label_MainArtistImage.setFont(font)
        self.Label_MainArtistImage.setStyleSheet("")
        self.Label_MainArtistImage.setText("")
        self.Label_MainArtistImage.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Label_MainArtistImage.setPixmap(QtGui.QPixmap(":/images/icons/Artwork_Sample.jpg"))
        self.Label_MainArtistImage.setScaledContents(True)
        self.Label_MainArtistImage.setObjectName("Label_MainArtistImage")
        self.Label_Year = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_Year.setGeometry(QtCore.QRect(270, 80, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Iosevka NFM SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.Label_Year.setFont(font)
        self.Label_Year.setStyleSheet("#Label_Year\n"
"{\n"
"    color: rgba(255, 255 ,255 ,255);\n"
"}")
        self.Label_Year.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Label_Year.setScaledContents(True)
        self.Label_Year.setObjectName("Label_Year")
        self.TView_Tracks = QtWidgets.QTableView(parent=self.GBox_Release)
        self.TView_Tracks.setGeometry(QtCore.QRect(10, 300, 885, 405))
        self.TView_Tracks.setStyleSheet("QHeaderView::section{\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#TView_Tracks{\n"
"    background-color: transparent;\n"
"    color: rgba(255, 255, 255, 255);\n"
"}")
        self.TView_Tracks.setShowGrid(False)
        self.TView_Tracks.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.TView_Tracks.setWordWrap(False)
        self.TView_Tracks.setObjectName("TView_Tracks")
        self.Button_Save = QtWidgets.QPushButton(parent=self.GBox_Release)
        self.Button_Save.setGeometry(QtCore.QRect(740, 130, 100, 70))
        self.Button_Save.setStyleSheet("#Button_Save{\n"
"    background-color: rgba(128, 128, 128, 180);\n"
"    border-radius: 10px;\n"
"    border: 2px;\n"
"    border-color: rgb(244, 255, 255);\n"
"    padding: 5px;\n"
"    margin: 1px;\n"
"    image: url(:/images/icons/File.png);\n"
"}\n"
"\n"
"#Button_Save:hover{\n"
"    background-color: rgba(192, 192, 192, 180);\n"
"    border-radius: 10px;\n"
"    border: 2px;\n"
"    padding: 5px;\n"
"    border-color: #5af2e9;\n"
"    margin: 1px;\n"
"    image: url(:/images/icons/File.png);\n"
"}\n"
"\n"
"#Button_Save:pressed{\n"
"    background-color: rgba(255, 255, 255, 180);\n"
"    border-radius: 10px;\n"
"    border: 2px;\n"
"    padding: 5px;\n"
"    border-color: #5af2e9;\n"
"    margin: 1px;\n"
"    image: url(:/images/icons/File.png);\n"
"}")
        self.Button_Save.setText("")
        self.Button_Save.setObjectName("Button_Save")
        self.Label_Label = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_Label.setGeometry(QtCore.QRect(400, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Iosevka NFM SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.Label_Label.setFont(font)
        self.Label_Label.setStyleSheet("#Label_Label\n"
"{\n"
"    color: rgba(255, 255 ,255 ,255);\n"
"}")
        self.Label_Label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Label_Label.setScaledContents(True)
        self.Label_Label.setObjectName("Label_Label")
        self.Label_Country = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_Country.setGeometry(QtCore.QRect(530, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Iosevka NFM SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.Label_Country.setFont(font)
        self.Label_Country.setStyleSheet("#Label_Country\n"
"{\n"
"    color: rgba(255, 255 ,255 ,255);\n"
"}")
        self.Label_Country.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Label_Country.setScaledContents(True)
        self.Label_Country.setObjectName("Label_Country")
        self.Label_Format = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_Format.setGeometry(QtCore.QRect(320, 80, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Iosevka NFM SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.Label_Format.setFont(font)
        self.Label_Format.setStyleSheet("#Label_Format\n"
"{\n"
"    color: rgba(255, 255 ,255 ,255);\n"
"}")
        self.Label_Format.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Label_Format.setScaledContents(True)
        self.Label_Format.setObjectName("Label_Format")
        self.Frame_Right = QtWidgets.QFrame(parent=WidgetSearch)
        self.Frame_Right.setGeometry(QtCore.QRect(285, 0, 915, 720))
        self.Frame_Right.setStyleSheet("#Frame_Right{\n"
"    background-color: qlineargradient(spread:pad, x1:0.295, y1:0, x2:0.653, y2:1, stop:0 rgba(217, 175, 217, 255), stop:1 rgba(151, 217, 225, 255));\n"
"}")
        self.Frame_Right.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Frame_Right.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Frame_Right.setObjectName("Frame_Right")
        self.Frame_Right_Upper = QtWidgets.QFrame(parent=self.Frame_Right)
        self.Frame_Right_Upper.setGeometry(QtCore.QRect(0, 280, 915, 430))
        self.Frame_Right_Upper.setStyleSheet("#Frame_Right_Upper{\n"
"    background-color: qlineargradient(spread:pad, x1:0.295, y1:0, x2:0.63, y2:1, stop:0 rgba(95, 118, 127, 197), stop:1 rgba(34, 34, 35, 255));\n"
"}")
        self.Frame_Right_Upper.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Frame_Right_Upper.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Frame_Right_Upper.setObjectName("Frame_Right_Upper")
        self.Frame_Left = QtWidgets.QFrame(parent=WidgetSearch)
        self.Frame_Left.setGeometry(QtCore.QRect(0, 0, 285, 720))
        self.Frame_Left.setStyleSheet("#Frame_Left{\n"
"    background-color: transparent;\n"
"}")
        self.Frame_Left.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Frame_Left.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Frame_Left.setObjectName("Frame_Left")
        self.Frame_Left.raise_()
        self.Frame_Right.raise_()
        self.GBox_Search.raise_()
        self.GBox_List.raise_()
        self.GBox_Release.raise_()

        self.retranslateUi(WidgetSearch)
        QtCore.QMetaObject.connectSlotsByName(WidgetSearch)

    def retranslateUi(self, WidgetSearch):
        _translate = QtCore.QCoreApplication.translate
        WidgetSearch.setWindowTitle(_translate("WidgetSearch", "Form"))
        self.GBox_Search.setTitle(_translate("WidgetSearch", "Search"))
        self.GBox_E.setTitle(_translate("WidgetSearch", "Release Year"))
        self.GBox_A.setTitle(_translate("WidgetSearch", "Catalog No."))
        self.GBox_B.setTitle(_translate("WidgetSearch", "Release Title"))
        self.GBox_D.setTitle(_translate("WidgetSearch", "Release Country"))
        self.GBox_C.setTitle(_translate("WidgetSearch", "Release Artist"))
        self.GBox_List.setTitle(_translate("WidgetSearch", "Results"))
        self.GBox_Release.setTitle(_translate("WidgetSearch", "Release View"))
        self.Label_Title.setText(_translate("WidgetSearch", "緩りらら"))
        self.Label_MainArtist.setText(_translate("WidgetSearch", "笠原瑠斗"))
        self.Label_Year.setText(_translate("WidgetSearch", "2023"))
        self.Label_Label.setText(_translate("WidgetSearch", "CBS Sony"))
        self.Label_Country.setText(_translate("WidgetSearch", "Japan"))
        self.Label_Format.setText(_translate("WidgetSearch", "CD"))
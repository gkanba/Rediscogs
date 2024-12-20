# Form implementation generated from reading ui file '.\rediscogs.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import urllib
import pprint

from PyQt6              import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets    import QMainWindow, QFileDialog, QGraphicsDropShadowEffect
from PyQt6.QtGui        import QPixmap

import images.images_rc
from dialogs            import Dialog_Alert, Widget_Message
from client             import DiscogClient
from models             import ListModelSearchResult, TableModelTracklist

class Widget_MainWindow(QMainWindow):
    def setupClient(self, clientIn):
        self._client                    = clientIn
        self._current_release_id        = -1
        self._results                   = None
        self._kwdic                     = None
        self._url_Artwork               = ""
        self._url_ArtistThumb           = ""

    def setupUi(self):
        self.setObjectName("Widget_MainWindow")
        self.resize(1200, 720)
        self.setFixedSize(1200, 720)
        self.setStyleSheet(
                "QCheckBox::indicator:checked{\n"
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
        self.GBox_Search = QtWidgets.QGroupBox(parent=self)
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
        self.Button_Search.setStyleSheet(
                "#Button_Search{\n"
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
        self.GBox_List = QtWidgets.QGroupBox(parent=self)
        self.GBox_List.setGeometry(QtCore.QRect(5, 370, 275, 345))
        self.GBox_List.setObjectName("GBox_List")
        self.LView_Releases = QtWidgets.QListView(parent=self.GBox_List)
        self.LView_Releases.setGeometry(QtCore.QRect(10, 20, 255, 315))
        self.LView_Releases.setStyleSheet("")
        self.LView_Releases.setObjectName("LView_Releases")
        self.GBox_Release = QtWidgets.QGroupBox(parent=self)
        self.GBox_Release.setGeometry(QtCore.QRect(290, 0, 905, 715))
        self.GBox_Release.setObjectName("GBox_Release")
        self.Label_Artwork = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_Artwork.setGeometry(QtCore.QRect(30, 60, 200, 200))
        self.Label_Artwork.setStyleSheet(
                "#Label_Artwork{\n"
                "    image: {\n"
                "            filter: drop-shadow(5px 5px 10px #000000);\n"
                "    };\n"
                "}")
        self.Label_Artwork.setText("")
        self.Label_Artwork.setPixmap(QtGui.QPixmap(":/images/icons/No_Image.png"))
        self.Label_Artwork.setScaledContents(True)
        self.Label_Artwork.setObjectName("Label_Artwork")
        self.Label_Title = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_Title.setGeometry(QtCore.QRect(260, 130, 621, 71))
        font = QtGui.QFont()
        font.setFamily("Iosevka NFM SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.Label_Title.setFont(font)
        self.Label_Title.setStyleSheet(
                "#Label_Title\n"
                "{\n"
                "    color: rgba(255, 255 ,255 ,255);\n"
                "}")
        self.Label_Title.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Label_Title.setScaledContents(True)
        self.Label_Title.setObjectName("Label_Title")
        self.Label_MainArtist = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_MainArtist.setGeometry(QtCore.QRect(300, 230, 511, 21))
        font = QtGui.QFont()
        font.setFamily("Iosevka NFM SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.Label_MainArtist.setFont(font)
        self.Label_MainArtist.setStyleSheet(
                "#Label_MainArtist\n"
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
        self.Label_MainArtistImage.setPixmap(QtGui.QPixmap(":/images/icons/No_Image.png"))
        self.Label_MainArtistImage.setScaledContents(True)
        self.Label_MainArtistImage.setObjectName("Label_MainArtistImage")
        self.Label_Year = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_Year.setGeometry(QtCore.QRect(270, 80, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Iosevka NFM SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.Label_Year.setFont(font)
        self.Label_Year.setStyleSheet(
                "#Label_Year\n"
                "{\n"
                "    color: rgba(255, 255 ,255 ,255);\n"
                "}")
        self.Label_Year.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Label_Year.setScaledContents(True)
        self.Label_Year.setObjectName("Label_Year")
        self.TView_Tracks = QtWidgets.QTableView(parent=self.GBox_Release)
        self.TView_Tracks.setGeometry(QtCore.QRect(10, 300, 885, 405))
        self.TView_Tracks.setStyleSheet("""
                QHeaderView::section{
                        background-color: transparent;
                        color: white;
                        font-weight: bold;
                        font-size: 18px;
                        padding: 4px;
                }
                QHeaderView{
                        background-color: transparent;
                }
                #TView_Tracks{
                        background-color: transparent;
                        border: none;
                }
                QTableView::item{
                        color: white;
                        margin: 2px;
                        font-size: 14px;
                }
                """)
        self.TView_Tracks.setShowGrid(False)
        self.TView_Tracks.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.TView_Tracks.setWordWrap(False)
        self.TView_Tracks.setObjectName("TView_Tracks")
        self.Button_Save = QtWidgets.QPushButton(parent=self.GBox_Release)
        self.Button_Save.setGeometry(QtCore.QRect(834, 230, 61, 41))
        self.Button_Save.setStyleSheet(
                "#Button_Save{\n"
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
        self.Label_Label.setGeometry(QtCore.QRect(530, 80, 351, 21))
        font = QtGui.QFont()
        font.setFamily("Iosevka NFM SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.Label_Label.setFont(font)
        self.Label_Label.setStyleSheet(
                "#Label_Label\n"
                "{\n"
                "    color: rgba(255, 255 ,255 ,255);\n"
                "}")
        self.Label_Label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Label_Label.setScaledContents(True)
        self.Label_Label.setObjectName("Label_Label")
        self.Label_Country = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_Country.setGeometry(QtCore.QRect(410, 80, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Iosevka NFM SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.Label_Country.setFont(font)
        self.Label_Country.setStyleSheet(
                "#Label_Country\n"
                "{\n"
                "    color: rgba(255, 255 ,255 ,255);\n"
                "}")
        self.Label_Country.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Label_Country.setScaledContents(True)
        self.Label_Country.setObjectName("Label_Country")
        self.Label_Format = QtWidgets.QLabel(parent=self.GBox_Release)
        self.Label_Format.setGeometry(QtCore.QRect(320, 80, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Iosevka NFM SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.Label_Format.setFont(font)
        self.Label_Format.setStyleSheet(
                "#Label_Format\n"
                "{\n"
                "    color: rgba(255, 255 ,255 ,255);\n"
                "}")
        self.Label_Format.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Label_Format.setScaledContents(True)
        self.Label_Format.setObjectName("Label_Format")
        self.Frame_Right = QtWidgets.QFrame(parent=self)
        self.Frame_Right.setGeometry(QtCore.QRect(285, 0, 915, 720))
        self.Frame_Right.setStyleSheet(
                "#Frame_Right{\n"
                "    background-color: qlineargradient(spread:pad, x1:0.295, y1:0, x2:0.653, y2:1, stop:0 rgba(217, 175, 217, 255), stop:1 rgba(151, 217, 225, 255));\n"
                "}")
        self.Frame_Right.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Frame_Right.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Frame_Right.setObjectName("Frame_Right")
        self.Frame_Right_Upper = QtWidgets.QFrame(parent=self.Frame_Right)
        self.Frame_Right_Upper.setGeometry(QtCore.QRect(0, 280, 915, 441))
        self.Frame_Right_Upper.setStyleSheet(
                "#Frame_Right_Upper{\n"
                "    background-color: qlineargradient(spread:pad, x1:0.295, y1:0, x2:0.63, y2:1, stop:0 rgba(95, 118, 127, 197), stop:1 rgba(34, 34, 35, 255));\n"
                "}")
        self.Frame_Right_Upper.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Frame_Right_Upper.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Frame_Right_Upper.setObjectName("Frame_Right_Upper")
        self.Frame_Left = QtWidgets.QFrame(parent=self)
        self.Frame_Left.setGeometry(QtCore.QRect(0, 0, 285, 720))
        self.Frame_Left.setStyleSheet(
                "#Frame_Left{\n"
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
        
        # Set Models
        self.MDL_RESULT_LIST = ListModelSearchResult()
        self.MDL_RESULT_TRACKLIST = TableModelTracklist(None, True)
        self.LView_Releases.setModel(self.MDL_RESULT_LIST)
        self.TView_Tracks.setModel(self.MDL_RESULT_TRACKLIST)

        # Connect Models
        self.Button_Search.clicked.connect(self.on_search_clicked)
        self.LView_Releases.clicked.connect(self.on_search_result_clicked)
        self.Button_Save.clicked.connect(self.on_save_as_clicked)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Widget_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Widget_MainWindow.setWindowTitle(_translate("WidgetSearch", "Rediscogs"))
        self.GBox_Search.setTitle(_translate("WidgetSearch", "Search"))
        self.GBox_E.setTitle(_translate("WidgetSearch", "Release Year"))
        self.GBox_A.setTitle(_translate("WidgetSearch", "Catalog No."))
        self.GBox_B.setTitle(_translate("WidgetSearch", "Release Title"))
        self.GBox_D.setTitle(_translate("WidgetSearch", "Release Country"))
        self.GBox_C.setTitle(_translate("WidgetSearch", "Release Artist"))
        self.GBox_List.setTitle(_translate("WidgetSearch", "Results"))
        self.GBox_Release.setTitle(_translate("WidgetSearch", "Release View"))
        self.Label_Title.setText(_translate("WidgetSearch", "Blank Title"))
        self.Label_MainArtist.setText(_translate("WidgetSearch", "Blank Artist"))
        self.Label_Year.setText(_translate("WidgetSearch", "Year"))
        self.Label_Label.setText(_translate("WidgetSearch", "Lebel"))
        self.Label_Country.setText(_translate("WidgetSearch", "Country"))
        self.Label_Format.setText(_translate("WidgetSearch", "Format"))

    def on_search_clicked(self):
        c = 0
        self._kwdict = {'type' : 'release'}
        if self.CBox_B.isChecked():
                self._kwdict['title'] = self.LEdit_B.text()
                c += 1
        if self.CBox_C.isChecked():
                self._kwdict['artist'] = self.LEdit_C.text()
                c += 1
        if self.CBox_A.isChecked():
                self._kwdict['catno'] = self.LEdit_A.text()
                c += 1
        if self.CBox_D.isChecked():
                self._kwdict['country'] = self.LEdit_D.text()
                c += 1
        if self.CBox_E.isChecked():
                self._kwdict['year'] = self.LEdit_E.text()
                c += 1
        if c != 0:
                dialog1 = Widget_Message("Searching for contents...\n This may take minutes due to API restriction.")
                dialog1.show()
                try:
                    self._results = self._client.search(**self._kwdict)
                    self.MDL_RESULT_LIST.set_search_result(self._results)
                except:
                    dialog3 = Dialog_Alert("Timed out. Specify more arguments to narrow down.")
                    dialog3.exec()
                dialog1.hide()
        else:
                dialog2 = Dialog_Alert("You must have at least one argument\n to search contents.")
                dialog2.exec()

    def on_search_result_clicked(self):
        model_index = self.LView_Releases.currentIndex()
        result = self._results[model_index.row()]
        #Tracklist
        self.MDL_RESULT_TRACKLIST = TableModelTracklist(result, False)
        self.TView_Tracks.setModel(self.MDL_RESULT_TRACKLIST)

        #debug
        #pprint.pprint(vars(result))
        #print(dir(result.artists[0]))

        #Informations
        self.Label_Title.setText(result.title)
        self.Label_MainArtist.setText(result.artists[0].name)

        if(len(result.labels) == 1):
            self.Label_Label.setText(result.labels[0].name)
        else:
            self.Label_Label.setText(result.labels[0].name + " etc.")

        self.Label_Year.setText(str(result.year))
        self.Label_Country.setText(result.country)
        self.Label_Format.setText(result.formats[0]['descriptions'][0] + "/" + result.formats[0]['name'])
        #Get Images Urls
        if result.images is not None:
                self._url_Artwork = result.images[0]["resource_url"]
                self._url_Atrwork_Null = False
        else:
                self._url_Atrwork_Null = True
        if result.artists[0].images is not None:
                self._url_ArtistThumb = result.artists[0].images[0]["resource_url"]
                self._url_ArtistThumb_Null = False
        else:
                self._url_ArtistThumb_Null = True
        
        #Download Images
        self.download_images(self._url_Artwork, self._url_ArtistThumb)
        #Set Images
        if not self._url_Atrwork_Null:
                self.Label_Artwork.setPixmap(QPixmap('./images/Artwork.jpg'))
                self.shadow_effect = QGraphicsDropShadowEffect()
                self.shadow_effect.setBlurRadius(10)
                self.shadow_effect.setOffset(3)
                self.Label_Artwork.setGraphicsEffect(self.shadow_effect)
        else:
                self.Label_Artwork.setPixmap(QPixmap(':/images/icons/No_Image'))
        if not self._url_ArtistThumb_Null:
                self.Label_MainArtistImage.setPixmap(QPixmap('./images/MainArtistImage.jpg'))
        else:
                self.Label_MainArtistImage.setPixmap(QPixmap(':/images/icons/No_Image'))

        self.TView_Tracks.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.column_widths = [20, 550, 100]
        self.TView_Tracks.verticalHeader().setHidden(True)
        self.TView_Tracks.setCornerButtonEnabled(False)
        for col in range(self.TView_Tracks.horizontalHeader().count()):
                self.TView_Tracks.setColumnWidth(col, self.column_widths[col])

    def on_save_as_clicked(self):
        dialog = QFileDialog()
        dialog.setDefaultSuffix('txt')
        dialog.setNameFilter("Text Files (*.txt)")
        filename = dialog.getSaveFileName()
        if filename[0] != '':
            fn = ""
            if not filename[0].endswith(".txt"):
                fn = filename[0] + ".txt"
            else:
                fn = filename[0]
            with open(fn,'w', newline='\n') as file:
                file.writelines(self.MDL_RESULT_TRACKLIST.get_release_data().artists[0].name + ' - '  + self.MDL_RESULT_TRACKLIST.get_release_data().title + '\n')
                file.writelines(self.MDL_RESULT_TRACKLIST.get_release_data().labels[0].name + ' - ' + str(self.MDL_RESULT_TRACKLIST.get_release_data().data['catno']) + '\n')
                file.writelines(str(self.MDL_RESULT_TRACKLIST.get_release_data().year) +'\n')
                file.writelines('\n')
                for track in self.MDL_RESULT_TRACKLIST.get_release_data().tracklist:
                        file.writelines(track.position + '\t' + track.title + '\t' + track.duration + '\n')
                file.close()

    def download_images(self, url_Artwork : str,  url_MainArtistImage : str):
        try:
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(url_Artwork, './images/Artwork.jpg')
            urllib.request.urlretrieve(url_MainArtistImage, './images/MainArtistImage.jpg')
        except Exception as e:
                print(e)
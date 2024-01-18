# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtGui import QPixmap
import datetime
import subprocess
import yt_dlp as youtube_dl
import downloader

download_sts = 'ready'
stream_type = 'mp4'
download_path = fr'{os.getcwd()}\Downloads'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1116, 669)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DOWNLOAD_BTN = QtWidgets.QToolButton(self.centralwidget)
        self.DOWNLOAD_BTN.setGeometry(QtCore.QRect(920, 580, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.DOWNLOAD_BTN.setFont(font)
        self.DOWNLOAD_BTN.setObjectName("DOWNLOAD_BTN")

        self.LENGTH_INFO = QtWidgets.QLabel(self.centralwidget)
        self.LENGTH_INFO.setGeometry(QtCore.QRect(610, 430, 600, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LENGTH_INFO.setFont(font)
        self.LENGTH_INFO.setObjectName("LENGTH_INFO")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(270, 100, 131, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.LANGUAGE_INFO = QtWidgets.QLabel(self.centralwidget)
        self.LANGUAGE_INFO.setGeometry(QtCore.QRect(640, 480, 600, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LANGUAGE_INFO.setFont(font)
        self.LANGUAGE_INFO.setObjectName("LANGUAGE_INFO")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(474, 10, 20, 631))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)

        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.URL_INPUT = QtWidgets.QLineEdit(self.centralwidget)
        self.URL_INPUT.setGeometry(QtCore.QRect(80, 17, 351, 31))
        self.URL_INPUT.setStyleSheet("QLineEdit { border-radius: 8px;border: 0.5px solid #bcbcbc; }");
        self.URL_INPUT.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.URL_INPUT.setFont(font)
        self.URL_INPUT.setObjectName("URL_INPUT")
        self.DOWNLOAD_STATUS_INFO_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.DOWNLOAD_STATUS_INFO_LABEL.setGeometry(QtCore.QRect(230, 500, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DOWNLOAD_STATUS_INFO_LABEL.setFont(font)
        self.DOWNLOAD_STATUS_INFO_LABEL.setObjectName("DOWNLOAD_STATUS_INFO_LABEL")
        self.VIDEO_TITLE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.VIDEO_TITLE_LABEL.setGeometry(QtCore.QRect(510, 340, 61, 21))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VIDEO_TITLE_LABEL.setFont(font)
        self.VIDEO_TITLE_LABEL.setObjectName("VIDEO_TITLE_LABEL")
        self.EXT_LEABEL = QtWidgets.QTextEdit(self.centralwidget)
        self.EXT_LEABEL.setEnabled(False)
        self.EXT_LEABEL.setGeometry(QtCore.QRect(130, 200, 51, 31))
        self.EXT_LEABEL.setObjectName("EXT_LEABEL")
        self.OPEN_DOWNLOAD = QtWidgets.QPushButton(self.centralwidget)
        self.OPEN_DOWNLOAD.setGeometry(QtCore.QRect(290, 585, 111, 31))
        self.OPEN_DOWNLOAD.setObjectName("OPEN_DOWNLOAD")

        self.THUMBNAIL_VIEW_AREA = QtWidgets.QGraphicsView(self.centralwidget)
        self.THUMBNAIL_VIEW_AREA.setGeometry(QtCore.QRect(500, 10, 601, 301))
     
        self.THUMBNAIL_VIEW_AREA.setObjectName("THUMBNAIL_VIEW_AREA")
        self.VIDEO_TITLE_INPUT = QtWidgets.QLineEdit(self.centralwidget)
        self.VIDEO_TITLE_INPUT.setGeometry(QtCore.QRect(590, 337, 449, 31))
        self.VIDEO_TITLE_INPUT.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.VIDEO_TITLE_INPUT.setMouseTracking(False)
        self.VIDEO_TITLE_INPUT.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.VIDEO_TITLE_INPUT.setAutoFillBackground(False)
        self.VIDEO_TITLE_INPUT.setText("")
        self.VIDEO_TITLE_INPUT.hide()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VIDEO_TITLE_INPUT.setFont(font)
        self.VIDEO_TITLE_INPUT.setObjectName("VIDEO_TITLE_INPUT")
        self.VIDEO_TITLE_INPUT.setStyleSheet("QLineEdit { border-radius: 8px; }");

        self.VIDEO_TITLE_INPUT.setReadOnly(True)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(270, 70, 141, 20))
        self.radioButton.setObjectName("radioButton")
        self.FILE_SIZE_LABEL = QtWidgets.QTextEdit(self.centralwidget)
        self.FILE_SIZE_LABEL.setEnabled(False)
        self.FILE_SIZE_LABEL.setGeometry(QtCore.QRect(180, 200, 101, 31))
        self.FILE_SIZE_LABEL.setObjectName("FILE_SIZE_LABEL")
        self.PROGRESSBAR = QtWidgets.QProgressBar(self.centralwidget)
        self.PROGRESSBAR.setGeometry(QtCore.QRect(40, 545, 431, 21))
        self.PROGRESSBAR.setProperty("value", 0)
        self.PROGRESSBAR.setObjectName("PROGRESSBAR")
        self.LANGUAGE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.LANGUAGE_LABEL.setGeometry(QtCore.QRect(510, 480, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LANGUAGE_LABEL.setFont(font)
        self.LANGUAGE_LABEL.setObjectName("LANGUAGE_LABEL")

        self.Error = QtWidgets.QLabel(self.centralwidget)
        self.Error.setGeometry(QtCore.QRect(590, 580, 3511, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Error.setFont(font)
        self.Error.setStyleSheet('color: #db2c3d')
        self.Error.setObjectName("Error")

        

        
        self.URL_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.URL_LABEL.setGeometry(QtCore.QRect(30, 20, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.URL_LABEL.setFont(font)
        self.URL_LABEL.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.URL_LABEL.setMouseTracking(False)
        self.URL_LABEL.setStyleSheet("font-family:sans-serif")
        self.URL_LABEL.setObjectName("URL_LABEL")
        self.AUDI_VIDEO_LABEL = QtWidgets.QTextEdit(self.centralwidget)
        self.AUDI_VIDEO_LABEL.setEnabled(False)
        self.AUDI_VIDEO_LABEL.setGeometry(QtCore.QRect(280, 200, 131, 31))
        self.AUDI_VIDEO_LABEL.setObjectName("AUDI_VIDEO_LABEL")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 480, 451, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.VIE_INFO = QtWidgets.QLabel(self.centralwidget)
        self.VIE_INFO.setGeometry(QtCore.QRect(590, 390, 600, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VIE_INFO.setFont(font)
        self.VIE_INFO.setObjectName("VIE_INFO")
        self.QUALITY_EXT_RESOLUTION_LIST = QtWidgets.QListWidget(self.centralwidget)
        self.QUALITY_EXT_RESOLUTION_LIST.setGeometry(QtCore.QRect(30, 231, 381, 181))
        self.QUALITY_EXT_RESOLUTION_LIST.setObjectName("QUALITY_EXT_RESOLUTION_LIST")

        self.SEARCH_FO_RESOLUTION_BTN = QtWidgets.QToolButton(self.centralwidget)
        self.SEARCH_FO_RESOLUTION_BTN.setGeometry(QtCore.QRect(270, 430, 141, 31))
        self.SEARCH_FO_RESOLUTION_BTN.setObjectName("SEARCH_FO_RESOLUTION_BTN")


        self.LENGTH_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.LENGTH_LABEL.setGeometry(QtCore.QRect(510, 430, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LENGTH_LABEL.setFont(font)
        self.LENGTH_LABEL.setObjectName("LENGTH_LABEL")
        self.DOWNLOAD_STATUS_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.DOWNLOAD_STATUS_LABEL.setGeometry(QtCore.QRect(40, 500, 600, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DOWNLOAD_STATUS_LABEL.setFont(font)
        self.DOWNLOAD_STATUS_LABEL.setObjectName("DOWNLOAD_STATUS_LABEL")
        self.AGE_RESTRICTION_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.AGE_RESTRICTION_LABEL.setGeometry(QtCore.QRect(510, 530, 600, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AGE_RESTRICTION_LABEL.setFont(font)
        self.AGE_RESTRICTION_LABEL.setObjectName("AGE_RESTRICTION_LABEL")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(590, 340, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.RESOLUTION_TEXT_LABEL = QtWidgets.QTextEdit(self.centralwidget)
        self.RESOLUTION_TEXT_LABEL.setEnabled(False)
        self.RESOLUTION_TEXT_LABEL.setGeometry(QtCore.QRect(30, 200, 101, 31))
        self.RESOLUTION_TEXT_LABEL.setObjectName("RESOLUTION_TEXT_LABEL")
        self.FILTERFROMEXELABEL = QtWidgets.QLabel(self.centralwidget)
        self.FILTERFROMEXELABEL.setGeometry(QtCore.QRect(50, 70, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FILTERFROMEXELABEL.setFont(font)
        self.FILTERFROMEXELABEL.setMouseTracking(True)
        self.FILTERFROMEXELABEL.setObjectName("FILTERFROMEXELABEL")
        self.VIEW_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.VIEW_LABEL.setGeometry(QtCore.QRect(510, 390, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VIEW_LABEL.setFont(font)
        self.VIEW_LABEL.setObjectName("VIEW_LABEL")
        self.AGE_RESTRICTIONS_INFO = QtWidgets.QLabel(self.centralwidget)
        self.AGE_RESTRICTIONS_INFO.setGeometry(QtCore.QRect(690, 530, 600, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AGE_RESTRICTIONS_INFO.setFont(font)
        self.AGE_RESTRICTIONS_INFO.setObjectName("AGE_RESTRICTIONS_INFO")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setStyleSheet("border-radius: 8px;border: 0.5px solid #bcbcbc;");
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 141, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.BROWS_BTN = QtWidgets.QToolButton(self.centralwidget)
        self.BROWS_BTN.setGeometry(QtCore.QRect(330, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.BROWS_BTN.setFont(font)
        self.BROWS_BTN.setObjectName("BROWS_BTN")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPrevious_Downloads = QtWidgets.QAction(MainWindow)
        self.actionPrevious_Downloads.setObjectName("actionPrevious_Downloads")
        self.actionDownload_Folder = QtWidgets.QAction(MainWindow)
        self.actionDownload_Folder.setObjectName("actionDownload_Folder")
        self.actionTuber_Help = QtWidgets.QAction(MainWindow)
        self.actionTuber_Help.setObjectName("actionTuber_Help")
        self.actionSearch_For_Updates = QtWidgets.QAction(MainWindow)
        self.actionSearch_For_Updates.setObjectName("actionSearch_For_Updates")
        self.actionAbout_Tuber = QtWidgets.QAction(MainWindow)
        self.actionAbout_Tuber.setObjectName("actionAbout_Tuber")
        self.actionAbout_Plugins = QtWidgets.QAction(MainWindow)
        self.actionAbout_Plugins.setObjectName("actionAbout_Plugins")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionPrevious_Downloads)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDownload_Folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionTuber_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionSearch_For_Updates)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Tuber)
        self.menuHelp.addAction(self.actionAbout_Plugins)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#################################################################################################

#BUTTON FUNCTIONS

    def getfiles(self):
        global download_path
        dialog = QtWidgets.QFileDialog()
        download_path = dialog.getExistingDirectory(None, "Select Folder")
        download_path = download_path.replace('/','\\')
        if download_path == "":
            download_path = fr'{os.getcwd()}\Downloads'
                                
        self.lineEdit_3.setText(download_path)
        try:
            if download_path[len(download_path)-1]=="\\":
                download_path = download_path.replace('\\','')  
        except:
            pass
       

    def previous_downloads_file(self):

        with open(r'assets/previous_downloads.txt' ,"r",encoding='utf-8') as f:
            k = f.readlines()
        l = []
        for i in k:
            i = i.replace("\n","")
            l.append(f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">{i}</span><br></p>\n")
        p = ""
        for i in l:
            p = p + f"{i}\n"
        

        def close_downloads():
            Dialog.close()

        Dialog = QtWidgets.QDialog()
        Dialog.setModal(True)
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(869, 539)

        
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 831, 461))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(760, 500, 93, 28))
        self.pushButton.setObjectName("pushButton")

        
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Previous Downloads"))
        Dialog.setWindowIcon(QtGui.QIcon(r'icons\icon.ico'))
        
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"    
    f"{p}"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
            
        self.pushButton.setText(_translate("Dialog", "Close"))

        self.pushButton.clicked.connect(close_downloads)
        Dialog.exec_()


    def downlaod_btn(self):
        global download_sts, res, stream_type, download_path, v_title
        link = self.URL_INPUT.text()

        
        try:
            if res != "mp4" or res!= "mp3":
                self.Error.setVisible(True)
        except:
            pass
           
        def downloadmp4(link):
            ydl_options = {
                "progress_hooks": [callable_hook],
                "format" : f"bestvideo[ext=mp4][format_note={res[0]}]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                'format_note': f'{res}',  # choice of quality
                'extractaudio': True,  # only keep the audio
                'audioformat': "mp3",  # convert to mp3
                'videoformat' : "mp4",
                'outtmpl': fr'{download_path}\%(title)s'+".mp4",  # name the file the ID of the video

            }
            with youtube_dl.YoutubeDL(ydl_options) as ydl:
                ydl.download([link])

        def downloadmp3(link):
            ydl_options = {
                "progress_hooks": [callable_hook],
                'format': 'bestaudio/best',
                'preferredquality': '192',
                'outtmpl': fr'{download_path}\%(title)s'+".mp3",  # name the file the ID of the video

            }
            with youtube_dl.YoutubeDL(ydl_options) as ydl:
                ydl.download([link])
            
          

        def callable_hook(response):
            if response["status"] == "downloading":
                speed = response["speed"]
              
                downloaded_percent = (response["downloaded_bytes"] * 100) / response["total_bytes"]
                self.PROGRESSBAR.setProperty("value", downloaded_percent)


        if download_sts == 'pending':
            self.DOWNLOAD_STATUS_INFO_LABEL.setText("Downloading")
            if stream_type == 'mp4':
                downloadmp4(link)
            else:
                downloadmp3(link)
            

            with open('assets\previous_downloads.txt','a',encoding='utf-8') as file:
                if stream_type == "mp4":
                    file.write(f"{v_title}(audio/video) - {datetime.datetime.now()}\n")
                else:
                    file.write(f"{v_title}(audio) - {datetime.datetime.now()}\n")
                
            self.DOWNLOAD_STATUS_INFO_LABEL.setText("Download Completed")
            self.QUALITY_EXT_RESOLUTION_LIST.clearSelection()
            self.SEARCH_FO_RESOLUTION_BTN.setText("Search for Resolutions")
            self.OPEN_DOWNLOAD.show()
            self.QUALITY_EXT_RESOLUTION_LIST.clear()
            download_sts = 'ready'

    def radioutput(self,b):
        global download_sts, stream_type
        if download_sts == 'ready':
            if b.text() == "video/audio (mp4)":
                if b.isChecked() == True:
                    ext = 'mp4'
                    stream_type = 'mp4'
                else:
                    ext = 'mp3'
                    stream_type = 'mp3'
           
        
        self.SEARCH_FO_RESOLUTION_BTN.setText("Search for Resolutions")
        self.QUALITY_EXT_RESOLUTION_LIST.clear()
                




    def search_for_res_clicked(self):
        global download_sts, v_title, res, stream_type, v_title
        link = self.URL_INPUT.text()
        valied = downloader.validator(link)
        if link and valied == "Link accepted":
            
            
            self.Error.setVisible(False)
            
            thumbnail = downloader.tumbnail(link)
            self.QUALITY_EXT_RESOLUTION_LIST.clear()
            self.THUMBNAIL_VIEW_AREA.show()
            self.THUMBNAIL_VIEW = QtWidgets.QLabel(self.centralwidget)
            self.pixmap = QPixmap(fr'{os.getcwd()}\cache\thumbnail.png')
            self.pixmap = self.pixmap.scaled(599, 299)
            self.THUMBNAIL_VIEW.setPixmap(self.pixmap)
            self.THUMBNAIL_VIEW.setGeometry(QtCore.QRect(501, 11, 0, 0))
            self.THUMBNAIL_VIEW.resize(self.pixmap.width(),
                                       self.pixmap.height(), )
            self.THUMBNAIL_VIEW.show()
            self.DOWNLOAD_STATUS_INFO_LABEL.setText("Pending")
            self.OPEN_DOWNLOAD.hide()
            self.PROGRESSBAR.setProperty("value", 0)

            v_title = downloader.video_title(link)
            v_views = downloader.video_views(link)
            v_length = downloader.video_length(link)
            v_age = downloader.video_age(link)

            

                
            
            self.VIDEO_TITLE_INPUT.show()
            self.VIDEO_TITLE_INPUT.setText(v_title)
            self.VIE_INFO.setText(str(v_views))
            self.LENGTH_INFO.setText(str(v_length))
            self.LANGUAGE_INFO.setText('en/us')
            self.AGE_RESTRICTIONS_INFO.setText(v_age)
            self.DOWNLOAD_STATUS_INFO_LABEL.setText("Pending")
            self.OPEN_DOWNLOAD.hide()
            
            

            if stream_type == 'mp3':
                q_list, size = downloader.quality_sizemp3(link)
                for i,k in enumerate(q_list):
                    
                    item = QtWidgets.QListWidgetItem()
                    self.QUALITY_EXT_RESOLUTION_LIST.addItem(item)
                    item = self.QUALITY_EXT_RESOLUTION_LIST.item(i)
                    if len(k) == 6: s = 18
                    elif len(k) == 7: s = 17
                    elif len(k) == 8: s = 15
                    elif len(k) == 9: s = 14                                     
                    x = "%10s %11s %15s %*s"%("medium","mp3",k,s,"audio")                    
                    item.setText(x)
                    
                self.SEARCH_FO_RESOLUTION_BTN.setText("Refresh")
                os.remove(rf'{os.getcwd()}\cache\thumbnail.png')
                download_sts = 'ready'
                res = "ready for resolution"
                
                
            else:
                q_list, size = downloader.quality_sizemp4(link)

                for i,k in enumerate(q_list):
                    
                    item = QtWidgets.QListWidgetItem()
                    self.QUALITY_EXT_RESOLUTION_LIST.addItem(item)
                    item = self.QUALITY_EXT_RESOLUTION_LIST.item(i)
                    if len(k) > 4:
                        if len(size[i]) == 6: s = 18
                        elif len(size[i]) == 7: s = 17
                        elif len(size[i]) == 8: s = 15
                        elif len(size[i]) == 9: s = 14
                        elif len(size[i]) == 10: s = 13
                        x = "%10s %13s %17s %*s"%(k,"mp4",size[i],s,"enabled")
                    else:
                        if len(size[i]) == 6: s = 17
                        elif len(size[i]) == 7: s = 16
                        elif len(size[i]) == 8: s = 15
                        elif len(size[i]) == 9: s = 14
                        elif len(size[i]) == 10: s = 12
                        x = "%10s %14s %17s %*s"%(k,"mp4",size[i],s,"enabled")
                    print(x)
                    item.setText(x)
                    
                self.SEARCH_FO_RESOLUTION_BTN.setText("Refresh")
                os.remove(rf'{os.getcwd()}\cache\thumbnail.png')
                download_sts = 'ready'
                res = "ready for resolution"
                
        else:
            pass

    def open_download(self):
        global v_title, stream_type
        if stream_type == 'mp4':
            subprocess.Popen(rf'explorer /open,"{download_path}\{v_title}.mp4"',encoding='utf-8')
            print(rf'explorer /open,"{download_path}\{v_title}.mp4"')
        else:
            subprocess.Popen(rf'explorer /open,"{download_path}\{v_title}.mp3"',encoding='utf-8')
            print(rf'explorer /open,"{download_path}\{v_title}.mp3"')

    def on_change(self):
        global download_sts, res
        self.Error.setVisible(False)
        res = [item.text() for item in self.QUALITY_EXT_RESOLUTION_LIST.selectedItems()]
        res = ''.join(res)
        res = res.split()
        download_sts = 'pending'

    def help(self):

        def close_help():
            Dialog.close()

        Dialog = QtWidgets.QDialog()
        Dialog.setModal(True)
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(892, 334)
        
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 871, 241))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 260, 731, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(760, 285, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        QtCore.QMetaObject.connectSlotsByName(Dialog)

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Help"))
        Dialog.setWindowIcon(QtGui.QIcon(r'icons\icon.ico'))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Tuber Help : -</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* Copy the link to the desired video and paste it into the URL section</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* If required, You can filter media from its extension.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* Click on the \'Search for resolution\' button, then Tuber will search for available media streams.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* Select a media stream</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* Click the Download button</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* Viola, now your video is ready to enjoy :-) :-)</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dialog", "Note:- This application is made for educational purposes only. So it has lot of bugs and crashes. \n"
"           If you have any concerns about using this application, please let me know."))
        self.pushButton.setText(_translate("Dialog", "Close"))

        self.pushButton.clicked.connect(close_help)
        Dialog.exec_()
        
        
    def close(self):
        sys.exit(app.exec_())



    def open_download_folder(self):
        subprocess.Popen(rf'explorer /open,"{os.getcwd()}\Downloads"')


    def quickstart(self):
        
        def close_quickstart():
            Dialog.close()

        Dialog = QtWidgets.QDialog()
        Dialog.setModal(True)
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(629, 368)

        
        
        self.Close = QtWidgets.QPushButton(Dialog)
        self.Close.setGeometry(QtCore.QRect(530, 330, 93, 28))
        self.Close.setObjectName("Close")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 611, 281))
        self.textBrowser.setObjectName("textBrowser")
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tuber Quick Start"))
        Dialog.setWindowIcon(QtGui.QIcon(r'icons\icon.ico'))
        self.Close.setText(_translate("Dialog", "Close"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Welcome to Tuber</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Quick Guid to start with Tuber :-</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">*</span><span style=\" font-size:11pt;\"> This is an experimental purpose application so you may </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">   experience many inconveniences while using this application.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">*</span><span style=\" font-size:11pt;\"> You can download youtube videos using this application.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">* </span><span style=\" font-size:11pt;\">Please don\'t use VPNs, Tunneling services with this application,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">   because some in-app installed plugins will against VPN protocols,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">   So you may experience many corruptions and bugs on this application. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">         </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">*</span><span style=\" font-size:11pt;\"> This is still a developing application, So not good for downloading  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">   videos higher than 2h.          </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">        </span></p></body></html>"))

        self.Close.clicked.connect(close_quickstart)
        Dialog.exec_()




    def plugins(self):
        
        def close_plugins():
            Dialog.close()

        Dialog = QtWidgets.QDialog()
        Dialog.setModal(True)
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(300, 476)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("asd")


        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 70, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 79, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(65)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")



        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(25, 130, 611, 279))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.graphicsView = QtWidgets.QGraphicsView(Dialog)

        self.THUMBNAIL_VIEW = QtWidgets.QLabel(Dialog)
        self.pixmap = QtGui.QPixmap(fr'{os.getcwd()}\icons\icon.ico')
        self.pixmap = self.pixmap.scaled(50, 50)
        self.THUMBNAIL_VIEW.setPixmap(self.pixmap)
        self.THUMBNAIL_VIEW.setGeometry(QtCore.QRect(55, 22, 31, 31))
        self.THUMBNAIL_VIEW.resize(self.pixmap.width(),
                                   self.pixmap.height(), )

        self.graphicsView.setGeometry(QtCore.QRect(65, 30, 31, 31))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 420, 93, 28))
        self.pushButton.setObjectName("pushButton")
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        ##################################################################

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Plugins"))
        Dialog.setWindowIcon(QtGui.QIcon(r'icons\icon.ico'))
        self.THUMBNAIL_VIEW.show()
        self.label.setText(_translate("Dialog", "Tuber")) 
        self.label_3.setText(_translate("Dialog", "In App Installed Plugins:- "))
        self.label_5.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"left\">Youtbe injector codec<br/>Python request<br>FTP injector<br>HTTPS input<br>Python winreg<br>SLSM codec<br>Pytube<br>FFMPEG<br>Real time py vlan<br>Python audio sepatizlizer<br>Image demuxer </p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Close"))

        self.pushButton.clicked.connect(close_plugins)

        Dialog.exec_()



    def about_tuber(self):

        def close_about_diolog():
            Dialog.close()

        Dialog = QtWidgets.QDialog()
        Dialog.setModal(True)
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(422, 436)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("asd")


        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 70, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 170, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 230, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 310, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)

        self.THUMBNAIL_VIEW = QtWidgets.QLabel(Dialog)
        self.pixmap = QtGui.QPixmap(fr'{os.getcwd()}\icons\icon.ico')
        self.pixmap = self.pixmap.scaled(50, 50)
        self.THUMBNAIL_VIEW.setPixmap(self.pixmap)
        self.THUMBNAIL_VIEW.setGeometry(QtCore.QRect(110, 22, 31, 31))
        self.THUMBNAIL_VIEW.resize(self.pixmap.width(),
                                   self.pixmap.height(), )

        self.graphicsView.setGeometry(QtCore.QRect(120, 30, 31, 31))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 400, 93, 28))
        self.pushButton.setObjectName("pushButton")
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        ##################################################################

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        Dialog.setWindowIcon(QtGui.QIcon(r'icons\icon.ico'))
        self.THUMBNAIL_VIEW.show()
        self.label.setText(_translate("Dialog", "Tuber"))
        self.label_2.setText(_translate("Dialog", "Version 1.1"))
        self.label_3.setText(_translate("Dialog", "Licenced To : Nipun Perera"))
        self.label_4.setText(_translate("Dialog", "Licenced Date : April, 2022"))
        self.label_5.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\">Ⓒ 2022 Nipun Perera,<br/>All Rights Reserved.</p></body></html>"))
        self.label_7.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\">www.nipunperera.com<br/>info@nipunperera.com<br/>(+94) 7* *** ****</p><p><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Close"))

        self.pushButton.clicked.connect(close_about_diolog)

        Dialog.exec_()


    def serch_for_upadates(self):

        def updater_close():
            Updater.close()

        Updater = QtWidgets.QDialog()
        Updater.setModal(True)
        Updater.setObjectName("Updater")
        Updater.resize(497, 170)
        self.label = QtWidgets.QLabel(Updater)
        self.label.setGeometry(QtCore.QRect(40, 10, 121, 41))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Updater)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Updater)
        self.label_4.setGeometry(QtCore.QRect(50, 80, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Updater)
        self.line.setGeometry(QtCore.QRect(160, 20, 321, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Updater)
        self.line_2.setGeometry(QtCore.QRect(470, 30, 20, 81))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Updater)
        self.line_3.setGeometry(QtCore.QRect(20, 100, 461, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Updater)
        self.line_4.setGeometry(QtCore.QRect(10, 30, 20, 81))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Updater)
        self.line_5.setGeometry(QtCore.QRect(20, 20, 16, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.pushButton = QtWidgets.QPushButton(Updater)
        self.pushButton.setGeometry(QtCore.QRect(390, 130, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Updater)
        self.pushButton_2.setGeometry(QtCore.QRect(232, 130, 131, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Updater)
        self.label_5.setGeometry(QtCore.QRect(250, 80, 271, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Updater)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 111, 21))
        self.label_2.setObjectName("label_2")

        QtCore.QMetaObject.connectSlotsByName(Updater)

        _translate = QtCore.QCoreApplication.translate
        Updater.setWindowTitle(_translate("Updater", "Updater"))
        Updater.setWindowIcon(QtGui.QIcon(r'icons\icon.ico'))
        self.label.setText(_translate("Updater",
                                      "<html><head/><body><p><span style=\" font-size:10pt;\">Product Details</span></p></body></html>"))
        self.label_3.setText(_translate("Updater", "Name :                      Tuber"))
        self.label_4.setText(_translate("Updater", "Installed Version :      1.1"))
        self.pushButton.setText(_translate("Updater", "Close"))
        self.pushButton_2.setText(_translate("Updater", "Cheack for Updates"))
        self.pushButton_2.setDisabled(True)
        self.label_5.setText(_translate("Updater", "(Latest)"))
        self.label_2.setText(_translate("Updater",
                                        "<html><head/><body><p><a href=\"https://nipunperera.com\"><span style=\" font-size:10pt; text-decoration: none; color:#0000ff;\">Options </span></a><a href=\"example.com\"></a></p></body></html>"))

        self.pushButton.clicked.connect(updater_close)
        Updater.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tuber"))
        MainWindow.setWindowIcon(QtGui.QIcon(r'icons\icon.ico'))
        self.DOWNLOAD_BTN.setText(_translate("MainWindow", "Download"))
        self.LENGTH_INFO.setText(_translate("MainWindow", ""))
        self.radioButton_3.setText(_translate("MainWindow", "audio only (mp3)"))
        self.radioButton.setChecked(True)
        self.LANGUAGE_INFO.setText(_translate("MainWindow", ""))
        self.DOWNLOAD_STATUS_INFO_LABEL.setText(_translate("MainWindow", "Pending"))
        self.VIDEO_TITLE_LABEL.setText(_translate("MainWindow", "Title :-"))
        
        self.Error.setText(_translate("MainWindow", "Please Select a Video Stream"))
        self.Error.setVisible(False)
        self.EXT_LEABEL.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">ext</span></p></body></html>"))
        self.OPEN_DOWNLOAD.hide()
        self.OPEN_DOWNLOAD.setText(_translate("MainWindow", "Open"))

        self.radioButton.setText(_translate("MainWindow", "video/audio (mp4)"))
        self.FILE_SIZE_LABEL.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">File Size</span></p></body></html>"))
        self.LANGUAGE_LABEL.setText(_translate("MainWindow", "Language :-"))
        self.URL_LABEL.setText(_translate("MainWindow", "URL"))
        self.AUDI_VIDEO_LABEL.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">audio/video</span></p></body></html>"))
        self.VIE_INFO.setText(_translate("MainWindow", ""))
        __sortingEnabled = self.QUALITY_EXT_RESOLUTION_LIST.isSortingEnabled()
        self.QUALITY_EXT_RESOLUTION_LIST.setSortingEnabled(False)
        self.QUALITY_EXT_RESOLUTION_LIST.setSortingEnabled(__sortingEnabled)
        self.SEARCH_FO_RESOLUTION_BTN.setText(_translate("MainWindow", "Search for resolutions"))
        self.LENGTH_LABEL.setText(_translate("MainWindow", "Length :-"))
        self.DOWNLOAD_STATUS_LABEL.setText(_translate("MainWindow", "Download Status :-"))
        self.AGE_RESTRICTION_LABEL.setText(_translate("MainWindow", "Age Restrictions :-"))
        self.RESOLUTION_TEXT_LABEL.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Resolution</span></p></body></html>"))
        self.FILTERFROMEXELABEL.setText(_translate("MainWindow", "Filter From Extention :-"))
        self.VIEW_LABEL.setText(_translate("MainWindow", "Views:-"))
        
        self.AGE_RESTRICTIONS_INFO.setText(_translate("MainWindow", ""))
        self.lineEdit_3.setText(_translate("MainWindow", f"{os.getcwd()}\Downloads"))
        self.BROWS_BTN.setText(_translate("MainWindow", "Download Path"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionPrevious_Downloads.setText(_translate("MainWindow", "Previous Downloads"))
        self.actionDownload_Folder.setText(_translate("MainWindow", "Download Folder"))
        self.actionTuber_Help.setText(_translate("MainWindow", "Tuber Help"))
        self.actionSearch_For_Updates.setText(_translate("MainWindow", "Search For Updates"))
        self.actionAbout_Tuber.setText(_translate("MainWindow", "About Tuber"))
        self.actionAbout_Plugins.setText(_translate("MainWindow", "Plugins"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# connect buttons to functions
        self.actionDownload_Folder.triggered.connect(self.open_download_folder)
        self.BROWS_BTN.clicked.connect(self.getfiles)
        self.actionClose.triggered.connect(self.close)
        self.SEARCH_FO_RESOLUTION_BTN.clicked.connect(self.search_for_res_clicked)
        self.QUALITY_EXT_RESOLUTION_LIST.itemSelectionChanged.connect(self.on_change)
        self.OPEN_DOWNLOAD.clicked.connect(self.open_download)
        self.DOWNLOAD_BTN.clicked.connect(self.downlaod_btn)
        self.actionSearch_For_Updates.triggered.connect(self.serch_for_upadates)
        self.actionTuber_Help.triggered.connect(self.help)
        self.actionAbout_Tuber.triggered.connect(self.about_tuber)
        self.actionAbout_Plugins.triggered.connect(self.plugins)
        self.actionPrevious_Downloads.triggered.connect(self.previous_downloads_file)
        self.radioButton_3.toggled.connect(lambda:self.radioutput(self.radioButton_3))
        self.radioButton.toggled.connect(lambda:self.radioutput(self.radioButton))
        try:
            f = open(fr"assets/registry.txt",'r')
            if f.read() == "0":
                self.quickstart()
                with open(fr"assets/registry.txt","w") as s:
                    p = 1
                    s.write(f"{p}")
        except:
            pass
        

if __name__ == "__main__":
    downloadpath = rf'{os.getcwd()}\Downloads'
    cachepath = rf'{os.getcwd()}\cache'
    if not os.path.exists(downloadpath):
        os.makedirs(downloadpath)
    if not os.path.exists(cachepath):
        os.makedirs(cachepath)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

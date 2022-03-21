import sys
import os
from tkinter import filedialog
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
def  getPaths():
## SET SERVER FOLDER
    ##  IF SERVER-FOLDER IS ALLREADY SET
    cachepath = os.getenv('APPDATA') + "\\HFServerUi"
    try:
        textLine = []
        file = open(f"{cachepath}\\cache")
        for line in file:
            textLine.append(line)
        serverFolder = textLine[0]
  

    ##  IF SERVER-FOLDER ISN'T SET
    except:
      try: os.mkdir(cachepath)
      except: pass
      serverFolder = filedialog.askdirectory(title="Chose your Server Directory" , initialdir="/")
      with open(f"{cachepath}\\cache", "w") as file:
        file.write(serverFolder)


## GET BATCH-FILE-PATHS
    pathList = []
    for root, dirs, files in os.walk(serverFolder):
        for file in files:
            if file.endswith('.bat'):
                 pathList.append(root+'/'+str(file))
    return(pathList)


paths = getPaths()
def pathNames():
    count = 0
    tempList = []
    global paths
    shortpath = []
    resList = []

    if len(paths) == 1:
        shortpath = paths


    else:
        for p1 in paths:
            for p2 in paths:
                singlepath = ""
                for i in range(0,len(p1)-1):
                    try:
                        if p1[i] != p2[i]:
                            singlepath += p1[i:]
                            break
                    except:
                        pass
                shortpath.append(singlepath)


    for i in range(1,(len(paths)**2)+1):
        count += 1
        tempList.append(shortpath[i-1])
        if count % len(paths) == 0:
            name_appereance = 0   
            for i in tempList:
                if i == "":
                    pass
                elif tempList.count(i) > name_appereance:
                    name_appereance = tempList.count(i)
                    name = i
            resList.append(name)
            tempList = []  
    return resList

## ==> MAIN WINDOW
from UI import Ui_MainWindow


## ==> GLOBALS
# YOUR APPLICATION
class Main_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        ## UI ==> INTERFACE CODES
        ########################################################################
        #Inserting Servers
        server_Name_List = pathNames()
        for i in server_Name_List:
          self.ui.ServerList.setRowCount(server_Name_List.index(i)+1)
          self.ui.ServerList.setItem(server_Name_List.index(i),0,QTableWidgetItem(f"{i}"))
        ## SET WINDOW POP UP IN FRONT
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ##REMOVE SCROLL BAR
        self.ui.ServerList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)    
        self.ui.frame.mouseMoveEvent = self.mouseMoveEvent


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


    ## ==> APP FUNCTIONS
    ########################################################################
    ##  CANCELBUTTON FUNCTION
        def cancelButtonClicked():
          self.close()
        self.ui.cancelButton.clicked.connect(cancelButtonClicked)


    ## ENABLE STARTBUTTON IS TIEM SELECTED
        self.ui.startButton.setDisabled(True)
        self.ui.ServerList.itemSelectionChanged.connect(lambda: self.ui.startButton.setDisabled(False))


    ## STARTBUTTON FUNCTION
        def startButtonClicked():
          focus = self.ui.ServerList.selectedIndexes()
          if not (focus == []):
            global paths
            path = paths[focus[0].row()]
            os.chdir(os.path.dirname(path))
            self.close()
            os.system(path)
          else: pass
        self.ui.startButton.clicked.connect(startButtonClicked)


                ## MOVE WINDOW BY DRAG
    def mousePressEvent(self, event):
      self.dragPos = event.globalPos()
    def mouseMoveEvent(self, event):
      if event.buttons() == QtCore.Qt.LeftButton:
        self.move(self.pos() + event.globalPos() - self.dragPos)
        self.dragPos = event.globalPos()
 

app = QApplication(sys.argv)
window = Main_Window()
sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.c=0
        self.d=0
        self.e=0
        self.f=0
        self.bat=0
        self.bowl=0
        self.ar=0
        self.wk=0
        self.selected=0
        self.points=1000
        self.used=0
        self.flag=0
        self.flags=0
        MainWindow.resize(800, 713)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(190, 230, 51, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(240, 230, 51, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(300, 230, 41, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(350, 230, 41, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(179, 259, 461, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout.addWidget(self.listWidget_2)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(186, 190, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 190, 47, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(416, 190, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 190, 47, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 225, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(180, 120, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(290, 120, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(400, 120, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(520, 120, 121, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(200, 140, 47, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(310, 140, 47, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(420, 140, 47, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(550, 140, 47, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 180, 20, 81))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(630, 180, 16, 81))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(170, 180, 16, 81))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(180, 170, 461, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 620, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(170, 80, 20, 101))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(630, 80, 20, 101))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(180, 70, 461, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(360, 260, 118, 3))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(150, 20, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(False)
        font.setUnderline(True)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(85, 170, 0);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(220, 560, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(290, 80, 47, 13))
        self.label_19.setObjectName("label_19")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionOpe_Team = QtWidgets.QAction(MainWindow)
        self.actionOpe_Team.setObjectName("actionOpe_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionOpe_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menuManage_Teams.addSeparator()
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.pushButton.clicked.connect(self.closeapplication)
        self.radioButton.toggled.connect(self.availableplayers)
        self.radioButton_2.toggled.connect(self.availableplayers)
        self.radioButton_3.toggled.connect(self.availableplayers)
        self.radioButton_4.toggled.connect(self.availableplayers)
        self.listWidget_2.itemDoubleClicked.connect(self.removelist1)
        self.listWidget.itemDoubleClicked.connect(self.removelist2)
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "BAT"))
        self.radioButton_2.setText(_translate("MainWindow", "BOWL"))
        self.radioButton_3.setText(_translate("MainWindow", "AR"))
        self.radioButton_4.setText(_translate("MainWindow", "WK"))
        self.label_16.setText(_translate("MainWindow", "       ->      "))
        self.label.setText(_translate("MainWindow", "Points Available :"))
        self.label_2.setText(_translate("MainWindow", "1000"))
        self.label_3.setText(_translate("MainWindow", "Points Used :"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Team Name  :"))
        self.label_7.setText(_translate("MainWindow", "Your Selections"))
        self.label_8.setText(_translate("MainWindow", "Batsman(BAT)"))
        self.label_9.setText(_translate("MainWindow", "Bowlers(BOWL)"))
        self.label_10.setText(_translate("MainWindow", "AllRounders(AR)"))
        self.label_11.setText(_translate("MainWindow", "Wicket-keeper(WK)"))
        self.label_12.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "Exit Application"))
        self.label_17.setText(_translate("MainWindow", "Welcome to Fantasy cricket league"))
        self.label_18.setText(_translate("MainWindow", "For selecting or deselecting double click the player name"))
        self.label_19.setText(_translate("MainWindow", "->"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionOpe_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))
    #
    def closeapplication(self):
        self.showdlg('Do you really want to close???')
        sys.exit()
    def menu(self,action):
        txt=action.text()
        if(txt=='New Team'):
            self.bat=0
            self.bowl=0
            self.ar=0
            self.wk=0
            self.listWidget_2.clear()
            self.listWidget.clear()
            self.selected=0
            self.points=1000
            self.used=0
            self.flag=0
            self.c=0
            self.d=0
            self.e=0
            self.f=0
            text, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter name of team:")
            sql4="select count(name) from teams where name='"+str(text)+"' ;"
            curschool.execute(sql4)
            rec=curschool.fetchall()
            if(str(rec[0][0])>str(0)):
                self.flags=1
            if (ok and self.flags==0 ):
                self.label_6.setText(str(text))
            else:
                self.showdlg('This name already exists!!')
            self.show()
        elif(txt=='Save Team'):
            count=self.listWidget.count()
            select=""
            for i in range(count):
                select+=self.listWidget.item(i).text()
                if i<(count-1):
                    select+=","
            if((self.bat+self.bowl+self.ar+self.wk)!=11):
                self.showdlg("Insufficient Players")
            else:
                sql2="insert into teams (name,players,value) values('"+self.label_6.text()+"','"+ select+"','"+str(self.used)+"');"
                try:
                    curschool.execute(sql2)
                    self.showdlg("Team saved successfully!!")
                    match.commit()
                except:
                    self.showdlg("Error!!")
                    match.rollback()
        elif(txt=='Open Team'):          
            self.openteam()
        elif(txt=='Evaluate Team'):
            from score import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()
    def show(self):
        self.label_2.setText(str(1000))
        self.label_4.setText(str(0))
        self.label_12.setText(str(0))
        self.label_13.setText(str(0))
        self.label_14.setText(str(0))
        self.label_15.setText(str(0))
    def openteam(self):
        text, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter name of team you want to view..")
        if ok:
            sql5="select * from teams"
            sql3="select players from teams where name='"+str(text)+"';"
            self.listWidget_2.clear()
            self.listWidget.clear()
            sis=curschool.execute(sql3)
            recordss=sis.fetchone()
            if(recordss==None):
                self.showdlg("No such team exists")
            else:
                self.bat=0
                self.bowl=0
                self.wk=0
                self.ar=0
                a=(recordss[0].split(','))
                self.listWidget.addItems(a)
                self.label_6.setText(str(text))
                sql9="select value from teams where name='"+str(text)+"';"
                pin=curschool.execute(sql9)
                r=pin.fetchone()
                r=r[0]
                p=1000-int(r)
                self.label_4.setText(str(r))
                self.label_2.setText(str(p))
                self.points=(str(p))
                self.used=str(r)
                sql11="delete from teams where name='"+str(text)+"';"
                curschool.execute(sql11)
                match.commit()
                for i in range(self.listWidget.count()):
                    x=self.listWidget.item(i).text()
                    sql10="select ctg from stats where player='"+str(x)+"';"
                    pins=curschool.execute(sql10)
                    y=pins.fetchone()
                    if(y[0]=='BAT'):
                        self.bat=self.bat+1
                    elif(y[0]=="BWL"):
                        self.bowl=self.bowl+1
                    elif(y[0]=="WK"):
                        self.wk=self.wk+1
                    elif(y[0]=='AR'):
                        self.ar=self.ar+1
                self.label_12.setText(str(self.bat))
                self.label_13.setText(str(self.bowl))
                self.label_14.setText(str(self.wk))
                self.label_15.setText(str(self.ar))   
    def showdlg(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Dream Team selector")
        ret=Dialog.exec()
    def availableplayers(self):
        if (self.radioButton.isChecked()==True):
            sql="select player from stats where ctg='BAT'; "
            curschool.execute(sql)
            record=curschool.fetchall()
            for i in record:
                if(self.c==0):
                    self.listWidget_2.addItem(i[0])
                elif(self.c==1):
                    self.listWidget_2.clear()
                    self.listWidget_2.addItem(i[0])
                    self.c=0
            self.c=self.c+1
        elif (self.radioButton_2.isChecked()==True):
            sql="select player from stats where ctg='BWL'; "
            curschool.execute(sql)
            record=curschool.fetchall()
            for i in record:
                if(self.d==0):
                    self.listWidget_2.addItem(i[0])
                elif(self.d==1):
                    self.listWidget_2.clear()
                    self.listWidget_2.addItem(i[0])
                    self.d=0
            self.d=self.d+1
        elif (self.radioButton_3.isChecked()==True):
            sql="select player from stats where ctg='AR'; "
            curschool.execute(sql)
            record=curschool.fetchall()
            for i in record:
                if(self.e==0):
                    self.listWidget_2.addItem(i[0])
                elif(self.e==1):
                    self.listWidget_2.clear()
                    self.listWidget_2.addItem(i[0])
                    self.e=0
            self.e=self.e+1
        elif (self.radioButton_4.isChecked()==True):
            sql="select player from stats where ctg='WK'; "
            curschool.execute(sql)
            record=curschool.fetchall()
            for i in record:
                if(self.f==0):
                    self.listWidget_2.addItem(i[0])
                elif(self.f==1):
                    self.listWidget_2.clear()
                    self.listWidget_2.addItem(i[0])
                    self.f=0
            self.f=self.f+1
    def removelist1(self, item):
        if(self.selected == 11 ):
            self.showdlg('You cannot select more than 11 players')
        if(self.flag==0 and self.selected==10 and self.wk==0):
            self.flag=1
            self.showdlg("Its a one time reminder Important to pick a Wicketkeeper as it increases chence of wiining!!!!")
        elif(self.radioButton.isChecked()==True and self.selected<=11 and self.points>0):
            if(self.bat==5):
                self.showdlg('You cannot select more than 5 batsman')
            else:
                sql="select value from stats where player='"+item.text()+"';"
                curschool.execute(sql)
                re=curschool.fetchall()
                value=re[0][0]
                self.used=self.used+value
                self.points=self.points-value
                if(self.points<=0):
                    self.points=self.points+value
                    self.used=self.used-value
                    self.showdlg(' As you ran out of points Either click on Exit application or select any other player than  "'+item.text()+'" ' )
                else:
                    self.label_2.setText(str(self.points))
                    self.label_4.setText(str(self.used))
                    self.listWidget_2.takeItem(self.listWidget_2.row(item))
                    self.listWidget.addItem(item.text())
                    self.bat=self.bat+1
                    self.label_12.setText(str(self.bat))
                    self.selected=self.selected+1
        elif(self.radioButton_2.isChecked()==True and self.selected<=11 and self.points>0): 
            if(self.bowl==5):
                self.showdlg('You cannot select more than 5 bowlers')
            else:
                sql="select value from stats where player='"+item.text()+"';"
                curschool.execute(sql)
                re=curschool.fetchall()
                value=re[0][0]
                self.points=self.points-value
                self.used=self.used+value
                if(self.points<=0):
                    self.points=self.points+value
                    self.used=self.used-value
                    self.showdlg(' As you ran out of points Either click on Exit application or select any other player than  "'+item.text()+'" ')
                else:
                    self.label_2.setText(str(self.points))
                    self.label_4.setText(str(self.used))
                    self.listWidget_2.takeItem(self.listWidget_2.row(item))
                    self.listWidget.addItem(item.text())
                    self.bowl=self.bowl+1
                    self.label_13.setText(str(self.bowl))
                    self.selected=self.selected+1
        elif(self.radioButton_3.isChecked()==True and self.selected<=11 and self.points>0):
            if(self.ar==1):
                self.showdlg('You cannot select more than 1 AllRounder')
            else:
                sql="select value from stats where player='"+item.text()+"';"
                curschool.execute(sql)
                re=curschool.fetchall()
                value=re[0][0]
                self.points=self.points-value
                self.used=self.used+value
                if(self.points<=0):
                    self.points=self.points+value
                    self.used=self.used-value
                    self.showdlg('As you ran out of points Either click on Exit application or select any other player than  "'+item.text()+'" ')
                else:
                    self.label_2.setText(str(self.points))
                    self.label_4.setText(str(self.used))
                    self.listWidget_2.takeItem(self.listWidget_2.row(item))
                    self.listWidget.addItem(item.text())
                    self.ar=self.ar+1
                    self.label_14.setText(str(self.ar))
                    self.selected=self.selected+1
        elif(self.radioButton_4.isChecked()==True and self.selected<=11 and self.points>0):
            if(self.wk==1):
                self.showdlg('You cannot select more than 1 WicketKeeper')
            else:
                sql="select value from stats where player='"+item.text()+"';"
                curschool.execute(sql)
                re=curschool.fetchall()
                value=re[0][0]
                self.points=self.points-value
                self.used=self.used+value
                if(self.points<=0):
                    self.points=self.points+value
                    self.used=self.used-value
                    self.showdlg(' As you ran out of points Either click on Exit application or select any other player than  "'+item.text()+'" ')
                else:
                    self.label_2.setText(str(self.points))
                    self.label_4.setText(str(self.used))
                    self.listWidget_2.takeItem(self.listWidget_2.row(item))
                    self.listWidget.addItem(item.text())
                    self.wk=self.wk+1
                    self.label_15.setText(str(self.wk))
                    self.selected=self.selected+1
    def removelist2(self,item):
        self.listWidget.takeItem(self.listWidget.row(item))
        sql="SELECT player,value, ctg from stats where player='"+item.text()+"'"
        curschool.execute(sql)
        row=curschool.fetchall()
        cate=row[0][2]
        value=row[0][1]
        self.points=int(self.points)+value
        self.used=int(self.used)-value
        self.label_2.setText(str(self.points))
        self.label_4.setText(str(self.used))
        if(cate=='BAT'):
            self.bat=self.bat-1
            self.selected=self.selected-1
            self.label_12.setText(str(self.bat))
        if(cate=='BWL'):
            self.bowl=self.bowl-1
            self.selected=self.selected-1
            self.label_13.setText(str(self.bowl))
        if(cate=='AR'):
            self.ar=self.ar-1
            self.selected=self.selected-1
            self.label_14.setText(str(self.ar))
        if(cate=='WK'):
            self.wk=self.wk-1
            self.selected=self.selected-1
            self.label_15.setText(str(self.wk))
        self.listWidget_2.addItem(item.text())
if __name__ == "__main__":
    import sqlite3
    match=sqlite3.connect('fantasy.db')
    curschool=match.cursor()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(573, 466)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(50, 100, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(37, 50, 511, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(410, 70, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(400, 100, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        # importing all the team names in the combobox
        import sqlite3
        match=sqlite3.connect('fantasy.db')
        curschool=match.cursor()
        sql="select name from teams;"
        v=curschool.execute(sql)
        for roe in v:
            self.comboBox.addItem(roe[0])
        self.list = QtWidgets.QListWidget(Dialog)
        self.list.setGeometry(QtCore.QRect(40, 200, 191, 192))
        self.list.setObjectName("list")
        self.list2 = QtWidgets.QListWidget(Dialog)
        self.list2.setGeometry(QtCore.QRect(360, 200, 201, 192))
        self.list2.setObjectName("list2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 420, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.totalprint = QtWidgets.QLabel(Dialog)
        self.totalprint.setGeometry(QtCore.QRect(430, 420, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.totalprint.setFont(font)
        self.totalprint.setObjectName("totalprint")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 170, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(430, 170, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_2.clicked.connect(self.calculate)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Points will be displayed below in the score section"))
        self.label_2.setText(_translate("Dialog", "Select Team name"))
        self.label_3.setText(_translate("Dialog", "Select Match"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "match1"))
        self.pushButton_2.setText(_translate("Dialog", "Calculate Score"))
        self.totalprint.setText(_translate("Dialog", "0"))
        self.label_5.setText(_translate("Dialog", "Players"))
        self.label_6.setText(_translate("Dialog", "Points"))
    #function for calculating the score of the team
    def calculate(self):
        import sqlite3
        match=sqlite3.connect('fantasy.db')
        curschool=match.cursor()
        team=self.comboBox.currentText()
        sql7="select players from teams where name='"+str(team)+"';"
        curschool.execute(sql7)
        roww=curschool.fetchone()
        c=roww[0].split(',')
        self.list.addItems(c)
        teamttl=0
        for i in range (self.list.count()):
            ttl=0
            batscore=0
            fieldscore=0
            bowlscore=0
            nm=self.list.item(i).text()
            sql8="select * from match where player ='"+str(nm)+"';"
            curschool.execute(sql8)
            ree=curschool.fetchone()
            #calculating the fieldpoint for every player
            fieldscore=10*(int(ree[11])+int(ree[9])+int(ree[10]))
            #calculating the batpoint for every player
            if(int(ree[1]>=50)):
                batscore=batscore+5
            if(int(ree[1]>=100)):
                batscore=batscore+10
            if(int(ree[1])>0 and int(ree[2])>0):
                if((int(ree[1])/int(ree[2])*100)>=80 and (int(ree[1])/int(ree[2])*100)<=100):
                    batscore=batscore+2
            if(int(ree[1])>0 and int(ree[2])>0):
                if((int(ree[1])/int(ree[2])*100)>100):
                    batscore=batscore+4
            batscore=batscore+(int(ree[3])*1)+(int(ree[4]*2))
            # calulating bowlpoint for every player
            bowlscore=bowlscore+int(ree[8]*10)
            if((int(ree[8])>=5)):
                bowlscore=bowlscore+10
            if((int(ree[8])>=3) and (int(ree[8])<5)):
                bowlscsore=bowlscore+5
            if(int(ree[7]/(int(ree[5]/6)>=3.5 and int(ree[7]/(int(ree[5]/6)<=4.5 and int(ree[7]>0) and int(ree[5]>0)))))):
                bowlscore=bowlscore+4
            if(int(ree[7]/int(ree[5]/6))<2 and int(ree[7]>0) and int(ree[5]>0)):
                bowlscore=bowlscore+10
            if(int(ree[7]/int(ree[5]/6))>=2 and int(ree[7]/(int(ree[5]/6))<3.5 and int(ree[7]>0) and int(ree[5]>0))):
                bowlscore=bowlscore+7
            ttl=bowlscore+batscore+fieldscore
            self.list2.addItem(str(ttl))
            # aggregating the teampoint
            teamttl=teamttl+ttl
        self.totalprint.setText(str(teamttl))
if __name__ == "__main__":
    import sqlite3
    match=sqlite3.connect('fantasy.db')
    curschool=match.cursor()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

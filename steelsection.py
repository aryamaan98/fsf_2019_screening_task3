from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from MainWindow import Ui_Steel
import sqlite3
import xlrd

class MainWindow(QMainWindow, Ui_Steel):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.conn = sqlite3.connect('steel_sections.sqlite')
        self.c = self.conn.cursor()

        self.connections()
        self.show()
    def connections(self):
        self.pushButton_a_load.clicked.connect(self.LoadAngle)
        self.pushButton_b_load.clicked.connect(self.LoadBeam)
        self.pushButton_c_load.clicked.connect(self.LoadChannel)
        self.pushButton_a_clear.clicked.connect(self.clear_a)
        self.pushButton_b_clear.clicked.connect(self.clear_b)
        self.pushButton_c_clear.clicked.connect(self.clear_c)
        self.pushButton_a_add.clicked.connect(self.add_a)
        self.pushButton_b_add.clicked.connect(self.add_b)
        self.pushButton_c_add.clicked.connect(self.add_c)
        self.pushButton_a_import.clicked.connect(self.import_a)
        self.pushButton_b_import.clicked.connect(self.import_b)
        self.pushButton_c_import.clicked.connect(self.import_c)
        self.pushButton_exit.clicked.connect(self.exit)
    def LoadAngle(self):
        designation = []
        self.c.execute("select * from Angles")
        data_angles = self.c.fetchall()
        for i in data_angles:
            designation.append(i[1])
        input_angle,ok=QtWidgets.QInputDialog.getItem(self,"ANGLES","Select from following Designations",designation,0,False)
        if ok:
            self.c.execute("select * from Angles where Designation='"+input_angle+"';")
            data = self.c.fetchall()
            for i in data:
                self.lineEdit_100.setText(str(i[0]))
                self.lineEdit_101.setText(str(i[1]))
                self.lineEdit_102.setText(str(i[2]))
                self.lineEdit_103.setText(str(i[3]))
                self.lineEdit_104.setText(str(i[4]))
                self.lineEdit_105.setText(str(i[5]))
                self.lineEdit_106.setText(str(i[6]))
                self.lineEdit_107.setText(str(i[7]))
                self.lineEdit_108.setText(str(i[8]))
                self.lineEdit_109.setText(str(i[9]))
                self.lineEdit_110.setText(str(i[10]))
                self.lineEdit_111.setText(str(i[11]))
                self.lineEdit_112.setText(str(i[12]))
                self.lineEdit_113.setText(str(i[13]))
                self.lineEdit_114.setText(str(i[14]))
                self.lineEdit_115.setText(str(i[15]))
                self.lineEdit_116.setText(str(i[16]))
                self.lineEdit_117.setText(str(i[17]))
                self.lineEdit_118.setText(str(i[18]))
                self.lineEdit_119.setText(str(i[19]))
                self.lineEdit_120.setText(str(i[20]))
                self.lineEdit_121.setText(str(i[21]))
                self.lineEdit_122.setText(str(i[22]))
                self.lineEdit_123.setText(str(i[23]))
        else:
            pass
    def LoadBeam(self):
        designation = []
        self.c.execute("select * from Beams")
        data_beams = self.c.fetchall()
        for i in data_beams:
            designation.append(i[1])
        input_beam,ok=QtWidgets.QInputDialog.getItem(self,"BEAMS","Select from following Designations",designation,0,False)
        if ok:
            self.c.execute("select * from Beams where Designation='"+input_beam+"';")
            data = self.c.fetchall()
            for i in data:
                self.lineEdit_200.setText(str(i[0]))
                self.lineEdit_201.setText(str(i[1]))
                self.lineEdit_202.setText(str(i[2]))
                self.lineEdit_203.setText(str(i[3]))
                self.lineEdit_204.setText(str(i[4]))
                self.lineEdit_205.setText(str(i[5]))
                self.lineEdit_206.setText(str(i[6]))
                self.lineEdit_207.setText(str(i[7]))
                self.lineEdit_208.setText(str(i[8]))
                self.lineEdit_209.setText(str(i[9]))
                self.lineEdit_210.setText(str(i[10]))
                self.lineEdit_211.setText(str(i[11]))
                self.lineEdit_212.setText(str(i[12]))
                self.lineEdit_213.setText(str(i[13]))
                self.lineEdit_214.setText(str(i[14]))
                self.lineEdit_215.setText(str(i[15]))
                self.lineEdit_216.setText(str(i[16]))
                self.lineEdit_217.setText(str(i[17]))
                self.lineEdit_218.setText(str(i[18]))
                self.lineEdit_219.setText(str(i[19]))
        else:
            pass
    def LoadChannel(self):
        designation = []
        self.c.execute("select * from Channels")
        data_angles = self.c.fetchall()
        for i in data_angles:
            designation.append(i[1])
        input_channel,ok=QtWidgets.QInputDialog.getItem(self,"Channels","Select from following Designations",designation,0,False)
        if ok:
            self.c.execute("select * from Channels where Designation='"+input_channel+"';")
            data = self.c.fetchall()
            for i in data:
                self.lineEdit_300.setText(str(i[0]))
                self.lineEdit_301.setText(str(i[1]))
                self.lineEdit_302.setText(str(i[2]))
                self.lineEdit_303.setText(str(i[3]))
                self.lineEdit_304.setText(str(i[4]))
                self.lineEdit_305.setText(str(i[5]))
                self.lineEdit_306.setText(str(i[6]))
                self.lineEdit_307.setText(str(i[7]))
                self.lineEdit_308.setText(str(i[8]))
                self.lineEdit_309.setText(str(i[9]))
                self.lineEdit_310.setText(str(i[10]))
                self.lineEdit_311.setText(str(i[11]))
                self.lineEdit_312.setText(str(i[12]))
                self.lineEdit_313.setText(str(i[13]))
                self.lineEdit_314.setText(str(i[14]))
                self.lineEdit_315.setText(str(i[15]))
                self.lineEdit_316.setText(str(i[16]))
                self.lineEdit_317.setText(str(i[17]))
                self.lineEdit_318.setText(str(i[18]))
                self.lineEdit_319.setText(str(i[19]))
                self.lineEdit_320.setText(str(i[20]))
        else:
            pass
    def clear_a(self):
        self.lineEdit_100.setText("")
        self.lineEdit_101.setText("")
        self.lineEdit_102.setText("")
        self.lineEdit_103.setText("")
        self.lineEdit_104.setText("")
        self.lineEdit_105.setText("")
        self.lineEdit_106.setText("")
        self.lineEdit_107.setText("")
        self.lineEdit_108.setText("")
        self.lineEdit_109.setText("")
        self.lineEdit_110.setText("")
        self.lineEdit_111.setText("")
        self.lineEdit_112.setText("")
        self.lineEdit_113.setText("")
        self.lineEdit_114.setText("")
        self.lineEdit_115.setText("")
        self.lineEdit_116.setText("")
        self.lineEdit_117.setText("")
        self.lineEdit_118.setText("")
        self.lineEdit_119.setText("")
        self.lineEdit_120.setText("")
        self.lineEdit_121.setText("")
        self.lineEdit_122.setText("")
        self.lineEdit_123.setText("")
        QMessageBox.question(self,"Clear Filed","Done !",QMessageBox.Ok,QMessageBox.Ok)
    def clear_b(self):
        self.lineEdit_200.setText("")
        self.lineEdit_201.setText("")
        self.lineEdit_202.setText("")
        self.lineEdit_203.setText("")
        self.lineEdit_204.setText("")
        self.lineEdit_205.setText("")
        self.lineEdit_206.setText("")
        self.lineEdit_207.setText("")
        self.lineEdit_208.setText("")
        self.lineEdit_209.setText("")
        self.lineEdit_210.setText("")
        self.lineEdit_211.setText("")
        self.lineEdit_212.setText("")
        self.lineEdit_213.setText("")
        self.lineEdit_214.setText("")
        self.lineEdit_215.setText("")
        self.lineEdit_216.setText("")
        self.lineEdit_217.setText("")
        self.lineEdit_218.setText("")
        self.lineEdit_219.setText("")
        QMessageBox.question(self,"Clear Filed","Done !",QMessageBox.Ok,QMessageBox.Ok)
    def clear_c(self):
        self.lineEdit_300.setText("")
        self.lineEdit_301.setText("")
        self.lineEdit_302.setText("")
        self.lineEdit_303.setText("")
        self.lineEdit_304.setText("")
        self.lineEdit_305.setText("")
        self.lineEdit_306.setText("")
        self.lineEdit_307.setText("")
        self.lineEdit_308.setText("")
        self.lineEdit_309.setText("")
        self.lineEdit_310.setText("")
        self.lineEdit_311.setText("")
        self.lineEdit_312.setText("")
        self.lineEdit_313.setText("")
        self.lineEdit_314.setText("")
        self.lineEdit_315.setText("")
        self.lineEdit_316.setText("")
        self.lineEdit_317.setText("")
        self.lineEdit_318.setText("")
        self.lineEdit_319.setText("")
        self.lineEdit_320.setText("")
        QMessageBox.question(self,"Clear Filed","Done !",QMessageBox.Ok,QMessageBox.Ok)
    def add_a(self):
        if self.empty_field("a") == False:
            QMessageBox.question(self,"Error","Fields can't be empty .",QMessageBox.Ok,QMessageBox.Ok)
        elif str(self.lineEdit_100.text()).isnumeric() == False:
            QMessageBox.question(self,"Error","ID should be an integer .",QMessageBox.Ok,QMessageBox.Ok)
        else:
            self.c.execute("select Id from Angles where Id =?",(str(self.lineEdit_100.text()),))
            q_check = self.c.fetchall()
            if q_check:
                QMessageBox.question(self,"Error","Steel with this id already exists. ",QMessageBox.Ok,QMessageBox.Ok)
            else:
                query = "insert into Angles values ('"+str(self.lineEdit_100.text())+"','"+str(self.lineEdit_101.text())+"','"+str(self.lineEdit_102.text())+"','"+str(self.lineEdit_103.text())+"',\
                    '"+str(self.lineEdit_104.text())+"','"+str(self.lineEdit_105.text())+"','"+str(self.lineEdit_106.text())+"','"+str(self.lineEdit_107.text())+"',\
                        '"+str(self.lineEdit_108.text())+"','"+str(self.lineEdit_109.text())+"','"+str(self.lineEdit_110.text())+"','"+str(self.lineEdit_111.text())+"',\
                            '"+str(self.lineEdit_112.text())+"','"+str(self.lineEdit_113.text())+"','"+str(self.lineEdit_114.text())+"','"+str(self.lineEdit_115.text())+"',\
                            '"+str(self.lineEdit_116.text())+"','"+str(self.lineEdit_117.text())+"','"+str(self.lineEdit_118.text())+"','"+str(self.lineEdit_119.text())+"',\
                                '"+str(self.lineEdit_120.text())+"','"+str(self.lineEdit_121.text())+"','"+str(self.lineEdit_122.text())+"','"+str(self.lineEdit_123.text())+"');"
                self.c.execute(query)
                self.conn.commit()
                QMessageBox.question(self,"Adding Angles","Done !",QMessageBox.Ok,QMessageBox.Ok)
    def add_b(self):
        if self.empty_field("b") == False:
            QMessageBox.question(self,"Error","Fields can't be empty .",QMessageBox.Ok,QMessageBox.Ok)
        elif str(self.lineEdit_200.text()).isnumeric() == False:
            QMessageBox.question(self,"Error","ID should be an integer .",QMessageBox.Ok,QMessageBox.Ok)
        else:
            self.c.execute("select Id from Beams where Id =?",(str(self.lineEdit_200.text()),))
            q_check = self.c.fetchall()
            if q_check:
                QMessageBox.question(self,"Error","Steel with this id already exists. ",QMessageBox.Ok,QMessageBox.Ok)
            else:
                query = "insert into Beams values ('"+str(self.lineEdit_200.text())+"','"+str(self.lineEdit_201.text())+"','"+str(self.lineEdit_202.text())+"','"+str(self.lineEdit_203.text())+"',\
                    '"+str(self.lineEdit_204.text())+"','"+str(self.lineEdit_205.text())+"','"+str(self.lineEdit_206.text())+"','"+str(self.lineEdit_207.text())+"',\
                        '"+str(self.lineEdit_208.text())+"','"+str(self.lineEdit_209.text())+"','"+str(self.lineEdit_210.text())+"','"+str(self.lineEdit_211.text())+"',\
                            '"+str(self.lineEdit_212.text())+"','"+str(self.lineEdit_213.text())+"','"+str(self.lineEdit_214.text())+"','"+str(self.lineEdit_215.text())+"',\
                            '"+str(self.lineEdit_216.text())+"','"+str(self.lineEdit_217.text())+"','"+str(self.lineEdit_218.text())+"','"+str(self.lineEdit_219.text())+"');"
                self.c.execute(query)
                self.conn.commit()
                QMessageBox.question(self,"Adding Beams","Done !",QMessageBox.Ok,QMessageBox.Ok)
    def add_c(self):
        if self.empty_field("c") == False:
            QMessageBox.question(self,"Error","Fields can't be empty .",QMessageBox.Ok,QMessageBox.Ok)
        elif str(self.lineEdit_300.text()).isnumeric() == False:
            QMessageBox.question(self,"Error","ID should be an integer .",QMessageBox.Ok,QMessageBox.Ok)
        else:
            self.c.execute("select Id from Channels where Id =?",(str(self.lineEdit_300.text()),))
            q_check = self.c.fetchall()
            if q_check:
                QMessageBox.question(self,"Error","Steel with this id already exists. ",QMessageBox.Ok,QMessageBox.Ok)
            else:
                query = "insert into Channels values ('"+str(self.lineEdit_300.text())+"','"+str(self.lineEdit_301.text())+"','"+str(self.lineEdit_302.text())+"','"+str(self.lineEdit_303.text())+"',\
                    '"+str(self.lineEdit_304.text())+"','"+str(self.lineEdit_305.text())+"','"+str(self.lineEdit_306.text())+"','"+str(self.lineEdit_307.text())+"',\
                        '"+str(self.lineEdit_308.text())+"','"+str(self.lineEdit_309.text())+"','"+str(self.lineEdit_310.text())+"','"+str(self.lineEdit_311.text())+"',\
                            '"+str(self.lineEdit_312.text())+"','"+str(self.lineEdit_313.text())+"','"+str(self.lineEdit_314.text())+"','"+str(self.lineEdit_315.text())+"',\
                            '"+str(self.lineEdit_316.text())+"','"+str(self.lineEdit_317.text())+"','"+str(self.lineEdit_318.text())+"','"+str(self.lineEdit_319.text())+"',\
                                '"+str(self.lineEdit_320.text())+"');"
                self.c.execute(query)
                self.conn.commit()
                QMessageBox.question(self,"Adding Channels","Done !",QMessageBox.Ok,QMessageBox.Ok)
    def import_a(self):
        book = xlrd.open_workbook('new_sections.xlsx')
        second_sheet = book.sheet_by_index(1)
        id_list = []
        for i in range(1,second_sheet.nrows):
            id_list.append(str(int(second_sheet.row_values(i)[0])))
        input_id,ok=QtWidgets.QInputDialog.getItem(self,"Import Angles","Select an id to import its data",id_list,0,False)
        if ok:
            data = second_sheet.row_values(int(input_id) - 6)
            self.c.execute("select Id from Angles where Id =?",(int(input_id),))
            q_check = self.c.fetchall()
            if q_check:
                QMessageBox.question(self,"Error","Steel with this id is already imported. ",QMessageBox.Ok,QMessageBox.Ok)
            else:
                query = "insert into Angles values ('"+str(data[0])+"','"+str(data[1])+"','"+str(data[2])+"','"+str(data[3])+"','"+str(data[4])+"','"+str(data[5])+"','"+str(data[6])+"','"+str(data[7])+"','"+str(data[8])+"',\
                    '"+str(data[9])+"','"+str(data[10])+"','"+str(data[11])+"','"+str(data[12])+"','"+str(data[13])+"','"+str(data[14])+"','"+str(data[15])+"','"+str(data[16])+"','"+str(data[17])+"','"+data[18]+"','"+data[19]+"','"+data[20]+"',\
                        '"+str(data[21])+"','"+str(data[22])+"','"+str(data[23])+"');"
                self.c.execute(query)
                self.conn.commit()
                QMessageBox.question(self,"Adding Angles","Done !",QMessageBox.Ok,QMessageBox.Ok)
        else:
            pass
    def import_b(self):
        book = xlrd.open_workbook('new_sections.xlsx')
        first_sheet = book.sheet_by_index(0)
        id_list = []
        for i in range(1,first_sheet.nrows):
            id_list.append(str(int(first_sheet.row_values(i)[0])))
        input_id,ok=QtWidgets.QInputDialog.getItem(self,"Import Beams","Select an id to import its data",id_list,0,False)
        if ok:
            data = first_sheet.row_values(int(input_id) - 9)
            self.c.execute("select Id from Beams where Id =?",(int(input_id),))
            q_check = self.c.fetchall()
            if q_check:
                QMessageBox.question(self,"Error","Steel with this id is already imported. ",QMessageBox.Ok,QMessageBox.Ok)
            else:
                query = "insert into Beams values ('"+str(data[0])+"','"+str(data[1])+"','"+str(data[2])+"','"+str(data[3])+"','"+str(data[4])+"','"+str(data[5])+"','"+str(data[6])+"','"+str(data[7])+"','"+str(data[8])+"',\
                    '"+str(data[9])+"','"+str(data[10])+"','"+str(data[11])+"','"+str(data[12])+"','"+str(data[13])+"','"+str(data[14])+"','"+str(data[15])+"','"+str(data[16])+"','"+str(data[17])+"','"+data[18]+"',\
                        '"+data[19]+"');"
                self.c.execute(query)
                self.conn.commit()
                QMessageBox.question(self,"Adding Angles","Done !",QMessageBox.Ok,QMessageBox.Ok)
        else:
            pass
    def import_c(self):
        book = xlrd.open_workbook('new_sections.xlsx')
        third_sheet = book.sheet_by_index(2)
        id_list = []
        for i in range(1,third_sheet.nrows):
            id_list.append(str(int(third_sheet.row_values(i)[0])))
        input_id,ok=QtWidgets.QInputDialog.getItem(self,"Import Channels","Select an id to import its data",id_list,0,False)
        if ok:
            data = third_sheet.row_values(int(input_id) - 6)
            self.c.execute("select Id from Channels where Id =?",(int(input_id),))
            q_check = self.c.fetchall()
            if q_check:
                QMessageBox.question(self,"Error","Steel with this id is already imported. ",QMessageBox.Ok,QMessageBox.Ok)
            else:
                query = "insert into Channels values ('"+str(data[0])+"','"+str(data[1])+"','"+str(data[2])+"','"+str(data[3])+"','"+str(data[4])+"','"+str(data[5])+"','"+str(data[6])+"','"+str(data[7])+"','"+str(data[8])+"',\
                    '"+str(data[9])+"','"+str(data[10])+"','"+str(data[11])+"','"+str(data[12])+"','"+str(data[13])+"','"+str(data[14])+"','"+str(data[15])+"','"+str(data[16])+"','"+str(data[17])+"','"+data[18]+"',\
                        '"+data[19]+"','"+data[20]+"');"
                self.c.execute(query)
                self.conn.commit()
                QMessageBox.question(self,"Adding Channels","Done !",QMessageBox.Ok,QMessageBox.Ok)
        else:
            pass
    def exit(self):
        import sys
        QMessageBox.question(self,"Exit","All Changes are saved !",QMessageBox.Ok,QMessageBox.Ok)
        sys.exit()
    def empty_field(self,f):
        if f == "a":
            if not str(self.lineEdit_100.text()):
                return False
            elif not str(self.lineEdit_101.text()):
                return False
            elif not str(self.lineEdit_102.text()):
                return False
            elif not str(self.lineEdit_103.text()):
                return False
            elif not str(self.lineEdit_104.text()):
                return False
            elif not str(self.lineEdit_105.text()):
                return False
            elif not str(self.lineEdit_106.text()):
                return False
            elif not str(self.lineEdit_107.text()):
                return False
            elif not str(self.lineEdit_108.text()):
                return False
            elif not str(self.lineEdit_109.text()):
                return False
            elif not str(self.lineEdit_110.text()):
                return False
            elif not str(self.lineEdit_111.text()):
                return False
            elif not str(self.lineEdit_112.text()):
                return False
            elif not str(self.lineEdit_113.text()):
                return False
            elif not str(self.lineEdit_114.text()):
                return False
            elif not str(self.lineEdit_115.text()):
                return False
            elif not str(self.lineEdit_116.text()):
                return False
            elif not str(self.lineEdit_117.text()):
                return False
            elif not str(self.lineEdit_118.text()):
                return False
            elif not str(self.lineEdit_119.text()):
                return False
            elif not str(self.lineEdit_120.text()):
                return False
            elif not str(self.lineEdit_121.text()):
                return False
            elif not str(self.lineEdit_122.text()):
                return False
            elif not str(self.lineEdit_123.text()):
                return False
            else:
                return True
        elif f == "b":
            if not str(self.lineEdit_200.text()):
                return False
            elif not str(self.lineEdit_201.text()):
                return False
            elif not str(self.lineEdit_202.text()):
                return False
            elif not str(self.lineEdit_203.text()):
                return False
            elif not str(self.lineEdit_204.text()):
                return False
            elif not str(self.lineEdit_205.text()):
                return False
            elif not str(self.lineEdit_206.text()):
                return False
            elif not str(self.lineEdit_207.text()):
                return False
            elif not str(self.lineEdit_208.text()):
                return False
            elif not str(self.lineEdit_209.text()):
                return False
            elif not str(self.lineEdit_210.text()):
                return False
            elif not str(self.lineEdit_211.text()):
                return False
            elif not str(self.lineEdit_212.text()):
                return False
            elif not str(self.lineEdit_213.text()):
                return False
            elif not str(self.lineEdit_214.text()):
                return False
            elif not str(self.lineEdit_215.text()):
                return False
            elif not str(self.lineEdit_216.text()):
                return False
            elif not str(self.lineEdit_217.text()):
                return False
            elif not str(self.lineEdit_218.text()):
                return False
            elif not str(self.lineEdit_219.text()):
                return False
            else:
                return True
        else:
            if not str(self.lineEdit_300.text()):
                return False
            elif not str(self.lineEdit_301.text()):
                return False
            elif not str(self.lineEdit_302.text()):
                return False
            elif not str(self.lineEdit_303.text()):
                return False
            elif not str(self.lineEdit_304.text()):
                return False
            elif not str(self.lineEdit_305.text()):
                return False
            elif not str(self.lineEdit_306.text()):
                return False
            elif not str(self.lineEdit_307.text()):
                return False
            elif not str(self.lineEdit_308.text()):
                return False
            elif not str(self.lineEdit_309.text()):
                return False
            elif not str(self.lineEdit_310.text()):
                return False
            elif not str(self.lineEdit_311.text()):
                return False
            elif not str(self.lineEdit_312.text()):
                return False
            elif not str(self.lineEdit_313.text()):
                return False
            elif not str(self.lineEdit_314.text()):
                return False
            elif not str(self.lineEdit_315.text()):
                return False
            elif not str(self.lineEdit_316.text()):
                return False
            elif not str(self.lineEdit_317.text()):
                return False
            elif not str(self.lineEdit_318.text()):
                return False
            elif not str(self.lineEdit_319.text()):
                return False
            elif not str(self.lineEdit_320.text()):
                return False
            else:
                return True


        
if __name__ == "__main__":
    import sys
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())


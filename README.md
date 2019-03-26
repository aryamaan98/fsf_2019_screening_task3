# fsf_2019_screening_task3
### Desktop Application for displayig the properties of Steel Sections
PyQt5 is a comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension modules and
enables Python to be used as an alternative application development language to C++ on all supported platforms 
including iOS and Android.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyQt5,xlrd and sqlite3.

```bash
pip install pyqt5
pip install xlrd
pip install pysqlite3 
```

## How does this work ?
Open the directory and type in the following command in your Terminal.


```bash
python steelsection.py
```

## Loading Channel data 

```python
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
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
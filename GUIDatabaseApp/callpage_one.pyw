import sys
from page_one import *
import pymysql


class MyForm(QtGui.QDialog):

    connected = False

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.P1PushButtonTest, QtCore.SIGNAL('clicked()'), self.test_connection)
        QtCore.QObject.connect(self.ui.P1PushButtonSave, QtCore.SIGNAL('clicked()'), self.store_logins)
        QtCore.QObject.connect(self.ui.P1PushButtonNext, QtCore.SIGNAL('clicked()'), self.next_page)

    def test_connection(self):
        logins = self.store_logins()
        connection_msg = QtGui.QMessageBox()

        try:
            conn = pymysql.connect(user=logins[0], passwd=logins[1], host=logins[2], database=logins[3])
            if conn:
                connection_msg.setText('Connection Successful')
                connection_msg.setStandardButtons(connection_msg.Ok)
                connection_msg.exec_()
                self.connected = True
        except Exception:
            connection_msg.setText('Connection Error')
            connection_msg.setStandardButtons(connection_msg.Ok)
            connection_msg.exec_()
            self.connected = False

    def store_logins(self):
        host = self.ui.P1LineEditHost.text()
        db = self.ui.P1LineEditDatabase.text()
        user = self.ui.P1LineEditUser.text()
        pw = self.ui.P1LineEditPassword.text()
        logins = [user, pw, host, db]

        return logins

    def next_page(self):

        if self.connected:
            pass
        elif not self.connected:
            msg = QtGui.QMessageBox()
            msg.setText('Please connect to a database')
            msg.setStandardButtons(msg.Ok)
            msg.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

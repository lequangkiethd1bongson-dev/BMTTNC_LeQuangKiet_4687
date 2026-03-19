import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.ecc import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btGenerateKey.clicked.connect(self.call_api_gen_keys)
        self.ui.btSign.clicked.connect(self.call_api_sign)
        self.ui.btVerity.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/ecc/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                QMessageBox.information(self, "Thông báo", data["message"])
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/ecc/sign"
        
        payload = {
            "message": self.ui.txtInformation.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                
                self.ui.txtSignature.setText(data["signature"])
                QMessageBox.information(self, "Thành công", "Signed Successfully")
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/ecc/verify"
        
        payload = {
            "message": self.ui.txtInformation.toPlainText(),
            "signature": self.ui.txtSignature.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data["is_verified"]:
                    QMessageBox.information(self, "Kết quả", "Verified Successfully")
                else:
                    QMessageBox.warning(self, "Kết quả", "Verified Fail")
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
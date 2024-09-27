import requests, webbrowser, subprocess, socket, wmi, psutil, platform, uuid, re, os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFrame, QTextEdit
from PyQt5.QtGui import QPixmap, QCursor, QFontDatabase, QFont, QIcon
from PyQt5.QtCore import Qt, QTimer
destination_pathcurs = f'C:\\SSE\\Images\\1.png'
destination_pathcurs1 = f'C:\\SSE\\Images\\2.png'
destination_path3 = f'C:\\SSE\\Images\\3.png'
destination_path4 = f'C:\\SSE\\Images\\4.png'
destination_path41 = f'C:\\SSE\\Font\\Font.ttf'
destination_pathdg = f'C:\\SSE\\Images\\5.png'
destination_pathcurs1dp = f'C:\\SSE\\Images\\6.png'
destination_path3dy = f'C:\\SSE\\Images\\7.png'
destination_path4cg = f'C:\\SSE\\Images\\8.png'
destination_path41cp = f'C:\\SSE\\Images\\9.png'
destination_path41cy = f'C:\\SSE\\Images\\10.png'
destination_path41cy1 = f'C:\\SSE\\Images\\11.png'
destination_path42 = f'C:\\SSE\\Images\\12.png'
destination_pathcurs11 = f'C:\\SSE\\Images\\13.png'
destination_pathcurs11c = f'C:\\SSE\\Images\\14.png'
def nonet():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowFlag(Qt.FramelessWindowHint)
    window.setWindowTitle('SSE > There is no internet connection')
    window.setAttribute(Qt.WA_TranslucentBackground)
    window.setFixedSize(460, 260)
    class move(QLabel):
        def __init__(self, parent):
            super().__init__(parent)
            self.draggable = False
            self.offset = None
        def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.draggable = True
                self.offset = event.pos()
        def mouseMoveEvent(self, event):
            if self.draggable:
                self.parent().move(event.globalPos() - self.offset)
        def mouseReleaseEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.draggable = False
                self.offset = None
    def exi():
        window.close()
        sys.exit()
    square5 = QFrame(window)
    square5.setGeometry(10, 10, 450, 250)
    square5.setStyleSheet("background: rgba(0, 0, 0, 0.2); border-radius: 20px; ")
    square3 = QFrame(window)
    square3.setGeometry(0, 0, 450, 250)
    square3.setStyleSheet("background: #1a1a1a; border-radius: 20px; ")
    square7 = QFrame(window)
    square7.setGeometry(0, 0, 450, 40)
    gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
            "stop:0 #2b2b2b, " \
            "stop:0.5 #1d1d1d, " \
            "stop:1 #2b2b2b)"
    square7.setStyleSheet(f"background: {gradient}; " \
                        "border-top-left-radius: 20px; " \
                        "border-top-right-radius: 20px;")
    gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
            "stop:0 #1b1b1b, " \
            "stop:0.5 #cfcfcf, " \
            "stop:1 #1b1b1b)"
    square8 = QFrame(window)
    square8.setGeometry(0, 40, 450, 2)
    square8.setStyleSheet(f"background: {gradient}; " \
                        "border-top-left-radius: 20px; " \
                        "border-top-right-radius: 20px;")
    gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
            "stop:0 #2b2b2b, " \
            "stop:1 #1d1d1d)"
    Title1 = QLabel("You will not be able to run the program properly\nwithout the Internet", window)
    Title1.setGeometry(19, 64, 410, 75)
    font = Title1.font()
    font.setPointSize(16)
    font.setFamily("Arial")
    Title1.setFont(font) 
    Title1.setStyleSheet(f"color: #fff; font-size: 14px; font-weight: 900; background: {gradient}; border-radius: 10px; padding: 10px;")
    gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
            "stop:0 #1b1b1b, " \
            "stop:0.5 #6b6b6b, " \
            "stop:1 #1b1b1b)"
    square8f = QFrame(window)
    square8f.setGeometry(20, 159, 410, 2)
    square8f.setStyleSheet(f"background: {gradient}; " \
                        "border-top-left-radius: 20px; " \
                        "border-top-right-radius: 20px;")
    bar = move(window)
    bar.setGeometry(0, 0, 1000, 40)
    button1 = QPushButton("Exit", window)
    button1.setGeometry(180, 185, 90, 35)
    button1.clicked.connect(exi)
    font = button1.font()
    font.setPointSize(16)
    font.setFamily("Arial")
    button1.setFont(font) 
    button1.setStyleSheet("""
        QPushButton {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #2b2b2b, stop:1 #1d1d1d);
            color: white;
            font-size: 16px;
            border: 2px solid transparent;
            border-radius: 10px;
            padding: 2px 2px;
            font-weight: 900;
        }
        QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #292929, stop:1 #1a1a1a);
        }
        QPushButton:pressed {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #222222, stop:1 #161616);
        }
    """)
    desktop = app.desktop()
    screen = desktop.screenGeometry()
    x = (screen.width() - window.width()) // 2
    y = (screen.height() - window.height()) // 2
    window.move(x, y)
    window.show()
    sys.exit(app.exec_())
try:
    url = 'http://www.google.com'
    timeout = 5

    try:
        response = requests.get(url, timeout=timeout)
        if not response.status_code == 200:
            nonet()
        def get_isp():
            try:
                response = requests.get('https://ipinfo.io/json')
                data = response.json()
                isp = data['org']
                return isp
            except Exception as e:
                pass
                return None
        def CIC():
            isp_name = get_isp()
            if isp_name:
                isp_name = f"ISP Name: {isp_name}\n"
            else:
                isp_name = "Failed to retrieve ISP name.\n"
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                ssid = ssid_line.group(1).decode().strip()
                cmd = f"netsh wlan show profile \"{ssid}\" key=clear"
                try:
                    output = subprocess.check_output(cmd, shell=True)
                    lines = output.decode().splitlines()
                    profile_details = {
                        "Profile Name": ssid,
                        "Wifi Password": "Not Found",
                        "Type": "Not Found",
                        "Version": "Not Found",
                        "Control options": "Not Found",
                        "Connection mode": "Not Found",
                        "Network broadcast": "Not Found",
                        "AutoSwitch": "Not Found",
                        "MAC Randomization": "Not Found",
                        "Number of SSIDs": "Not Found",
                        "SSID name": "Not Found",
                        "Network type": "Not Found",
                        "Radio type": "Not Found",
                        "Vendor extension": "Not Found",
                        "Authentication": "Not Found",
                        "Cipher": "Not Found",
                        "Security key": "Not Found",
                        "Cost": "Not Found",
                        "Congested": "Not Found",
                        "Approaching Data Limit": "Not Found",
                        "Over Data Limit": "Not Found",
                        "Roaming": "Not Found",
                        "Cost Source": "Not Found",
                    }
                    for line in lines:
                        if "Key Content" in line:
                            profile_details["Wifi Password"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Type" in line:
                            profile_details["Type"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Version" in line:
                            profile_details["Version"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Control options" in line:
                            profile_details["Control options"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Connection mode" in line:
                            profile_details["Connection mode"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Network broadcast" in line:
                            profile_details["Network broadcast"] = line.split(":")[-1].strip() or "Not Found"
                        elif "AutoSwitch" in line:
                            profile_details["AutoSwitch"] = line.split(":")[-1].strip() or "Not Found"
                        elif "MAC Randomization" in line:
                            mac_randomization = line.split(":")[-1].strip() or "Not Found"
                            profile_details["MAC Randomization"] = "OFF" if mac_randomization == "Disabled" else mac_randomization
                        elif "Number of SSIDs" in line:
                            profile_details["Number of SSIDs"] = line.split(":")[-1].strip() or "Not Found"
                        elif "SSID name" in line:
                            profile_details["SSID name"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Network type" in line:
                            profile_details["Network type"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Radio type" in line:
                            profile_details["Radio type"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Vendor extension" in line:
                            profile_details["Vendor extension"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Authentication" in line:
                            profile_details["Authentication"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Cipher" in line:
                            profile_details["Cipher"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Security key" in line:
                            profile_details["Security key"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Cost" in line:
                            profile_details["Cost"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Congested" in line:
                            profile_details["Congested"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Approaching Data Limit" in line:
                            profile_details["Approaching Data Limit"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Over Data Limit" in line:
                            profile_details["Over Data Limit"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Roaming" in line:
                            profile_details["Roaming"] = line.split(":")[-1].strip() or "Not Found"
                        elif "Cost Source" in line:
                            profile_details["Cost Source"] = line.split(":")[-1].strip() or "Not Found"
                    profile_text = ""
                    for key, value in profile_details.items():
                        if key == "ISP Name":
                            value = "STC Broadband"
                        profile_text += f"{key}: {value}\n"
                    text_area.setText(profile_text)
                except subprocess.CalledProcessError as e:
                    pass
            else:
                pass
        def txta1():
            if ssid_line:
                CIC()
            else:
                text_area.append(f"<font color='#ff1919'>Internet connection failed</font>")
        cmd = "netsh wlan show interfaces"
        connected_network = subprocess.check_output(cmd, shell=True)
        ssid_line = re.search(b"SSID\\s+:\\s(.+)", connected_network)
        
        if not os.path.exists(f"C:\\SSE"):
            os.makedirs(f"C:\\SSE")
        if not os.path.exists(f"C:\\SSE\\Images"):
            os.makedirs(f"C:\\SSE\\Images")
        if not os.path.exists(destination_pathcurs):
            curs = 'https://i.postimg.cc/KY66Z9WX/1.png'
            destination_pathcurs = f'C:\\SSE\\Images\\1.png'
            responsecurs = requests.get(curs)
            if responsecurs.status_code == 200:
                with open(destination_pathcurs, 'wb') as file:
                    file.write(responsecurs.content)
                pass
            else:
                pass 
        curs1 = 'https://i.postimg.cc/sDLwdM8q/2.png'
        if not os.path.exists(destination_pathcurs1):
            responsecurs1 = requests.get(curs1)
            if responsecurs1.status_code == 200:
                with open(destination_pathcurs1, 'wb') as file:
                    file.write(responsecurs1.content)
                pass
            else:
                pass 
        image_Name3 = 'https://i.postimg.cc/h4krPXcd/X-2.png'
        if not os.path.exists(destination_path3):
            response3 = requests.get(image_Name3)
            if response3.status_code == 200:
                with open(destination_path3, 'wb') as file:
                    file.write(response3.content)
                pass
            else:
                pass
        image_Name4 = 'https://i.postimg.cc/Dwj40NLM/5e75920bc9d5d463.png'
        if not os.path.exists(destination_path4):
            response4 = requests.get(image_Name4)
            if response4.status_code == 200:
                with open(destination_path4, 'wb') as file:
                    file.write(response4.content)
                pass
            else:
                pass
        
        if not os.path.exists(f"C:\\SSE\\Font"):
            os.makedirs(f"C:\\SSE\\Font")
            image_Name41 = 'https://raw.githubusercontent.com/8ad7/Cloud/main/cmd.ttf'
            if not os.path.exists(destination_path41):
                response41 = requests.get(image_Name41)
                if response41.status_code == 200:
                    with open(destination_path41, 'wb') as file:
                        file.write(response41.content)
                    pass
                else:
                    pass

        dg = 'https://i.postimg.cc/wBjrGc5h/download-logo-png-image-772922.png'
        if not os.path.exists(destination_pathdg):
            responsedg = requests.get(dg)
            if responsedg.status_code == 200:
                with open(destination_pathdg, 'wb') as file:
                    file.write(responsedg.content)
                pass
            else:
                pass 
        curs1dp = 'https://i.postimg.cc/Kv5Jh38Q/download-logo-png-image-772921.png'
        if not os.path.exists(destination_pathcurs1dp):
            responsecurs1dp = requests.get(curs1dp)
            if responsecurs1dp.status_code == 200:
                with open(destination_pathcurs1dp, 'wb') as file:
                    file.write(responsecurs1dp.content)
                pass
            else:
                pass
        image_Name3dy = 'https://i.postimg.cc/fyNj6M46/download-logo-png-image-77292.png'
        if not os.path.exists(destination_path3dy):
            response3dy = requests.get(image_Name3dy)
            if response3dy.status_code == 200:
                with open(destination_path3dy, 'wb') as file:
                    file.write(response3dy.content)
                pass
            else:
                pass
        image_Name4cg = 'https://i.postimg.cc/C1BSWVCH/1621635.png'
        if not os.path.exists(destination_path4cg):
            response4cg = requests.get(image_Name4cg)
            if response4cg.status_code == 200:
                with open(destination_path4cg, 'wb') as file:
                    file.write(response4cg.content)
                pass
            else:
                pass
        image_Name41cp = 'https://i.postimg.cc/VN2300Mn/16216351.png'
        if not os.path.exists(destination_path41cp):
            response41cp = requests.get(image_Name41cp)
            if response41cp.status_code == 200:
                with open(destination_path41cp, 'wb') as file:
                    file.write(response41cp.content)
                pass
            else:
                pass
        image_Name41cy = 'https://i.postimg.cc/x8pGqMNS/16216352.png'
        if not os.path.exists(destination_path41cy):
            response41cy = requests.get(image_Name41cy)
            if response41cy.status_code == 200:
                with open(destination_path41cy, 'wb') as file:
                    file.write(response41cy.content)
                pass
            else:
                pass
        image_Name41cy1 = 'https://i.postimg.cc/W15tyPZz/Chain-link-icon-slanted.png'
        if not os.path.exists(destination_path41cy1):
            response41cy1 = requests.get(image_Name41cy1)
            if response41cy1.status_code == 200:
                with open(destination_path41cy1, 'wb') as file:
                    file.write(response41cy1.content)
                pass
            else:
                pass
        image_Name42 = 'https://i.postimg.cc/bvtnSK3g/instagram-logo-instagram-icon-transparent-free-png.png'
        if not os.path.exists(destination_path42):
            response42 = requests.get(image_Name42)
            if response42.status_code == 200:
                with open(destination_path42, 'wb') as file:
                    file.write(response42.content)
                pass
            else:
                pass
        curs11 = 'https://i.postimg.cc/C1gVChVr/25231.png'
        if not os.path.exists(destination_pathcurs11):
            responsecurs11 = requests.get(curs11)
            if responsecurs11.status_code == 200:
                with open(destination_pathcurs11, 'wb') as file:
                    file.write(responsecurs11.content)
                pass
            else:
                pass 
        curs11c = 'https://i.postimg.cc/sgV54X01/lemon-54-1-300x277.png'
        if not os.path.exists(destination_pathcurs11c):
            responsecurs11c = requests.get(curs11c)
            if responsecurs11c.status_code == 200:
                with open(destination_pathcurs11c, 'wb') as file:
                    file.write(responsecurs11c.content)
                pass
            else:
                pass
        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowIcon(QIcon(destination_pathcurs11c))
        window.setWindowFlag(Qt.FramelessWindowHint)
        window.setWindowTitle('SSE')
        window.setAttribute(Qt.WA_TranslucentBackground)
        window.setFixedSize(1010, 460)
        class DraggableImageLabe121111s1(QLabel):
            def __init__(self, parent):
                super().__init__(parent)
                self.setScaledContents(True)
                self.setPixmap(QPixmap(destination_path3))
                self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                self.draggable = False
                self.offset = None
                self.setWindowOpacity(0.5)
        class DraggableImageLabe121111s1h(QLabel):
            def __init__(self, parent):
                super().__init__(parent)
                self.setScaledContents(True)
                self.setPixmap(QPixmap(destination_path3))
                self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                self.draggable = False
                self.offset = None
                self.setWindowOpacity(0.5)
        class DraggableImageLabe121111s2(QLabel):
            def __init__(self, parent):
                super().__init__(parent)
                self.setScaledContents(True)
                self.setPixmap(QPixmap(destination_path4))
                self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                self.draggable = False
                self.offset = None
                self.setWindowOpacity(0.5)
        class DraggableImageLabe121111s11(QLabel):
            def __init__(self, parent):
                super().__init__(parent)
                self.setScaledContents(True)
                self.setPixmap(QPixmap(destination_pathdg))
                self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                self.draggable = False
                self.offset = None
                self.setWindowOpacity(0.5)
        class DraggableImageLabe121111s22(QLabel):
            def __init__(self, parent):
                super().__init__(parent)
                self.setScaledContents(True)
                self.setPixmap(QPixmap(destination_pathcurs1dp))
                self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                self.draggable = False
                self.offset = None
                self.setWindowOpacity(0.5)
        class DraggableImageLabe121111s13(QLabel):
            def __init__(self, parent):
                super().__init__(parent)
                self.setScaledContents(True)
                self.setPixmap(QPixmap(destination_path3dy))
                self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                self.draggable = False
                self.offset = None
                self.setWindowOpacity(0.5)
        class DraggableImageLabe121111s24(QLabel):
            def __init__(self, parent):
                super().__init__(parent)
                self.setScaledContents(True)
                self.setPixmap(QPixmap(destination_path4cg))
                self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                self.draggable = False
                self.offset = None
                self.setWindowOpacity(0.5)
        class DraggableImageLabe121111s135(QLabel):
            def __init__(self, parent):
                super().__init__(parent)
                self.setScaledContents(True)
                self.setPixmap(QPixmap(destination_path41cp))
                self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                self.draggable = False
                self.offset = None
                self.setWindowOpacity(0.5)
        class DraggableImageLabe121111s246(QLabel):
            def __init__(self, parent):
                super().__init__(parent)
                self.setScaledContents(True)
                self.setPixmap(QPixmap(destination_path41cy))
                self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                self.draggable = False
                self.offset = None
                self.setWindowOpacity(0.5)
        class DraggableImageLabe121111s2461(QLabel):
            def __init__(self, parent):
                super().__init__(parent)
                self.setScaledContents(True)
                self.setPixmap(QPixmap(destination_path41cy1))
                self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                self.draggable = False
                self.offset = None
                self.setWindowOpacity(0.5)
        class DraggableImageLabe121111s115(QLabel):
                def __init__(self, parent):
                    super().__init__(parent)
                    self.setScaledContents(True)
                    self.setPixmap(QPixmap(destination_pathcurs11))
                    self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                    self.draggable = False
                    self.offset = None
                    self.setWindowOpacity(0.5)
        class DraggableImageLabe121111s21(QLabel):
            def __init__(self, parent):
                super().__init__(parent)
                self.setScaledContents(True)
                self.setPixmap(QPixmap(destination_path42))
                self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                self.draggable = False
                self.offset = None
                self.setWindowOpacity(0.5)
        class move(QLabel):
            def __init__(self, parent):
                super().__init__(parent)
                self.draggable = False
                self.offset = None
            def mousePressEvent(self, event):
                if event.button() == Qt.LeftButton:
                    self.draggable = True
                    self.offset = event.pos()
            def mouseMoveEvent(self, event):
                if self.draggable:
                    self.parent().move(event.globalPos() - self.offset)
            def mouseReleaseEvent(self, event):
                if event.button() == Qt.LeftButton:
                    self.draggable = False
                    self.offset = None
        def exi():
            window.close()
            sys.exit()
        def mini():
            window.showMinimized()
        
        font_id = QFontDatabase.addApplicationFont(destination_path41)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        default_cursor_path = destination_pathcurs
        button_cursor_path = destination_pathcurs1
        default_pixmap = QPixmap(default_cursor_path)
        button_pixmap = QPixmap(button_cursor_path)
        default_cursor = QCursor(default_pixmap, 2, 2)
        window.setCursor(default_cursor)
        default_cursor = QCursor(default_pixmap, 2, 2)
        window.setCursor(default_cursor)
        button_cursor = QCursor(button_pixmap, -115, -115)
        square = QFrame(window)
        square.setGeometry(10, 10, 1000, 450)
        square.setStyleSheet("background: rgba(0, 0, 0, 0.5); border-radius: 20px; ")
        square = QFrame(window)
        square.setGeometry(0, 0, 1000, 450)
        square.setStyleSheet("background: #0e0e0e; border-radius: 20px;")
        square = QFrame(window)
        square.setGeometry(0, 0, 1000, 60)
        gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
                "stop:0 #1b1b1b, " \
                "stop:0.5 #111111, " \
                "stop:1 #1b1b1b)"
        square.setStyleSheet(f"background: {gradient}; " \
                            "border-top-left-radius: 20px; " \
                            "border-top-right-radius: 20px;")
        gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
                "stop:0 #1b1b1b, " \
                "stop:0.5 #cfcfcf, " \
                "stop:1 #1b1b1b)"
        square = QFrame(window)
        square.setGeometry(0, 60, 1000, 2)
        square.setStyleSheet(f"background: {gradient}; " \
                            "border-top-left-radius: 20px; " \
                            "border-top-right-radius: 20px;")
        Title = QLabel("Soul System Extractor", window)
        Title.setGeometry(30, 5, 350, 50)
        Title.setFont(QFont(font_family))
        Title.setStyleSheet("color: #fff; font-size: 25px; font-weight: 900;")
        TitleLine = QFrame(window)
        TitleLine.setGeometry(15, 15, 4, 30)
        TitleLine.setStyleSheet("background: #fff; border-radius: 2px; border-top-right-radius: 1px; border-bottom-left-radius: 1px;")
        bar = move(window)
        bar.setGeometry(0, 0, 1000, 67)
        image_label1211111551 = DraggableImageLabe121111s1(window)
        image_label1211111551.setGeometry(955, 10, 35, 35)
        image_label1211111s661 = DraggableImageLabe121111s2(window)
        image_label1211111s661.setGeometry(917, 5, 20, 35)
        image_label1211111s661 = DraggableImageLabe121111s2461(window)
        image_label1211111s661.setGeometry(872, 18, 25, 25)
        button1 = QPushButton("", window)
        button1.setGeometry(955, 10, 35, 35)
        button1.clicked.connect(exi)
        button1.setFont(QFont(font_family))
        button1.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 6px;
                border: 2px solid transparent;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                padding: 2px 2px;
                font-weight: 900;
            }
            QPushButton:hover {
                background: rgba(27, 27, 27, 0.264);
            }
            QPushButton:pressed {
                background: rgba(27, 27, 27, 0.364);
            }
        """)
        button1.setEnabled(True)
        button1.setCursor(button_cursor)
        def settings():
            square5.setGeometry(0, 0, 1000, 1000)
            square3.setGeometry(275, 125, 450, 250)
            square7.setGeometry(275, 125, 450, 40)
            square8.setGeometry(275, 165, 450, 2)
            image_label1211111551.setGeometry(688, 130, 32, 32)
            button1s.setGeometry(688, 130, 32, 32)
            Title1.setGeometry(295, 187, 410, 75)
            Title2.setGeometry(392, 207, 410, 75)
            button1h.setGeometry(392, 237, 30, 15)
            square8f.setGeometry(295, 280, 410, 2)
            image_label121111155.setGeometry(509, 310, 35, 35)
            image_label1211111s66.setGeometry(429, 288, 80, 80)
            button241.setGeometry(453, 310, 35, 35)
            button2411.setGeometry(508, 310, 40, 35)
        button13 = QPushButton("", window)
        button13.setGeometry(872, 18, 25, 25)
        button13.clicked.connect(settings)
        button13.setFont(QFont(font_family))
        button13.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 6px;
                border: 2px solid transparent;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                padding: 2px 2px;
                font-weight: 900;
            }
            QPushButton:hover {
                background: rgba(27, 27, 27, 0.264);
            }
            QPushButton:pressed {
                background: rgba(27, 27, 27, 0.364);
            }
        """)
        button13.setEnabled(True)
        button13.setCursor(button_cursor)
        button2 = QPushButton("", window)
        button2.setGeometry(912, 10, 35, 35)
        button2.clicked.connect(mini)
        button2.setFont(QFont(font_family))
        button2.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 6px;
                border: 2px solid transparent;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                padding: 2px 2px;
                font-weight: 900;
            }
            QPushButton:hover {
                background: rgba(27, 27, 27, 0.264);
            }
            QPushButton:pressed {
                background: rgba(27, 27, 27, 0.364);
            }
        """)
        button2.setEnabled(True)
        button2.setCursor(button_cursor)
        ips = socket.gethostname()
        ipp = (socket.gethostbyname(ips))
        square = QFrame(window)
        square.setGeometry(35, 135, 300, 305)
        square.setStyleSheet("background: rgba(0, 0, 0, 0.2); border-radius: 20px; ")
        square = QFrame(window)
        square.setGeometry(360, 135, 300, 305)
        square.setStyleSheet("background: rgba(0, 0, 0, 0.2); border-radius: 20px; ")
        square = QFrame(window)
        square.setGeometry(685, 135, 300, 305)
        square.setStyleSheet("background: rgba(0, 0, 0, 0.2); border-radius: 20px; ")
        WifiT = QLabel("Wifi", window)
        WifiT.setGeometry(142, 72, 350, 50)
        WifiT.setFont(QFont(font_family))
        WifiT.setStyleSheet("color: #08e400; font-size: 25px; font-weight: 900;")
        SystemT = QLabel("System", window)
        SystemT.setGeometry(455, 72, 350, 50)
        SystemT.setFont(QFont(font_family))
        SystemT.setStyleSheet("color: #9d33ff; font-size: 25px; font-weight: 900;")
        AddressT = QLabel("Address", window)
        AddressT.setGeometry(780, 72, 350, 50)
        AddressT.setFont(QFont(font_family))
        AddressT.setStyleSheet("color: #ffd900; font-size: 25px; font-weight: 900;")
        text_area = QTextEdit("", window)
        text_area.setFont(QFont(font_family))
        text_area.setReadOnly(True)
        text_area.setGeometry(25, 125, 300, 305)
        text_area.setStyleSheet("""
            QTextEdit {
                Background: #1f1f1f;
                font-weight: 100;
                border: 2px solid transparent;
                outline: none;
                color: #08e400;
                font-size: 20px;
                border-radius: 20px;
                padding-top: 10px;
                padding-left: 10px;
                padding-right: 10px;
                padding-bottom: 38px;
                text-decoration: none;
            }
            QScrollBar:vertical {
                border: none;
                background: #2e2e2e;
                width: 12px;
                margin: 15px 0 15px 0;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #08e400;
                min-height: 20px;
                border-radius: 2px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
            QScrollBar:vertical {
                border: 1px solid #1f1f1f;
                background: #2e2e2e;
                width: 8px;
                margin: 15px 0 15px 0;
            }
            QScrollBar::handle:vertical {
                background: #08e400;
                border-radius: 2px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: #06a800;
            }
            QScrollBar::handle:vertical:pressed {
                background: #058a00;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
                border: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        text_area.setGeometry(25, 125, 300, 305)
        text_area.setPlainText("\n".join([f"Line {i}" for i in range(1, 51)]))
        text_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        text_area1 = QTextEdit("", window)
        text_area1.setFont(QFont(font_family))
        text_area1.setReadOnly(True)
        text_area1.setGeometry(350, 125, 300, 305)
        text_area1.setStyleSheet("""
            QTextEdit {
                Background: #1f1f1f;
                font-weight: 100;
                border: 2px solid transparent;
                outline: none;
                color: #9d33ff;
                font-size: 20px;
                border-radius: 20px;
                padding-top: 10px;
                padding-left: 10px;
                padding-right: 10px;
                padding-bottom: 38px;
                text-decoration: none;
            }
            QScrollBar:vertical {
                border: none;
                background: #2e2e2e;
                width: 12px;
                margin: 15px 0 15px 0;
                border-radius: 2px;
            }
            QScrollBar::handle:vertical {
                background: #9d33ff;
                min-height: 20px;
                border-radius: 2px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
            QScrollBar:vertical {
                border: 1px solid #1f1f1f;
                background: #2e2e2e;
                width: 8px;
                margin: 15px 0 15px 0;
            }
            QScrollBar::handle:vertical {
                background: #9d33ff;
                border-radius: 2px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: #8221dd;
            }
            QScrollBar::handle:vertical:pressed {
                background: #7014c5;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
                border: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        text_area1.setGeometry(350, 125, 300, 305)
        text_area1.setPlainText("\n".join([f"Line {i}" for i in range(1, 51)]))
        text_area1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        text_area2 = QTextEdit("", window)
        text_area2.setFont(QFont(font_family))
        text_area2.setReadOnly(True)
        text_area2.setGeometry(675, 125, 300, 305)
        text_area2.setStyleSheet("""
            QTextEdit {
                Background: #1f1f1f;
                font-weight: 100;
                border: 2px solid transparent;
                outline: none;
                color: #ffd900;
                font-size: 20px;
                border-radius: 20px;
                padding-top: 10px;
                padding-left: 10px;
                padding-right: 10px;
                padding-bottom: 38px;
                text-decoration: none;
            }
            QScrollBar:vertical {
                border: none;
                background: #2e2e2e;
                width: 8px;
                margin: 15px 0 15px 0;
                border-radius: 2px;
            }
            QScrollBar::handle:vertical {
                background: #ffd900;
                min-height: 20px;
                border-radius: 2px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
            QScrollBar:vertical {
                border: 1px solid #1f1f1f;
                background: #2e2e2e;
                width: 8px;
                margin: 15px 0 15px 0;
            }
            QScrollBar::handle:vertical {
                background: #ffd900;
                border-radius: 2px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: #e6c800;
            }
            QScrollBar::handle:vertical:pressed {
                background: #c9ae00;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
                border: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        text_area2.setGeometry(675, 125, 300, 305)
        text_area2.setPlainText("\n".join([f"Line {i}" for i in range(1, 51)]))
        text_area2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        image_label1211111551 = DraggableImageLabe121111s11(window)
        image_label1211111551.setGeometry(285, 390, 35, 35)
        image_label1211111s661 = DraggableImageLabe121111s22(window)
        image_label1211111s661.setGeometry(610, 390, 35, 35)
        image_label1211111551 = DraggableImageLabe121111s13(window)
        image_label1211111551.setGeometry(935, 390, 35, 35)
        image_label1211111s661 = DraggableImageLabe121111s24(window)
        image_label1211111s661.setGeometry(255, 398, 20, 20)
        image_label1211111551 = DraggableImageLabe121111s135(window)
        image_label1211111551.setGeometry(580, 398, 20, 20)
        image_label1211111s661 = DraggableImageLabe121111s246(window)
        image_label1211111s661.setGeometry(905, 398, 20, 20)
        def hideerr():
            err.setGeometry(2615, 125, 375, 40)
            err.setStyleSheet("""
            QLabel{
                background: #009c08;
                color: #fff;
                outline: none;
                border: 6px solid transparent;
                font-size: 20px;
                padding-left: 0px;
                padding-right: 10px;
                font-weight: 900;
                border-bottom-color: #00ff0d;
            }
                        """)
        def Ok():
            err.setStyleSheet("""
            QLabel{
                background: #009c08;
                color: #fff;
                outline: none;
                border: 6px solid transparent;
                font-size: 20px;
                padding-left: 0px;
                padding-right: 10px;
                font-weight: 900;
                border-bottom-color: #00ff0d;
            }
                        """)
            err.setGeometry(325, 100, 350, 40)
            timer = QTimer(window)
            timer.singleShot(3000, hideerr)
        def No():
            err.setStyleSheet("""
            QLabel{
                background: #ff3434;
                color: #fff;
                outline: none;
                border: 6px solid transparent;
                font-size: 20px;
                padding-left: 0px;
                padding-right: 10px;
                font-weight: 900;
                border-bottom-color: #850000;
            }
                        """)
            err.setGeometry(325, 100, 350, 40)
            timer = QTimer(window)
            timer.singleShot(3000, hideerr)
        def DownloadW():
            try:
                text = text_area.toPlainText()
                os.makedirs(f"C:\\Users\\{os.getlogin()}\\Documents\\Soul info", exist_ok=True)
                os.makedirs(f"C:\\Users\\{os.getlogin()}\\Documents\\Soul info\\Wifi", exist_ok=True)
                with open(f"C:\\Users\\{os.getlogin()}\\Documents\\Soul info\\Wifi\\Wifi.txt", "w", encoding="utf-8") as file:
                    file.write(text)
                os.startfile(f"C:\\Users\\{os.getlogin()}\\Documents\\Soul info\\Wifi")
                err.setText("Wifi info has been saved .")
                Ok()
            except Exception as e:
                err.setText(f"Failed to save Wifi info !")
                No()
        def DownloadS():
            try:
                text = text_area1.toPlainText()
                os.makedirs(f"C:\\Users\\{os.getlogin()}\\Documents\\Soul info", exist_ok=True)
                os.makedirs(f"C:\\Users\\{os.getlogin()}\\Documents\\Soul info\\System", exist_ok=True)
                with open(f"C:\\Users\\{os.getlogin()}\\Documents\\Soul info\\System\\System.txt", "w", encoding="utf-8") as file:
                    file.write(text)
                os.startfile(f"C:\\Users\\{os.getlogin()}\\Documents\\Soul info\\System")
                err.setText("System info has been saved .")
                Ok()
            except Exception as e:
                err.setText(f"Failed to save System info !")
                No()
        def DownloadA():
            try:
                text = text_area2.toPlainText()
                os.makedirs(f"C:\\Users\\{os.getlogin()}\\Documents\\Soul info", exist_ok=True)
                os.makedirs(f"C:\\Users\\{os.getlogin()}\\Documents\\Soul info\\Address", exist_ok=True)
                with open(f"C:\\Users\\{os.getlogin()}\\Documents\\Soul info\\Address\\Address.txt", "w", encoding="utf-8") as file:
                    file.write(text)
                os.startfile(f"C:\\Users\\{os.getlogin()}\\Documents\\Soul info\\Address")
                err.setText("Address info has been saved .")
                Ok()
            except Exception as e:
                err.setText(f"Failed to save Address info !")
                No()
        def CopyW():
            try:
                text = text_area.toPlainText()
                clipboard = QApplication.clipboard()
                clipboard.setText(text)
                err.setText("Wifi info has been copied .")
                Ok()
            except Exception as e:
                err.setText(f"Failed to copy Wifi info !")
                No()
        def CopyS():
            try:
                text = text_area1.toPlainText()
                clipboard = QApplication.clipboard()
                clipboard.setText(text)
                err.setText("System info has been copied .")
                Ok()
            except Exception as e:
                err.setText(f"Failed to copy System info !")
                No()
        def CopyA():
            try:
                text = text_area2.toPlainText()
                clipboard = QApplication.clipboard()
                clipboard.setText(text)
                err.setText("Address info has been copied .")
                Ok()
            except Exception as e:
                err.setText(f"Address to copy Wifi info !")
                No()
        buttondg = QPushButton("", window)
        buttondg.setGeometry(285, 390, 35, 35)
        buttondg.clicked.connect(DownloadW)
        buttondg.setFont(QFont(font_family))
        buttondg.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 6px;
                border: 2px solid transparent;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                padding: 2px 2px;
                font-weight: 900;
            }
            QPushButton:hover {
                background: rgba(31, 31, 31, 0.264);
            }

            QPushButton:pressed {
                background: rgba(31, 31, 31, 0.364);
            }
        """)
        buttonds = QPushButton("", window)
        buttonds.setGeometry(610, 390, 35, 35)
        buttonds.clicked.connect(DownloadS)
        buttonds.setFont(QFont(font_family))
        buttonds.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 6px;
                border: 2px solid transparent;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                padding: 2px 2px;
                font-weight: 900;
            }
            QPushButton:hover {
                background: rgba(31, 31, 31, 0.264);
            }
            QPushButton:pressed {
                background: rgba(31, 31, 31, 0.364);
            }
        """)
        buttondi = QPushButton("", window)
        buttondi.setGeometry(935, 390, 35, 35)
        buttondi.clicked.connect(DownloadA)
        buttondi.setFont(QFont(font_family))
        buttondi.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 6px;
                border: 2px solid transparent;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                padding: 2px 2px;
                font-weight: 900;
            }
            QPushButton:hover {
                background: rgba(31, 31, 31, 0.264);
            }
            QPushButton:pressed {
                background: rgba(31, 31, 31, 0.364);
            }
        """)
        buttoncw = QPushButton("", window)
        buttoncw.setGeometry(255, 393, 20, 25)
        buttoncw.clicked.connect(CopyW)
        buttoncw.setFont(QFont(font_family))
        buttoncw.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 6px;
                border: 2px solid transparent;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                padding: 2px 2px;
                font-weight: 900;
            }
            QPushButton:hover {
                background: rgba(31, 31, 31, 0.264);
            }
            QPushButton:pressed {
                background: rgba(31, 31, 31, 0.364);
            }
        """)
        buttondcs = QPushButton("", window)
        buttondcs.setGeometry(580, 393, 20, 25)
        buttondcs.clicked.connect(CopyS)
        buttondcs.setFont(QFont(font_family))
        buttondcs.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 6px;
                border: 2px solid transparent;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                padding: 2px 2px;
                font-weight: 900;
            }
            QPushButton:hover {
                background: rgba(31, 31, 31, 0.264);
            }
            QPushButton:pressed {
                background: rgba(31, 31, 31, 0.364);
            }
        """)
        buttondcA = QPushButton("", window)
        buttondcA.setGeometry(905, 393, 20, 25)
        buttondcA.clicked.connect(CopyA)
        buttondcA.setFont(QFont(font_family))
        buttondcA.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 6px;
                border: 2px solid transparent;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                padding: 2px 2px;
                font-weight: 900;
            }
            QPushButton:hover {
                background: rgba(31, 31, 31, 0.264);
            }
            QPushButton:pressed {
                background: rgba(31, 31, 31, 0.364);
            }
        """)
        buttondg.setEnabled(True)
        buttondg.setCursor(button_cursor)
        buttonds.setEnabled(True)
        buttonds.setCursor(button_cursor)
        buttondi.setEnabled(True)
        buttondi.setCursor(button_cursor)
        buttoncw.setEnabled(True)
        buttoncw.setCursor(button_cursor)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                #  @9omw
        buttondcs.setEnabled(True)
        buttondcs.setCursor(button_cursor)
        buttondcA.setEnabled(True)
        buttondcA.setCursor(button_cursor)
        cmd = "netsh wlan show interfaces"
        connected_network = subprocess.check_output(cmd, shell=True)
        ssid_line = re.search(b"SSID\\s+:\\s(.+)", connected_network)
        txta1()
        def get_ip_address():
            try:
                response = requests.get('https://api64.ipify.org?format=json')
                response.raise_for_status()
                ip_data = response.json()
                return ip_data['ip']
            except requests.RequestException as e:
                return None

        def get_ip_info(ip_address):
            try:
                response = requests.get(f'http://ip-api.com/json/{ip_address}')
                response.raise_for_status()
                ip_info = response.json()
                if ip_info['status'] == 'fail':
                    return None
                return ip_info
            except requests.RequestException as e:
                return None

        ip_address = get_ip_address()
        if ip_address:
            ip_info = get_ip_info(ip_address)
            if ip_info:
                try:
                    response = requests.get("http://ip-api.com/json/?fields=225545")
                    response.raise_for_status()
                    r = response.json()
                    if r.get("status") != "success":
                        raise Exception("Failed to get additional IP info")
                    data = (f"Cellular Network: {'No Found' if not r['mobile'] else 'Found'}\n"
                            f"VPN: {'No Found' if not r['proxy'] else 'Found'}\n"
                            f"IPv4: {r['query']}\n"
                            f"IPv6: {ip_address}\n"
                            f"timezone: {ip_info['timezone']}\n"
                            f"country: {ip_info['country']}\n"
                            f"countryCode: {ip_info['countryCode']}\n"
                            f"city: {ip_info['city']}\n"
                            f"zip: {ip_info['zip']}\n"
                            f"lat: {ip_info['lat']}\n"
                            f"lon: {ip_info['lon']}")
                except Exception as e:
                    pass
            else:
                pass
        else:
            pass
        text_area2.setText(data)
        system_type = platform.system()
        system_version = platform.win32_ver()[0] if system_type == "Windows" else platform.release()
        oss = f"{system_type} {system_version}"
        name = platform.node()
        total_memory = psutil.virtual_memory().total
        total_memory_str = ""
        if total_memory >= 1024 ** 4: 
            total_memory_str = f"{total_memory / (1024 ** 4):.2f} TB"
        elif total_memory >= 1024 ** 3: 
            total_memory_str = f"{total_memory / (1024 ** 3):.2f} GB"
        elif total_memory >= 1024 ** 2: 
            total_memory_str = f"{total_memory / (1024 ** 2):.2f} MB"
        else:
            total_memory_str = f"{total_memory / 1024:.2f} KB"
        TotalMemory = f"{total_memory_str}"
        cpu = platform.processor()
        wmi_obj = wmi.WMI()
        disk_usage = psutil.disk_usage('/')
        total_space = disk_usage.total / (1024**3)
        used_space = disk_usage.used / (1024**3)
        free_space = disk_usage.free / (1024**3)
        percent_used = disk_usage.percent
        query = "SELECT Name FROM Win32_VideoController"
        result = wmi_obj.query(query)
        gpu = result[0].Name if len(result) > 0 else "None"
        try:
            productKey = subprocess.run("powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SoftwareProtectionPlatform' -Name BackupProductKeyDefault", capture_output=True, shell=True).stdout.decode(errors='ignore').strip()
        except NameError:
            productKey = "None"
        generated_uuid = uuid.uuid4()
        uui = str(generated_uuid)
        system = f"Computer Name: {name}\nDevice IP: {ipp}\nComputer OS: {oss}\nTotal Memory: {TotalMemory}\nTotal space: {total_space:.2f} GB\nUsed space: {used_space:.2f} GB\nFree space: {free_space:.2f} GB\nPercentage used: {percent_used}%\nUUID: {uui}\nCPU: {cpu}\nGPU: {gpu}\nProduct Key: {productKey}"
        text_area1.setText(system)
        def offSettings():
            square5.setGeometry(111110, 0, 1000, 1000)
            square3.setGeometry(2751, 125, 450, 250)
            square7.setGeometry(2715, 125, 450, 40)
            square8.setGeometry(2715, 165, 450, 2)
            image_label1211111551.setGeometry(6881, 130, 32, 32)
            button1s.setGeometry(6818, 130, 32, 32)
            Title1.setGeometry(2195, 187, 410, 75)
            Title2.setGeometry(3921, 207, 410, 75)
            button1h.setGeometry(3192, 237, 30, 15)
            square8f.setGeometry(1295, 280, 410, 2)
            image_label121111155.setGeometry(5019, 310, 35, 35)
            image_label1211111s66.setGeometry(4219, 288, 80, 80)
            button241.setGeometry(4513, 310, 35, 35)
            button2411.setGeometry(5108, 310, 40, 35)
        def DownloadSrc():
            cmd = "netsh wlan show interfaces"
            connected_network = subprocess.check_output(cmd, shell=True)
            ssid_line = re.search(b"SSID\\s+:\\s(.+)", connected_network)
            if ssid_line:
                webbrowser.open("https://codeload.github.com/Q8G/SSE/zip/refs/heads/main")
                os.startfile(f"C:\\Users\\{os.getlogin()}\\Downloads")
            else:
                err.setText("There is no internet connection")
                No()
        def insta():
            cmd = "netsh wlan show interfaces"
            connected_network = subprocess.check_output(cmd, shell=True)
            ssid_line = re.search(b"SSID\\s+:\\s(.+)", connected_network)
            if ssid_line:
                url = "https://www.instagram.com/9omw/"
                webbrowser.open(url)
            else:
                err.setText("There is no internet connection")
                No()
        def git():
            cmd = "netsh wlan show interfaces"
            connected_network = subprocess.check_output(cmd, shell=True)
            ssid_line = re.search(b"SSID\\s+:\\s(.+)", connected_network)
            if ssid_line:
                url = "https://github.com/Q8G"
                webbrowser.open(url)
            else:
                err.setText("There is no internet connection")
                No()
        square5 = QFrame(window)
        square5.setGeometry(111110, 0, 1000, 1000)
        square5.setStyleSheet("background: rgba(0, 0, 0, 0.6); border-radius: 20px; ")
        square3 = QFrame(window)
        square3.setGeometry(2175, 125, 450, 250)
        square3.setStyleSheet("background: #1a1a1a; border-radius: 20px; ")
        square7 = QFrame(window)
        square7.setGeometry(2715, 125, 450, 40)
        gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
                "stop:0 #2b2b2b, " \
                "stop:0.5 #1d1d1d, " \
                "stop:1 #2b2b2b)"
        square7.setStyleSheet(f"background: {gradient}; " \
                            "border-top-left-radius: 20px; " \
                            "border-top-right-radius: 20px;")
        gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
                "stop:0 #1b1b1b, " \
                "stop:0.5 #cfcfcf, " \
                "stop:1 #1b1b1b)"
        square8 = QFrame(window)
        square8.setGeometry(2751, 165, 450, 2)
        square8.setStyleSheet(f"background: {gradient}; " \
                            "border-top-left-radius: 20px; " \
                            "border-top-right-radius: 20px;")
        image_label1211111551 = DraggableImageLabe121111s1(window)
        image_label1211111551.setGeometry(6881, 130, 32, 32)
        button1s = QPushButton("", window)
        button1s.setGeometry(6881, 130, 32, 32)
        button1s.clicked.connect(offSettings)
        button1s.setFont(QFont(font_family))
        button1s.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 6px;
                border: 2px solid transparent;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                padding: 2px 2px;
                font-weight: 900;
            }
            QPushButton:hover {
                background: rgba(27, 27, 27, 0.264);
            }
            QPushButton:pressed {
                background: rgba(27, 27, 27, 0.364);
            }
        """)
        button1s.setEnabled(True)
        button1s.setCursor(button_cursor)
        gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
                "stop:0 #2b2b2b, " \
                "stop:1 #1d1d1d)"
        Title1 = QLabel("If you want to learn how to create such a program,\nthe open source program can\nbe obtained     ", window)
        Title1.setGeometry(2951, 187, 410, 75)
        Title1.setFont(QFont(font_family))
        Title1.setStyleSheet(f"color: #fff; font-size: 14px; font-weight: 900; background: {gradient}; border-radius: 10px; padding: 10px;")
        Title2 = QLabel("here", window)
        Title2.setGeometry(3921, 207, 410, 75)
        Title2.setFont(QFont(font_family))
        Title2.setStyleSheet(f"color: #08e400; font-size: 14px; font-weight: 900;")
        button1h = QPushButton("", window)
        button1h.setGeometry(3921, 237, 30, 15)
        button1h.clicked.connect(DownloadSrc)
        button1h.setFont(QFont(font_family))
        button1h.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 6px;
                border: 2px solid transparent;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                padding: 2px 2px;
                font-weight: 900;
            }
            QPushButton:hover {
                background: rgba(36, 36, 36, 0.264);
            }
            QPushButton:pressed {
                background: rgba(36, 36, 36, 0.364);
            }
        """)
        button1h.setEnabled(True)
        button1h.setCursor(button_cursor)
        gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
                "stop:0 #1b1b1b, " \
                "stop:0.5 #6b6b6b, " \
                "stop:1 #1b1b1b)"
        square8f = QFrame(window)
        square8f.setGeometry(2951, 280, 410, 2)
        square8f.setStyleSheet(f"background: {gradient}; " \
                            "border-top-left-radius: 20px; " \
                            "border-top-right-radius: 20px;")
        image_label121111155 = DraggableImageLabe121111s115(window)
        image_label121111155.setGeometry(5019, 310, 35, 35)
        image_label1211111s66 = DraggableImageLabe121111s21(window)
        image_label1211111s66.setGeometry(4219, 288, 80, 80)
        button241 = QPushButton("", window)
        button241.setGeometry(4513, 310, 35, 35)
        button241.clicked.connect(insta)
        button241.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 6px;
                border: 2px solid transparent;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                padding: 2px 2px;
                font-weight: 900;
            }
            QPushButton:hover {
                background: rgba(26, 26, 26, 0.264);
            }
            QPushButton:pressed {
                background: rgba(26, 26, 26, 0.364);
            }
        """)
        button241.setEnabled(True)
        button241.setCursor(button_cursor)
        button2411 = QPushButton("", window)
        button2411.setGeometry(5081, 310, 40, 35)
        button2411.clicked.connect(git)
        button2411.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 6px;
                border: 2px solid transparent;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                padding: 2px 2px;
                font-weight: 900;
            }
            QPushButton:hover {
                background: rgba(26, 26, 26, 0.264);
            }
            QPushButton:pressed {
                background: rgba(26, 26, 26, 0.364);
            }
        """)
        button2411.setEnabled(True)
        button2411.setCursor(button_cursor)
        err = QLabel("Wifi info has been copied .", window)
        err.setFont(QFont(font_family))
        err.setGeometry(3125, 100, 350, 40)
        err.setStyleSheet("""
            QLabel{
                background: #ff3434;
                color: #fff;
                outline: none;
                border: 6px solid transparent;
                font-size: 20px;
                padding-left: 0px;
                padding-right: 10px;
                font-weight: 900;
                border-bottom-color: #850000;
            }
                        """)
        desktop = app.desktop()
        screen = desktop.screenGeometry()
        x = (screen.width() - window.width()) // 2
        y = (screen.height() - window.height()) // 2
        window.move(x, y)
        window.show()
        sys.exit(app.exec_())
    except requests.ConnectionError:
        nonet()
except Exception as e:
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowFlag(Qt.FramelessWindowHint)
    window.setWindowTitle('SSE > an error occurred')
    window.setAttribute(Qt.WA_TranslucentBackground)
    window.setFixedSize(460, 260)
    class move(QLabel):
        def __init__(self, parent):
            super().__init__(parent)
            self.draggable = False
            self.offset = None
        def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.draggable = True
                self.offset = event.pos()
        def mouseMoveEvent(self, event):
            if self.draggable:
                self.parent().move(event.globalPos() - self.offset)
        def mouseReleaseEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.draggable = False
                self.offset = None
    def exi():
        window.close()
        sys.exit()
    def settings():
        Title1.setGeometry(295, 187, 410, 75)
        Title2.setGeometry(392, 207, 410, 75)
        button1h.setGeometry(392, 237, 30, 15)
        square8f.setGeometry(295, 280, 410, 2)
        image_label121111155.setGeometry(509, 310, 35, 35)
        image_label1211111s66.setGeometry(429, 288, 80, 80)
        button241.setGeometry(453, 310, 35, 35)
        button2411.setGeometry(508, 310, 40, 35)
    square5 = QFrame(window)
    square5.setGeometry(10, 10, 450, 250)
    square5.setStyleSheet("background: rgba(0, 0, 0, 0.2); border-radius: 20px; ")
    square3 = QFrame(window)
    square3.setGeometry(0, 0, 450, 250)
    square3.setStyleSheet("background: #1a1a1a; border-radius: 20px; ")
    square7 = QFrame(window)
    square7.setGeometry(0, 0, 450, 40)
    gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
            "stop:0 #2b2b2b, " \
            "stop:0.5 #1d1d1d, " \
            "stop:1 #2b2b2b)"
    square7.setStyleSheet(f"background: {gradient}; " \
                        "border-top-left-radius: 20px; " \
                        "border-top-right-radius: 20px;")
    gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
            "stop:0 #1b1b1b, " \
            "stop:0.5 #cfcfcf, " \
            "stop:1 #1b1b1b)"
    square8 = QFrame(window)
    square8.setGeometry(0, 40, 450, 2)
    square8.setStyleSheet(f"background: {gradient}; " \
                        "border-top-left-radius: 20px; " \
                        "border-top-right-radius: 20px;")
    gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
            "stop:0 #2b2b2b, " \
            "stop:1 #1d1d1d)"
    Title1 = QLabel(f"An error occurred in running the application. Make\nsure you are connected to the Internet or delete the\napplication and download it again", window)
    Title1.setGeometry(19, 64, 410, 75)
    font = Title1.font()
    font.setPointSize(16)
    font.setFamily("Arial")
    Title1.setFont(font) 
    Title1.setStyleSheet(f"color: #fff; font-size: 14px; font-weight: 900; background: {gradient}; border-radius: 10px; padding: 10px;")
    gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, " \
            "stop:0 #1b1b1b, " \
            "stop:0.5 #6b6b6b, " \
            "stop:1 #1b1b1b)"
    square8f = QFrame(window)
    square8f.setGeometry(20, 159, 410, 2)
    square8f.setStyleSheet(f"background: {gradient}; " \
                        "border-top-left-radius: 20px; " \
                        "border-top-right-radius: 20px;")
    bar = move(window)
    bar.setGeometry(0, 0, 1000, 40)
    button1 = QPushButton("Exit", window)
    button1.setGeometry(180, 185, 90, 35)
    button1.clicked.connect(exi)
    font = button1.font()
    font.setPointSize(16)
    font.setFamily("Arial")
    button1.setFont(font) 
    button1.setStyleSheet("""
        QPushButton {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #2b2b2b, stop:1 #1d1d1d);
            color: white;
            font-size: 16px;
            border: 2px solid transparent;
            border-radius: 10px;
            padding: 2px 2px;
            font-weight: 900;
        }
        QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #292929, stop:1 #1a1a1a);
        }
        QPushButton:pressed {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #222222, stop:1 #161616);
        }
    """)
    desktop = app.desktop()
    screen = desktop.screenGeometry()
    x = (screen.width() - window.width()) // 2
    y = (screen.height() - window.height()) // 2
    window.move(x, y)
    window.show()
    sys.exit(app.exec_())

import sys

import calendar
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow, 
    QPushButton,
    QDesktopWidget,
    QWidget,
    QGridLayout,
    QInputDialog
)

def center_window(qwidget: QWidget):
    """_summary_

    Args:
        qwidget (QWidget): _description_
    """
    window_size = qwidget.size()

    x = (SCREEN_SIZE.width() - window_size.width()) // 2
    y = (SCREEN_SIZE.height() - window_size.height()) // 2

    qwidget.move(x, y)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    """
    Main Window of our App
    """
    
    def __init__(self, title: str = "Main") -> None:
        super().__init__()
        
        # UI Config
        # - Window size
        scale_factor = 0.65
        dimensions = (SCREEN_SIZE.width(), SCREEN_SIZE.height())
        dimensions = (int(x * scale_factor) for x in dimensions)
        self.setMinimumSize(*dimensions)
        center_window(self)
        
        # - Miscellaneous
        self.setWindowTitle(title)
        
        # - Build UI
        self.__init_UI()
        
    def __init_UI(self):
        layout = QGridLayout()
        cal = calendar.Calendar()
        days_of_month = cal.monthdatescalendar(2022, 11)
        for w, week in enumerate(days_of_month):
            for d, day in enumerate(week):
                btn = QPushButton(str(day.day))
                days_of_month[w][d] = btn
                layout.addWidget(btn, w, d)
                

        # Layout order
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
                

def run():
    app = QApplication(sys.argv)
    
    # We create QWidgets after creating a QApplication
    global SCREEN_SIZE
    SCREEN_SIZE = QDesktopWidget().screenGeometry()
    
    window = MainWindow()
    window.show()
    app.exec() 
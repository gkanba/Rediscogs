import client
import widgets
import os, sys
from PyQt6.QtWidgets import QApplication

class Rediscogs(QApplication):
    # def application constants
    APPLICATION_NAME    = 'Discogs Integration/1.0/gkanba'
    APPLICATION_TOKEN   = 'gvCILUfKDakfUmPcGNFvqECAdMISXhAXhfiKJvMw'
    MAIN_WINDOW_TITLE   = 'Rediscogs'

    def __init__(self, argv : list[str]) -> None:
        super().__init__(argv)

        self.client = client.DiscogClient(user_agent=self.APPLICATION_NAME, user_token=self.APPLICATION_TOKEN).instance()
        self.main_window = widgets.Widget_MainWindow()

    def main(self):
        self.main_window.setWindowTitle(self.MAIN_WINDOW_TITLE)
        self.main_window.setupUi()
        self.main_window.setupClient(self.client)
        self.main_window.show()

if __name__ == '__main__':
    # init application
    try:
        os.mkdir("./images")
    except:
        print("Failed to create directory.")
    app = Rediscogs(sys.argv)
    # exec application
    app.main()
    # exit application
    sys.exit(app.exec())
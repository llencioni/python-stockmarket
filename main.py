#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################
#
# Get stock prices though Python
#
# By luiz.lencioni@gmail.com
#
######################################


from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLineEdit
import sys

# Import other Python files
from src.menu import UI


# Run this file as script mode (main)
if __name__ == "__main__":
    print("\nNada a declarar")
    # Create an instance of QtWidgets.QApplication
    app = QApplication(sys.argv)
    # Call menu constructor
    MainWindow = UI()
    MainWindow.show()
    # Run application
    app.exec_()






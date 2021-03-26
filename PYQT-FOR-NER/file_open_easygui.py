'''
easygui Web:
    https://easygui.readthedocs.io/en/latest

easygui Documentation(pdf):
    https://readthedocs.org/projects/easygui/downloads/pdf/latest/
'''

import easygui

# fileopenbox: fileopenbox returns the name of a file


def OpenWinFileExplorer():
    multiSearchFilePath = easygui.fileopenbox()
    return multiSearchFilePath

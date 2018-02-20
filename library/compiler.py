from PyQt5.QtWidgets import QApplication
from library.jsonToQt import mapping
from json import load
from sys import argv, exit

if __name__ == '__main__':
    with open('../test.json', 'r') as markupFile:
        markup = load(markupFile)

    for w, _ in markup.items():
        try:
            widget = mapping[w]
        except KeyError:
            pass

    app = QApplication(argv)
    mainWidget = widget()
    mainWidget.show()
    exit(app.exec_())

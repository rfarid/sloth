from PyQt4.QtGui import QPen
from PyQt4.Qt import Qt
from sloth.items import RectItem

#__________________________________________________________________________________________
#
# RectColorWithLabel
#
#__________________________________________________________________________________________
class RectColorWithLabel(RectItem):

    #defaultAutoTextKeys = ['x', 'y']

    def __init__(self, model_item=None, prefix="", parent=None, color=Qt.black,label=""):
        RectItem.__init__(self, model_item, prefix, parent)
        self._userColor=color
        self._userLabel=label
        self.setColor(self._userColor)
        self._text_item.setHtml(self._userLabel)
        self.setPen(QPen(self._userColor, 2))

    def __call__(self, *args, **kwargs):
        newitem = RectItem(*args, **kwargs)
        newitem.setColor(self._userColor)
        newitem._text_item.setHtml(self._userLabel)
        return newitem

# colors={1:'ColorDarkRed',2:'ColorDarkGreen',4:'ColorDarkBlue',6:'ColorDarkGray',8:'ColorRed',10:'ColorGreen',12:'ColorBlue',14:'ColorDarkCyan',16:'ColorBlack'}
'''
Qt::white	    3	White (#ffffff)
Qt::black	    2	Black (#000000)
Qt::red	        7	Red (#ff0000)
Qt::darkRed	    13	Dark red (#800000)
Qt::green	    8	Green (#00ff00)
Qt::darkGreen	14	Dark green (#008000)
Qt::blue	    9	Blue (#0000ff)
Qt::darkBlue	15	Dark blue (#000080)
Qt::cyan	    10	Cyan (#00ffff)
Qt::darkCyan	16	Dark cyan (#008080)
Qt::magenta	    11	Magenta (#ff00ff)
Qt::darkMagenta	17	Dark magenta (#800080)
Qt::yellow	    12	Yellow (#ffff00)
Qt::darkYellow	18	Dark yellow (#808000)
Qt::gray	    5	Gray (#a0a0a4)
Qt::darkGray	4	Dark gray (#808080)
Qt::lightGray	6	Light gray (#c0c0c0)
Qt::transparent	19	a transparent black value (i.e., QColor(0, 0, 0, 0))
Qt::color0	0	0 pixel value (for bitmaps)
Qt::color1	1	1 pixel value (for bitmaps)
'''


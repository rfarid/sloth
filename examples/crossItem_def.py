# Reza Farid, Fugro Roames
# Created:      Based on coloredRectItemWithLabel_def.py in 2015
# Last update:  2016/04/22
#
# an extension to sloth to select a point, show it as a cross with associated colour and label
# the size of the cross can be controlled by radius parameter
#
from PyQt4.QtGui import QPen
from PyQt4.Qt import Qt
from sloth.items import ItemInserter, BaseItem
from PyQt4.QtGui import *
from PyQt4.Qt import *

#__________________________________________________________________________________________
#
# CrossItem
#   It is similar to PointItem
#   Additionally, it has color, label and radius as input parameters
#   Paint module is also different by drawing a cross instead of ellipse
#__________________________________________________________________________________________
class CrossItem(BaseItem):
    """
    Visualization item for points.
    """

    def __init__(self, model_item=None, prefix="", parent=None, color=Qt.black, label="", radius=5):
        BaseItem.__init__(self, model_item, prefix, parent)

        self._point = None
        self._radius=radius
        self._userColor=color
        self._userLabel=label
        self.setColor(self._userColor)
        self.setRadius(self._radius)
        self._text_item.setHtml(self._userLabel)
        self.updatePoint()

    def setRadius(self, radius):
        self.prepareGeometryChange()
        self._radius = radius
        self.update()

    def radius(self):
        return self._radius

    def __call__(self, *args, **kwargs):
        crossitem = CrossItem(*args, **kwargs)
        crossitem.setRadius(self._radius)
        crossitem.setColor(self._userColor)
        crossitem._text_item.setHtml(self._userLabel)
        crossitem.setPen(self.pen())
        crossitem.setBrush(self.brush())
        return crossitem

    def dataChange(self):
        self.updatePoint()

    def updateModel(self):
        self._model_item.update({
            self.prefix() + 'x': self.scenePos().x(),
            self.prefix() + 'y': self.scenePos().y(),
        })

    def updatePoint(self):
        if self._model_item is None:
            return

        try:
            point = QPointF(float(self._model_item[self.prefix() + 'x']),
                            float(self._model_item[self.prefix() + 'y']))
        except KeyError as e:
            LOG.debug("CrossItem: Could not find expected key in item: "
                      + str(e) + ". Check your config!")
            self.setValid(False)
            self._point = None
            return

        if point == self._point:
            return

        self.prepareGeometryChange()
        self._point = point
        self.setPos(self._point)

    def boundingRect(self):
        r = self._radius
        return QRectF(-r, -r, 2 * r, 2 * r)

    def paint(self, painter, option, widget=None):
        BaseItem.paint(self, painter, option, widget)

        pen = self.pen()
        if self.isSelected():
            pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        # bb=self.boundingRect()
        # painter.drawEllipse(bb)
        # painter.drawRect(bb)        
        r = self._radius
        r_4=r/4
        r_2=2*r_4
        hr=QRectF(-r, -r_4, 2 * r, r_2)
        vr=QRectF(-r_4, -r, r_2, 2 * r)
        # print r,hr,vr        
        painter.drawRect(hr)
        painter.drawRect(vr)

    def keyPressEvent(self, event):
        BaseItem.keyPressEvent(self, event)
        step = 1
        if event.modifiers() & Qt.ShiftModifier:
            step = 5
        ds = {Qt.Key_Left:  (-step, 0),
              Qt.Key_Right: (step, 0),
              Qt.Key_Up:    (0, -step),
              Qt.Key_Down:  (0, step)
             }.get(event.key(), None)
        if ds is not None:
            self.moveBy(*ds)
            event.accept()

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

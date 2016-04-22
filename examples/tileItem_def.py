# Reza Farid, Fugro Roames
# Created:      2016/04/22
# Last update:  2016/04/22
#
# an extension to sloth to select a tile by choosing a point
# the size of the tile is the defined as tile_w, tile_h
#
from PyQt4.QtGui import QPen
from PyQt4.Qt import Qt
from sloth.items import ItemInserter, BaseItem, RectItem
from PyQt4.QtGui import *
from PyQt4.Qt import *

#__________________________________________________________________________________________
#
# TileItem
#   It is similar to PointItem and RectItem
#   Additionally, it has color, label, pen_width and tile width/height as input parameters
#   Paint module is also different by drawing a rectangle instead of ellipse
#__________________________________________________________________________________________
class TileItem(BaseItem):
    """
    Visualization item for points.
    """

    def __init__(self, model_item=None, prefix="", parent=None, color=Qt.red, pen_width=2, label="",tile=(10,10),tile_border=(0,0), point_as_centre=False):
        BaseItem.__init__(self, model_item, prefix, parent)
        self._point = None
        # self._rect = None
        self._radius=2
        self._userColor=color
        self._userLabel=label
        self.setColor(self._userColor)
        self._text_item.setHtml(self._userLabel)
        self._imgw = 3000
        self._imgh = 3000
        self._tile = tile
        self._tile_border = tile_border
        self._point_as_centre=point_as_centre
        self._pen_width = pen_width
        # self.ImageDim()
        self.updatePoint()

    def __call__(self, *args, **kwargs):
        newitem = TileItem(*args, **kwargs)
        newitem.setColor(self._userColor)
        newitem._text_item.setHtml(self._userLabel)
        newitem.setPen(self.pen())
        # newitem.setBrush(self.brush())
        newitem._tile=self._tile
        newitem._tile_border=self._tile_border
        newitem._pen_width = self._pen_width
        newitem.setDim(3000,3000)
        newitem._point_as_centre=self._point_as_centre
        return newitem

    # def ImageDim(self):
    #     new_image = self._labeltool.currentImage()
    #     img = self._labeltool.getImage(new_image)
    #     self._imgw=img.shape[1]
    #     self._imgh=img.shape[0]
    #     print self._imgw,self._imgh

    def findTile(self,x,y):
        xmin=-1
        ymin=-1
        tw=self._tile[0]
        th=self._tile[1]
        tbw=self._tile_border[0]
        tbh=self._tile_border[1]
        imgw=self._imgw
        imgh=self._imgh
        tws = tw + tbw
        ths = th + tbh
        for x1 in range(0,imgw,tws):
            if x>=x1 and x<x1+tws:
                xmin=x1
                break
        for y1 in range(0,imgh,ths):
            if y>=y1 and y<y1+ths:
                ymin=y1
                break
        if xmin>-1 and ymin>-1:
            ans=[xmin,ymin,xmin+tw,ymin+th]
            return ans

    def setDim(self, w,h):
        self._imgw=w
        self._imgh=h

    def setTile(self, tile):
        self._tile=tile        
        # self.update()

    def setTileBorder(self,tile_border):
        self._tile_border=tile_border

    def tile(self):
        return self._tile

    def tile_border(self):
        return self._tile_border


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
            LOG.debug("TileItem: Could not find expected key in item: "
                      + str(e) + ". Check your config!")
            self.setValid(False)
            self._point = None
            return

        if point == self._point:
            return

        self.prepareGeometryChange()
        self._point = point
        self.setPos(self._point)
        # self._rect = self.boundingRect()

    def boundingRect(self):
        tile = self._tile
        tw_2=tile[0]/2
        th_2=tile[1]/2
        if self._point_as_centre:
            return QRectF(-tw_2, -th_2, tile[0], tile[1])
        else:
            x = float(self._model_item[self.prefix() + 'x'])
            y = float(self._model_item[self.prefix() + 'y'])
            bb = self.findTile(x=x,y=y)
            if bb is not None:
                # print x,y,bb
                return QRectF(bb[0]-x, bb[1]-y, float(tile[0]), float(tile[1]))
            else:
                return QRectF(-tw_2, -th_2, tile[0], tile[1])            

    def paint(self, painter, option, widget=None):
        BaseItem.paint(self, painter, option, widget)
        pen = self.pen()
        if self.isSelected():
            pen.setStyle(Qt.DashLine)
        pen.setWidth ( self._pen_width )
        painter.setPen(pen)
        painter.drawRect(self.boundingRect())

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

# Reza Farid, Fugro Roames
# Created:      2016/04/22
# Last update:  2016/04/26
#
# an extension to sloth to select a tile by choosing a point
# the size of the tile is the defined as tile_w, tile_h
#
from PyQt4.QtGui import QPen
from PyQt4.Qt import Qt
from sloth.items import ItemInserter, BaseItem, RectItem, RectItemInserter
from PyQt4.QtGui import *
from PyQt4.Qt import *

TILE=(96,124)
TILE_BORDER=(5,2)
IMG_W=3000
IMG_H=3000

def findTile_base(x,y,imgw,imgh,tile,tile_border):
    xmin=-1
    ymin=-1
    tw=tile[0]
    th=tile[1]
    tbw=tile_border[0]
    tbh=tile_border[1]
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

class TileItemInserter(ItemInserter):

    def __init__(self, labeltool, scene, default_properties=None, prefix="", commit=True):
        ItemInserter.__init__(self, labeltool, scene, default_properties, prefix, commit)

        self._init_pos = None
        self._imgw = IMG_W
        self._imgh = IMG_H
        self._tile = TILE
        self._tile_border = TILE_BORDER
        self._point_as_centre=False

    def formTile(self,x,y):
        tile = self._tile
        tw_2=tile[0]/2
        th_2=tile[1]/2
        if self._point_as_centre:
            return QRectF(x-tw_2, y-th_2, tile[0], tile[1])
        else:
            bb = self.findTile(x=x,y=y)
            if bb is not None:
                # print x,y,bb
                return QRectF(bb[0], bb[1], float(tile[0]), float(tile[1]))
            else:
                return QRectF(x-tw_2, y-th_2, tile[0], tile[1])            

    def findTile(self,x,y):
        return findTile_base(x,y,self._imgw,self._imgh,self._tile,self._tile_border)

    def mousePressEvent_simulate(self, event, x,y, image_item,class_name):
        rect = self.formTile(x, y)
        # print pos.x(),pos.y(), rect        
        # self._item.setPen(self.pen())
        # self._scene.addItem(self._item)
        self._ann.update({self._prefix + 'class': class_name,
                          self._prefix + 'x': rect.x(),            
                          self._prefix + 'y': rect.y(),
                          self._prefix + 'width': rect.width(),
                          self._prefix + 'height': rect.height()})
        self._ann.update(self._default_properties)
        if self._commit:
            image_item.addAnnotation(self._ann)
        self.annotationFinished.emit()
        self._init_pos = None
        self._item = None

        event.accept()

    def mousePressEvent(self, event, image_item):
        pos = event.scenePos()
        self._init_pos = pos
        rect = self.formTile(pos.x(), pos.y())
        # print pos.x(),pos.y(), rect        
        # self._item.setPen(self.pen())
        # self._scene.addItem(self._item)
        self._ann.update({self._prefix + 'x': rect.x(),
                          self._prefix + 'y': rect.y(),
                          self._prefix + 'width': rect.width(),
                          self._prefix + 'height': rect.height()})
        self._ann.update(self._default_properties)
        if self._commit:
            image_item.addAnnotation(self._ann)
        self.annotationFinished.emit()
        self._init_pos = None
        self._item = None
        event.accept()

    # def mouseMoveEvent(self, event, image_item):
    #     if self._item is not None:
    #         assert self._init_pos is not None
    #         rect = QRectF(self._init_pos, event.scenePos()).normalized()
    #         self._item.setRect(rect)

    #     event.accept()

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

class TileItemInserter_centred(TileItemInserter):

    def __init__(self, labeltool, scene, default_properties=None, prefix="", commit=True):
        TileItemInserter.__init__(self, labeltool, scene, default_properties, prefix, commit)
        self._point_as_centre=True
#__________________________________________________________________________________________
#
# BulkTileItem
class BulkTileItemInserter(RectItemInserter):

    def __init__(self, labeltool, scene, default_properties=None, prefix="", commit=True):
        RectItemInserter.__init__(self, labeltool, scene, default_properties, prefix, commit)

        self._init_pos = None
        self._imgw = IMG_W
        self._imgh = IMG_H
        self._tile = TILE
        self._tile_border = TILE_BORDER
        self._point_as_centre=False
        self._labeltool=labeltool
        self._scene=scene
        self._class_name="pole"

    def mousePressEvent(self, event, image_item):
        pos = event.scenePos()
        self._init_pos = pos
        self._item = QGraphicsRectItem(QRectF(pos.x(), pos.y(), 0, 0))
        self._item.setPen(self.pen())
        self._scene.addItem(self._item)
        event.accept()

    def mouseMoveEvent(self, event, image_item):
        if self._item is not None:
            assert self._init_pos is not None
            rect = QRectF(self._init_pos, event.scenePos()).normalized()
            self._item.setRect(rect)

        event.accept()

    def mouseReleaseEvent(self, event, image_item):
        if self._item is not None:
            if self._item.rect().width() > 1 and \
               self._item.rect().height() > 1:
                rect = self._item.rect()
                rx=int(rect.x())
                ry=int(rect.y())
                rw=int(rect.width())
                rh=int(rect.height())
                # upper bound
                rxw=rx+rw+self.tile_border()[0]
                ryh=ry+rh+self.tile_border()[1]
                # step
                bw=self.tile()[0]+self.tile_border()[0]
                bh=self.tile()[1]+self.tile_border()[1]
                # consider initial x,y to update the upper bound
                init=findTile_base(rx,ry,self._imgw,self._imgh,self._tile,self._tile_border)
                initx=abs(rx-init[0])
                inity=abs(ry-init[1])
                rxw+=initx
                ryh+=inity
                # going through covering tiles
                for x in range(rx,rxw,bw):
                    for y in range(ry,ryh,bh):
                        new_item = TileItemInserter(self._labeltool,self._scene)
                        new_item.mousePressEvent_simulate(event,x,y,image_item,self._class_name)
            self._scene.removeItem(self._item)
            self.annotationFinished.emit()
            self._init_pos = None
            self._item = None

        event.accept()

    def allowOutOfSceneEvents(self):
        return True

    def abort(self):
        if self._item is not None:
            self._scene.removeItem(self._item)
            self._item = None
            self._init_pos = None
        ItemInserter.abort(self)

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

class BulkTileItemInserter_tree(BulkTileItemInserter):

    def __init__(self, labeltool, scene, default_properties=None, prefix="", commit=True):
        BulkTileItemInserter.__init__(self, labeltool, scene, default_properties, prefix, commit)
        self._class_name="tree"


class BulkTileItemInserter_sign(BulkTileItemInserter):

    def __init__(self, labeltool, scene, default_properties=None, prefix="", commit=True):
        BulkTileItemInserter.__init__(self, labeltool, scene, default_properties, prefix, commit)
        self._class_name="sign"


class BulkTileItemInserter_road_light(BulkTileItemInserter):

    def __init__(self, labeltool, scene, default_properties=None, prefix="", commit=True):
        BulkTileItemInserter.__init__(self, labeltool, scene, default_properties, prefix, commit)
        self._class_name="road_light"


class BulkTileItemInserter_power_line(BulkTileItemInserter):

    def __init__(self, labeltool, scene, default_properties=None, prefix="", commit=True):
        BulkTileItemInserter.__init__(self, labeltool, scene, default_properties, prefix, commit)
        self._class_name="power_line"

class BulkTileItemInserter_misc(BulkTileItemInserter):

    def __init__(self, labeltool, scene, default_properties=None, prefix="", commit=True):
        BulkTileItemInserter.__init__(self, labeltool, scene, default_properties, prefix, commit)
        self._class_name="misc"
#__________________________________________________________________________________________
#
# TileItem
#   It is similar to PointItem and RectItem
#   Additionally, it has color, label, pen_width and tile width/height as input parameters
#   Paint module is also different by drawing a rectangle instead of ellipse
#
#   WARNING: TileItem can select and display Tile correctly, 
#               however it saves the tile as x,y
#            Use TileItemInserter for inserter and RectColorWithLabel for item instead
#__________________________________________________________________________________________
class TileItem(BaseItem):

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

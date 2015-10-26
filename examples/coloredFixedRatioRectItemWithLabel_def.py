from PyQt4.QtGui import *
from PyQt4.Qt import *
from sloth.items import BaseItem, RectItem, RectItemInserter, FixedRatioRectItemInserter
import math
from coloredRectItemWithLabel_def import RectColorWithLabel
#
# WARNING:
# You need to change the following parameters based on your images RectColorWithLabel
# FixedRatioRectItem_cutom
#        self._max_w=3840
#        self._max_h=2160
#__________________________________________________________________________________________
#__________________________________________________________________________________________
#
# FixedRatioRectItem_cutom
#
#__________________________________________________________________________________________
class FixedRatioRectItem_cutom(RectColorWithLabel):

#    def __init__(self, model_item=None, prefix="", parent=None,color=Qt.black,label=""):
#        RectColorWithLabel.__init__(self, model_item, prefix, parent)
#    def __init__(self, *args, **kwargs):
#        RectColorWithLabel.__init__(self, *args, **kwargs)
    def __init__(self, model_item=None, prefix="", parent=None,color=Qt.black,label=""):
        #print 'color=',color,'label=',label
        RectColorWithLabel.__init__(self, model_item, prefix, parent,color,label)
        self._max_w=3840
        self._max_h=2160
        #self.setPen(QPen(self._userColor, 2))

    def __call__(self, *args, **kwargs):
        newitem = FixedRatioRectItem_cutom(*args, **kwargs)
        newitem.setColor(self._userColor)
        newitem._text_item.setHtml(self._userLabel)
        return newitem

    def mousePressEvent(self, event):
        #print "FixedRatioRectItem_cutom::mousePressEvent"
        if event.button() & Qt.RightButton != 0:
            w=self._rect.width()
            h=self._rect.height()
            centre_x=self._rect.center().x()
            centre_y=self._rect.center().y()
            ratio=self._rect.width()/self._rect.height()

            self._resize = True
            self._resize_start = event.scenePos()
            self._resize_start_rect = QRectF(self._rect)
            self._upper_half_clicked = (event.scenePos().y() < self._resize_start_rect.center().y())
            self._left_half_clicked  = (event.scenePos().x() < self._resize_start_rect.center().x())
            event.accept()
            #new_w=self._resize_start_rect.width()
            #new_h=new_w/ratio
            #x = centre_x - new_w/2
            #y = centre_y - new_h/2
            #rect = QRectF(QPointF(x,y), QSizeF(new_w, new_h)).normalized()
            #self._updateRect(rect)
            #self.updateModel()
            #event.accept()
        else:
            BaseItem.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        #print "FixedRatioRectItem_cutom::mouseMoveEvent"
        if self._resize:
            diff = event.scenePos() - self._resize_start
            ratio=self._rect.width()/self._rect.height()
            centre_x=self._rect.center().x()
            centre_y=self._rect.center().y()

            changed=False
            if self._left_half_clicked:
                new_w = self._resize_start_rect.width() - diff.x()
                if (new_w>10):
                    w = new_w
                    h = w/ratio
                    changed=True
            else:
                new_w = self._resize_start_rect.width() + diff.x()
                if (new_w>10):
                    w = new_w
                    h = w/ratio
                    changed=True

            if self._upper_half_clicked:
                new_h=self._resize_start_rect.height() - diff.y()
                if (new_h>10):
                    h = new_h
                    w = ratio*h
                    changed=True
            else:
                new_h=self._resize_start_rect.height() + diff.y()
                if (new_h>10):
                    h = new_h
                    w = ratio*h
                    changed=True

            if (changed):
                x = centre_x - w/2
                y = centre_y - h/2
                if (x+w<=self._max_w and y+h<=self._max_h and x>=0 and y>=0):
                    rect = QRectF(QPointF(x,y), QSizeF(w, h)).normalized()
                    self._updateRect(rect)

            self.updateModel()
            event.accept()
        else:
            currentRect=self._rect
            BaseItem.mouseMoveEvent(self, event)
            accepted=True
            if (self._rect.x()<0 or self._rect.y()<0):
                accepted=False
            elif (self._rect.x()+self._rect.width()>self._max_w or self._rect.y()+self._rect.height()>self._max_h):
                accepted=False
            if not(accepted):
                self._updateRect(currentRect)
                self.updateModel()
                event.accept()


    def keyPressEvent(self, event):
        BaseItem.keyPressEvent(self, event)
        step = 1
        if event.modifiers() & Qt.ShiftModifier:
            step = 5
        ds = {Qt.Key_Left:  (-step, 0),
              Qt.Key_Right: (step, 0),
              Qt.Key_Up:    (0, -step),
              Qt.Key_Down:  (0, step),
             }.get(event.key(), None)
        if ds is not None:
            if event.modifiers() & Qt.ControlModifier:
                centre_x=self._rect.center().x()#self._rect.x()+self._rect.width()/2
                centre_y=self._rect.center().y()#self._rect.y()+self._rect.height()/2
                ratio=self._rect.width()/self._rect.height()
                changed=False
                if (ds[0]==0): # change of height
                    newh=self._rect.height() + ds[1]*-2
                    if (newh>10):
                        h = newh
                        w = ratio*h
                        changed=True
                else: # change of width
                    neww=self._rect.width() + ds[0]*2
                    if (neww>10):
                        w = neww
                        h = w/ratio
                        changed=True
                if (changed):
                    x = centre_x - w/2
                    y = centre_y - h/2
                    if (x>=0 and y>=0 and x+w<=self._max_w and y+h<=self._max_h):
                        rect = QRectF(QPointF(x,y), QSizeF(w, h)).normalized()
                        self._updateRect(rect)
            else:
                rect = self._rect.adjusted(*(ds + ds))
                if (rect.x()>=0 and rect.y()>=0 and rect.x()+rect.width()<=self._max_w and rect.y()+rect.height()<=self._max_h):
                    self._updateRect(rect)
            self.updateModel()
            event.accept()

#
# FixedRatioRectItemInserter_custom_base
#
#__________________________________________________________________________________________

class FixedRatioRectItemInserter_custom_base(FixedRatioRectItemInserter):
    def __init__(self, labeltool, scene, default_properties=None,
                 prefix="", commit=True,ratio=.5):
        default_properties['_ratio']=ratio
        FixedRatioRectItemInserter.__init__(self, labeltool, scene, default_properties,
                                  prefix, commit)
        #self._ratio=ratio
        #self._width = 222
        #self._height = 74
        self.setOthers()

#    def __init__(self, *args, **kwargs):
#        print args
#        print kwargs
#        self._width = kwargs.get('rw',222)
#        self._height = kwargs.get('rh',74)
#        print self._width
#        if 'rw' in kwargs:
#            del kwargs['rw']
#        if 'rh' in kwargs:
#            del kwargs['rh']
#        RectItemInserter.__init__(self, *args, **kwargs)
#        self.setOthers()


    def setOthers(self):
        # ratio
        # self._ratio= float(self._width/self._height)
        # max W,H
        new_image = self._labeltool.currentImage()
        img = self._labeltool.getImage(new_image)
        self._max_w=img.shape[1]
        self._max_h=img.shape[0]

    def mousePressEvent_mine(self, event, image_item):
        #print "FixedRatioRectItemInserter_custom::mousePressEvent"
        pos = event.scenePos()

        # check if it is out of image boundary
        if (pos.x()<0 or pos.y()<0):
            return
        if (pos.x()>self._max_w or pos.y()>self._max_h):
            return

        self._init_pos = pos
        xmin=self._init_pos.x()-(self._width/2)
        ymin=self._init_pos.y()-(self._height/2)
        if xmin<0:
            xmin=0
        if ymin<0:
            ymin=0
        w=self._width
        h=self._height
        if (xmin+w>self._max_w):
            w=self._max_w-xmin
            h=w/self._ratio
        if (ymin+h>self._max_h):
            h=self._max_h-ymin
            w=h*self._ratio
        self._item = QGraphicsRectItem(QRectF(xmin,ymin,w,h))
        #self._item.setPen(self.pen())
        self._scene.addItem(self._item)
        event.accept()

    def mouseMoveEvent(self, event, image_item):
        if self._item is not None:
            #print "FixedRatioRectItemInserter_custom::mouseMoveEvent"

            new_geometry = QRectF(self._item.rect().topLeft(),
                                  event.scenePos())
            dx = new_geometry.width()
            dy = new_geometry.height()
            d = math.sqrt(dx * dx + dy * dy)
            r = self._ratio
            k = math.sqrt(r * r + 1)
            h = d / k
            w = d * r / k
            new_geometry.setWidth(w)
            new_geometry.setHeight(h)

            # check if it is out of image boundary
            if new_geometry.x()+new_geometry.width()>self._max_w:
                return
            if new_geometry.y()+new_geometry.height()>self._max_h:
                return

            self._item.setRect(new_geometry.normalized())

        event.accept()

    def mouseMoveEvent_original(self, event, image_item):
        if self._item is not None:
            #new_geometry = QRectF(self._current_item.rect().topLeft(), event.scenePos())
            new_geometry = QRectF(self._item.rect().topLeft(), event.scenePos())
            dx = new_geometry.width()
            dy = new_geometry.height()
            d = math.sqrt(dx * dx + dy * dy)
            r = self._ratio
            k = math.sqrt(r * r + 1)
            h = d / k
            w = d * r / k
            new_geometry.setWidth(w)
            new_geometry.setHeight(h)
            #self._current_item.setRect(new_geometry.normalized())
            self._item.setRect(new_geometry.normalized())

        event.accept()
#
# FixedRatioRectItemInserter_custom1
#
#__________________________________________________________________________________________
class FixedRatioRectItemInserter_custom1(FixedRatioRectItemInserter_custom_base):
    def __init__(self, labeltool, scene, default_properties=None,
                 prefix="", commit=True):
        FixedRatioRectItemInserter_custom_base.__init__(self, labeltool, scene, default_properties,
                                  prefix, commit,ratio=0.5)

#
# FixedRatioRectItemInserter_custom2
#
#__________________________________________________________________________________________
class FixedRatioRectItemInserter_custom2(FixedRatioRectItemInserter_custom_base):
    def __init__(self, labeltool, scene, default_properties=None,
                 prefix="", commit=True):
        FixedRatioRectItemInserter_custom_base.__init__(self, labeltool, scene, default_properties,
                                  prefix, commit,ratio=2)

#class FixedRatioRectItemInserter_custom2(FixedRatioRectItemInserter_custom):
#    def __init__(self, labeltool, scene, default_properties=None,
#                 prefix="", commit=True):
#        FixedRatioRectItemInserter_custom.__init__(self, labeltool, scene, default_properties,
#                                  prefix, commit)
#        self._width *= 2
#        self._height *= 2
#        self.setOthers()

#
# FixedRatioRectItemInserter_custom3
#
#__________________________________________________________________________________________
class FixedRatioRectItemInserter_custom3(FixedRatioRectItemInserter_custom_base):
    def __init__(self, labeltool, scene, default_properties=None,
                 prefix="", commit=True):
        FixedRatioRectItemInserter_custom_base.__init__(self, labeltool, scene, default_properties,
                                  prefix, commit,ratio=1.5)
#
# FixedRatioRectItemInserter_custom3
#
#__________________________________________________________________________________________

#class FixedRatioRectItemInserter_custom4(FixedRatioRectItemInserter_custom):
#    def __init__(self, labeltool, scene, default_properties=None,
#                 prefix="", commit=True):
#        FixedRatioRectItemInserter_custom.__init__(self, labeltool, scene, default_properties,
#                                  prefix, commit)
#        self._width *= 3
#        self._height *= 3
#        self.setOthers()

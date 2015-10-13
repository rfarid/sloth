import math
from PyQt4.QtGui import *
from PyQt4.Qt import *
from sloth.items import BaseItem, RectItem, RectItemInserter

class FixedRatioRectItem(RectItem):

    def mousePressEvent(self, event):
        #print "FixedRatioRectItem::mousePressEvent"
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
        #print "FixedRatioRectItem::mouseMoveEvent"
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
                rect = QRectF(QPointF(x,y), QSizeF(w, h)).normalized()
                self._updateRect(rect)

            self.updateModel()
            event.accept()
        else:
            BaseItem.mouseMoveEvent(self, event)

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
                    newh=self._rect.height() + ds[1]*2
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
                    rect = QRectF(QPointF(x,y), QSizeF(w, h)).normalized()
                    self._updateRect(rect)
            else:
                rect = self._rect.adjusted(*(ds + ds))
                self._updateRect(rect)
            self.updateModel()
            event.accept()

class FixedRatioRectItemInserter(RectItemInserter):
    def __init__(self, labeltool, scene, default_properties=None,
                 prefix="", commit=True):
        RectItemInserter.__init__(self, labeltool, scene, default_properties,
                                  prefix, commit)
        self._width = 222
        self._height = 74
        self._ratio= float(self._width/self._height)

    def mousePressEvent(self, event, image_item):
        #print "FixedRatioRectItemInserter::mousePressEvent"
        pos = event.scenePos()
        self._init_pos = pos
        xmin=self._init_pos.x()-(self._width/2)
        ymin=self._init_pos.y()-(self._height/2)

        self._item = QGraphicsRectItem(QRectF(xmin,ymin,self._width,self._height))
        self._item.setPen(self.pen())
        self._scene.addItem(self._item)
        event.accept()

    def mouseMoveEvent(self, event, image_item):
        if self._item is not None:
            #print "FixedRatioRectItemInserter::mouseMoveEvent"
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
            self._item.setRect(new_geometry.normalized())

        event.accept()

class FixedRatioRectItemInserter2(FixedRatioRectItemInserter):
    def __init__(self, labeltool, scene, default_properties=None,
                 prefix="", commit=True):
        RectItemInserter.__init__(self, labeltool, scene, default_properties,
                                  prefix, commit)
        self._width = 444
        self._height = 148
        self._ratio= float(self._width/self._height)

class FixedRatioRectItemInserter3(FixedRatioRectItemInserter):
    def __init__(self, labeltool, scene, default_properties=None,
                 prefix="", commit=True):
        RectItemInserter.__init__(self, labeltool, scene, default_properties,
                                  prefix, commit)
        self._width = 666
        self._height = 222
        self._ratio= float(self._width/self._height)

# This is sloth's default configuration.
#
# The configuration file is a simple python module with module-level
# variables.  This module contains the default values for sloth's 
# configuration variables.
#
# In all cases in the configuration where a python callable (such as a
# function, class constructor, etc.) is expected, it is equally possible
# to specify a module path (as string) pointing to such a python callable.
# It will then be automatically imported.

# LABELS
#
# List/tuple of dictionaries that defines the label classes
# that are handled by sloth.  For each label, there should
# be one dictionary that contains the following keys:
#
#   - 'item' : Visualization item for this label. This can be
#              any python callable or a module path string 
#              implementing the visualization item interface.
#
#   - 'inserter' : (optional) Item inserter for this label.
#                  If the user selects to insert a new label of this class
#                  the inserter is responsible to actually 
#                  capture the users mouse actions and insert
#                  a new label into the annotation model.
#
#   - 'hotkey' : (optional) A keyboard shortcut starting 
#                the insertion of a new label of this class.
#
#   - 'attributes' : (optional) A dictionary that defines the
#                    keys and possible values of this label
#                    class.
#
#   - 'text' : (optional) A label for the item's GUI button.
LABELS = (
    {
        'attributes': {
            'class':      'FixedRatioRect',
        },
        'inserter': FixedRatioRectItemInserter,
        'item':     FixedRatioRectItem,
        'hotkey':   'f',
        'text':     'FixedRatioRect_222x74',
    },
    {
        'attributes': {
            'class':      'FixedRatioRect2',
        },
        'inserter': FixedRatioRectItemInserter2,
        'item':     FixedRatioRectItem,
        'hotkey':   'g',
        'text':     'FixedRatioRect_444x148',
    },
    {
        'attributes': {
            'class':      'FixedRatioRect3',
        },
        'inserter': FixedRatioRectItemInserter3,
        'item':     FixedRatioRectItem,
        'hotkey':   'h',
        'text':     'FixedRatioRectangle_666x222',
    },
#    {
#        'attributes': {
#            'class':      'rect',
#        },
#        'inserter': 'sloth.items.RectItemInserter',
#        'item':     'sloth.items.RectItem',
#        'hotkey':   'r',
#        'text':     'Rectangle',
#    },
)

# HOTKEYS
#
# Defines the keyboard shortcuts.  Each hotkey is defined by a tuple
# with at least 2 entries, where the first entry is the hotkey (sequence),
# and the second entry is the function that is called.  The function
# should expect a single parameter, the labeltool object.  The optional
# third entry -- if present -- is expected to be a string describing the 
# action.
HOTKEYS = (
    ('Space',     [lambda lt: lt.currentImage().confirmAll(),
                   lambda lt: lt.currentImage().setUnlabeled(False),
                   lambda lt: lt.gotoNext()
                  ],                                         'Mark image as labeled/confirmed and go to next'),
    ('Backspace', lambda lt: lt.gotoPrevious(),              'Previous image/frame'),
    ('PgDown',    lambda lt: lt.gotoNext(),                  'Next image/frame'),
    ('PgUp',      lambda lt: lt.gotoPrevious(),              'Previous image/frame'),
    ('Tab',       lambda lt: lt.selectNextAnnotation(),      'Select next annotation'),
    ('Shift+Tab', lambda lt: lt.selectPreviousAnnotation(),  'Select previous annotation'),
    ('Ctrl+f',    lambda lt: lt.view().fitInView(),          'Fit current image/frame into window'),
    ('Del',       lambda lt: lt.deleteSelectedAnnotations(), 'Delete selected annotations'),
    ('ESC',       lambda lt: lt.exitInsertMode(),            'Exit insert mode'),
    ('Shift+l',   lambda lt: lt.currentImage().setUnlabeled(False), 'Mark current image as labeled'),
    ('Shift+c',   lambda lt: lt.currentImage().confirmAll(), 'Mark all annotations in image as confirmed'),
)

# CONTAINERS
#
# A list/tuple of two-tuples defining the mapping between filename pattern and
# annotation container classes.  The filename pattern can contain wildcards
# such as * and ?.  The corresponding container is expected to either a python
# class implementing the sloth container interface, or a module path pointing
# to such a class.
CONTAINERS = (
    ('*.json',       'sloth.annotations.container.JsonContainer'),
    ('*.msgpack',    'sloth.annotations.container.MsgpackContainer'),
    ('*.yaml',       'sloth.annotations.container.YamlContainer'),
    ('*.pickle',     'sloth.annotations.container.PickleContainer'),
    ('*.sloth-init', 'sloth.annotations.container.FileNameListContainer'),
)

# PLUGINS
#
# A list/tuple of classes implementing the sloth plugin interface.  The
# classes can either be given directly or their module path be specified 
# as string.
PLUGINS = (
)



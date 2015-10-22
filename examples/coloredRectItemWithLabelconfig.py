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
        self.setPen(QPen(self._userColor, 2))
        return newitem

# colors={1:'ColorDarkRed',2:'ColorDarkGreen',4:'ColorDarkBlue',6:'ColorDarkGray',8:'ColorRed',10:'ColorGreen',12:'ColorBlue',14:'ColorDarkCyan',16:'ColorBlack'}
LABELS = (
    {
        'attributes': {
            'class':      'rect',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     'sloth.items.RectItem',
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorDarkRed',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkRed),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'Vegetation',
            #'label':      'Vegetation',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkGreen,label="Vegetation"),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'Sky',
            #'label':      'Sky',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkBlue,label="SKY"),
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorDarkGray',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkGray),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorRed',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.red),
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorGreen',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.green),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorBlue',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.blue),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorDarkCyan',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkCyan),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorBlack',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.black),  
        'text':     'Rectangle',
    },

)

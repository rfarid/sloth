from PyQt4.QtGui import QPen
from PyQt4.Qt import Qt
from sloth.items import RectItem


class RectColor(RectItem):
    def __init__(self, model_item=None, prefix="", parent=None, color=Qt.red):
        RectItem.__init__(self, model_item, prefix, parent)
	self._userColor=color
        # set drawing pen to red with width 2
        self.setPen(QPen(color, 2))

    def __call__(self, *args, **kwargs):
        newitem = RectItem(*args, **kwargs)
	newitem.setColor(self._userColor)
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
        'item':     RectColor(color=Qt.darkRed),  # use custom rect item instead of sloth's standard item
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorDarkGreen',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColor(color=Qt.darkGreen),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorDarkBlue',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColor(color=Qt.darkBlue),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorDarkGray',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColor(color=Qt.darkGray),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorRed',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColor(color=Qt.red),
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorGreen',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColor(color=Qt.green),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorBlue',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColor(color=Qt.blue),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorDarkCyan',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColor(color=Qt.darkCyan),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorBlack',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColor(color=Qt.black),  
        'text':     'Rectangle',
    },

)


from coloredRectItemWithLabel_def import RectColorWithLabel
from PyQt4.Qt import Qt

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
            'class':      'rectColorDarkGreen',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkGreen),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'rectColorDarkBlue',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkBlue),  
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

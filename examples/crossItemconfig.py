from crossItem_def import CrossItem, CrossItemInserter
from PyQt4.Qt import Qt

LABELS = (
    {
        'attributes': {
            'class':      'point',
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     'sloth.items.PointItem',
        'text':     'Point',
    },
    {
        'attributes': {
            'class':      'pole',
        },
        'inserter': 'crossItem_def.CrossItemInserter',
        'item':     CrossItem(color=Qt.darkRed,radius=10,label="Pole"),  
        'text':     'Point',
    },
    {
        'attributes': {
            'class':      'tree',
        },
        'inserter': 'crossItem_def.CrossItemInserter',
        'item':     CrossItem(color=Qt.darkGreen,label="tree"),  
        'text':     'Point',
    },
    {
        'attributes': {
            'class':      'sky_cloud',
        },
        'inserter': 'crossItem_def.CrossItemInserter',
        'item':     CrossItem(color=Qt.darkBlue,label="sky_cloud"),  
        'text':     'Point',
    },
    {
        'attributes': {
            'class':      'pointColorDarkGray',
        },
        'inserter': 'crossItem_def.CrossItemInserter',
        'item':     CrossItem(color=Qt.darkGray),  
        'text':     'Point',
    },
    {
        'attributes': {
            'class':      'pointColorRed',
        },
        'inserter': 'crossItem_def.CrossItemInserter',
        'item':     CrossItem(color=Qt.red),
        'text':     'Point',
    },
    {
        'attributes': {
            'class':      'pointColorGreen',
        },
        'inserter': 'crossItem_def.CrossItemInserter',
        'item':     CrossItem(color=Qt.green),  
        'text':     'Point',
    },
    {
        'attributes': {
            'class':      'pointColorBlue',
        },
        'inserter': 'crossItem_def.CrossItemInserter',
        'item':     CrossItem(color=Qt.blue),  
        'text':     'Point',
    },
    {
        'attributes': {
            'class':      'pointColorDarkCyan',
        },
        'inserter': 'crossItem_def.CrossItemInserter',
        'item':     CrossItem(color=Qt.darkCyan),  
        'text':     'Point',
    },
    {
        'attributes': {
            'class':      'pointColorBlack',
        },
        'inserter': 'crossItem_def.CrossItemInserter',
        'item':     CrossItem(color=Qt.black),  
        'text':     'Point',
    },

)

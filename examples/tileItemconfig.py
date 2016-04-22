from tileItem_def import TileItem
from coloredRectItemWithLabel_def import RectColorWithLabel
from PyQt4.Qt import Qt
TILE=(96,124)
TILE_BORDER=(5,2)
# pole, tree, sign, power_line
LABELS = (
    # {
    #     'attributes': {
    #         'class':      'tile_pac',
    #     },
    #     'inserter': 'sloth.items.PointItemInserter',
    #     'item':     TileItem(color=Qt.red,tile=(90,45),point_as_centre=True),  
    #     'text':     'Point',
    # },
    {
        'attributes': {
            'class':      'pole_Rect',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.yellow,label="pole"),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'pole',
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     TileItem(color=Qt.white,pen_width=4,label="pole",tile=TILE,tile_border=TILE_BORDER,point_as_centre=False),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'tree_Rect',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkGreen,label="tree"),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'tree',
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     TileItem(color=Qt.darkGreen,pen_width=4,label="tree",tile=TILE,tile_border=TILE_BORDER,point_as_centre=False),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'sign_Rect',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkBlue,label="sign"),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'sign',
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     TileItem(color=Qt.darkBlue,pen_width=4,label="sign",tile=TILE,tile_border=TILE_BORDER,point_as_centre=False),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'power_line_Rect',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkRed,label="power_line"),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'power_line',
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     TileItem(color=Qt.darkRed,pen_width=4,label="power_line",tile=TILE,tile_border=TILE_BORDER,point_as_centre=False),  
        'text':     'Rectangle',
    },
)

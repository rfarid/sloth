from tileItem_def import TileItemInserter, TileItemInserter_centred
from coloredRectItemWithLabel_def import RectColorWithLabel
from sloth.items import RectItemInserter
from PyQt4.Qt import Qt
TILE=(96,124)
TILE_BORDER=(5,2)

additional_classes=['tree', 'sign', 'road_light' , 'power_line']
colours=[Qt.darkMagenta,Qt.darkBlue,Qt.darkRed,Qt.cyan]
LABELS = (
    {
        'attributes': {
            'class':      'Rect',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     'sloth.items.RectItem',
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'tile_pac',
        },
        'inserter': TileItemInserter_centred,
        'item':     RectColorWithLabel(color=Qt.red,label="tile_pac"),
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'pole_Rect',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.yellow,label="pole",pen_width=2),  
        'text':     'Rectangle',
    },
    {
        'attributes': {
            'class':      'pole',
        },
        'inserter': TileItemInserter,
        'item':     RectColorWithLabel(color=Qt.white,label="pole",pen_width=4),
        'text':     'Rectangle',
    },
)
n=len(additional_classes)
for i in range(n):
    rclass=additional_classes[i]
    rcolor=colours[i]
    ne_class=rclass+"_Rect"
    # if len(ne_class)>12:
    #     ne_class=ne_class[:12]
    new_entry=    {
        'attributes': {
            'class':      ne_class,
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=rcolor,label=rclass,pen_width=2),
        'text':     'Rectangle',
    }
    LABELS += (new_entry,)
    new_entry=    {
        'attributes': {
            'class':      rclass,
        },
        'inserter': TileItemInserter,
        'item':     RectColorWithLabel(color=rcolor,label=rclass,pen_width=4),
        'text':     'Rectangle',
    }
    LABELS += (new_entry,)

    # {
    #     'attributes': {
    #         'class':      'tree_Rect',
    #     },
    #     'inserter': 'sloth.items.RectItemInserter',
    #     'item':     tileItem_def.RectColorWithLabel(color=Qt.darkGreen,label="tree"),  
    #     'text':     'Rectangle',
    # },
    # {
    #     'attributes': {
    #         'class':      'tree',
    #     },
    #     'inserter': tileItem_def.TileItemInserter(tile=TILE,tile_border=TILE_BORDER,point_as_centre=False),
    #     'item':     'sloth.items.RectItem',
    #     'text':     'Rectangle',
    # },
    # {
    #     'attributes': {
    #         'class':      'sign_Rect',
    #     },
    #     'inserter': 'sloth.items.RectItemInserter',
    #     'item':     RectColorWithLabel(color=Qt.darkBlue,label="sign"),  
    #     'text':     'Rectangle',
    # },
    # {
    #     'attributes': {
    #         'class':      'sign',
    #     },
    #     'inserter': TileItemInserter(tile=TILE,tile_border=TILE_BORDER,point_as_centre=False),
    #     'item':     TileItem(color=Qt.darkBlue,pen_width=4,label="sign",tile=TILE,tile_border=TILE_BORDER,point_as_centre=False),  
    #     'text':     'Rectangle',
    # },
    # {
    #     'attributes': {
    #         'class':      'power_line_Rect',
    #     },
    #     'inserter': 'sloth.items.RectItemInserter',
    #     'item':     RectColorWithLabel(color=Qt.darkRed,label="power_line"),  
    #     'text':     'Rectangle',
    # },
    # {
    #     'attributes': {
    #         'class':      'power_line',
    #     },
    #     'inserter': TileItemInserter(tile=TILE,tile_border=TILE_BORDER,point_as_centre=False),
    #     'item':     TileItem(color=Qt.darkRed,pen_width=4,label="power_line",tile=TILE,tile_border=TILE_BORDER,point_as_centre=False),  
    #     'text':     'Rectangle',
    # },
    # {
    #     'attributes': {
    #         'class':      'road_light_Rect',
    #     },
    #     'inserter': 'sloth.items.RectItemInserter',
    #     'item':     RectColorWithLabel(color=Qt.darkCyan,label="road_light"),  
    #     'text':     'Rectangle',
    # },
    # {
    #     'attributes': {
    #         'class':      'road_light',
    #     },
    #     'inserter': TileItemInserter(tile=TILE,tile_border=TILE_BORDER,point_as_centre=False),
    #     'item':     TileItem(color=Qt.darkCyan,pen_width=4,label="road_light",tile=TILE,tile_border=TILE_BORDER,point_as_centre=False),  
    #     'text':     'Rectangle',
    # },
# )

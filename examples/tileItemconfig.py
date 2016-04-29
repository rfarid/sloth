import tileItem_def
from coloredRectItemWithLabel_def import RectColorWithLabel
from sloth.items import RectItemInserter
from PyQt4.Qt import Qt
TILE=(96,124)
TILE_BORDER=(5,2)

class_names=['pole','tree', 'sign', 'road_light' , 'power_line','misc']
colours=[Qt.white,Qt.darkMagenta,Qt.darkBlue,Qt.darkRed,Qt.cyan,Qt.yellow]
bulk_inserters=  [tileItem_def.BulkTileItemInserter, tileItem_def.BulkTileItemInserter_tree, 
            tileItem_def.BulkTileItemInserter_sign, tileItem_def.BulkTileItemInserter_road_light,
            tileItem_def.BulkTileItemInserter_power_line,tileItem_def.BulkTileItemInserter_misc]
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
        'inserter': tileItem_def.TileItemInserter_centred,
        'item':     RectColorWithLabel(color=Qt.red,label="tile_pac"),
        'text':     'Rectangle',
    },
    # {
    #     'attributes': {
    #         'class':      'pole_Rect',
    #     },
    #     'inserter': 'sloth.items.RectItemInserter',
    #     'item':     RectColorWithLabel(color=Qt.yellow,label="pole",pen_width=2),  
    #     'text':     'Rectangle',
    # },
    # {
    #     'attributes': {
    #         'class':      'pole',
    #     },
    #     'inserter': TileItemInserter,
    #     'item':     RectColorWithLabel(color=Qt.white,label="pole",pen_width=4),
    #     'text':     'Rectangle',
    # },
    # {
    #     'attributes': {
    #         'class':      'pole_bulk',
    #     },
    #     'inserter': BulkTileItemInserter,
    #     'item':     RectColorWithLabel(color=Qt.white,label="pole",pen_width=4),
    #     'text':     'Rectangle',
    # },
)
n=len(class_names)

for i in range(n):
    rclass=class_names[i]
    rcolor=colours[i]
    ne_class=rclass+"Rec"
    new_entry=    {
        'attributes': {
            'class':      ne_class,
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=rcolor,label=rclass,pen_width=2),
        'text':     'Rectangle',
    }
    LABELS += (new_entry,)

for i in range(n):
    rclass=class_names[i]
    rcolor=colours[i]
    new_entry=    {
        'attributes': {
            'class':      rclass,
        },
        'inserter': tileItem_def.TileItemInserter,
        'item':     RectColorWithLabel(color=rcolor,label=rclass,pen_width=4),
        'text':     'Rectangle',
    }
    LABELS += (new_entry,)


for i in range(n):
    rclass=class_names[i]
    new_entry= {
        'attributes': {
            'class':      rclass+'_bulk',
        },
        'inserter': bulk_inserters[i],
        'item':     RectColorWithLabel,
        'text':     'Rectangle',
    }
    LABELS += (new_entry,)

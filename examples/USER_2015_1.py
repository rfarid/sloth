# Half pole top     0.37                    yellow
# Cross-arm Rect    3.0 (angled:0.66)       darkMagenta
# Transformer       0.75                    magenta
# Insulator                                 
# Road Light        1.0                     white
# BackGround        No Fixed Ratio
#   SKY                 darkBlue
#   CLOUD               blue
#   GRASS               green
#   VEGETATION          darkGreen
#   BUILDING            
#   ROAD_SIGN           
#   ROAD_SURFACE        darkGray
#   OTHER               darkRed

from coloredFixedRatioRectItemWithLabel_def import FixedRatioRectItemInserter_custom_base, FixedRatioRectItem_cutom, RectColorWithLabel
from PyQt4.QtGui import *
from PyQt4.Qt import *
from sloth.items import BaseItem, RectItem, RectItemInserter, FixedRatioRectItemInserter
import math
#
# FRWL_cross_arm
#
#__________________________________________________________________________________________
class FRWL_cross_arm(FixedRatioRectItemInserter_custom_base):
    def __init__(self, labeltool, scene, default_properties=None,
                 prefix="", commit=True):
        FixedRatioRectItemInserter_custom_base.__init__(self, labeltool, scene, default_properties,
                                  prefix, commit,ratio=3.0)
#
# FRWL_angled_cross_arm
#
#__________________________________________________________________________________________
class FRWL_angled_cross_arm(FixedRatioRectItemInserter_custom_base):
    def __init__(self, labeltool, scene, default_properties=None,
                 prefix="", commit=True):
        FixedRatioRectItemInserter_custom_base.__init__(self, labeltool, scene, default_properties,
                                  prefix, commit,ratio=0.66)
#__________________________________________________________________________________________
# FRWL_half_pole_top
#
#__________________________________________________________________________________________
class FRWL_half_pole_top(FixedRatioRectItemInserter_custom_base):
    def __init__(self, labeltool, scene, default_properties=None,
                 prefix="", commit=True):
        FixedRatioRectItemInserter_custom_base.__init__(self, labeltool, scene, default_properties,
                                  prefix, commit,ratio=0.37)
#__________________________________________________________________________________________
# FRWL_transformer
#
#__________________________________________________________________________________________
class FRWL_transformer(FixedRatioRectItemInserter_custom_base):
    def __init__(self, labeltool, scene, default_properties=None,
                 prefix="", commit=True):
        FixedRatioRectItemInserter_custom_base.__init__(self, labeltool, scene, default_properties,
                                  prefix, commit,ratio=0.75)

#__________________________________________________________________________________________
# FRWL_road_light
#
#__________________________________________________________________________________________
class FRWL_road_light(FixedRatioRectItemInserter_custom_base):
    def __init__(self, labeltool, scene, default_properties=None,
                 prefix="", commit=True):
        FixedRatioRectItemInserter_custom_base.__init__(self, labeltool, scene, default_properties,
                                  prefix, commit,ratio=1.0)

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
            'class':      'FRWL_cross_arm',
        },
        'inserter': FRWL_cross_arm,
        'item':     FixedRatioRectItem_cutom(color=Qt.black,label="cross_arm"),
        'hotkey':   'c',
        'text':     'Cross arm',
    },
        'attributes': {
            'class':      'FRWL_angled_cross_arm',
        },
        'inserter': FRWL_cross_arm,
        'item':     FixedRatioRectItem_cutom(color=Qt.darkMagenta,label="angled_cross_arm"),
        'hotkey':   'c',
        'text':     'Cross arm(Angled)',
    },
    {
        'attributes': {
            'class':      'FRWL_half_pole_top',
        },
        'inserter': FRWL_half_pole_top,
        'item':     FixedRatioRectItem_cutom(color=Qt.yellow,label="half_pole_top"),
        'hotkey':   'p',
        'text':     'half_pole_top',
    },
    {
        'attributes': {
            'class':      'FRWL_transformer',
        },
        'inserter': FRWL_transformer,
        'item':     FixedRatioRectItem_cutom(color=Qt.magenta,label="transformer"),
        'hotkey':   't',
        'text':     'Transformer',
    },
    {
        'attributes': {
            'class':      'FRWL_road_light',
        },
        'inserter': FRWL_road_light,
        'item':     FixedRatioRectItem_cutom(color=Qt.white,label="road_light"),
        'hotkey':   'r',
        'text':     'Road light',
    },
    {
        'attributes': {
            'class':      'Sky',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkBlue,label="SKY"),
        'hotkey':   's',
        'text':     'SKY',
    },
    {
        'attributes': {
            'class':      'Cloud',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.blue,label="Cloud"),
        'text':     'CLOUD',
    },
    {
        'attributes': {
            'class':      'Grass',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.green,label="Grass"),
        'text':     'GRASS',
    },
    {
        'attributes': {
            'class':      'Vegetation',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkGreen,label="Vegetation"),
        'text':     'VEGETATION',
    },
    {
        'attributes': {
            'class':      'Road Surface',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkGray,label="Road Surface"),
        'text':     'ROAD SURFACE',
    },
    {
        'attributes': {
            'class':      'Other',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     RectColorWithLabel(color=Qt.darkRed,label="Other"),
        'text':     'OTHER',
    },
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



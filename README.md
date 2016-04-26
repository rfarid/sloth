sloth
=====

[![Build Status](https://travis-ci.org/cvhciKIT/sloth.svg)](https://travis-ci.org/cvhciKIT/sloth)

sloth is a tool for labeling image and video data for computer vision research.

The documentation can be found at http://sloth.readthedocs.org/ .

Latest Releases
===============

2013/11/29 v1.0: 2e69fdae40f89050fbaeef22491eee2a92e78b4f [.zip](https://github.com/cvhciKIT/sloth/archive/v1.0.zip) [.tar.gz](https://github.com/cvhciKIT/sloth/archive/v1.0.tar.gz)

For a full list, visit https://github.com/cvhciKIT/sloth/releases

About This Fork
===============
This fork includes some additional changes. For example:

1. Adding "Add Images" icon to the UI to load more than one image at once.
2. Fixing the issue of setting proper file path while saving.
3. Some modification to guarantee that the Rectangle Coordinates are not out of image __boundary__.
3. Adding various versions of __FixedRatioRect__ including colored and labeled options.
4. Adding __Cross__ item similar to Point item by showing the selected point as a size-controlled coloured cross with a proper label
5. Adding __Tile__ item __inserter__ similar to Point item by showing the corresponding rectangular tile
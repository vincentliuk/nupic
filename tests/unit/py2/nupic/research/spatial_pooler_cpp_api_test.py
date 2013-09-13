#! /usr/bin/env python


import unittest2 as unittest

from nupic.bindings.algorithms import SpatialPooler as CPPSpatialPooler

import spatial_pooler_py_api_test as pytest

pytest.SpatialPooler = CPPSpatialPooler

SpatialPoolerCPPAPITest = pytest.SpatialPoolerAPITest


if __name__ == "__main__":
  unittest.main()
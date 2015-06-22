#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-06-22.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import binary
from fhirdate import FHIRDate


class BinaryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        return binary.Binary(js)
    
    def testBinary1(self):
        inst = self.instantiate_from("binary-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Binary instance")
        self.implBinary1(inst)
        inst2 = binary.Binary(inst.as_json())
        self.implBinary1(inst2)
    
    def implBinary1(self, inst):
        self.assertEqual(inst.contentType, "application/pdf")
        self.assertEqual(inst.id, "example")


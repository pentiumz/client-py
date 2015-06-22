#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-06-22.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import bodysite
from fhirdate import FHIRDate


class BodySiteTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        return bodysite.BodySite(js)
    
    def testBodySite1(self):
        inst = self.instantiate_from("bodysite-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodySite instance")
        self.implBodySite1(inst)
        inst2 = bodysite.BodySite(inst.as_json())
        self.implBodySite1(inst2)
    
    def implBodySite1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "53120007")
        self.assertEqual(inst.code.coding[0].display, "Arm")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Arm")
        self.assertEqual(inst.description, "front of upper left arm directly below the tattoo")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://www.acmehosp.com/bodysites")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.image[0].contentType, "image/png;base64")
        self.assertEqual(inst.image[0].title, "ARM")
        self.assertEqual(inst.mod[0].coding[0].code, "419161000")
        self.assertEqual(inst.mod[0].coding[0].display, "Unilateral left")
        self.assertEqual(inst.mod[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.mod[0].text, "Left")
        self.assertEqual(inst.mod[1].coding[0].code, "261183002")
        self.assertEqual(inst.mod[1].coding[0].display, "Upper")
        self.assertEqual(inst.mod[1].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.mod[1].text, "Upper")
        self.assertEqual(inst.mod[2].coding[0].code, "255549009")
        self.assertEqual(inst.mod[2].coding[0].display, "Anterior")
        self.assertEqual(inst.mod[2].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.mod[2].text, "Anterior")
        self.assertEqual(inst.text.status, "generated")


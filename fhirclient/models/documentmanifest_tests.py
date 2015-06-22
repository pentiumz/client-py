#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-06-22.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import documentmanifest
from fhirdate import FHIRDate


class DocumentManifestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        return documentmanifest.DocumentManifest(js)
    
    def testDocumentManifest1(self):
        inst = self.instantiate_from("documentmanifest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DocumentManifest instance")
        self.implDocumentManifest1(inst)
        inst2 = documentmanifest.DocumentManifest(inst.as_json())
        self.implDocumentManifest1(inst2)
    
    def implDocumentManifest1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2004-12-25T23:50:50-05:00").date)
        self.assertEqual(inst.created.as_json(), "2004-12-25T23:50:50-05:00")
        self.assertEqual(inst.description, "Physical")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.masterIdentifier.system, "http://example.org/documents")
        self.assertEqual(inst.masterIdentifier.value, "23425234234-2346")
        self.assertEqual(inst.source, "urn:oid:1.3.6.1.4.1.21367.2009.1.2.1")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.div, "<div>Text</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.text, "History and Physical")


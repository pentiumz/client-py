#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-06-22.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import eligibilityresponse
from fhirdate import FHIRDate


class EligibilityResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        return eligibilityresponse.EligibilityResponse(js)
    
    def testEligibilityResponse1(self):
        inst = self.instantiate_from("eligibilityresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityResponse instance")
        self.implEligibilityResponse1(inst)
        inst2 = eligibilityresponse.EligibilityResponse(inst.as_json())
        self.implEligibilityResponse1(inst2)
    
    def implEligibilityResponse1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Policy is currently in-force.")
        self.assertEqual(inst.id, "E2500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/eligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "881234")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.text.div, "<div>A human-readable rendering of the EligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")


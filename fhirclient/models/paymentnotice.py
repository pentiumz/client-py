#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/PaymentNotice) on 2015-06-22.
#  2015, SMART Health IT.


import coding
import domainresource
import fhirdate
import fhirreference
import identifier


class PaymentNotice(domainresource.DomainResource):
    """ PaymentNotice request.
    
    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """
    
    resource_name = "PaymentNotice"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.paymentStatus = None
        """ Status of the payment.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.request = None
        """ Request reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.response = None
        """ Response reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.target = None
        """ Insurer or Regulatory body.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        super(PaymentNotice, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(PaymentNotice, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("organization", "organization", fhirreference.FHIRReference, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False),
            ("paymentStatus", "paymentStatus", coding.Coding, False),
            ("provider", "provider", fhirreference.FHIRReference, False),
            ("request", "request", fhirreference.FHIRReference, False),
            ("response", "response", fhirreference.FHIRReference, False),
            ("ruleset", "ruleset", coding.Coding, False),
            ("target", "target", fhirreference.FHIRReference, False),
        ])
        return js


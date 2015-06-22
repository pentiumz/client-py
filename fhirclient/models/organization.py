#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Organization) on 2015-06-22.
#  2015, SMART Health IT.


import address
import codeableconcept
import contactpoint
import domainresource
import fhirelement
import fhirreference
import humanname
import identifier


class Organization(domainresource.DomainResource):
    """ A grouping of people or organizations with a common purpose.
    
    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, etc.
    """
    
    resource_name = "Organization"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.active = None
        """ Whether the organization's record is still in active use.
        Type `bool`. """
        
        self.address = None
        """ An address for the organization.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact for the organization for a certain purpose.
        List of `OrganizationContact` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifies this organization  across multiple systems.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name used for the organization.
        Type `str`. """
        
        self.partOf = None
        """ The organization of which this organization forms a part.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the organization.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Kind of organization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Organization, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Organization, self).elementProperties()
        js.extend([
            ("active", "active", bool, False),
            ("address", "address", address.Address, True),
            ("contact", "contact", OrganizationContact, True),
            ("identifier", "identifier", identifier.Identifier, True),
            ("name", "name", str, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js


class OrganizationContact(fhirelement.FHIRElement):
    """ Contact for the organization for a certain purpose.
    """
    
    resource_name = "OrganizationContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Visiting or postal addresses for the contact.
        Type `Address` (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the contact.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.purpose = None
        """ The type of contact.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Contact details (telephone, email, etc)  for a contact.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(OrganizationContact, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(OrganizationContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False),
            ("name", "name", humanname.HumanName, False),
            ("purpose", "purpose", codeableconcept.CodeableConcept, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js


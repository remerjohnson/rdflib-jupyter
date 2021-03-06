#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Graph, plugin
from rdflib.serializer import Serializer
import json

# f1 = open('test.json', 'w')

datamares='''
@prefix mads:  <http://www.loc.gov/mads/rdf/v1#> .
@prefix damsid: <http://library.ucsd.edu/ark:/20775/> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix dams:  <http://library.ucsd.edu/ontology/dams#> .

damsid:bd1176351d  a                   dams:Object ;
        dams:copyright                 [ a                           dams:Copyright ;
                                         dams:copyrightJurisdiction  "US" ;
                                         dams:copyrightNote          "Constraint(s) on Use: This work is protected by the U.S. Copyright Law (Title 17, U.S.C.). Use of this work beyond that allowed by fair use requires written permission of the UC Regents. Responsibility for obtaining permissions and any use and distribution of this work rests exclusively with the user and not the UC San Diego Library. Inquiries can be made to the UC San Diego Library program having custody of the work." ;
                                         dams:copyrightPurposeNote   "Use: This work is available from the UC San Diego Library. This digital copy of the work is intended to support research, teaching, and private study." ;
                                         dams:copyrightStatus        "Under copyright"
                                       ] ;
        dams:date                      [ a               dams:Date ;
                                         rdf:value       "2015-03-01 to 2015-03-30" ;
                                         dams:beginDate  "2015-03-01" ;
                                         dams:encoding   "w3cdtf" ;
                                         dams:endDate    "2015-03-30" ;
                                         dams:type       "collected"
                                       ] ;
        dams:event                     damsid:bd7285620z ;
        dams:geographic                damsid:bd0664401n ;
        dams:language                  damsid:bb06839335 , damsid:bb87044465 ;
        dams:note                      [ a          dams:Note ;
                                         rdf:value  "Data collected with acoustic transects inside and outside of Cabo Pulmo National Park. The analysis methods allowed us to estimate the number and size of the fish that were surveyed during the field campaign." ;
                                         dams:type  "description"
                                       ] ;
        dams:note                      [ a                  dams:Note ;
                                         rdf:value          "Research Data Curation Program, UC San Diego, La Jolla, 92093-0175 (http://libraries.ucsd.edu/services/data-curation/)" ;
                                         dams:displayLabel  "digital object made available by" ;
                                         dams:type          "local attribution"
                                       ] ;
        dams:note                      [ a          dams:Note ;
                                         rdf:value  "Software used: Microsoft Excel and BioSonics acoustic software. Coordinate system: UTM WGS1984." ;
                                         dams:type  "technical details"
                                       ] ;
        dams:note                      [ a          dams:Note ;
                                         rdf:value  "The data described here have been embargoed until 2016-11-30. Inquiries should be directed to Jack Egerton (osp23e@bangor.ac.uk)" ;
                                         dams:type  "scope and content"
                                       ] ;
        dams:note                      [ a          dams:Note ;
                                         rdf:value  "Egerton, Jack (20##): Acoustic survey of fish in Cabo Pulmo National Park. In dataMares Project: Fisheries. UC San Diego Library Digital Collections." ;
                                         dams:type  "preferred citation"
                                       ] ;
        dams:note                      [ a          dams:Note ;
                                         rdf:value  "Acoustic survey" ;
                                         dams:type  "methods"
                                       ] ;
        dams:provenanceCollectionPart  damsid:bd9606463x ;
        dams:relatedResource           [ a                 dams:RelatedResource ;
                                         dams:description  "Finding fish with sound at Cabo Pulmo National Park" ;
                                         dams:type         "related" ;
                                         dams:uri          <http://datamares.ucsd.edu/eng/projects/promonitor/finding-fish-with-sound-at-cabo-pulmo-national-park/>
                                       ] ;
        dams:relationship              [ a                  dams:Relationship ;
                                         dams:personalName  damsid:bd9879500h ;
                                         dams:role          damsid:bb5086960s
                                       ] ;
        dams:relationship              [ a                  dams:Relationship ;
                                         dams:personalName  damsid:bd9879500h ;
                                         dams:role          damsid:bb1673895k
                                       ] ;
        dams:relationship              [ a                   dams:Relationship ;
                                         dams:corporateName  damsid:bb27660034 ;
                                         dams:role           damsid:bb3585182w
                                       ] ;
        dams:rightsHolderCorporate     [ a                        mads:CorporateName ;
                                         mads:authoritativeLabel  "UC Regents" ;
                                         mads:elementList         ( [ a                  mads:FullNameElement ;
                                                                      mads:elementValue  "UC Regents"
                                                                    ] )
                                       ] ;
        dams:title                     [ a                        mads:Title ;
                                         mads:authoritativeLabel  "Acoustic survey of fish in Cabo Pulmo National Park" ;
                                         mads:elementList         ( [ a                  mads:MainTitleElement ;
                                                                      mads:elementValue  "Acoustic survey of fish in Cabo Pulmo National Park"
                                                                    ] )
                                       ] ;
        dams:unit                      damsid:bb6827300d .
'''


g = Graph().parse(data=datamares, format="turtle")

context = {"mads": "http://www.loc.gov/mads/rdf/v1#", "damsid": "http://library.ucsd.edu/ark:/20775/", "owl": "http://www.w3.org/2002/07/owl#", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "dams": "http://library.ucsd.edu/ontology/dams#"}

json_f = g.serialize(format='json-ld', context=context, indent=4)
print(str(json_f, 'utf-8'))

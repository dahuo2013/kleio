__author__ = 'szednik'

from kleio import prov

# load the existing PROV-O graph
prov.default_graph.load("load-example.json", format="json-ld")

# get a reference to the existing entity with id="test:entity"
entity = prov.Entity("test:entity")

# define a new entity and say it was derived from "test:entity"
derived_entity = prov.Entity("test:derived_entity")
derived_entity.set_label("derived example entity")
derived_entity.set_was_derived_from(entity)

# note, right now the context of the import is not retained
# add test and foaf namespace to prov.context for serialization
prov.context.update({"test": "http://tw.rpi.edu/ns/test#",
                     "foaf": "http://xmlns.com/foaf/0.1/"})

# print out the updated provenance graph
print(prov.serialize(format="json-ld"))
CONTEXT="""
{
   "@context": {
      "type": "@type",
      "biolinkml": "https://w3id.org/biolink/biolinkml/",
      "dc": "http://purl.org/dc/terms/",
      "dcterms": "http://purl.org/dc/terms/",
      "owl": "http://www.w3.org/2002/07/owl#",
      "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
      "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
      "sssom": "http://example.org/sssom/",
      "@vocab": "http://example.org/sssom/",
      "confidence": {
         "@type": "xsd:double"
      },
      "creator_id": {
         "@type": "@id"
      },
      "information_content_mica_score": {
         "@type": "xsd:double"
      },
      "mapping_set_id": {
         "@type": "@id"
      },
      "mappings": {
         "@type": "@id"
      },
      "object_id": {
         "@type": "@id",
         "@id": "owl:annotatedTarget"
      },
      "object_match_field": {
         "@type": "@id"
      },
      "predicate_id": {
         "@type": "@id",
         "@id": "owl:annotatedProperty"
      },
      "semantic_similarity_score": {
         "@type": "xsd:double"
      },
      "subject_id": {
         "@type": "@id",
         "@id": "owl:annotatedSource"
      },
      "subject_match_field": {
         "@type": "@id"
      },
      "Mapping": {
         "@id": "owl:Axiom"
      }
   }
}
"""

def get_jsonld_context():
    return CONTEXT
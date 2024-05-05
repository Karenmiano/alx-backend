# REST API

* R - REpresentational
* S - State
* T  - Transfer

Transferring the present state of the representation of a resource.
REST operates fully based on the HTTP protocol.(Resources/ Nouns)
Loosely coupled applications. Distributed applications.
CSRF - not only IP address but also port too.
HTTP Caching - server sends instructions to client on how to manage the sent resource in response headers.(Browser Cache, Proxy Cache, CDN Cache)
SOAP - Simple Object Access Protocol (Protocol), XML only.
REST - Architectural Style


### 6 Constraints to the REST Architecture:
1. Client-Server
2. Stateless - the server doesn't store any session related client data, everything that the server needs to know with regards to the resource should be present within the request.
-- The client takes the responsibility of storing its state and sending to server in its requests. (Improves Scability)
3. Cache - responses must define themselves as either cacheable or not.
4. Uniform interface - different types of software applications should expect the same interface for interacting with the api.
-- Identification of resources through URL
-- Manipulation of resources through Representations - through the representation of a resource, a client is able to modify the state of the resource on the server.
-- Self descriptive messages for each request
-- HATEOAS
5. Layered System -  allows the system to be composed of multiple hierachical layers, each layer doesn't need to know anything beyond what is in the immediate layer. (Security policy enforced)
6. Code on Demand

Serialization and Deserialization - data storage, inter-process communication, and web services. Popular serialization formats include JSON (JavaScript Object Notation), XML (eXtensible Markup Language), and Protocol Buffers.
-- Serialization is the process of converting an object into a format that can be easily stored or transmitted across a network, typically as a stream of bytes.

Cross Origin Resource Sharing:
-- 2 urls have the same origin if they have the same schemes, hosts and ports

### Caching
Cache headers: Expires Header, Cache-control Header

### HATEOAS
-- Hypermedia As The Engine Of Application State
-- Documentation that help developers know how to use an API without having to know everything about it, give extra information more or less related to the request made. (Self documenting)

# PAGINATION
Types of pagination:
* Offset
* Keyset / Cursor based
* Seek 
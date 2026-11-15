# Overview
This repository contains the [slides](./Python_Mock_Objects_Workshop.pdf) and the [exercises](./exercises) of the workshop _Let's test with Python mock objects, shall we?_ held at [PyCon Wroclaw 2026](https://www.pyconwroclaw.com/). The slides are available both in PDF and LibreOffice format.

# Abstract
Dependency management is one of the most challenging tasks in software engineering. While there exist tools that can effectively support the development process, testing software that depends upon third-party packages is generally problematic. Such packages, in fact, are often used to access external resources, e.g., databases and cloud-based repositories, which are frequently not available to the developer.

To address these challenges, the `unittest` module, part of the Python Standard Library, allows mocking objects. What does this mean? How does this work? What are the pitfalls of this approach? To answer these questions, this workshop will include theoretical and hands-on sessions, which will help the attendees familiarise themselves with the key features of the Python Mock library.

# Description
The Python mock objects workshop will be structured as follows:
- What is the Mock object library?
  - After an introduction focused on key, mocking-related concepts, the attendees will familiarise themselves with the online resources prepared for this workshop. Very simple exercises will be proposed to consolidate the acquired knowledge.
- How can I use the Mock object library?
  - The objective of this part is to introduce the most important features of the library. Attendees will make use of these to write unit tests.
- Pitfalls are annoying, aren't they?
  - Developing tests that rely on mock objects is not without challenges. The workshop will end by illustrating some of them as well as possible countermeasures. This will provide the opportunity to introduce object specifications, one of the advanced features of the Mock object library.

Help will be available for all attendees. However, an intermediate-level knowledge of functions, classes, and the `unittest` module is highly recommended.

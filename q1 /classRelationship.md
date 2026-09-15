# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Oil
Description: All oils have a type, an average price, a main ingredient, and an appearance.
## New Related Class
Class: Oil Refinery
Description: All Oil Refineries have oil.
## Association
Relationship: Oil Refinery HAS Oil
Explanation: All oil refineries have oil, unless if the place runs out of oil.
## Multiplicity
Multiplicity: One-to-Many (1 to 0..*)
Explanation: Because oil can be transferred into a refinery but a refinery cannot be transferred into an oil, because oils aren't machines.
-  LLM was used here: <img width="170" height="151" alt="Screenshot 2026-09-15 123750" src="https://github.com/user-attachments/assets/4c2b63e4-19dc-4bc1-818c-3806ed0de5f4" />

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?

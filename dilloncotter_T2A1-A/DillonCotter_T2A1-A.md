# Dillon Cotter T2A1-A - Workbook.  
## RfQ Response

### Describe the architecture of a typical Flask application
A Flask application is built on simplicity and flexibility, allowing it to handle simple and complex tasks.

The core of a Flask application is the Flask class, which forms the basis for creating instances of the web application. These instances are WSGI (Web Server Gateway Interface) applications, providing a common link between web servers and web applications.

Flask applications follow the Model-View-Controller (MVC) design pattern, which separates different concerns:

- Model: Deals with the database and holds data and its behaviours.

- View: This is the user interface where data from the Model is displayed. Flask uses templates to handle this.

- Controller: Responds to user inputs and interacts with the Model. It updates the View when the Model changes. In Flask, this is done using routes and view functions.

Flask uses routing to match client requests with specific view functions. The view functions are then associated with particular URLs.

Request dispatching in Flask is done through Werkzeug, a WSGI utility library. Flask also supports unit testing and allows extensions for various functionalities like form validation and authentication mechanisms.

Flask supports the creation of blueprints, enabling developers to create reusable sections of an application, streamlining the codebase.

Flask doesn't impose a strict project structure, granting developers flexibility. As projects grow, it's common to split them into modules for better organisation.

### Identify a database management system (DBMS) commonly used in web applications (including Flask) and discuss the pros and cons of this database

### Discuss the implementation of Agile project management methodology

### Provide an overview and description of a standard source control workflow


### Provide an overview and description of a standard software testing process (e.g. manual testing)

### Discuss and analyse requirements related to information system security and how they relate to the project

### Discuss common methods of protecting information and data and how you would apply them to the project

### Research what your legal obligations are in relation to handling user data and how they can be met for the project

### Describe the structural aspects of the relational database model. Your description should include information about the structure in which data is stored and how relations are represented in that structure.

### Describe the integrity aspects of the relational database model. Your description should include information about the types of data integrity and how they can be enforced in a relational database.

### Describe the manipulative aspects of the relational database model. Your description should include information about the ways in which data is manipulated (added, removed, changed, and retrieved) in a relational database.

### Conduct research into a web application (app) and answer the following parts:  
- a. List and describe the software used by the app.
- b. Describe the hardware used to host the app.
- c. Describe the interaction of technologies within the app
- d. Describe the way data is structured within the app
- e. Identify entities which must be tracked by the app
- f. Identify the relationships and associations between the entities you have identified in part (e)
- g. Design a schema using an Entity Relationship Diagram (ERD) appropriate for the database of this website (assuming a relational database model)
# Dillon Cotter T3A1 - Workbook.  

### 1. Provide an overview and description of a standard source control process for a large project  
Source control assists in managing and tracking changes to code.  
You will first have to decide on which system to use (EG. Git)
1. Create a central repository where all the project's code and documents are held.  
2. Master/Main branch will hold the stable code.  
3. Developers create separate branches for new features or fixes.  
4. Changes from these branches are reviewd with a pull or merge request  
5. Git will do some automatic checking to ensure code does not overwrite itself, but does not test code.
6. Larger projects you may also need peer review to ensure code is acceptable to the overall project guidlines.  
7. Once checking is complete, the branch can be fully merged to the Main/Master branch.  
8. This code should then be tested by other developers and/or non-development testers from the project team.  
9. All developers should ensure to clone main/master followed by branching before any work starts, to ensure they are running the most up to date codebase.  

Other considerations are to have clear lines of communcation amongst the team at all times, and that each commit has meaningful messages for the changes made, with developers also responsible for updating documentation.  
It may also be good practice to incorporate Backup and recovery methods to prvent potential data loss and for a disaster recovery plan.

### 2. What are the most important aspects of quality software?
1. Functionality  
Referring to how well the software meets the needs it was designed for.  This includes suitability, accuracy, compliance and security.  

2. Reliability  
How stable and dependable is the software. It includes aspects like maturity, fault tolerance, and recoverability in the event of crash or errors.  

3. Usability  
How easy and pleasant the software is to use. This may be understandability, learnability, operability and attractiveness.  

4. Efficiency  
This relates to the software's performance and resource usage. It includes time behaviour and resource utilisation.  

5. Maintainability  
How easy is it to modify and update the software.  This may encompas modularity, reusability, changeability and testability.  

6. Portability 
How easy is it for software to transfer from one environemtn to another. This could be installability and replaceability, and how easy it is to run on various platforms.  

https://www.turing.com/blog/software-quality-assurance-and-its-importance/

### 3. Outline a standard high level structure for a MERN stack application and explain the components

A MERN stack typically consists of four components:
- MongoDB,
- Express.js,
- React.js, and
- Node.js

<strong>1. MongoDB: </strong> is a NoSQL database that stores data in flexibile JSON-like documents, and is used for the application's data.  
This Database is schema-less, meaning the data structure can be altered over time.  
<strong>2. Express.js: </strong>is a web application framework for Node.js. It is used to build the backend of the application, handling HTTP requests and responses, simplifying the server-side development by providing a large set of features for web and mobile apps.  
<strong>3. React.js: </strong>is a JavaScript library for building user interfaces, primarily for front-end. This allows developers to create large web apps that can update a data without needing to reload the page. Mostly this can be used to build UI components, making the code more readable and maintainable.
<strong>4. Node.js: </strong>is a JavaScript runtime allowing execution of JavaScript code on the server side. With Node, JavaScript can run on both server and client side, leading to a more consolidated development process.

Front-end is built with React.js, which communicates to the backend through HTTP requests.  
Back-end server is setup using Node.js with Express.js handling and responding to client requests.  
MongoDB serves as the database, accessed by the backend to store and retrieve application data.

This is considered a 'Full-stack' solution.

https://www.mongodb.com/mern-stack

### 4. A team is about to engage in a project, developing a website for a small business. What knowledge and skills would they need in order to develop the project?

A Project team would need to be made up of Technical skills and Business skills (soft skills)
<b>Technical Skills</b>
1. Web Development Fundamentals: An understanding of HTML, CSS and JavaScript, and the concept of responsive design to ensure a website works on various screen sizes and devices.  
2. Back-end Development: Proficiency with a server-side language (EG. Node.js, Python etc) and frameworks (EG. Express.js or Django) and database management skills, including knowledge of SQL or NoSQL databases (EG. PostgreSQL or MongoDB)
3. Front-end Development: Experience with front-end libraries like React.js or Angular. Knowledge of client-side technologies and frameworks.  
4. Version control: Familiarity with version/source control systems like Git, for tracking changes and collaboration.  
5. Web Hosting and Deployment: Understanding of web hosting services and deployment processes. Knowledge of domain registration and DNS management.  
6. Security: Awareness of web security pracictes to protect the site and its users.  
7. SEO and Accessibility: A basic understanding of Serach Engine Optimisation to improve visibility and Knowledge of web accessibility standards to make the website usable for people with screen readers.  

<b>Soft Skills</b>  
1. Communication: Ability to communicate with team members, and creating/using  readable documenation.  
2. Collaboration: Openness to feedback and adaptability to change.  
3. Project Management: Working on prioritisation and familitarity with project management tools and methadologies (EG. Agile).  
4. Business Requirements: Ability to understand/interpret the business needs of the client into technical requirements.  
5. User Experience and User Interface Design: Understanding the principles of UX/UI design to create an appealing website.

### 5. With reference to one of your own projects, discuss what knowledge or skills were required to complete your project, and to overcome challenges
### 6. With reference to one of your own projects, evaluate how effective your knowledge and skills were for this project, and suggest changes or improvements for future projects of a similar nature

### 7. Explain control flow, using an example from the JavaScript programming language  

Control flow refers to the order in which individual statements, instructions or function calls are executed. In JavaScript the control flow is dictated by conditional statements, loops and function calls:  

<b>1. Conditional Statements (if-else):</b>  
Allows your code to make decisions based on certain conditions. They execute particular code if a specified condition is true and optionally define alternative blocks if code if false.  
Example:  
```
let number = 10;

if (number > 5) {
    console.log("The number is greater than 5.");
} else {
    console.log("The number is 5 or less.");
}
```

<b>2. Loops (for/while):</b>

Loops are used to execute a block repeatedly until a condition is met.
Example:  
```
for (let i = 0; i < 5; i++) {
    console.log("The value of i is: " + i);
}
```  

3. Function Calls:  
Function calls direct flow to a different part of the program. When a function is called, the execution jumps to that function and runs its code.  
```
function greet (name) {
    console.log(`Hello, ${name}`);
}

greet("Dillon");
greet("Jairo");
```

https://developer.mozilla.org/en-US/docs/Glossary/Control_flow

### 8. Explain type coercion, using examples from the JavaScript programming language

Type coercion refers to the automatic or implicit conversion of values from one data type to another. This can happen because variable in JavaScript are not directly bound to a specific data type.  
There are two main types of coercion: implicit and explicit.  

<b>Implicit</b>
This occurs when JavaScript automatically converts types behind the scenes.  
Example:  
```
let value1 = '5'; // Stored as a string
let value2 = 10; // Stored as a number
let result = value1 + value2; 
console.log(result); // Outputs: '510'
```
In this example, JavaScript has converted the value2 number to a string and concatenates it with the string '5'   
Example:  
```
let value1 = '5'; // Stored as a string
let value2 = 10; // Stored as a number
let result = value1 * value2; 
console.log(result); // Outputs: '50'
```
In this example, JavaScript has converted the value1 string to a number and performs the multipication.  

<b>Explicit</b>  
This is when a developer intentionally converts values from one type to another.  
Example:  
```
let value = 123;
let stringValue = String(value);
console.log(stringValue); // Outputs: '123'
```
Example:  
```
let value = 'hello';
let booleanValue = Boolean(value);
console.log(booleanValue); // Outputs: true
```

https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion

### 9. Explain data types, using examples from the JavaScript programming language

Data types are the classifications given to different kinds of data that we can use. JavaScript does not require a developer to declare the data type of a variable ahead of time. JavaScript has many built-in data types, which can be categorised into two main groups: Primitive and Reference types.  

<b>Primitive Types</b>  
These are basic, immutable data types. They do not have properties or methods (with the exception of `null` and `undefined`, which are special).  
The main primitive data types in JavaScript are:  
1. Number: Represents both integer and floating numbers.
```
let num1 = 10; // Integer
let num2 = 5.5; // Floating point
```
2. String: Represents sequences of characters
```
let text = "Hello, world!";
```
3. Boolean: Represents a logical entity and can have two values: `true` and `false`
```
let isCoderAcademyFun = true;
```
4. Undefined: Represents a variable that has been decalred, but not assigned a value.
```
let testVariable;
console.log(testVariable); // Outputs: undefined
```
5. Null: Represents the intentional absence of any object value. usually assigned to a variable as a representation of no value
```
let emptyVariable = null;
```
6. Symbol: Represents a unique value, not equal to any other value.
```
let uniqueSymbol = Symbol('symbol');
```
7. BigInt: Represents integers larger than 2^53 - 1, the largest number JavaScript can reliably represent
```
let largeNumber = BigInt(1234567890123456789012345678901234567890);
```

<b>Reference Types</b>  
These are objects that store collections of data or more complex entities.  
These are different to primatives where they are mutable and can have properties and methods.  

1. Object: The most basic reference type, can store collections of data and more complex entities.
```
let person = {
    firstName: "Dillon",
    lastName: "Cotter"
};
```
2. Array: A Type of object to store multiple values in a single variable
```
let colours = ['Red', 'Blue', 'Green'];
```
3. Function: A callable object that executes a code block
```
function greet(name) {
    return "Hello, " + name
}
```

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures

### 10. Explain how arrays can be manipulated in JavaScript, using examples from the JavaScript programming language




https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Arrays

### 11. Explain how objects can be manipulated in JavaScript, using examples from the JavaScript programming language
### 12. Explain how JSON can be manipulated in JavaScript, using examples from the JavaScript programming language
### 13. For the code snippet provided below, write comments for each line of code to explain its functionality. In your comments you must demonstrates your ability to recognise and identify functions, ranges and classes
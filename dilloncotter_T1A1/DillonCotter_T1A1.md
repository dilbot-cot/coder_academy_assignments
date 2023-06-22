# T1A1 - Workbook
#### Dillon Cotter
##### Student ID: 14582

## Q1: <strong>Identify</strong> and <strong>explain</strong> common and important components and concepts of web development markup languages:
Some of the components of markup languages include HTML and CSS. 
1. HTML is short for HyperText Markup Language and is the actual content displayed in web browsers. While other aspects of web development languages are important for styling and interactivity, HTML is necessary so that a user can view the website. 
2. CSS is short for Cascading Style Sheets, this is used to inform the corresponding html file on its style. This allows control over the layout, colours, fonts, and most other visual aspects of a site. 
The name "cascading" informs that the format is applied from top to bottom, allowing for different styles to apply to different tags, ids and sections.

By separating the style from the content it is easier to make adjustments to either section without unintended consequences.

Within both of these 'languages' there are some important concepts to consider with web development:  
1. Semantic Markup: 
This is the concept of using correct and descriptive labels and tags within the HTML to assist with the structure and organisation so that the webpage displays correctly, but is also easily readable in development.  
2. Meta Tags: 
These are bits of code that give information about the HTML document. These primarily include the character set used by the document and how it displays on a given device/browser.

## Q2: <strong>Define</strong> the features of the following technologies that are essential in terms of the development of the internet:
## - Packets
## - IP addresses (IPv4 and IPv6)
## - routers and routing
## - domains and DNS

## <strong>Explain</strong> how each technology has contributed to the development of the internet.
- Packets:  
A packet is a small unit of data that is transmitted over a network. It is made up of 2 main parts: The actual data being sent (images, text, videos etc) and the information on the source and destination addresses so it can be delivered.  
A packet allows large amounts of data to be divided into easier to manage sections, lessening the load on a network, and allowing for more efficient routing. If a packet is lost, only a small portion of the overall data is missing to be repaired, replicated or resent.  
(https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-packet/)
- IP addresses (IPv4 and IPv6):  
IP addresses are unique numbers used to identify devices connected to a network and provide the address information for sending and receiving data.  
    - IPv4 is a set of 4 numbers separated by '.', with each number ranging from 0 to 255.  
    - IPv6 is a set of 8 groups of hexadecimal digits (numbers 0-9 and letters A-F) separated by ':'.  

    The transition from 4 numbers to 8 groups, and the use of hexadecimals, significantly increases the number of available addresses, allowing for a larger allocation of devices.  
    IP addresses play a vital role in enabling global connectivity, allowing devices worldwide to connect, communicate, and route data over the internet using a standardized approach.
(https://www.simplilearn.com/tutorials/cyber-security-tutorial/difference-between-ipv4-and-ipv6#:~:text=IPv4%20is%20composed%20of%2032,the%20Internet%20Protocol%20(IP).))
(https://www.geeksforgeeks.org/differences-between-ipv4-and-ipv6/)
- Routers and routing:  
Routers are devices that connect networks together and efficiently direct data packets to their destinations.  
Through the process of routing, routers exchange information and determine the best paths for packet delivery by analyzing destination addresses.  
This ability has allowed the internet to expand in scale and complexity, enabling seamless communication between countless devices. Routers effectively manage network traffic and utilize routing tables to ensure efficient and reliable data transmission. Their contribution has been crucial in shaping the internet into a global network that connects people, businesses, and information across the world.  
(https://www.cloudflare.com/en-gb/learning/network-layer/what-is-routing/)
- Domains and DNS:  
A Domain can be thought of as a website name, like google.com.  
DNS (which stands for Domain Name System) converts this Domain and translates this into an IP address.  
When coupled together a user does not need to remember a complicated set of IPv4 or IPv6 addresses to manually input to a web browser to show a page, instead they can use a domain name and rely on the DNS to lookup the correct address this should return.
(https://www.cloudflare.com/en-gb/learning/dns/what-is-dns/)  

## Q3: <strong>Define</strong> the features of the following technologies that are essential in terms of the development of the internet:
## - TCP
## - HTTP and HTTPS
## - web browsers

## <strong>Explain</strong> how each technology has contributed to the development of client and server communication over the internet 
- TCP:  
TCP, short for Transmission Control Protocol, plays a crucial role in networks by reassembling all the packets sent over a network into a usable format.  
Its primary objective is to ensure reliable data delivery. To achieve this, TCP employs a mechanism of acknowledgment requests. These requests are sent from the recipient location back to the source, confirming the successful reception and correct assembly of all packets.  
(https://www.cloudflare.com/en-gb/learning/ddos/glossary/tcp-ip/)
- HTTP and HTTPS:  
HTTP (Hypertext Transfer Protocol) is a protocol used in networks to facilitate communication between web servers and clients. It enables the transfer of hypertext, such as HTML, and other resources like images and videos.  
HTTP's provides a simple and efficient means of transmitting information. However, it does not ensure secure transmission, as data is sent in plain text, making it susceptible to interception and tampering.  
HTTPS (Hypertext Transfer Protocol Secure) is an extension of HTTP that incorporates security measures to protect data during transmission. It utilises encryption protocols, such as SSL (Secure Sockets Layer) or TLS (Transport Layer Security), to establish a secure and encrypted connection between the server and client. By encrypting the data, HTTPS safeguards sensitive information, such as login credentials and financial details, from unauthorized access and manipulation.
(https://www.cloudflare.com/en-gb/learning/ssl/why-is-http-not-secure/)
- Web Browsers:  
Web browsers are software applications that allow users to access and interact with websites on the internet. They assist in rendering and displaying web content, such as HTML, CSS, and JavaScript, in a user-friendly manner.  
Web browsers provide a graphical interface that enables users to navigate through web pages, submit forms, and interact with multimedia elements.
Newer web browsers also offer additional features, including tabbed browsing, bookmarks, extensions, and privacy settings. They also support HTTP and HTTPS protocols, ensuring secure and reliable communication with web servers.

## Q4: <strong>Identify</strong> THREE data structures used in the Python programming language and explain the reasons for using each.
- Lists:  
Lists are ordered and mutable objects that allow the storage of multiple items into a single variable.  
Lists allow for duplicate values, addition, removal or alteration of items in the object.
Lists are good for use where you may need to alter the items after creation (such as a shopping list that you need to add items to when you run out, or remove items from if you buy them.)
(https://www.w3schools.com/python/python_lists.asp)
- Tupples:  
Tuples are also ordered, however they are unmutable objects.  
Similar to Lists, they do allow duplicate values, however items cannot be added, changed or removed after the object is initialised (instead you would need to create a new tuple)  
Tuples are good for use where you do not want the content to alter, such as a user's DOB, which would not likely change.  
Tuples are also faster than a list, for times where you may wish to use the tuple in a loop iteration, the code will return sooner when using this data structure.
(https://www.w3schools.com/python/python_tuples.asp)
- Dictionaries:  
Dictionaries store their data in key: value relationships, and are ordered and mutable objects.  
Dictionaries do not allow duplicate values, as each key can only be assigned a single value, and can add or remove key: values.  
Dictionaries are good for use where you may wish to recall what an item value 'means' later in the code. E.G. if you had a dictionary for a car, you would be able to call on any values present individually - Colour, Make, Model, Year etc, where if this was stored as a list you would only see the values.  
(https://www.w3schools.com/python/python_dictionaries.asp)

## Q5: <strong>Describe</strong> the features of interpreters and compilers and how they are different.
Both Interpreters and compilers are tools in programming used to convert readable source-code into machine executable code.
- Interpreters:  
    - Performs actions one statement at a time.
    - Translates source code to machine code during the run-time.
    - As code is run line-by-line, errors are reported immediatly on discovery.
    - Using in scripting languages (EG. Python)
- Compilers:
    - Takes all of the source code and translates it first.
    - Are typically faster in execution, after it has been pre-translated.
    - Used in non-scripting languages (EG. Java)  

(https://www.programiz.com/article/difference-compiler-interpreter)
## Q6: <strong>Identify</strong> TWO commonly used programming languages and explain the benefits and drawbacks of each.

- Python:
    - Benefits:
    1. Python has an easily readable syntax and is beginner friendly.
    2. Code can be written concicely, reducing development time.
    3. Large Support and Community are available for libraries and frameworks, making it so developers do not need to 're-create the wheel' for each new program.
    - Drawbacks:
    1. Slower execution time compared to compiled languages.
    2. For more complicated designs, the simplicity of python can be a drawback.
    3. Python uses high memory in projects  
(https://www.pixelcrayons.com/blog/python-pros-and-cons/)

- Java
    - Benefits:
    1. Java allows programs to run on multiple platforms without major modifications.
    2. Large Community and Support are available fo resources.
    3. Object-Oriented Programming with reusable code.
    - Drawbacks:
    1. Java tends to require more lines of code to run functions than other languages.
    2. It has a steep learning curve to become proficient
    3. There is also some performance issues, where Java cannot match other languagesfor high-performance tasks.  
(https://anywhere.epam.com/business/pros-and-cons-java)

## Q7: <strong>Identify</strong> TWO ethical issues from the areas below and discuss the extent to which an IT professional is ethically responsible in terms of the issue.
 
 - Access to a user’s personal information (medical, family, financial, personal attributes such as sexuality, religion, or beliefs)

 - aggressive sales and marketing practices designed to mislead and deceive consumers  

For each ethical issue identify a source of legal information relating to the ethical issue and discuss whether the law is helpful in assisting a developer to act in an ethical way. (Word count guide: 200 words max)

### Access to a user's personal information:
An IT professional has significant ethical responsibilities with user's personal infromation.  
In Australia this is regulated by the Privacy Act 1988 that sets out the Australian Privacy Principles (APPs).  
These APPs provide a framework on how you can collect, store, use and disclose personal information and the guidelines to ensure data security.  
While the law provides a basic framework, it does not necissarily ensure ethical behaviour. Ethical conduct extends beyond legal requirements, demanding respect for a user's privacy, full transparency in their data usage, and informed consent for data collection and use.  
While the Privacy Act and the APPs set a legal benchmark for IT Professionals, they, like many legal frameworks, lag behind in addressing the challenges posed by new and emerging technologies.   
Emerging technologies such as AI, Blockchain, and the Internet of Things may not conform to current guidelines on information transparency, posing new legislative challenges  
Therefore, developers must proactively employ their ethical judgment to ensure they respect user trust and privacy, even in areas not yet fully covered by legislation.  
(https://www.legislation.gov.au/Details/C2022C00361)

### Aggressive sales and marketing practices designed to mislead and deceive consumers:
The ACCC (Australian Competition and Consumer Commission) provides legal framework under the ACL (Australian Consumer Law) including regulation around misleading/deceptive conduct, making false representations and unfair practices.  
As with personal information above, these do provide a legal boundary, however technological advances often outpaces the legislation quite significantly.  
One example of this is how digital platforms can capture user data and use this in targeted advertising. This could be considered agressive or manipulative, however is not specifically addressed in the law.  
Additionally, while outright deceptive or false advertising is prohibited, *Dark Patterns* can be used to manipulate users. Using design techniques that can drive behaviour to a desired outcome for the business, at the expense of the customer.  
 Examples of this include:
- Trick Questions designed to confuse a user, EG. A user might click to cancel their subscription, then be led to a page with a question, "Do you want to continue enjoying our premium features?" The responses might be framed confusingly, such as "No, I want to lose my benefits" and "Yes, keep my subscription." 
- Hidden costs only being revealed at the final step of a transaction.
- Forced Continuity where free trials automatically renew into paid subscriptions without consent.  

(https://www.deceptive.design/)

### Conduct research into a case study of ONE of the ethical issues you have chosen discuss how an ethical IT professional should respond to the case study and how they might mitigate or prevent ethical breaches.

# Python Class
A quick but comprehensive view of Python

### Useful Sublime Shortcuts
* cmd + shift + p
* cmd + D (highlight stuff and then press cmd + D to repeat highlight for same stuff)
* cmd + ctrl + G (highlight stuff and then press, the rest of same stuff will be highlighted)
* cmd + l (highlight a line your cursor is on)

### Git Commands
#### Basic Flow
```
git clone                     # Get the code base
git checkout -b myNewBranch   # 
git status                    # Lists the changed files
git diff                      # shows exact lines in code that have changed
git add .                     
git commit -m "commit message here"
git push (git may tell to set up remote branch and give you the command for it)
```
#### Git Flow
![Git Flow Chart](https://wac-cdn.atlassian.com/dam/jcr:61ccc620-5249-4338-be66-94d563f2843c/05%20(2).svg?cdnVersion=766)

### General Components of an Application
1. Frontend (Web GUI)
	- (1990s/2000s) HTML, CSS server-side rendering
		- Go to an internet endpoint specified by ip address/domain name
		- directory
			- index.html
				- references other files
				- each file is a new page load
				- within each file may be a CSS tag and/or JS tag which helps the browser render styles and funcionality
		- Super simple frontend rendering
		- Everything done on backend (but mostly serving html pages so also simple)
		- [Example Fast HTML page](https://people.clarkson.edu/~gberry/tc391/ugly.html)
	- (Late 2000s/2010s) Client-Side Rendering
		- Pros:
			- No page reload needed (navigating to a new page doesn't mean you have to grab everything)
				- potentially less network traffic because entire page doesn't have to be sent each time
			- Lots of functionality on the frontend
				- User Value
				- features can be implemented quickly
			- Can request different things at different times
			(if something is really big/slow, it doesn't have to slow down everything else)
			- JS Frameworks
				- Makes it easier to get started and implement functionality
				- Provides a lot of the boiler code to make a JS site from scratch (React, Angular vs JQuery)
		- Cons:
			- More taxing for frontend (old/slow phone would suffer)
			- More code
			- More network requests (many request for 1 page)
2. Backend
	- SOAP: Stateful
		- sessions are tied to physical machines
	- REST: Stateless
		- you don't have to care about which machine is handling which user. Just look at load for balancing machines
		- CRUD: (Create, Read, Update, Delete)
		- Each request is atomic (you don't need any more information than what is in the request to serve it)
		- request
			- GET domain.com/api/v1/resources/{resourceID}
				- authenticate with some cookie or JWT (JSON Web Tokens)
					- { key: "theSecretJWTStringGeneratedByBackend", otherInfo: "helpful stuff for processing in backend" }
					- JSON decode is universal with a set of algorithms 
					- [JWT](https://jwt.io/)
				- JSON (Javascript Object Notation)
		- generally use plural nouns through the route
	- GraphQL:
		- Allows you to make intricate queries on data
		- Many DBs are supporting GraphQL queries natively so it can even bypass backend server code (less code to write!)


### Designing the language for accessing a resource (REST API)
Start with:
* frontend website that allows people to view and potentially adopt dogs
	- be able to get a list of dogs w/ basic information
	- get details on a single dog
	- be able to verify user is real person
		- be able to create account/sign-in/auth
	- be able to compare dogs
	- be able to donate money to a single dog or many dogs
	- be able to buy food treats for dogs
	- be able to buy clothes for dogs
	- be able to buy toys for dogs
	- view assortment of treats, clothes, and toys (on separate pages)
	- be able to adopt a dog
* DB of:
	- dogs
	- food treats
	- users
	- clothes
	- toys

What API routes do you need?:
```GET domain.com/api/v1/resources/{resourceID}```
- bestdogswebsite.com
- /api/v1/users
	- /api/v1/users
		- GET, POST
	- /api/v1/users/{userId}
		- GET, PUT(update), DELETE
- /api/v1/dogs/{dogId}
	- 

What does the flow of an API call handled with good practices look like?
1. Client Side
	- Check where JWT or cookie is stored to add to request
	- package anything needed into the request body/headers/query parameters
	- Sending request from browser
	- encrypt w/ https/SSL encryption
		- Certificate Managers all over the world (a few trusted ones manage for everyone)
		- Go to certificate manager to get public certificate
		(may be cached)
		- Use to encrypt your request, so only private key can decrypt
		- Send request
		- Bad guy without private key cannot read request
		- Backend Server with private key is the only one who can read request
	- On its way to the Server!
2. Server Side
	- Ingres Point
		- handle SSL decryption
		- handle load balancing (send you to optimal server)
		- Examples:
			- HAProxy Kubernetes Ingres
			- server which you've configured to be hit first and handles relevant cases
			- Load Balancer Solutions
				- NGINX
			- AWS, GCP, Azure probably have baked solution
	- Backend Server
		- Route/Match URL path
		- If path needs authentication
			- Check JWT/Other authentication
		- Middleware for populating authenticated user if needed
		- Validate Request Body/Headers/Query Parameters
			- make sure its sending valid content
			- ex. Add a new toy: 
			{ title: "Chewy", "description": "very chewable toy"}
			vs
			{ title: "\os.rmdir()", "description": "?^DROP TABLES" }
		- Function to handle logic for request
			- db calls
			- starting task on async task queue/message broker
			- return HTTP code and, if desired, some body/message

























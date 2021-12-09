# Day 7 - Migration Without Security

- Interact with the MongoDB server to find the flag. What is the flag?

	- `***{********************************}`

We discussed how to bypass login pages as an admin. Can you log into the application that Grinch Enterprise controls as admin and retrieve the flag?

Use the knowledge given in AoC3 day 4 to setup and run Burp Suite proxy to intercept the HTTP request for the login page. Then modify the POST parameter.

	- `***{********************************}`

- Once you are logged in, use the gift search page to list all usernames that have guest roles. What is the flag?

	- `***{********************************}`

- Use the gift search page to perform NoSQL injection and retrieve the mcskidy record. What is the details record?

	- `*************************************`
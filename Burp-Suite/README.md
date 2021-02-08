# Burp Suite

- Read the overview and continue on into installation!

	  no answer needed

- If you'll be installing Burp (as it's commonly referred to) from scratch, you'll need to first visit this link: https://portswigger.net/burp/communitydownload

	  no answer needed

- Once you've reached the Port Swigger downloads page, go ahead and download the appropriate version for your operating system

	  no answer needed

- Once you've got everything setup move onto our next task, Gettin' [CA] Certified!

	  no answer needed

- Launch Burp!

	  no answer needed

- Once this pops-up, click 'Temporary project' and then 'Next'.

	  no answer needed

- This option is included as it can be incredibly useful to create a custom configuration file for your proxy or other settings, especially depending on how your network configuration and/or if Burp Suite is being launched remotely such as via x11 forwarding.

	  no answer needed

- Finally, let's go ahead and Start Burp! Click 'Start Burp' now!

	  no answer needed

- Since we now have Burp Suite running, the proxy service will have started by default with it. In order to fully leverage this proxy, we'll have to install the CA certificate included with Burp Suite (otherwise we won't be able to load anything with SSL). To do this, let's launch Firefox now!

	  no answer needed

- Go ahead and install this now!

	  no answer needed

- Next, we'll move onto adding the certificate for Burp!

	  no answer needed

- With Firefox, navigate to the following address: http://localhost:8080

	  no answer needed

- Click on 'CA Certificate' in the top right to download and save the CA Certificate.

	  no answer needed

- Click on 'View Certificates'

	  no answer needed

- Next, in the Authorities tab click on 'Import'

	  no answer needed

- Navigate to where you saved the CA Certificate we downloaded previously. Click 'OK' once you've selected this certificate.

	  no answer needed

- Select 'OK' once you've done this. Congrats, we've now installed the Burp Suite CA Certificate!

	  no answer needed

- Which tool in Burp Suite can we use to perform a 'diff' on responses and other pieces of data?

	- `Comparer`

- What tool could we use to analyze randomness in different pieces of data such as password reset tokens?

	- `Sequencer`

- Which tool can we use to set the scope of our project?

	- `Target`

- While only available in the premium versions of Burp Suite, which tool can we use to automatically identify different vulnerabilities in the application we are examining?

	- `Scanner`

- Encoding or decoding data can be particularly useful when examining URL parameters or protections on a form, which tool allows us to do just that?

	- `Decoder`

- Which tool allows us to redirect our web traffic into Burp for further examination?

	- `Proxy`

- Simple in concept but powerful in execution, which tool allows us to reissue requests?

	- `Repeater`

- With four modes, which tool in Burp can we use for a variety of purposes such as field fuzzing?

	- `Intruder`

- Last but certainly not least, which tool allows us to modify Burp Suite via the addition of extensions?

	- `Extender`

- With Burp Suite launched, let's first navigate to the 'User options' tab.

	  no answer needed

- Next, click on the 'Display' sub-tab.

	  no answer needed

- Now, click on the 'Look and feel' drop-down menu. Select 'Darcula'.

	  no answer needed

- Finally, close and relaunch Burp Suite to have dark theme (or whichever theme you picked) take effect.

	  no answer needed

- Deploy the VM attached to this task!

	  no answer needed

- By default, the Burp Suite proxy listens on only one interface. What is it? Use the format of IP:PORT

	- `127.0.0.1:8080`

- In Burp Suite, navigate to the Intercept sub-tab of the Proxy section. Enable Intercept

	  no answer needed

- Take a look at the actions, which shortcut allows us to forward the request to Repeater?

	- `CRTL-r`

- How about if we wanted to forward our request to Intruder?

	- `CTRL-i`

- What is the name of the first section wherein general web requests (GET/POST) are saved?

	- `http history`

- what is the name of the second section of our saved history in Burp Suite?

	- `websockets history`

- Here we can apply further fine-grained rules to define which requests we would like to intercept. Perhaps the most useful out of the default rules is our only AND rule. What is it's match type?

	- `url`

- How about it's 'Relationship'?

	- `is in target scope`

- Before leaving the Proxy tab, switch Intercept to disabled. We'll still see the pages we navigate to in our history and the target tab, just having Intercept constantly stopping our requests for this next bit will get old fast.

	  no answer needed

- Navigate to the Target tab in Burp. In our last task, Proxy, we browsed to the website on our target machine (in this case OWASP Juice Shop). Find our target site in this list and right-click on it. Select 'Add to scope'.

	  no answer needed

- Clicking 'Add to scope' will trigger a pop-up. This will stop Burp from sending out-of-scope items to our site map.

	  no answer needed

- Select 'Yes' to close the popup.

	  no answer needed

- What do we call this representation of the collective web application?

	- `site map`

- What is the term for browsing the application as a normal user prior to examining it further?

	- `happy path`

- One last thing before moving on. Within the target tab, you may have noticed a sub-tab for issue definitions. Click into that now.

	  no answer needed

- Which poisoning issue arises when an application behind a cache process input that is not included in the cache key?

	- `web cache poisoning`

- To start, click 'Account' (this might be 'Login' depending on the version of Juice Shop) in the top right corner of Juice Shop in order to navigate to the login page.

	  no answer needed

- Try logging in with invalid credentials. What error is generated when login fails?

	- `Invalid email or password.`

- But wait, didn't we want to send that request to Repeater? Even though we didn't send it to Repeater initially via intercept, we can still find the request in our history. Switch over to the HTTP sub-tab of Proxy. Look through these requests until you find our failed login attempt. Right-click on this request and send it to Repeater and then send it to Intruder, too!

	  no answer needed

- Now that we've sent the request to Repeater, let's try adjusting the request such that we are sending a single quote (') as both the email and password. What error is generated from this request?

	- `SQLITE_ERROR`

- Now that we've leveraged Repeater to gain proof of concept that Juice Shop's login is vulnerable to SQLi, let's try something a little more mischievous and attempt to leave a devastating zero-star review. First, click on the drawer button in the top-left of the application. If this isn't present for you, just skip to the next question.

	  no answer needed

- Next, click on 'Customer Feedback' (depending on the version of Juice Shop this also might be along the top of the page next to 'Login' under 'Contact Us')

	  no answer needed

- With the Burp proxy on submit feedback. Once this is done, find the POST request in your HTTP History in Burp and send it to Repeater.

	  no answer needed

- What field do we have to modify in order to submit a zero-star review?

	- `rating`

- Submit a zero-star review and complete this challenge in Juice Shop!

	  no answer needed

- Which attack type allows us to select multiple payload sets (one per position) and iterate through them simultaneously?

	- `pitchfork`

- How about the attack type which allows us to use one payload set in every single position we've selected simultaneously?

	- `Battering ram`

- Which attack type allows us to select multiple payload sets (one per position) and iterate through all possible combinations?

	- `cluster bomb`

- Perhaps the most commonly used, which attack type allows us to cycle through our payload set, putting the next available payload in each position in turn?

	- `sniper`

- Download the wordlist attached to this room, this is a shortened version of the fuzzdb SQLi platform detection list.

	  no answer needed

- Return to the Intruder in Burp. In our previous task, we passed our failed login attempt to both Repeater and Intruder for further examination. Open up the Positions sub-tab in the Intruder tab with this request now and verify that 'Sniper' is selected as our attack type.

	  no answer needed

- Burp attempts to automatically highlight possible fields of interest for Intruder, however, it doesn't have it quite right for what we'll be looking at in this instance. Hit 'Clear' on the right-hand side to clear all selected fields.

	  no answer needed

- Next, let's highlight the email field between the double quotes ("). This will be whatever you entered in the email field for our previous failed login attempt.

	  no answer needed

- Now click 'Add' to select our email field as a position for our payloads.

	  no answer needed

- Next, let's switch to the payloads sub-tab of Intruder. Once there, hit 'Load' and select the wordlist you previously downloaded in question five that is attached to this task.

	  no answer needed

- Almost there! Scroll down and uncheck 'URL-encode these characters'. We don't want to have the characters sent in our payloads to be encoded as they otherwise won't be recognized by SQL.

	  no answer needed

- Finally, click 'Start attack'. What is the first payload that returns a 200 status code, showing that we have successfully bypassed authentication?


	- `** ** *****`

- Switch over to the HTTP history sub-tab of Proxy. 

	  no answer needed

- We're going to dig for a response which issues a cookie. Parse through the various responses we've received from Juice Shop until you find one that includes a 'Set-Cookie' header. 

	  no answer needed

- Once you've found a request response that issues a cookie, right-click on the request and select 'Send to Sequencer'.

	  no answer needed

- Change over Sequencer and select 'Start live capture'

	  no answer needed

- Let Sequencer run and collect ~10,000 requests. Once it hits roughly that amount hit 'Pause' and then 'Analyze now'

	  no answer needed

- Parse through the results. What is the effective estimated entropy measured in?

	- `bits`

- In order to find the usable bits of entropy we often have to make some adjustments to have a normalized dataset. What item is converted in this process?

	- `token`

- Read through the remaining results of the token analysis

	  no answer needed

- Let's first take a look at decoder by revisiting an old friend. Previously we discovered the scoreboard within the site JavaScript. Return to our target tab and find the API endpoint highlighted in the following request.

	  no answer needed

- Copy the first line of that request and paste it into Decoder. Next, select 'Decode as ...' URL

	  no answer needed

- What character does the %20 in the request we copied into Decoder decode as?

	- `space`

- Similar to CyberChef, Decoder also has a 'Magic' mode where it will automatically attempt to decode the input it is provided. What is this mode called? 

	- `smart decode`

- What can we load into Comparer to see differences in what various user roles can access? This is very useful to check for access control issues.

	- `site maps`

- Comparer can perform a diff against two different metrics, which one allows us to examine the data loaded in as-is rather than breaking it down into bytes?

	- `words`

- To start, let's go ahead and switch over to the Options sub-tab of the Extender tab. 

	  no answer needed

- Scroll down until you reach the 'Python Environment' section. Note, Burp requires the standalone edition of Jython.

	  no answer needed

- Download the standalone version of Jython from here: [Link](https://www.jython.org/download.html) - I suggest saving this or moving it to your Documents folder

	  no answer needed

- Return back to Burp and hit 'Select file' under the Python Environment subsection for Jython standalone. Navigate to where you just downloaded this file and select it.

	  no answer needed

- Burp is now set to go for installing extensions. Switch to the BApp Store sub-tab of Extender and look through the various extensions offered.

	  no answer needed

- Which extension allows us too bookmark various requests?

	- `bookmarks`

- Download the report attached to this task. What is the only critical issue?

	- `Cross-origin resource sharing: arbitrary origin trusted`

- How many 'Certain' low issues did Burp find?

	- `12`

- Check out the provided links and keep learning!

	  no answer needed




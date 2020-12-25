# LFI Basics

- Start the VM and access it using your browser.

	no answer needed

- Access the first walkthrough, and add a parameter at the end of the link named "?page=".

	no answer needed

- Let's include the home page. At the "?page=" parameter enter home.html to include the home page.

	no answer needed

- What's the message you get when you include the home.html?

	`You included home.html`

- Type /etc/passwd in the parameter to read it.

	no answer needed

- What user that it's not by default there is present?

	- `lfi`

- Well done! You've exploited your first local file inclusion!

	no answer needed

- Now that we know what Directory Traversal is, let's access the second walkthrough.

	no answer needed

- Add the "?page=" parameter, and try to include the home page again. Does it work (Yes/No)?

	- `No`

- Use "../" to move one directory up.

	no answer needed

- What are the credit card numbers?

	- `http://<TARGET_IP>/lfi2/lfi.php?page=../creditcard`
	- `****-****-****-****`

- The same way you can include the passwd file. You'll have to move more directories up. Try reading the passwd file.

	no answer needed

	- `http://<TARGET_IP>/lfi2/lfi.php?page=../../../../../etc/passwd`

- Well done! You've exploited your first LFI using Directory Traversal.

	no answer needed

- We got our hands a bit dirty with basic LFI and LFI using path traversal. Let's dig a little deeper, and use log poisoning to get access to the underlying operating system.

	no answer needed

- We will inject some malicious php code into the server's log.

	no answer needed

- Access the third walkthrough, add the "?page=" parameter and let's try reading the apache log file.
The log file is located at the following path: /var/log/apache2/access.log

	no answer needed
	
	- `http://<TARGET_IP>/lfi/lfi.php?page=/var/log/apache2/access.log`

- Can you read the log?

	- `yes`

- Forward the request and add your parameter to the link (in my case lfi).
The link becomes: http://<IP>/lfi/lfi.php?page=/var/log/apache2/access.log&lfi=
Now you can execute commands on the system!

	no answer needed

	- Open Burpsuite and set up the proxy.
	- Catch a request and edit it as shown, then forward it.
	- Add the lfi command to the url.

- Give it a try and run uname -r. What's the output of the command?

	- `4.15.0-72-generic`

- With this knowledge read the flag from the lfi user home directory

	- Add the command `ls%20/home/lfi` instead of `uname -r`
	- Add th command `cat%20/home/lfi/flag.txt`
	- `THM{************22******************}`



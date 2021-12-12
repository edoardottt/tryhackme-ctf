# Day 6 - Patch Management Is Hard

- Deploy the attached VM and look around. What is the entry point for our web application?

	- `err`

- Use the entry point to perform LFI to read the /etc/flag file. What is the flag?

	- `***************************`

- Use the PHP filter technique to read the source code of the index.php. What is the $flag variable's value?

	- `***************************`

McSkidy forgot his login credential. Can you help him to login in order to recover one of the server's passwords?
Now that you read the index.php, there is a login credential PHP file's path. Use the PHP filter technique to read its content. What are the username and password?

	- `MCSkidy:**********`

- Use the credentials to login into the web application. Help McSkidy to recover the server's password. What is the password of the flag.thm.aoc server? 

	- `**************************`

- The web application logs all users' requests, and only authorized users can read the log file. Use the LFI to gain RCE via the log file page. What is the hostname of the webserver? The log file location is at ./includes/logs/app_access.log.

	- `**************************************`

- Bonus: The current PHP configuration stores the PHP session files in /tmp. Use the LFI to call the PHP session file to get your PHP code executed. 

		No answer needed

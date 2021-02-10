# GoldenEye

![Bond](https://github.com/edoardottt/tryhackme-ctf/blob/main/GoldenEye/goldeneye.jpg)

- First things first, connect to our network and deploy the machine.

	  no answer needed

- Use nmap to scan the network for all ports. How many ports are open?

	- `nmap -p- <TARGET_IP>` or
	- `scilla port -target <TARGET_IP>`
	- `4`

- Take a look on the website, take a dive into the source code too and remember to inspect all scripts!

	  no answer needed

- Who needs to make sure they update their default password?

	- `Boris`

- Whats their password?

	- Go to [CyberChef](https://gchq.github.io/CyberChef) and set recipe From HTML Entity.
	- `****************`

- Now go use those credentials and login to a part of the site.
	
	  no answer needed
	
	- Go to `/sev-home/` and enter username (boris) and password.

- Take a look at some of the other services you found using your nmap scan. Are the credentials you have re-usable?

	  no answer needed

- If those creds don't seem to work, can you use another program to find other users and passwords? Maybe Hydra?Whats their new password?

	- `hydra -l boris -P /data/src/wordlists/fasttrack.txt pop3://<TARGET_IP>:55007`
	- `*******`

- Inspect port 55007, what services is configured to use this port?

	- `telnet`

- Login using that service and the credentials you found earlier.

	  no answer needed

- What can you find on this service?

	- `emails`

- What user can break Boris' codes?

	- `natalya`

- Using the users you found on this service, find other users passwords

	  no answer needed

- Keep enumerating users using this service and keep attempting to obtain their passwords via dictionary attacks.

	  no answer needed

- If you remembered in some of the emails you discovered, there is the severnaya-station.com website. To get this working, you need up update your DNS records to reveal it.

	  no answer needed

- Once you have done that, in your browser navigate to: http://severnaya-station.com/gnocertdir

	  no answer needed

- Try using the credentials you found earlier. Which user can you login as?

	- `x****`

- Have a poke around the site. What other user can you find?

	- `do**`

- What was this users password?

	- `hydra -l do** -P /data/src/wordlists/fasttrack.txt pop3://<TARGET_IP>:55007`
	- `****`

- Use this users credentials to go through all the services you have found to reveal more emails.

	  no answer needed

- What is the next user you can find from doak?

	- `dr_doak`

- What is this users password?

	- `4*******!`

- Take a look at their files on the moodle (severnaya-station.com)

	  no answer needed

- Download the attachments and see if there are any hidden messages inside them?

	  no answer needed

- Using the information you found in the last task, login with the newly found user.

	  no answer needed

- Take a look into Aspell, the spell checker plugin.

	  no answer needed

- Enumerate the machine manually.

	  no answer needed

- Whats the kernel version?

	- `3.**.0-**-generic`

- You can download the exploit from here: [https://www.exploit-db.com/exploits/37292](https://www.exploit-db.com/exploits/37292)

	  no answer needed

- What is the root flag?

	- `5686**************************`

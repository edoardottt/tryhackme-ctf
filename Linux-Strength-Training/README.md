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

- Find a file named readME_hint.txt inside topson's directory and read it. Using the instructions it gives you, get the second flag.

	- `find / -type f | grep readME_hint.txt`
	- `cat /home/topson/corperateFiles/RecordsFinances/readME_hint.txt`
	- `find ~ -type f | grep MoveMe.txt`
	- `find ~ -type d | grep march`
	- `mv /home/topson/corperateFiles/RecordsFinances/-MoveMe.txt "/home/topson/corperateFiles/RecordsFinances/-march folder"`
	- `cd "/home/topson/corperateFiles/RecordsFinances/-march folder"`
	- `ls`
	- `./-runME.sh`
	- `****{****************}`

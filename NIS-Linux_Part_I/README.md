# NIS - Linux Part I

- What is shiba3's password?

	- `ssh chad@<TARGET_IP>` and enter password.
	- See [Linux Fundamentals](https://github.com/edoardottt/tryhackme-ctf/tree/main/Linux-Fundamentals)
	- `**************`

- What is shiba4's password?

	- See [Linux Fundamentals](https://github.com/edoardottt/tryhackme-ctf/tree/main/Linux-Fundamentals)
	- `**********`

- How do you run the ls command?

	- `ls`

- How do you run the ls command to show all the files inside the folder?

	- `ls -a`

- How do you run the ls command to not show the current directory and the previous directory in the output? (almost everything)

	- `ls -A`

- How do you show the information in a long listing format using ls?

	- `ls -l`

- How do you show the size in readable format? e.g. k, Mb, etc

	- `ls -h`

- How do you do a recursive ls?

	- `ls --recursive`

- How many files did you locate in the home folder of the user?(non-hidden and not inside other folders)

	- `13`

- What is the content of cat.txt?

	- `cat cat.txt`
	- `************************`

- What is the content of tac.txt?

	- `cat tac.txt`
	- `************************`

- What is the content of head.txt?

	- `cat head.txt`
	- `************************`

- What is the content of tail.txt?

	- `cat tail.txt`
	- `************************`

What is the content of the xxd.txt?

	- `cat xxd.txt`
	- `************************`

- What is the content of base64.txt?

	- `cat base64.txt`
	- `************************`

- How many .txt files did you find in the current folder?

	- `find . -type f -name "*.txt"`
	- `8`

- How many SUID files have you found inside the home folder?

	- `find . -type f -perm -4000 -exec ls -l {} \;`
	- `0`

- How many times does the word "hacker" appear in the grep files? (including variations)

	- `grep "hacker" *.txt`
	- `15`

- Is the user allowed to run the above command? (Yay/Nay)

	- `sudo -l`
	- `Nay`

- Read the above.

	  no answer needed

- What command would you use to echo the word "Hackerman" ?

	- `echo "Hackerman"`

- How would you read all files with extension .bak using xargs?

	- `find / -name *.bak -type f -print | xargs /bin/cat`

- Read the above.

	  no answer needed

- How would you grab the headers silently of [https://tryhackme.com](https://tryhackme.com) but grepping only the HTTP status code?

	- `curl -I -s https://tryhackme.com | grep http`

- What command would you run to get the flag.txt from [https://tryhackme.com/](https://tryhackme.com) ?

	- `wget https://ryhackme.com/flag.txt`

- What command would you run to download recursively up to level 5 from [https://tryhackme.com](https://tryhackme.com) ?

	- `wget -R https://tryhackme.com/`

- What is the flag from the tar file?

	- `tar -xf tarball.tar`
	- `cat flag.txt`
	- `********************`

- What is the content of gzip.txt?

	- `gzip -d gzip.txt.gz`
	- `cat gzip.txt`
	- `******************`

- What is the flag inside the 7zip file?

	- `7z x 7zip.7z`
	- `cat 7zip.txt`
	- `******************`

- What is the content of binwalk.txt?

	- `binwalk -e binwalk.png`
	- `ls _binwalk.png.extracted`
	- `cat _binwalk.png.extracted/binwalk.txt`
	- `*******************`



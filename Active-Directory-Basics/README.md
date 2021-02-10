# Active Directory Basics

- I understand what Active Directory is and why it is used.

	  no answer needed

- What database does the AD DS contain?

	- `NTDS.dit`

- Where is the NTDS.dit stored?

	- `%SystemRoot%\NTDS`

- What type of machine can be a domain controller?

	- `Windows server`

- What is the term for a hierarchy of domains in a network?

	- `tree`

- What is the term for the rules for object creation?

	- `Domain schema`

- What is the term for containers for groups, computers, users, printers, and other OUs?

	- `Organization units`

- Which type of groups specify user permissions?

	- `Security groups`

- Which group contains all workstations and servers joined to the domain?

	- `Domain computers`

- Which group can publish certificates to the directory?

	- `Cert publisher`

- Which user can make changes to a local machine but not to a domain controller?

	- `Local administrators`

- Which group has their passwords replicated to read-only domain controllers?

	- `Allowed RODC Password Replication Group`

- What type of trust flows from a trusting domain to a trusted domain?

	- `Directional`

- What type of trusts expands to include other trusted domains?

	- `Transitive`

- What type of authentication uses tickets?

	- `Kerberos`

- What domain service can create, validate, and revoke public key certificates?

	- `Certificate Services`

- What is the Azure AD equivalent of LDAP?

	- `Rest apis`

- What is the Azure AD equivalent of Domains and Forests?

	- `Tenants`

- What is the Windows Server AD equivalent of Guests?

	- `Trusts`

- Deploy the machine

	  no answer needed

- What is the name of the Windows 10 operating system?
 
	- `Get-NetComputer -fulldata | select operatingsystem`
	- `*********** ** ********* **********`

- What is the second "Admin" name?

	- `Get-NetUser | select cn`
	- `******`

- Which group has a capital “V” in the group name?

	- `net localgroup`
	- `Hyper-V Administrators`

- When was the password last set for the SQLService user?

	- `Get-ADUser -identity SQLService -properties *`
	- `5/**/2020 *:**:** PM`

- I understand the basics of Active Directory

	  no answer needed



# Time for some ELForensics

User name: `littlehelper`
User password: `iLove5now!`

Open Remmina and connect yourself to the remote machine. 

- Read the contents of the text file within the Documents folder. What is the file hash for db.exe?

	- Open PowerShell in remote machine
	- `Set-Location Documents`
	- `Get-ChildItem`
	- `Get-Content '.\db file hash.txt'`
	- `********************856E6A78E3A1`

- What is the file hash of the mysterious executable within the Documents folder?

	- `Get-FileHash -Algorithm MD5 deebee.exe`
	- `********************6EB12AED09F0`

- Using Strings find the hidden flag within the executable?

	- `C:\Tools\strings64.exe -accepteula deebee.exe`
	- Read carefully the output
	- `THM{*******************************}`

- What is the flag that is displayed when you run the database connector file?

	- `Get-Item -Path .\deebee.exe -Stream *`
	- `wmic process call create $(Resolve-Path .\deebee.exe:hidedb)`
	- `THM{*******************************}`



### see you ...

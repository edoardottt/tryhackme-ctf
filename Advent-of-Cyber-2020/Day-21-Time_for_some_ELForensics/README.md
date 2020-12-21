# Time for some ELForensics

User name: `littlehelper`
User password: `iLove5now!`

Open Remmina and connect yourself to the remote machine. 

- Read the contents of the text file within the Documents folder. What is the file hash for db.exe?

	- Open PowerShell in remote machine
	- `Set-Location Documents`
	- `Get-ChildItem`
	- `Get-Content '.\db file hash.txt'`
	- `596690FFC54AB6101932856E6A78E3A1`

- What is the file hash of the mysterious executable within the Documents folder?

	- `Get-FileHash -Algorithm MD5 deebee.exe`
	- `5F037501FB542AD2D9B06EB12AED09F0`

- Using Strings find the hidden flag within the executable?

	- `C:\Tools\strings64.exe -accepteula deebee.exe`
	- Read carefully the output
	- `THM{f6**7e6c******413**********cb6f9}`

- What is the flag that is displayed when you run the database connector file?

	- `Get-Item -Path .\deebee.exe -Stream *`
	- `wmic process call create $(Resolve-Path .\deebee.exe:hidedb)`
	- `THM{0**731dd******ecca**********97c}`






### see you ...

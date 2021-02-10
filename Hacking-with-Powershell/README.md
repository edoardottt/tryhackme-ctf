# Hacking with Powershell

- Read the above and deploy the machine!

	  no answer needed

- What is the command to get help about a particular cmdlet(without any parameters)?

	- `Get-Help`

- What is the location of the file "interesting-file.txt"

	- `Get-ChildItem -Path C:\ -Include *interesting-file.txt* -File -Recurse -ErrorAction SilentlyContinue`
	- `*:********* *****`

- Specify the contents of this file

	- `Get-Content "*******************\interesting-file.txt.txt"`
	- `************************`

- How many cmdlets are installed on the system(only cmdlets, not functions and aliases)?

	- `Get-Command | Where-Object -Parameter CommandType -eq Cmdlet | measure`
	- `****`

- Get the MD5 hash of interesting-file.txt

	- `Get-FileHash -Path "***************\interesting-file.txt.txt" -Algorithm MD5`
	- `*********************************`

- What is the command to get the current working directory?

	- `Get-Location`

- Does the path "C:\Users\Administrator\Documents\Passwords" Exist(Y/N)?

	- `n`

- What command would you use to make a request to a web server?

	- `Invoke-WebRequest`

- Base64 decode the file b64.txt on Windows.

	- `certutil -decode "C:\Users\Administrator\Desktop\b64.txt" out.txt`
	- `Get-Content out.txt`
	- `****************************`

- How many users are there on the machine?

	- `Get-LocalUser`
	- `*`

- Which local user does this SID(S-1-5-21-1394777289-3961777894-1791813945-501) belong to?

	- `Get-LocalUser -SID "S-1-5-21-1394777289-3961777894-1791813945-501"`
	- `*****`

- How many users have their password required values set to False?

	- `Get-LocalUser | Where-Object -Property PasswordRequired -Match false`
	- `*`

- How many local groups exist?

	- `Get-LocalGroup | measure`
	- `**`

- What command did you use to get the IP address info?

	- `Get-NetIPAddress`

- How many ports are listed as listening?

	- `Get-NetTCPConnection | Where-Object -Property State -Match Listen | measure`
	- `**`

- What is the remote address of the local port listening on port 445?

	- `::`

- How many patches have been applied?

	- `Get-Hotfix | measure`
	- `**`

- When was the patch with ID KB4023834 installed?

	- `Get-Hotfix -Id KB4023834`
	- `***********************`

- Find the contents of a backup file.

	- `Get-ChildItem -Path C:\ -Include *.bak* -File -Recurse -ErrorAction SilentlyContinue`
	- `Get-Content ***********`
	- `***************`

- Search for all files containing `API_KEY`

	- `Get-ChildItem C:\* -Recurse | Select-String -pattern API_KEY`
	- `**********`

- What command do you do to list all the running processes?

	- `Get-Process`

- What is the path of the scheduled task called new-sched-task?

	- `/`

- Who is the owner of the C:\

	- `Get-Acl c:/`
	- `** ************************`

- What file contains the password?

	- `Doc3M`

- What is the password?

	- `***********************`

- What files contains an HTTPS link?

	- `Doc2Mary`

- How many open ports did you find between 130 and 140(inclusive of those two)?

	- `11`

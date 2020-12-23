# The Grinch strikes again!

![win10-ransom](https://github.com/edoardottt/tryhackme-ctf/blob/main/Advent-of-Cyber-2020/Day-23-The_Grinch_strikes_again!/win-ransomware.png)

Use Remmina to connect to the target machine as the documentation in the [proper page](https://tryhackme.com/room/adventofcyber2) tells you.

  - User name: `administrator`
  - User password: `sn0wF!akes!!!`


- Decrypt the fake 'bitcoin address' within the ransom note. What is the plain text value?

	- `echo -n "bm9tb3JlYmVzdGZlc3RpdmFsY29tcGFueQ==" | base64 -d`
	- `nomorebestfestivacompany`

- At times ransomware changes the file extensions of the encrypted files. What is the file extension for each of the encrypted files?

	- `.grinch`

- What is the name of the suspicious scheduled task?

	- `opidsfsdf`

- Inspect the properties of the scheduled task. What is the location of the executable that is run at login?

	- `C:\Users\Administrator\Desktop\oidsfsdf.exe`

- There is another scheduled task that is related to VSS. What is the ShadowCopyVolume ID?

	- `7a9eea15-000-0000-0000-010000000000`

- Assign the hidden partition a letter. What is the name of the hidden folder?

	- `confidential`

- Right-click and inspect the properties for the hidden folder. Use the 'Previous Versions' tab to restore the encrypted file that is within this hidden folder to the previous version. What is the password within the file?

	- `m****55w0**********e!`




# see you ...

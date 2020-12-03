# Day 3 - Christmas Chaos

- Deploy your AttackBox (the blue "Start AttackBox" button) and the tasks machine (green button on this task) if you haven't already. Once both have deployed, open FireFox on the AttackBox and copy/paste the machines IP (<TARGET_IP>) into the browser search bar.

	// no answer needed

- Use BurpSuite to bruteforce the login form.  Use the following lists for the default credentials:

| Username | Password |
|---|---|
| root | root |
| admin | password |
| user | 12345 |

Use the correct credentials to log in to the Santa Sleigh Tracker app. Don't forget to turn off Foxyproxy once BurpSuite has finished the attack.

   - First of all make sure you're under proxy. If not, follow the instructions above (on the CTF page) to enable it if you're using AttackBox. If not, add FoxyProxy to the extensions, then create a record with options: name: `Burp` or whatever you like; Proxy type: `HTTP`; Proxy IP: `127.0.0.1`; Port: `8080`. Then save and enable it.

   - Open BurpSuite and perform a login (with random user and pass) request with the Browser.

   - On the proxy tab of BurpSuite you should see a new request captured. Something like this:
		
		```POST /login HTTP/1.1
		Host: <TARGET_IP>
		User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
		Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
		Accept-Language: en-US,en;q=0.5
		Accept-Encoding: gzip, deflate
		Content-Type: application/x-www-form-urlencoded
		Content-Length: 31
		Origin: http://<TARGET_IP>
		Connection: close
		Referer: http://<TARGET_IP>/
		Upgrade-Insecure-Requests: 1

		username=<USERNAME>&password=<PASSWORD>
		```

   - Right click on it and click `send to Intruder`.

   -  Go to Intruder tab and then on position sub-tab.

   - Change the attack type from `Sniper` to `Cluster Bomb`.
	
   - Make sure the <USERNAME> and the <PASSWORD> are selected with these symbols `username=§<USERNAME>§&password=§<PASSWORD>§`. If not, highlight them with the cursor and click on `Add §`.
	
   - Then switch to Payloads sub-tab and set all the payloads. We have two payloads: username and password, respectively 1 and 2. So, for instance, to set the list of possible payloads for the username, the option `Payload set` will be set to `1` and the we add to the list of payloads our three (just an example, in real we can perform thousands of requests) items. Same for password.

   - Start the attack.

   - You can see one of the result rows has different length in respect to the others... Let's try with that login credentials!

   - It works!

   - `THM{88**fab9******84751**********d1a}`

## see you ...

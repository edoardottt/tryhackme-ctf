# Day 6 - Be careful with what you wish on a Christmas night

- Deploy your AttackBox (the blue "Start AttackBox" button) and the tasks machine (green button on this task) if you haven't already. Once both have deployed, open Firefox on the AttackBox and copy/paste the machines IP (http://<TARGET_IP>:5000) into the browser search bar (the webserver is running on port 5000, so make sure this is included in your web requests).

	  no answer needed
	
	![santasportal](https://github.com/edoardottt/tryhackme-ctf/blob/main/Advent-of-Cyber-2020/Day-06-Be_careful_with_what_you_wish_on_a_Christmas_night/santasportal.png)

- What vulnerability type was used to exploit the application?

	- `stored crosssite scripting`

- What query string can be abused to craft a reflected XSS?

	- If you query one example on the first search bar, you will see there's a new char appended to URL.
	- `q`

- Launch the OWASP ZAP Application

	  no answer needed

- Run a ZAP (zaproxy) automated scan on the target. How many alerts does it display?

	- `5`

- How many types of XSS are there in the scan?

	- `2`

- Explore the XSS alerts that ZAP has identified, are you able to make an alert appear on the "Make a wish" website?

	  no answer needed

## see you ...

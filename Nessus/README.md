# Nessus

- I have read the description!

	  no answer needed

- Go to https://www.tenable.com/products/nessus/nessus-essentials and register an account. 

	  no answer needed

- We will then download the `Nessus-#.##.#-debian6_amd64.deb` file

	  no answer needed

- In the terminal we will navigate to that folder and run the following command: `sudo dpkg -i package_file.deb`

	  no answer needed

- We will now start the Nessus Service with the command: `sudo /bin/systemctl start nessusd.service`

	  no answer needed

- Open up Firefox and goto the following URL: https://localhost:8834/

	  no answer needed

- Next, we will set up the scanner. Select the option Nessus Essentials

	  no answer needed

- Fill out the Username and Password fields. Make sure to use a strong password!

	  no answer needed

- Nessus will now install the plugins required for it to function.

	  no answer needed

- Log in with the account credentials you made earlier.

	  no answer needed

- You have now successfully installed Nessus!

	  no answer needed

- What is the name of the button which is used to launch a scan?

	- `new scan`

- What side menu option allows us to create custom templates?

	- `policies`

- What menu allows us to change plugin properties such as hiding them or changing their severity?

	- `plugin rules`

- In the 'Scan Templates' section after clicking on 'New Scan', what scan allows us to see simply what hosts are alive?

	- `host discovery`

- One of the most useful scan types, which is considered to be 'suitable for any host'?

	- `basic network scan`

- What scan allows you to 'Authenticate to hosts and enumerate missing updates'?

	- `credential patch audit`

- What scan is specifically used for scanning Web Applications? 

	- `web application tests`

- Create a new 'Basic Network Scan' targeting the deployed VM. What option can we set under 'BASIC' (on the left) to set a time for this scan to run? This can be very useful when network congestion is an issue.

	- `schedule`

- Under 'DISCOVERY' (on the left) set the 'Scan Type' to cover ports 1-65535. What is this type called?

	- `port scan (all ports)`

- What 'Scan Type' can we change to under 'ADVANCED' for lower bandwidth connection?

	- `scan low bandwidth links`

- With these options set,  launch the scan. 

	  no answer needed

- After the scan completes, which 'Vulnerability' in the 'Port scanners' family can we view the details of to see the open ports on this host?

	- `Nessus SYN scanner`

- What Apache HTTP Server Version is reported by Nessus?

	- `2.4.**`

- What is the plugin id of the plugin that determines the HTTP server type and version?

	- Google it
	- `*****`

- What authentication page is discovered by the scanner that transmits credentials in cleartext?

	- `*****.php`

- What is the file extension of the config backup?

	- `.bak`

- Which directory contains example documents? (This will be in a php directory)

	- `/********/phpids/*.*/****/********/`

- What vulnerability is this application susceptible to that is associated with X-Frame-Options?

	- `C************`



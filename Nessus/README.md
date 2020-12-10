# Nessus

- Deploy the virtual machine!

	no answer needed

- First, create a basic Ubuntu box (or any other system of your choice). Minimum 4 2GHz cores, 4 GB RAM (8 Recommended) and 30 GB of disk space.

	no answer needed

- Next, go ahead and register for a Nessus Home license. This can be used to scan up to 16 IP addresses at a time. Be sure to keep this license information safe, you'll need it for any manual work. Here's the registration link: https://www.tenable.com/products/nessus-home

	no answer needed

- Follow the installation instructions on Tenable's website, once Nessus is set up connect the machine that it lives on to the network using your VPN file.

	no answer needed

- As we log into Nessus, we are greeted with a button to launch a scan, what is the name of this button?

	- `new scan`

- Nessus allows us to create custom templates that can be used during the scan selection as additional scan types, what is the name of the menu where we can set these?

	- `policies`

- Nessus also allows us to change plugin properties such as hiding them or changing their severity, what menu allows us to change this?

	- `plugin rules`

- Nessus can also be run through multiple 'Scanners' where multiple installations can work together to complete scans or run scans on remote networks, what menu allows us to see all of these installations?

	- `scanners`

- Let's move onto the scan types, what scan allows us to see simply what hosts are 'alive'?

	- `host discovery`

- One of the most useful scan types, which is considered to be 'suitable for any host'?

	- `basic network scan`

- Following a few basic scans, it's often useful to run a scan wherein the scanner can authenticate to systems and evaluate their patching level. What scan allows you to do this?

	- `credentialed patch audit`

- When performing Web App tests it's often useful to run which scan? This can be incredibly useful when also using nitko, zap, and burp to gain a full picture of an application. 

	- `web application test`

- Deploy the machine and connect to the network

	no answer needed

- Create a new 'Basic Network Scan' targeting the deployed VM. What option can we set under 'BASIC' to set a time for this scan to run? This can be very useful when network congestion is an issue.

	- `schedule`

- Under discovery set the scan to cover ports 1-65535. What is this type called?

	- `port scan (all ports)`

- As we are connected to the network via a VPN, it may be to our benefit to 'tone down' the scan a bit. What scan type can we change to under 'ADVANCED' for this lower bandwidth connection?

	- `scan low bandwidth links`

- With these options set (other than the time to run) save and launch the scan.

	no answer needed

- After the scan completes, which 'Vulnerability' can we view the details of to see the open ports on this host?

	- `Nessus SYN scanner`

- There seems to be a chat server running on this machine, what port is it on?

	- `6667`

- Looks like we have a medium level vulnerability relating to SSH, what is this vulnerability named?

	- `ssh weak algorithms supported`

- What web server type and version is reported by Nessus?

	- `Apache/2.4.99`

- An optional but awesome additional step, link your Nessus box up to an SMTP server via the Settings panel. Google provides this for free if you already have a Gmail account. Adding 2-factor authentication on your account and create an app password, then link Nessus to the Gmail SMTP server via these following settings: https://www.siteground.com/kb/google\_free\_smtp\_server/

	no answer needed

- Run a web application scan against this new box.

	no answer needed

- What is the plugin id of the plugin that determines the HTTP server type and version?

	- `10107`

- What authentication page is discovered by the scanner that transmits credentials in cleartext?

	- `login.php`

- What is the file extension of the config backup?

	- `.bak`

- Which directory contains example documents? (This will be in a php directory)

	- `/external/phpids/0.6/docs/examples/`

- What vulnerability is this application susceptible to that is associated with X-Frame-Options?

	- `clickjacking`

- What version of php is the server using?

	- `5.5.9-1ubuntu4.26`








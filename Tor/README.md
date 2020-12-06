# Tor

- Run apt-get install tor to install/update your Tor packages

	  no answer needed

- Run `service tor start` to start the Tor service

	  no answer needed

- Run `service tor status` to check Tor's availability

	  no answer needed

- Run `service tor stop` to stop the Tor service

	  no answer needed

- Let's start with running `apt install proxychains` to install/update proxychains tool

	  no answer needed

- Run `nano /etc/proxychains.conf` to edit the settings. (Note: You can use any text editing tool instead of nano)

	  no answer needed

- We can now see, that most of the methods are under comment mark. You can read their description and decide on using one of them in the future. For this lesson let's uncomment `dynamic_chain` and comment others (simply put '#' to the left). Additionally, it is useful to uncomment `proxy_dns` in order to prevent DNS leak. Scroll through the document and see whenever you want to add some additional proxies at the bottom of the page (which is not required at this point).

Apply all the settings.

	no answer needed

- Start the TOR service and run `proxychains firefox`. Usually, you are required to put 'proxychains' command before anything in order to force it to transfer data through Tor.

	  no answer needed

- After the firefox has loaded, check if your IP address has changed with any website that provides such information. Also, try running a test on `dnsleaktest.com` and see if your DNS address changed too.

NOTE: All other web browser windows should be closed before opening firefox through proxychains!

	no answer needed

- Finish the installation

	  no answer needed

- Launch the Tor Browser and set your privacy settings to Level 2 (Safer)

	  no answer needed

- Access the website below and capture the flag by copying bitcoin address at the bottom of the page!
http://danielas3rtn54uwmofdo3x2bsdifr47huasnmbgqzfrec5ubupvtpid.onion/

	- `1K91**vvE4P******T7z**********HBm5`




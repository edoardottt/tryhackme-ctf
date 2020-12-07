# The Grinch Really Did Steal Christmas

Download the ZIP file "aocpcaps.zip" that is attached to this task, use a combination of the filters and features of Wireshark we've covered to answer the questions below:

- Open "pcap1.pcap" in Wireshark. What is the IP address that initiates an ICMP/ping?

	- `10.11.3.2`

- If we only wanted to see HTTP GET requests in our "pcap1.pcap" file, what filter would we use?

	- `http.request.method == get`

- Now apply this filter to "pcap1.pcap" in Wireshark, what is the name of the article that the IP address "10.10.67.199" visited?

	- `reindeer-of-the-week`

- Let's begin analysing "pcap2.pcap". Look at the captured FTP traffic; what password was leaked during the login process?
There's a lot of irrelevant data here - Using a filter here would be useful!

	- `plaintext_password_fiasco`

- Continuing with our analysis of "pcap2.pcap", what is the name of the protocol that is encrypted?

	- `ssh`

- Analyse "pcap3.pcap" and recover Christmas!
What is on Elf McSkidy's wishlist that will be used to replace Elf McEager?

	- `Rubber ducky`

## see you ...

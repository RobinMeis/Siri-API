Siri-API
========

Siri-API is a tool which opens Siri for your own wishes WITHOUT the requirement of a Jailbreak. Basically it is like GoogolPlex but it is much more flexible since you can host it on your own computer.
You need a Linux running computer (i.e. Raspberry Pi) and a Squid Proxy version compiled with SSL support. These versions aren't available from official package sources, so you have to compile it by yourself. You can follow the instructions below.
You can watch the demo video on ... to see what is possible with Siri-API. I use the program for my home automation system but any other usage is possible. You just have to write your own rules and commands in Python 3. With the easy to use API it is just a game. I also provide a working squid.conf configuration file for usage with the API. If you're already running Squid Proxy for other services you HAVE to change it so, that Squid still works in your environment.
I tested Siri-API on an iPhone 5S with iOS 7 but it should also work with other iDevices supporting Siri and older iOS versions.

=== System requirements ===
- Linux PC (i.e. Raspberry Pi)
- Squid Proxy with SSL support (see instructions below)
- Python3 interpreter to run the API's server

=== Installation of Squid Proxy ===
Since you will need to compile Squid Proxy on your own, you need to install the following packages. On Debian (based) systems you can use the following commands:

sudo apt-get install build-essential
sudo apt-get install libssl-dev

After that you need to install Squid Proxy. You can download the latest version from http://www.squid-cache.org/Versions/. I suggest to use Version 3.4.4 because I've done my sample setup with it. If you use another version you might have to change the configuration file. If you got it running with another version (with and without modifying the sample configuration file), please inform me by open an Issue on GitHub (https://github.com/HcDevel/Siri-API/pulls). Then I will add this version of Squid to the supported versions.
In the following instructions I emanate you have downloaded version 3.4.4. If not, you have to change the paths in the instructions. This isn't to complicated.

1. Download Squid (I would suggest to do this in you home directory)
   wget http://www.squid-cache.org/Versions/v3/3.4/squid-3.4.4.tar.gz
   
2. Extract Squid at the same place
   tar -xvzf squid-3.4.4.tar.gz
   
3. Change into the extracted directory of squid
   cd squid-3.4.4/
   
4. Compile Squid. Just copy the commands, they are ready to compile Squid with SSL support. Compiling might take a long time. On my Raspberry Pi it took about 6 hours
   sudo ./configure --prefix=/usr/local/squid --enable-icap-client --enable-ssl --enable-ssl-crtd --with-default-user=squid
   sudo make all
   sudo make install
   
5. Create permissions. We compiled squid with default user squid, so we have to add the required user and permissions
   useradd squid
   chown -R squid:squid /usr/local/squid/var/logs/
   
6. Now you should create the swap directories. This can be done by running
   /usr/local/squid/sbin/squid -z
   
7. Next you have to generate the SSL certificates. I won't explain every command, so just copy it!
   cd /usr/local/squid
   mkdir ssl_cert
   cd ssl_cert
   openssl req -new -newkey rsa:1024 -days 365 -nodes -x509 -keyout myCA.pem -out myCA.pem
   
=== Installation of Siri-API ===

1. To run Siri-API you need to install the Python3 interpreter.
   On Debian (based) systems you can do this with running sudo apt-get install python3
   
2. Download Siri-API
   sudo apt-get install git # (Again, apt only works on Debian based systems)
   git clone https://github.com/HcDevel/Siri-API
   

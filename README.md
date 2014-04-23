Siri-API
========

Siri-API is a tool which opens Siri for your own wishes WITHOUT the requirement of a Jailbreak. Basically it is like GoogolPlex but it is much more flexible since you can host it on your own computer.

You need a Linux running computer (i.e. Raspberry Pi) and a Squid Proxy version compiled with SSL support. These versions aren't available from official package sources, so you have to compile it by yourself. You can follow the instructions in the documentation.

You can watch the demo video on ... to see what is possible with Siri-API. I use the program for my home automation system but any other usage is possible. You just have to write your own rules and commands in Python 3. With the easy to use API it is just a game. I also provide a working squid.conf configuration file for usage with the API. If you're already running Squid Proxy for other services you HAVE to change it so, that Squid still works in your environment.

I tested Siri-API on an iPhone 5S with iOS 7 but it should also work with other iDevices supporting Siri and older iOS versions.

You can find the documentation under https://github.com/HcDevel/Siri-API/wiki/_pages  
The installation instructions are under https://github.com/HcDevel/Siri-API/wiki/Installation

If you have any problem, please report it by opening an issue in the issue tracker.
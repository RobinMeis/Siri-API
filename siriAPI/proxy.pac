function FindProxyForURL(url, host) {
    var keyword = url.toLowerCase().indexOf("<keyword>");
    if (url.toLowerCase().indexOf("search?p=") >= 0)	{
		return "PROXY <squid_host>:<squid_port>";
	}

	return "DIRECT";
}

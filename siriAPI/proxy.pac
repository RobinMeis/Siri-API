function FindProxyForURL(url, host) {
    var keyword = url.toLowerCase().indexOf("<keyword>");
    if (url.toLowerCase().indexOf("search?p=") >= 0 || dnsDomainIs(host, "<google_domain>") && (keyword >= 0) && url.toLowerCase().indexOf("search?q=") >= 0)	{
		return "PROXY <squid_host>:<squid_port>";
	}

	return "DIRECT";
}

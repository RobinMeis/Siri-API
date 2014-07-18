function FindProxyForURL(url, host)
{
	isYahoo = dnsDomainIs(host, "<yahoo_domain>");
	if (isYahoo && url.toLowerCase().indexOf("search?p=") >= 0)	{
		return "PROXY <squid_host>:<squid_port>";
	}
  
	var keyword = url.toLowerCase().indexOf("<keyword>");
	if (dnsDomainIs(host, "<google_domain>") && (keyword >= 0) && url.toLowerCase().indexOf("search?q=") >= 0)	{
		return "PROXY <squid_host>:<squid_port>";
	}
	return "DIRECT";
}
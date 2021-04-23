#ATLAS Ripe Data API 
Titles below correspond to a section of [https://stat.ripe.net/docs/data_api](this site). Their info is copy pasted from the same site. 

Note: append `data_overload_limit=ignore` after every query. 
# ASN's per country
This data call provides information on a country's registered and routed ASNs. Registered ASNs are based on registration information made public by the Regional Internet Registries. The routing information is based on the data collected with the RIPE NCC's RIS system, https://ris.ripe.net.
The data call supports history, with data points being aligned to times dumps are created in RIS (00:00, 08:00 and 16:00 UTC).
By default, the data call returns just the number of registered and routed ASNs. This is mainly to prevent returning thousands of ASNs. See parameter settings below to further tailor the output to your needs.
#### Count
https://stat.ripe.net/data/country-asns/data.json?resource=gb&lod=1
#### List
https://stat.ripe.net/data/country-asns/data.json?resource=gb

# Country Resource Stats
This data call returns statistics on Internet resources for a country - this includes:

- number of ASNs seen in routing data and registration data
- number of prefixes in routing data and registration data (split into IPv4 and IPv6)
- amount of IPv4 space seen in routing data as well as registration data

The results can be restricted to a specific time period as well the granularity is variable but can be set explicitly.

https://stat.ripe.net/data/country-resource-stats/data.json?resource=gb&starttime=2019-12-01T12:00&resolution=1w 

# Country Resource List
This data call lists the Internet resources associated with a country, including ASNs, IPv4 ranges and IPv4/6 CIDR prefixes.

https://stat.ripe.net/data/country-resource-list/data.json?resource=at&time=2012-12-01

# M-lab Activity Count
This data call returns a count of all the hosts within a certain resource for which any network tests occurred.

The data is based on active host measurements collected by the Measurement Lab platform (M-Lab).

The measurements are commonly ran using the M-Lab Network Detection Tool (NDT), available as a stand-alone network speed test application, and also included in a popular BitTorrent client.
Note that due to the nature the data is processed data can be delayed for around two days at the beginning of each month!

https://stat.ripe.net/data/mlab-activity-count/data.json?resource=193.0.0.0/16&starttime=2013-08-21T07:00&endtime=2013-18-27T12:00 

Note: Unavailable, under maintanance.

# M-lab Bandwidth
This data call returns a set of all the measured network bandwidths for a certain resource.

The data is based on active host measurements collected by the Measurement Lab platform (M-Lab).

The bandwidth of a host is determined as the maximum network throughput value for all the tests/measurements performed by that host during the specified time period.
The value of the measurement throughput is computed as the number of octets transmitted between the host and the chosen M-Lab server, divided by their transfer time.

The measurements are commonly ran using the M-Lab Network Detection Tool (NDT), available as a stand-alone network speed test application, and also included in a popular BitTorrent client.
Note that due to the nature the data is processed data can be delayed for around two days at the beginning of each month!

https://stat.ripe.net/data/mlab-bandwidth/data.json?resource=cy&starttime=2013-08-21T07:00&endtime=2013-18-27T12:00 

Note: Unavailable, under maintanance.

# M-lab Clients
This data call returns a set of all the hosts within a certain resource for which any network tests occurred.

The data is based on active host measurements collected by the Measurement Lab platform (M-Lab).

The measurements are commonly ran using the M-Lab Network Detection Tool (NDT), available as a stand-alone network speed test application, and also included in a popular BitTorrent client.
Note that due to the nature the data is processed data can be delayed for around two days at the beginning of each month!

https://stat.ripe.net/data/mlab-clients/data.json?resource=193.0.0.0/16&starttime=2013-08-21T07:00&endtime=2013-18-27T12:00 


# RIR Stats country 
This data call returns geographical information for Internet resources based on RIR Statistics data.

https://stat.ripe.net/data/rir-stats-country/data.json?resource=uk

# Atlas Probe Deployment 
This data call provides information on the number of RIPE Atlas probes in a region, a country or network (ASN). It supports history, with a general start in 2014.
The information is based on data from the RIPE Atlas probe archive, ftp://ftp.ripe.net/ripe/atlas/probes/archive/, which is processed once a day.

https://stat.ripe.net/data/atlas-probe-deployment/data.json?resource=cc_nl

# Atlas probes
This data call provides information on the RIPE Atlas probes in an network (ASN), a prefix or a country.
The information is based on data coming from the RIPE Atlas REST API, https://atlas.ripe.net/docs/api/v2/manual/.

https://stat.ripe.net/data/atlas-probes/data.json?resource=at 


# Atlas targets
This data call provides information on the RIPE Atlas measurements that target an network (ASN), a prefix or a hostname.
The information is based on data coming from the RIPE Atlas REST API, https://atlas.ripe.net/docs/api/v2/manual/.

https://stat.ripe.net/data/atlas-targets/data.json?resource=140.78/16

Note: Resource can't be a country code here. 

# Country ASNs 
This data call provides information on a country's registered and routed ASNs. Registered ASNs are based on registration information made public by the Regional Internet Registries. The routing information is based on the data collected with the RIPE NCC's RIS system, https://ris.ripe.net.
The data call supports history, with data points being aligned to times dumps are created in RIS (00:00, 08:00 and 16:00 UTC).
By default, the data call returns just the number of registered and routed ASNs. This is mainly to prevent returning thousands of ASNs. See parameter settings below to further tailor the output to your needs.






























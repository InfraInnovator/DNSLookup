import dns.resolver
import argparse

def get_dns_records(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        for rdata in answers:
            print(rdata.to_text())
    except dns.resolver.NoAnswer:
        print(f"No {record_type} records found for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain name {domain} does not exist")
    except dns.resolver.NoNameservers:
        print(f"No nameservers found for {domain}")
    except dns.exception.DNSException as e:
        print(f"Error fetching {record_type} records: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def parse_args():
    parser = argparse.ArgumentParser(description='Fetch DNS records for a specified domain.')
    parser.add_argument('domain', help='The domain to fetch DNS records for')
    parser.add_argument('record_type', nargs='?', default='-all',
                        help='The type of DNS record to fetch (A, AAAA, MX, NS, TXT, CNAME, SOA, or -all for all types)')
    return parser.parse_args()

def main():
    args = parse_args()

    if args.record_type.lower() == '-all':
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']
        for r_type in record_types:
            print(f"\n{r_type} records for {args.domain}:")
            get_dns_records(args.domain, r_type)
    else:
        get_dns_records(args.domain, args.record_type)

if __name__ == "__main__":
    main()

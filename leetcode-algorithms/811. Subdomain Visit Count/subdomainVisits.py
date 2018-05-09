class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_dict = {}
        for cp in cpdomains:
            [num, url] = cp.split(" ")
            domains = url.split(".")
            for i in range(len(domains)):
                sub_domain = ".".join(domains[i:])
                if domain_dict.get(sub_domain, 0):
                    domain_dict[sub_domain] += int(num)
                else:
                    domain_dict[sub_domain] = int(num)

        output = []
        for sub_domain in domain_dict:
            output.append(str(domain_dict[sub_domain]) + " " + sub_domain)

        return output


solution = Solution()
result = solution.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
print(result)
print(type(result))

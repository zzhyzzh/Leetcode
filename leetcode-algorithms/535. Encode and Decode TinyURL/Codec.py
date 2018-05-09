class Codec:
    table = {}
    count = 0
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.table[self.count] = longUrl
        url = "http://tinyurl.com/" + str(self.count)
        self.count += 1
        return url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.table[int(shortUrl[len("http://tinyurl.com/"):])]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
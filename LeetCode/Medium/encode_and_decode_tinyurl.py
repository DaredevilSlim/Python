#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
import random

# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it
# returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.
# There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be
# encoded to a tiny URL and the tiny URL can be decoded to the original URL.
# Implement the Solution class:
# - Solution() Initializes the object of the system.
# - String encode(String longUrl) Returns a tiny URL for the given longUrl.
# - String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given
# shortUrl was encoded by the same object.
# Example 1:
# Input: url = "https://leetcode.com/problems/design-tinyurl"
# Output: "https://leetcode.com/problems/design-tinyurl"
# Explanation:
# Solution obj = new Solution();
# string tiny = obj.encode(url); // returns the encoded tiny url.
# string ans = obj.decode(tiny); // returns the original url after decoding it.
# Constraints:
# 1 <= url.length <= 104
# url is guranteed to be a valid URL.
class Codec:

    def __init__(self):
        self.code2url = {}
        self.url2code = {}

    def encode(self, long_url):
        letter_set = string.ascii_letters + string.digits
        while long_url not in self.url2code:
            code = ''.join([random.choice(letter_set) for i in range(6)])
            if code not in self.code2url:
                self.code2url[code] = long_url
                self.url2code[long_url] = code
        return  'http://tinyurl.com/' + self.url2code[long_url]

    def decode(self, short_url):
        return self.code2url[short_url[-6:]]


codec = Codec()
print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))

# Created by Aashish Adhikari at 4:35 PM 2/15/2021

'''
Time Complexity:
O(m+n)

Space Complexity:
O(m+n)
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """


        left = 0
        right = 0
        sol = ""


        from collections import Counter
        dict_t = Counter(t)

        required = len(dict_t)


        # current window dictionary
        current_window_dictionary = {}

        # formed counts the number of unique characters that match between t and the current window
        formed = 0

        while right < len(s):

            char = s[right]

            # take the next character and put into the window dictionary
            if char in current_window_dictionary:
                current_window_dictionary[char] += 1
            else:
                current_window_dictionary[char] = 1

            # if this character is also in t and the count of this character in t matches the count in the current dictionary
            if char in dict_t and dict_t[char] == current_window_dictionary[char]:
                formed += 1

            # if all the characters in t are present in the current window, save this solution if better than before and try to reduce the window from the left to see if it is helpful
            while formed == required and left <= right:
                if sol == "":
                    sol = s[left:right+1]
                else:
                    if right-left + 1 < len(sol):
                        sol = s[left:right+1]

                char = s[left]

                current_window_dictionary[char] -= 1

                if char in dict_t and current_window_dictionary[char] < dict_t[char]:
                    formed -= 1

                left += 1


            # expand the window again
            right += 1


        return sol




















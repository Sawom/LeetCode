class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if(sorted_s == sorted_t) :
            return True
        else:
            return False

# check result in ide
if _name_ == "_main_":
    obj = Solution()
    first_word = input('first word: ')
    second_word = input('second word: ' )

    result = obj.isAnagram(first_word, second_word)

    if(result):
        print('anagram')
    else:
        print('not anagram')

    # or i can test it by this way
    # obj = Solution()
    # print(obj.isAnagram("race", "care"))
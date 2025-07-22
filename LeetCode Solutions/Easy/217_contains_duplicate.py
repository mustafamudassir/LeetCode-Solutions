from typing import List  # Import List type for type hinting

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create an empty set to store unique elements

        # Iterate through each number in the input list
        for num in nums:
            if num in seen:
                # If number is already in set, it's a duplicate
                return True
            seen.add(num)  # Add number to the set if it's not already present

        return False  # No duplicates found, return False

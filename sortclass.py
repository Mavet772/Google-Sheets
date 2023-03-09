
class Array(object):
    
    def __init__(self, initialSize):
        # Constructor
        self.__a = [None] * initialSize # The array stored as a list
        self.__nItems = 0 # No items in array initially

    def __len__(self):
        # Special def for len() func
        return self.__nItems # Return number of items

    def get(self, n):
        # Return the value at index n
        if 0 <= n and n < self.__nItems:
            # Check if n is in bounds, and
            return self.__a[n] # only return item if in bounds

    def set(self, n, value):
        # Set the value at index n
        if 0 <= n and n < self.__nItems:
            # Check if n is in bounds, and
            self.__a[n] = value # only set item if in bounds

    def swap(self, j, k):
        # Swap the values at 2 indices
        if (0 <= j and j < self.__nItems and # Check if indices are in bounds, before processing
            0 <= k and k < self.__nItems):
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):
        # Insert item at end
        if self.__nItems >= len(self.__a):
            # If array is full, raise exception
            raise Exception("Array overflow")
        self.__a[self.__nItems] = item # Item goes at current end
        self.__nItems += 1 # Increment number of items

    def find(self, item):
        # Find index for item
        for j in range(self.__nItems): # Among current items
            if self.__a[j] == item: # If found, then return index to element
                return j
        return -1 # Not found -> return -1

    def search(self, item):
        # Search for item and return item if found
        return self.get(self.find(item))

    def delete(self, item):
        # Delete first occurrence of an item
        for j in range(self.__nItems): # of an item
            if self.__a[j] == item: # Found item
                self.__nItems -= 1 # One fewer at end
                for k in range(j, self.__nItems): # Move items from right over 1
                    self.__a[k] = self.__a[k+1]
                return True # Return success flag
        return False # Made it here, so couldn't find the item

    def traverse(self, function=print):
        # Traverse all items and apply a function
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):
        # Special def for str() func
        ans = "[" # Surround with square brackets
        for i in range(self.__nItems): # Loop through items
            if len(ans) > 1: # Except next to left bracket, separate items with comma
                ans += ", "
            ans += str(self.__a[i]) # Add string form of item
        ans += "]" # Close with right bracket
        return ans

    def bubbleSort(self):               # Sort comparing adjacent vals
      for last in range(self.__nItems-1, 0, -1):  # and bubble up
         for inner in range(last):     # inner loop goes up to last
            if self.__a[inner] > self.__a[inner+1]:  # If item less
               self.swap(inner, inner+1)
                    

    def selectionSort(self): # Sort by selecting min and swapping min to leftmost
        for outer in range(self.__nItems-1):
            min = outer # Assume min is leftmost
            for inner in range(outer+1, self.__nItems): # Hunt to right
                if self.__a[inner] < self.__a[min]: # If we find new min, update the min index
                    min = inner # __a[min] is smallest among __a[outer]...__a[__nItems-1]
            self.swap(outer, min) # Swap leftmost and min

    def insertionSort(self): # Sort by repeated inserts
        for outer in range(1, self.__nItems): # Mark one element
            temp = self.__a[outer] # Store marked elem in temp
            inner = outer # Inner loop starts at mark
            while inner > 0 and temp < self.__a[inner-1]: # If marked elem smaller, then shift elem to right
                self.__a[inner] = self.__a[inner-1]
                inner -= 1
            self.__a[inner] = temp # Move marked elem to 'hole'
            
    
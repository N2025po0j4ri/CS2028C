## Project 3: Bloom Filters ##

_author_ = "Nirupama Poojari"
_credits_ = ["Your list of helpers"]
_email_ = "poojarna@mail.uc.edu"  # Your email address

'''
You should test a Bloom Filter of size 1000,
a sample_data set of at least 500 words,
and a test_data of at least 500 false members.
'''
from bloom_filter import BloomFilter


sample_data = ["apple", "banana", "grape", "orange", "strawberry", "blueberry", "kiwi",
               "watermelon", "pineapple", "pear", "peach", "plum", "cherry", "melon",
               "lemon", "lime", "mango", "papaya", "apricot", "avocado", "coconut", "fig",
               "nectarine", "tangerine", "cranberry", "raspberry", "blackberry", "grapefruit",
               "dragonfruit", "guava", "lychee", "persimmon", "pomegranate", "quince", "starfruit",
               "passionfruit", "durian", "date", "elderberry", "boysenberry", "mulberry",
               "currant", "gooseberry", "kumquat", "rhubarb", "plantain", "jackfruit",
               "breadfruit", "cherimoya", "sapodilla", "salak", "tamarind", "ugli fruit"] * 10

# Creating test data with 500 words containing some fruit words
test_data = ["table", "chair", "lamp", "book", "pen", "computer", "keyboard", "monitor",
             "desk", "clock", "matches", "guitar", "piano", "violin", "trumpet", "drum",
             "tangerine", "speaker", "headphone", "kiwi", "television", "remote", "charger",
             "battery", "wallet", "bag", "shoe", "hat", "jacket", "coat", "dress", "shirt",
             "pants", "shorts", "coconut", "scarf", "glove", "umbrella", "belt", "tie", "watch",
             "ring", "bracelet", "necklace", "earrings", "sunglasses", "apple", "soap", "shampoo",
             "toothbrush", "toothpaste", "towel", "mirror", "brush", "comb", "scissors", "orange",
             "spoon", "fork", "plate", "bowl", "cup", "glass", "mug", "napkin", "straw"] * 10

# Initialize the Bloom Filter
bloom = BloomFilter(size=1000, hash_count=2)  # Using size 1000 as per the requirement
for item in sample_data:
    bloom.add(item)

# Test the Bloom Filter
results = {item: bloom.check(item) for item in test_data}

# Calculate the false positive rate
false_positives = sum(1 for item in test_data if item not in sample_data and bloom.check(item))
false_positive_rate = false_positives / len(test_data)

# Output results in specified format
print("Bloom Filter Configuration:")
print(f" Size: {1000}")  # Fixed size as per the requirement
print(f" HashCount: {2}")  # Fixed hash count as per the requirement
print()
print(f"  Sample Data: {sample_data} (or filename)")  # Assuming filename output as per the example
print()
print(f"  Test Data: {test_data} (or filename)")  # Assuming filename output as per the example
print()
print("  Results:", end=" ")
for item in results:
    print(f"{item}: {results[item]}", end=" ")
print(f"\n  False Positive Rate: {false_positive_rate:.2f}")

print("############################################################")

'''
Vary the number of hash functions from 2 to 10.
Analyze the false_positive rate for each?
'''
sample_data2 = ["apple", "banana", "grape", "orange", "strawberry"]
test_data2 = ["apple", "banana", "grape", "watermelon", "pineapple"]

# Analyze the false positive rate for hash counts from 2 to 10 and size from 2 to 10:
for size in range(2, 11):
    for hash_count in range(2, 11):
        bloom = BloomFilter(size=size, hash_count=hash_count)
        for item in sample_data2:
            bloom.add(item)

        # Test the Bloom Filter and calculate false positives:
        false_positives = sum(1 for item in test_data2 if item not in sample_data2 and bloom.check(item))
        false_positive_rate = false_positives / len(test_data2)

        # Print with a new line before size changes
        if hash_count == 2:
            print()  # Start with a new line for each new size
        print(f"Size: {size}, Hash Count: {hash_count}, False Positive Rate: {false_positive_rate:.2f}")
        
'''
Note: The formatting needs to be fixed ASAP before the deadline.
'''

print("############################################################")


# Initialize the Bloom Filter with size 5 and hash_count 2 for sample_data3
sample_data3 = ["apple", "banana", "grape", "orange", "strawberry"]
test_data3 = ["apple", "banana", "grape", "watermelon", "pineapple"]

bloom = BloomFilter(size=5, hash_count=2)
for item in sample_data3:
    bloom.add(item)

# Test the Bloom Filter and calculate false positives
results = {item: bloom.check(item) for item in test_data3}
false_positives = sum(1 for item in test_data3 if item not in sample_data3 and bloom.check(item))
false_positive_rate = false_positives / len(test_data3)

# Output results for the Bloom Filter with size 5 and hash_count 2
print("\nBloom Filter Configuration:")
print(f" Size: {bloom.size}")
print(f" HashCount: {bloom.hash_count}")
print(f" Sample Data: {sample_data3}")
print(f" Test Data: {test_data3}")
print(" Results:", end=" ")
for item in results:
    print(f"{item}: {results[item]}", end=" ")
print(f"\n False Positive Rate: {false_positive_rate:.2f}")
print("############################################################")

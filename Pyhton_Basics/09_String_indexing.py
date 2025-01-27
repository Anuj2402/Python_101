# string Indexing -> is a way to access the characters in a string using their position .
# using the index operator [].
#                -> Syntax -> string[index]
#                -> [start:End:step] -> start -> starting index, end -> ending index, step -> step size
        #          starting index is inclusive and ending index is exclusive
#                -> Example -> "Hello"[0] -> "H"

credits_number = "1234-5678-9012-3456";

print(credits_number[0]); #1
print(credits_number[4]); #-
print(credits_number[:4]); #1234
print(credits_number[5:]); #5678-9012-3456
print(credits_number[5:9]); #5678
print(credits_number[5:9:2]); #57
print(credits_number[-1]); #6
print(credits_number[-4]); #5
print(credits_number[-4:]); #3456
print(credits_number[-4:-1]); #345  starting index is inclusive and ending index is exclusive
print(credits_number[-4:-1:2]); #35
credits_number = credits_number[::-1]; #Reverse the string
print(credits_number); #6543-2109-8765-4321


lst = input("enter elements separated by space ").split()
d = {}
keys = int(input("enter the no of keys"))
for _ in range(keys):
    key = input("key ")
    value = input("value ")
    d[key] = value
searchElem = input("Enter the key to search: ")
if searchElem in lst and searchElem in d:
    print(f"{searchElem} from {d[searchElem]}")
else:
    print(f"Key '{searchElem}' is not present in both list and dictionary.")

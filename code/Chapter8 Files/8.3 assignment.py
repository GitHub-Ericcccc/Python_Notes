# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fh = open('mbox.txt')

count = 0
num = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.strip()
    str = line[-6:]
    num = float(str)
    print(num)
    count = count + 1
print(count)
print("Done")


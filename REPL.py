# how to break out of a while loop before it runs again

while True:
        response = input()
        if int(response) % 7 == 0:
                break
print("broken!")
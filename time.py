# Input Variables
currentTimeStr = int(input("What is the current time (in hours 0-24)?"))  # string was fixed when we added int
waitTimeStr = int(input("How many hours do you want to wait?"))  # string wasn't fixed when we added int

# Calculate the final time
finalTimeInt = (currentTimeStr + waitTimeStr)

# Print the output
finalTimeInt = currentTimeStr + waitTimeStr
print("The current time after you waited is", finalTimeInt)  # Fixed name error and also string

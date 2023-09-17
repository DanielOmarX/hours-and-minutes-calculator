print("Welcome to the hours and minutes calculator")

second = int(input("Enter Your duration in seconds: \n"))
Hours = second // 3600
Minutes = (second % 3600) // 60
remaing_second = second % 60
print( f"The duratoin is :{Hours} Hours, {Minutes} Minutes, and {remaing_second} seconds")

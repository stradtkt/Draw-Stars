def draw_stars(arr):
  for x in arr:
    print("*"*x)

nums = [6,2,5,7,9]
draw_stars(nums)

def draw_stars2(arr):
  #loop through the items in the list which is also an array of items
  for x in arr:
    if isinstance(x, int):
      #print the amount of * that the number is
      print("*"*x)
    elif isinstance(x, str):
      #getting the len() of x which is the item in the list and then setting it to length
      length = len(x)
      #getting the first letter from x which is the item in the list
      letter = x[0].lower()
      # printing the letter times the length of the item in the list
      print(letter * length)
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x)

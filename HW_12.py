# 1
my_img = ('1920', '1080')

info = f"{my_img[0]}x{my_img[1]}" if len(
    my_img) == 2 else "Incorrect image formatting"
print(info)
# 1920x1082

# 2
my_image = ('1920', '1080')

if len(my_image) == 2:
    info = f"{my_image[0]}x{my_image[1]}"
else:
    info = "Incorrect image formatting"
print(info)
# 1920x1080

# 3
my_str = "The weather is fine and we'r gonna visit our friends and comreads at the seaside"

print("The string is long") if len(my_str) >= 100 else print(
    "The string is short")
#  The string is short

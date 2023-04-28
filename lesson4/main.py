# class CustomException(Exception):
#     def __init__(self, message='it is my custom ex',*args: object) -> None:
#         super().__init__(*args)
#         self.message=message
#     def __str__(self) -> str:
#         return self.message
# raise CustomException()
def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
      
    while number:
        div = number // num[i]
        number %= num[i]
  
        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1
dict_rom_to_arab={'I':1,'V':5,'X':10}

def from_roman_to_arab(roman,d):
    temp_arr=list(roman)
    print(temp_arr)
    arr_res=[]
    for i in temp_arr:
        arr_res.append(d[i])
    i=len(arr_res)-1
    while i !=0:
        if arr_res[i] > arr_res[i-1]: 
            arr_res[i-1]=-arr_res[i-1]
        i-=1
    return sum(arr_res)
print(from_roman_to_arab('XXIV',dict_rom_to_arab))
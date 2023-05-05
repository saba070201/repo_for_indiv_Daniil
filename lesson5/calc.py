# import json
# with open('lesson5/metrospb.json','r',encoding='UTF-8') as f:
#     data=json.load(f)
#     print(data['stations'][0]['name'])
from bidict import bidict

class RomanValueError(Exception):
    def __init__(self,message) -> None:
       self.message=message
    def __str__(self) :
        return self.message

class Mathes:
    @staticmethod
    def get_matches():
        return bidict({'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000})
    

class Converter:
    @staticmethod
    def from_arab_to_roman(value):
        value=str(value)
        value=[i for i in value]
        ms=Mathes.get_matches()
        romans = list([ i for i in ms])
        str_arabic = value[::-1]
        str_arabic_len = len(str_arabic)
        result = str()
        romans_pointer = 0
        for i in range(str_arabic_len):
            if str_arabic[i] in ['0', '1', '2', '3']:
                result = romans[romans_pointer] * int(str_arabic[i]) + result
            elif str_arabic[i] in ['4']:
                result = romans[romans_pointer] + romans[romans_pointer + 1] + result
            elif str_arabic[i] in ['5', '6', '7', '8']:
                result = romans[romans_pointer + 1] + romans[romans_pointer] * (int(str_arabic[i]) - 5) + result
            elif str_arabic[i] in ['9']:
                result = romans[romans_pointer] + romans[romans_pointer + 2] + result
            romans_pointer += 2
        return result
    @staticmethod
    def from_roman_to_arab(roman):
        temp_arr=list(roman)
       
        arr_res=[]
        for i in temp_arr:
            arr_res.append(Mathes.get_matches()[i])
        i=len(arr_res)-1
        while i !=0:
            if arr_res[i] > arr_res[i-1]: 
                arr_res[i-1]=-arr_res[i-1]
            i-=1
        return sum(arr_res)


class RomanValue:
    def check(self,value):
        counter=1
        for i in range(len(value)):
            if value[i] not in Mathes.get_matches():
                return False
            if i >0:
              if value[i-1]==value[i]:
                  counter+=1
              else : 
                  counter=1
            if counter>3:
                return False
        return True
    def __init__(self,value):
        if isinstance(value,int):
            self.romanvalue=Converter.from_arab_to_roman(value)
            self.arabicvalue=value
        elif isinstance(value,str):
            if self.check(value): 
                self.romanvalue=value
                self.arabicvalue=Converter.from_roman_to_arab(value)
            else:
                raise RomanValueError('incorrect value')
    def __add__(self,other):
        if isinstance(other,int):
            return other + self.arabicvalue
        elif isinstance(other,RomanValue):
            return RomanValue(self.arabicvalue+other.arabicvalue)
        else:
            raise RomanValueError('unsupported opperand')
    def __eq__(self,other):
        if isinstance(other,int):
            if other == self.arabicvalue:
                return True
            else:
                return False
        elif isinstance(other,RomanValue):
            if other.arabicvalue == self.arabicvalue:
                return True
            else:
                return False
        else:
            raise RomanValueError('unsupported opperand')
    def __str__(self):
        return f'{self.romanvalue=} {self.arabicvalue=}'
    def __truediv__(self,other):
        if isinstance(other,int):
              return  self.arabicvalue//other
        elif isinstance(other,RomanValue):
            return RomanValue(self.arabicvalue//other.arabicvalue)
        else:
            raise RomanValueError('unsupported opperand')
rv=RomanValue('III')
rv1=RomanValue('X')
res=RomanValue(rv+10)
print(rv1/rv)
print(res)



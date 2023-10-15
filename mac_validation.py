import re
def mac_validation(addr):
    match=re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$",addr)
    if match:
        return True
    return False
    
print(mac_validation("12-34-aa-32-33-55"))
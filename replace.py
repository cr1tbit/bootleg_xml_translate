import re
import sys,os

'''
THIS IS FUN
cat * | sed 's/./&\n/g' | LC_COLLATE=C sort -u | tr -d '\n'                                      
 !"()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]_
 `abcdefghijklmnopqrstuvwxyz~çêñзийкрсуыя""←、。
 东中乌乡京他仡仫伦伯体佤佬侗依俄保傈傣僳克其别南古吉吾哈
 哲回固土基塔壮孜安家尔尼山巴布彝德怒拉撒文斡斯族日昂昌春
 普景朗朝本柯毛民水汉温满独珞瑶畲白祜简米繁纳维罗羌苗萨蒙
 藏裕西語诺赫达鄂锡门阿颇體高鲜黎龙국어한！，：？%
'''

def translate_text(text:str)->str:
    stream = os.popen(f'trans -brief :pl "{text}"')
    return stream.read().rstrip()

def just_text(text:str)->str:
    return f'**{text}**'

def group_operation(match:re.match) ->str:
    group = match.group(1)
    return ">" + translate_text(group) + "<\\"

return_str = ""

for line in sys.stdin: 
    return_str += re.sub(r">([a-zA-Z0-9\s\n !\"()*+,-.?\/0123456789:;！，：？%]+)<\/", group_operation, line)

print(return_str) 
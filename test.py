s="посмотрите как Рите нравится ритмично"

# for n,c in enumerate(s.lower()):
#     try:
#         if c+s[n+1] +s[n+2]== "рит":
#             print(n)
#     except: pass
#

k=s.lower()
i = 0
try:
    while i < len(k):
        i = k.find("рит", i)
        print(i)
        i +=3
except:
    pass
#
#
# print([n for n in range(len(s)) if s.find('рит', n) == n])

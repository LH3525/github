fileName = ('F:\\0005_1.txt')
# fileOut = 'F:\\file1.txt'
# # with open(fileDir1) as RF,open(fileDir2) as WF:
# #     print(RF.read().splitlines())
# def putInfoToDict(filename):
#     with open(filename) as RF, open(fileOut) as WF:
#         lines = RF.read().splitlines()#(',\n')
#         # print(lines)
#         #
#
#         # for line in lines:
#         #     if line == '':
#         #         continue
#         #     else:
#         #         key = line[-4:-1]
#         #     if
#         #     print(line)
#         #

def putInfoToDict(fileName):
    retDict = {}
    with open(fileName) as f:
        lines = f.read().splitlines()
        for line in lines:
            # remove '(' and ')'
            line = line.replace('(', '').replace(')', '').replace(';', '').strip()
            print(line)

#             parts = line.split(',')
#             ciTime = parts[0].strip().replace("'", '')
#             lessonid = int(parts[1].strip())
#
#             userid = int(parts[2].strip())
#
#             toAdd = {'lessonid': lessonid, 'checkintime': ciTime}
#             # if not in, need to create list first
#             if userid not in retDict:
#                 retDict[userid] = []
#             retDict[userid].append(toAdd)
#
#             # or just
#             # retDict.setdefault(userid,[]).append(toAdd)
#
#     return retDict
#
# ret = putInfoToDict('F:\\0005_1.txt')
#
# import pprint
#
# pprint.pprint(ret)
#
putInfoToDict(fileName)


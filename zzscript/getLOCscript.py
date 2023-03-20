cProgramList="/home/yantingchi/Desktop/Lab/indirectCall/OSS-Fuzz/myStuff/resultWithCProgram"
testList="/home/yantingchi/Desktop/Lab/indirectCall/OSS-Fuzz/oss-fuzz/testCProg"
cProgramFile=open(cProgramList, "r")
githubResult=[]
notGithubResult=[]
resultFile=open("/home/yantingchi/Desktop/Lab/indirectCall/OSS-Fuzz/oss-fuzz/repoResult",'w')
for line in cProgramFile.readlines():
    place=line.find(":")
    yamlFilePath=line[0:place]
    yamlFilePath=("/home/yantingchi/Desktop/Lab/indirectCall/OSS-Fuzz/oss-fuzz/projects/")+yamlFilePath
    with open(yamlFilePath,'r') as yamlFile:
        for subLine in yamlFile.readlines():
            if "main_repo" in subLine:
                pos=subLine.find("github.com/")
                endPos=subLine.rfind('\'')
                if(endPos==-1):
                    endPos=subLine.rfind('\"')
                if(pos==-1):
                    notGithubResult.append(subLine[12:-2])
                else:
                    if(subLine.find(".git")!=-1):
                        endPos-=4
                    realPos=pos+11
                    print(subLine[realPos:endPos])
                    githubResult.append(subLine[realPos:endPos])
print(len(githubResult))
for item in githubResult:
    resultFile.write(item+'\n')
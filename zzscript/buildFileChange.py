# sudo python3 infra/helper.py check_build json-c
# search for all the files and add for all the files 
import os
OSS_Path="/home/yantingchi/Desktop/Lab/indirectCall/OSS-Fuzz/oss-fuzz"
pathTemplate=OSS_Path+"/projects/{}/build.sh"
pathOldTemplate=OSS_Path+"/projects/{}/build.sh.old"
cFile=OSS_Path+"/zzscript/appList"
cFile=open(cFile,'r')
names=[]
for line in cFile.readlines():
    names.append(line[:-1])

def phase1():

    # read and rewrite the build files
    lines='''
CFLAGS="-O1 -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION -fsanitize=cfi-icall -flto -fvisibility=hidden -fno-sanitize-trap=all  -fuse-ld=lld"
CXXFLAGS="-O1 -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION -fsanitize=cfi-icall -flto -fvisibility=hidden -fno-sanitize-trap=all  -stdlib=libc++ -fuse-ld=lld"
    '''
    for item in names:
        path=pathTemplate.format(item)
        pathOld=pathOldTemplate.format(item)
        try:
            os.system("cp {} {}".format(pathOld, path))
        except:
            print(item)
            os.system("cp {} {}".format(path, pathOld))
        try:
            with open(path, 'r+') as f:   
                content=f.read()
                f.seek(0,0)
                f.write("#!/bin/bash -eu"+lines.rstrip('\r\n')+'\n'+content)
        except FileNotFoundError:
            print(path)
phase1()
## phase2 build automatically 
# appNames=[]
# outputRecord=open("/home/yantingchi/Desktop/Lab/indirectCall/OSS-Fuzz/oss-fuzz/analyzeResult","w")
# for item in directory:
#     nameLoc=item.rfind('/')
#     appNames.append(item[nameLoc+1:])
# print(appNames)
# commandTemplate="time python3 infra/helper.py build_fuzzers {} --sanitizer address --engine afl"
# for name in appNames:
#     command=commandTemplate.format(name)
#     os.system(command)
#     outputRecord.write(name+'\n')
'''
./projects/uriparser/project.yaml:language: c++
./projects/json-c/project.yaml:language: c++
./projects/rocksdb/project.yaml:language: c++
./projects/grpc/project.yaml:language: c++
./projects/librawspeed/project.yaml:language: c++
./projects/glib/project.yaml:language: c++
./projects/dng_sdk/project.yaml:language: c++
./projects/vorbis/project.yaml:language: c++
./projects/freeradius/project.yaml:language: c++
./projects/trafficserver/project.yaml:language: c++
./projects/lzma/project.yaml:language: c++
./projects/xmlsec/project.yaml:language: c++
./projects/lldb-eval/project.yaml:language: c++
./projects/skia/project.yaml:language: c++
./projects/libsodium/project.yaml:language: c++
./projects/proxygen/project.yaml:language: c++
./projects/jansson/project.yaml:language: c++
./projects/speex/project.yaml:language: c++
./projects/xz/project.yaml:language: c++
./projects/libigl/project.yaml:language: c++
./projects/geos/project.yaml:language: c++
./projects/skcms/project.yaml:language: c++
./projects/num-bigint/project.yaml:language: c++
./projects/nghttp2/project.yaml:language: c++
./projects/libpng-proto/project.yaml:language: c++
./projects/cpp-httplib/project.yaml:language: c++
./projects/qpdf/project.yaml:language: c++
./projects/wget2/project.yaml:language: c++
./projects/graphicsfuzz-spirv/project.yaml:language: c++
./projects/piex/project.yaml:language: c++
./projects/radare2/project.yaml:language: c++
./projects/fmt/project.yaml:language: c++
./projects/libidn2/project.yaml:language: c++
./projects/jsoncons/project.yaml:language: c++
./projects/wabt/project.yaml:language: c++
./projects/libexif/project.yaml:language: c++
./projects/solidity/project.yaml:language: c++
./projects/xerces-c/project.yaml:language: c++
./projects/curl/project.yaml:language: c++
./projects/openweave/project.yaml:language: c++
./projects/openjpeg/project.yaml:language: c++
./projects/cryptofuzz/project.yaml:language: c++
./projects/poppler/project.yaml:language: c++
./projects/libxls/project.yaml:language: c++
./projects/http-parser/project.yaml:language: c++
./projects/cfengine/project.yaml:language: c++
./projects/uwebsockets/project.yaml:language: c++
./projects/php/project.yaml:language: c++
./projects/libarchive/project.yaml:language: c++
./projects/tpm2-tss/project.yaml:language: c++
./projects/neomutt/project.yaml:language: c++
./projects/leveldb/project.yaml:language: c++
./projects/bitcoin-core/project.yaml:language: c++
./projects/cras/project.yaml:language: c++
./projects/htslib/project.yaml:language: c++
./projects/libvnc/project.yaml:language: c++
./projects/c-ares/project.yaml:language: c++
./projects/proj4/project.yaml:language: c++
'''
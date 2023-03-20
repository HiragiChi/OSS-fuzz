import subprocess
import json
import time
testFile=open("/home/yantingchi/Desktop/Lab/indirectCall/OSS-Fuzz/oss-fuzz/testCProg",'r')
realFile=open("/home/yantingchi/Desktop/Lab/indirectCall/OSS-Fuzz/oss-fuzz/repoResult")

commandProto="https://api.codetabs.com/v1/loc?github="

for line in realFile.readlines():
    try:
        command=commandProto+line[:-1]
        returnJson=subprocess.check_output(["GET",command])
        
        returnDict=json.loads(returnJson)
        result=[]
        result.append(line[:-1])
        for item in returnDict:
            if (item['language']=='C' or item['language']=='C Header' or item['language']=="C++" ):
                result.append(item['language'])
                result.append(item['linesOfCode'])
        print(result)
    except:
        print(line[:-1],returnDict)
        time.sleep(5)

'''
json-c/json-c
facebook/rocksdb
grpc/grpc
darktable-org/rawspeed
FreeRADIUS/freeradius-server
apache/trafficserver
apache/httpd
lsh123/xmlsec
google/lldb-eval
zyantific/zydis
uber/h3
jedisct1/libsodium
facebook/proxygen
akheron/jansson
stephane/libmodbus
libigl/libigl
rust-num/num-bigint
nghttp2/nghttp2
yhirose/cpp-httplib
nginx/unit
qpdf/qpdf
coturn/coturn
guidovranken/piex
radareorg/radare2
fmtlib/fmt
danielaparker/jsoncons
WebAssembly/wabt
libexif/libexif
ethereum/solidity
curl/curl
openweave/openweave-core
uclouvain/openjpeg
guidovranken/cryptofuzz
libxls/libxls
nodejs/http-parser
cfengine/core
OpenPrinting/cups
uNetworking/uWebSockets
'''
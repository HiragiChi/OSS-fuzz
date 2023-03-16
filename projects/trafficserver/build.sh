#!/bin/bash -eu
CFLAGS="-O1 -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION -fsanitize=cfi-icall -flto -fvisibility=hidden -fno-sanitize-trap=all -fsanitize-recover=all -fuse-ld=lld"
CXXFLAGS="-O1 -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION -fsanitize=cfi-icall -flto -fvisibility=hidden -fno-sanitize-trap=all -fsanitize-recover=all  -stdlib=libc++ -fuse-ld=lld"
#!/bin/bash -eu
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################
autoreconf -if
./configure --enable-debug
make -j$(nproc) --ignore-errors

pushd fuzzer/
make
cp FuzzEsi $OUT/FuzzEsi
#cp FuzzHTTP $OUT/FuzzHTTP
popd

pushd $SRC/oss-fuzz-bloat/trafficserver/
cp FuzzEsi_seed_corpus.zip $OUT/FuzzEsi_seed_corpus.zip
cp FuzzHTTP_seed_corpus.zip $OUT/FuzzHTTP_seed_corpus.zip
popd

mkdir $OUT/lib
cp src/tscore/.libs/libtscore.so* $OUT/lib/.
cp src/tscpp/util/.libs/libtscpputil.so* $OUT/lib/.

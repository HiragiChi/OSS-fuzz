#!/bin/bash -eu
CFLAGS="-O1 -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION -fsanitize=cfi-icall -flto -fvisibility=hidden -fno-sanitize-trap=all -fsanitize-recover=all -fuse-ld=lld"
CXXFLAGS="-O1 -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION -fsanitize=cfi-icall -flto -fvisibility=hidden -fno-sanitize-trap=all -fsanitize-recover=all  -stdlib=libc++ -fuse-ld=lld"
#!/bin/bash -eu
# Copyright 2023 Google LLC
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

cmake . -DSTATIC_ONLY=ON -DICAL_GLIB=False
make install -j$(nproc)


$CXX $CXXFLAGS -std=c++11 $SRC/libical_fuzzer.cc $LIB_FUZZING_ENGINE /usr/local/lib/libical.a -o $OUT/libical_fuzzer
$CXX $CXXFLAGS -std=c++11 $SRC/libical_extended_fuzzer.cc $LIB_FUZZING_ENGINE /usr/local/lib/libical.a -o $OUT/libical_extended_fuzzer

find . -name *.ics -print | zip -q $OUT/libical_fuzzer_seed_corpus.zip -@

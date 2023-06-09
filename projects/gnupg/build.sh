#!/bin/bash -eu
CFLAGS="-O1 -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION -fsanitize=cfi-icall -flto -fvisibility=hidden -fno-sanitize-trap=all -fsanitize-recover=all -fuse-ld=lld"
CXXFLAGS="-O1 -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION -fsanitize=cfi-icall -flto -fvisibility=hidden -fno-sanitize-trap=all -fsanitize-recover=all  -stdlib=libc++ -fuse-ld=lld"
#!/bin/bash -eu
# Copyright 2018 Google Inc.
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

#compile and link statically dependencies
cd ..
cd libgpg-error
sed -i 's/0.19/0.20/g' ./po/Makefile.in.in
./autogen.sh
./configure --disable-doc --enable-static --disable-shared
make
make install
cd ..
cd libgcrypt
./autogen.sh
./configure --disable-doc --enable-static --disable-shared
make
make install
cd ..
cd libassuan
./autogen.sh
./configure --disable-doc --enable-static --disable-shared
make
make install
cd ..
cd libksba
./autogen.sh
./configure --disable-doc --enable-static --disable-shared
make
make install
cd ..
cd npth
./autogen.sh
./configure --disable-doc --enable-static --disable-shared
make
make install
cd ..


# build project
cd gnupg
mkdir tests/fuzz
cp ../fuzz_* tests/fuzz
git apply ../fuzz.diff
./autogen.sh
./configure --disable-doc --enable-maintainer-mode
make -j$(nproc) all

# build fuzzers
cd tests/fuzz
# export fuzzers and other associated stuff
cp fuzz_* $OUT/

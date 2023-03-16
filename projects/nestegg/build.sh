#!/bin/bash -eu
CFLAGS="-O1 -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION -fsanitize=cfi-icall -flto -fvisibility=hidden -fno-sanitize-trap=all -fsanitize-recover=all -fuse-ld=lld"
CXXFLAGS="-O1 -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION -fsanitize=cfi-icall -flto -fvisibility=hidden -fno-sanitize-trap=all -fsanitize-recover=all  -stdlib=libc++ -fuse-ld=lld"
#!/bin/bash -eu

$CC $CFLAGS -c -I./include src/nestegg.c
$CXX $CXXFLAGS -o $OUT/fuzz -I./include nestegg.o test/fuzz.cc $LIB_FUZZING_ENGINE


mkdir corpus/
cp -R ../testdata/*.webm corpus/
cp test/media/*.webm corpus/
zip -rj0 $OUT/fuzz_seed_corpus.zip corpus/*.webm

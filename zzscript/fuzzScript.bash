#!/bin/bash
# programName=$1
# python3 infra/helper.py build_fuzzers $programName --engine afl
# python3 python3 infra/helper.py build_image $programName
# python3 infra/helper.py run_fuzzer --corpus-dir=<path-to-temp-corpus-dir> $PROJECT_NAME <fuzz_target> —engine afl
projectName=$1
fuzzTarget=$2
if test "$#" -eq 4; then
    corpusDir=$3
    python3 ../infra/helper.py run_fuzzer --corpus-dir=$corpusDir $1 $2 —engine afl
else
    python3 ../infra/helper.py run_fuzzer $1 $2 --engine afl
fi

#!/bin/bash
programName=$1
python3 ../infra/helper.py build_fuzzers $programName --engine afl 2>&1 | tee ./result/$programName.buildLog
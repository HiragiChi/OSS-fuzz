#!/bin/bash
programName=$1
python3 ../infra/helper.py build_image $programName 2>&1 | tee ./result/$programName.buildLog
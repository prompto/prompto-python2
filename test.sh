#!/usr/bin/env bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/Python2-Core/src/generated
export PYTHONPATH=$PYTHONPATH:$(pwd)/Python2-Core/src/main
nosetests --exe --with-xunit --xunit-file=testResults1.xml Python2-Core/src/test/prompto/
export PYTHONPATH=$PYTHONPATH:$(pwd)/Python2-Runtime/src/main
export PYTHONPATH=$PYTHONPATH:$(pwd)/Python2-Core/src/test
nosetests --exe --with-xunit --xunit-file=testResults2.xml Python2-Runtime/src/test/
python readXUnitTestResults.py testResults1.xml testResults2.xml
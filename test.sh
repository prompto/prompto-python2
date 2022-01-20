#!/usr/bin/env bash
ls -all
echo "PYTHONPATH" $PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$CIRCLE_WORKING_DIRECTORY/Python2-Core/src/generated
export PYTHONPATH=$PYTHONPATH:$CIRCLE_WORKING_DIRECTORY/Python2-Core/src/main
echo "PYTHONPATH" $PYTHONPATH
nosetests --exe --with-xunit --xunit-file=testResults1.xml Python2-Core/src/test/prompto/
echo "PYTHONPATH" $PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$CIRCLE_WORKING_DIRECTORY/Python2-Runtime/src/main
export PYTHONPATH=$PYTHONPATH:$CIRCLE_WORKING_DIRECTORY/Python2-Core/src/test
echo "PYTHONPATH" $PYTHONPATH
nosetests --exe --with-xunit --xunit-file=testResults2.xml Python2-Runtime/src/test/
python readXUnitTestResults.py testResults1.xml testResults2.xml
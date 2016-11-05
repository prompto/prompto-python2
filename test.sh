export PYTHONPATH=$PYTHONPATH:$TRAVIS_BUILD_DIR/Python2-Core/src/generated
export PYTHONPATH=$PYTHONPATH:$TRAVIS_BUILD_DIR/Python2-Core/src/main
nosetests --exe Python2-Core/src/test/prompto/
export PYTHONPATH=$PYTHONPATH:$TRAVIS_BUILD_DIR/Python2-Runtime/src/main
export PYTHONPATH=$PYTHONPATH:$TRAVIS_BUILD_DIR/Python2-Core/src/test
nosetests --exe Python2-Runtime/src/test/

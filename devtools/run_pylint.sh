echo "Running Pylint on settings defined in pylintrc..."
pylint ../desc  ../tests > "pylint.output"
echo "Done!"
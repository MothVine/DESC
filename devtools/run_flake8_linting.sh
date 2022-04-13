rm -f flake8.output

echo "Running Flake8 using settings defined in settings.cfg..."
flake8 --config ../settings.cfg --output-file flake8_errors.output ../desc/ ../tests/

echo "Generating Flake8 report..."
flake8 --config ../settings.cfg -qqq --statistics --output-file flake8_summary.output ../desc/ ../tests/
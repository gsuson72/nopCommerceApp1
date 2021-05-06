rem pytest -v -s testCases\test_login.py --browser chrome
rem pytest -v -s testCases\test_login.py --browser firefox
rem pytest -v -s  -n=2 testCases/test_login.py --browser firefox
pytest -v --capture=tee-sys -n=2 --html=Reports\report.html testCases\test_login.py --browser chrome
rem pytest -v --capture=tee-sys --html=Reports\report.html testCases\test_addCustomer.py --browser chrome
rem pytest -v --capture=tee-sys -m "sanity" --html=Reports\report.html testCases\ --browser chrome

# -*- coding:utf-8 -*-																		
# Author : 小吴老师                                                                        
# Data ：2019/7/12 7:41                                                                    
from tools.os import shell_tool
import pytest
                                                                                           
if __name__ == '__main__':                                                                 
    # 修改成要执行的测试用例                                                               
    # test_case = './test_case/test_hello.py'
    test_case = './test_case/request_demo/test_request.py'
                                                                                           
    xml_report_path = './reports/xml/'                                                     
    html_report_path = './reports/html/'                                                   
                                                                                           
    pytest.main(['-s', '-q', '--alluredir',                                                
                 xml_report_path, test_case,"-v"])
    cmd1 = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    # cmd1 = 'allure generate reports/xml -o reports/html --clean'
    shell_tool.invoke(cmd1)

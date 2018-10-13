from appium import webdriver
import sys, getopt

def main(argv):
    '''
    命令行传参
    上海-悠悠博客：https://www.cnblogs.com/yoyoketang/
    '''
    name = "leidian" # 给个默认值

    try:
        # 这里的 h 就表示该选项无参数，n:表示 n 选项后需要有参数
        opts, args = getopt.getopt(argv, "hn:", ["name="])
    except getopt.GetoptError:
        print('Error: start.py -n <devicename>')
        print('   or: start.py --name=<devicename>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print('start.py -n <devicename>')
            print('or: start.py --name=<devicename>')
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg

    print('run device name : %s' % name)
    return name
des_leidian = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "platformVersion": "5.1.1",
                "appPackage": "com.yipiao",
                "noReset": True,
                "udid": "emulator-5554",   # 识别手机唯一标识
                "appActivity": "com.yipiao.activity.LaunchActivity"
                }

des_yeshen = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:62001",
                "platformVersion": "4.4.2",
                "appPackage": "com.yipiao",
                "udid": "127.0.0.1:62001",
                "noReset": True,
                "appActivity": "com.yipiao.activity.LaunchActivity"
                }


def start_app(n=None):
    if n == None:
        deviceName = main(sys.argv[1:])
    else:
        deviceName = n

    if deviceName == "leidian":
        des = des_leidian
    elif deviceName == "yeshen":
        des = des_yeshen
    else:
        des = des_leidian
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
    return driver

if __name__ == "__main__":
    driver = start_app()

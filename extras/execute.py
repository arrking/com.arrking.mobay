import sys, subprocess

def print_usage():
    print 'Make sure you have installed nodejs and cordova-cli. \n \
            Usage: python %s [install-plugins]' % (__file__)

plugins = ['com.ibm.mobile.cordova.ibmbluemix',
        'com.ibm.mobile.cordova.ibmpush',
        'org.apache.cordova.console',
        'org.apache.cordova.splashscreen',
        'org.apache.cordova.device',
        'org.apache.cordova.statusbar',
        'com.phonegap.plugins.barcodescanner',
        'com.ionic.keyboard',
        'org.apache.cordova.network-information',
        'org.apache.cordova.geolocation',
        'org.apache.cordova.camera',
        'https://git.oschina.net/ubiware/cordova-ios-emailcomposer.git'
        ]

def install_plugins():
    for x in plugins:
        print 'install cordova plugin %s' % (x)
        p = subprocess.Popen('grunt plugin:add:%s' % (x), shell = True)
        p.wait()

if __name__ == '__main__':
    params = sys.argv[1:]
    if len(params) == 0 : print_usage()
    if 'install-plugins' in params: install_plugins()

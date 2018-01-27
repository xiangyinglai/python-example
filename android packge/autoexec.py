import pyautogui
import time

class AutoCmd:
    def __init__(self):
        pass
    def run(self):
        cmd_list = ["adb remount",
                    "adb shell pm clear io.vsim.agent",
                    "adb shell",
                    "cd sdcard",
                    "rm -r vsim",
                    "exit",
                    "adb shell",
                    r"cd system/priv-app",
                    "rm -r Agent_v2.1.0_staging_20180118.apk",
                    "reboot",
                    "adb remount",
                    r"adb push ~desktop/Agent_v2.1.0_staging_20180118.apk/ system/priv-app",
                    r"adb push ~desktop/DZ_mtk_service_release.apk system/priv-app",
                    r"adb push ~Desktop/libvsim_tee_client.so system/lib",
                    "adb reboot"
                    ]
        pyautogui.click(100, 100)

        for cmd in cmd_list:
            pyautogui.typewrite(cmd+"\n")
            if cmd == "reboot":
                time.sleep(8)
            else:
                time.sleep(1)

if __name__ == '__main__':
    auto_write = AutoCmd()
    auto_write.run()

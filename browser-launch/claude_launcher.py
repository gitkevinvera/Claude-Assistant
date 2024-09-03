import subprocess
import time
import win32gui
import win32con
import threading
import os

def launch_chrome_kiosk_mode():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    url = "https://claude.ai/chat"
    user_data_dir = os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data\ClaudeProfile"
    chrome_options = [
        "--app=" + url,
        "--window-size=800,700",
        "--window-position=100,100",
        f"--user-data-dir={user_data_dir}",
        "--disable-extensions",
        "--disable-plugins",
        "--disable-software-rasterizer",
        "--disable-dev-tools",
        "--no-first-run",
        "--no-default-browser-check"
    ]

    try:
        subprocess.Popen([chrome_path] + chrome_options)
        print("Chrome launched successfully.")
    except Exception as e:
        print(f"Failed to launch Chrome: {e}")

def find_claude_window():
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and "Claude" in win32gui.GetWindowText(hwnd):
            hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds[0] if hwnds else None

def keep_on_top(hwnd):
    while True:
        try:
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, 
                                  win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            time.sleep(0.1)
        except:
            print("Claude window no longer exists. Stopping keep-on-top.")
            break

def main():
    launch_chrome_kiosk_mode()
    time.sleep(5)  # Wait for Chrome to start

    hwnd = find_claude_window()
    if hwnd:
        print("Claude window found. Setting always on top.")
        threading.Thread(target=keep_on_top, args=(hwnd,), daemon=True).start()
    else:
        print("Failed to find Claude window.")

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
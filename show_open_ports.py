import subprocess

def show_open_ports():
    try:
        # اجرای دستور netstat برای نمایش پورت‌های باز
        result = subprocess.run("netstat -an | findstr LISTENING", shell=True, capture_output=True, text=True)
        
        if result.stdout:
            print("Open ports:")
            print(result.stdout)
        else:
            print("No open ports found.")
    
    except Exception as e:
        print(f"Error while fetching open ports: {e}")

if __name__ == "__main__":
    show_open_ports()

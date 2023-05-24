from shadowsocks.core.config import parse_config
from shadowsocks.crypto import randombytes
import os

# مسیر فایل حاوی لینک‌های شادوساکس
input_file_path = "./links.txt"

# مسیر فایل برای ذخیره نتایج
output_file_path = "./output.txt"

# باز کردن فایل ورودی و خواندن لینک‌ها
with open(input_file_path, "r") as f:
    ss_links = [line.strip() for line in f.readlines()]

print(f"Total {len(ss_links)} links found.")

# باز کردن فایل خروجی برای نوشتن نتایج
with open(output_file_path, "w") as f:
    success_count = 0

    # تست هر لینک
    for i, link in enumerate(ss_links):
        try:
            print(f"Testing link {i+1}/{len(ss_links)}: {link}")

            # تست اتصال با حداکثر زمان انتظار ۵ ثانیه
            config = parse_config(link)
            shell.check_config(config)

            # نوشتن لینک در فایل خروجی اگر اتصال موفق بود
            f.write(f"{link}\n")
            success_count += 1
            print("Success!")
        except Exception as e:
            print(f"Error: {str(e)}")

    print(f"Testing finished. {success_count} links succeeded.")

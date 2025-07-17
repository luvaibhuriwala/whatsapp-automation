# whatsapp-automation
Send bulk messages through whatsapp
Here’s a professional and well-structured `README.md` file tailored for your WhatsApp automation script using Selenium and Python:

# 📲 WhatsApp Bulk Messenger using Selenium & Python

This project automates the process of sending personalized WhatsApp messages to multiple contacts using **Selenium WebDriver** and **WhatsApp Web**.

> ⚠️ **Note:** This script is for educational purposes only. Use it responsibly and respect WhatsApp's [terms of service](https://www.whatsapp.com/legal/terms-of-service).

---

## 🚀 Features

- Automatically reads contacts from an Excel file.
- Sends customized messages to each contact via WhatsApp Web.
- Adds country code if missing.
- Implements retries and random delays to avoid detection.
- Supports multiline messages.

---

## 🧰 Requirements

- Python 3.7+
- Google Chrome
- WebDriver Manager (automatically installs the right `chromedriver`)

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/luvaibhuriwala/whatsapp-automation.git
cd whatsapp-automation
````

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Prepare your Excel file:**

Create a file named `Book1.xlsx` with the following columns (can be adjusted as per requirement):

| Name     | Contact    | Amount | Time   |
| -------- | ---------- | ------ | ------ |
| John Doe | 3001234567 | 500    | 2 days |

> The `Contact` number should be without the country code (e.g., `3001234567`). The script will automatically add `+92` if missing.

---

## 🧪 Usage

1. Run the script:

```bash
python whatsapp.py
```

2. A Chrome browser will open with WhatsApp Web.

3. **Scan the QR code** using your phone's WhatsApp.

4. The script will start sending messages automatically.

---

## ✉️ Message Format

The message is dynamically generated for each contact like:

```
Hello
John Doe,

Thank you
Best Regards
```

You can customize the message body in the `message` variable inside the script.

---

## 🛑 Disclaimer

* This project is **not affiliated with WhatsApp**.
* Spamming users may result in your number being banned by WhatsApp.
* Use this script only with consent from message recipients.

---

## 📄 License

This project is open-sourced under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 🧠 Credits

Developed by [Luvai Bhuriwala](https://github.com/luvaibhuriwala)

---

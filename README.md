# 📸 Ubuntu Image Fetcher

*A tool for mindfully collecting images from the web*

> **"I am because we are." — Ubuntu Philosophy**  
> This script embodies the spirit of Ubuntu: community, respect, and sharing through responsible image fetching.

---

## 🌍 Project Overview

The **Ubuntu Image Fetcher** is a Python script that respectfully connects to the global web, fetches shared image resources, and organizes them locally. It handles network errors gracefully, avoids duplicates, and ensures only valid images are downloaded.

---

## 🚀 Features

✅ Accepts one or multiple image URLs (comma-separated)  
✅ Creates a `Fetched_Images/` directory if it doesn't exist  
✅ Validates content type before saving (image only)  
✅ Generates meaningful filenames from the URL  
✅ Avoids downloading duplicates using SHA-256 hashing  
✅ Logs image hashes to prevent repeated downloads  
✅ Fully respectful of the network (timeouts, error handling, clean requests)

---

## 🧠 Ubuntu Principles in Practice

| Principle      | Implementation                                                                 |
|----------------|---------------------------------------------------------------------------------|
| **Community**  | Connects to shared resources on the internet                                   |
| **Respect**    | Gracefully handles errors, only downloads legitimate image files               |
| **Sharing**    | Organizes images in a central `Fetched_Images` folder for later use            |
| **Practicality** | Offers a real-world tool for curated image collection                        |

---

## 🛠️ How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Ubuntu_Requests.git
cd Ubuntu_Requests

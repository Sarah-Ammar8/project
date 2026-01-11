# Base Backend Service – Technical Documentation

## 1. وصف المشروع (What is this project?)
هذا المشروع عبارة عن خدمة Backend بسيطة تم تطويرها لأغراض تعليمية ضمن المرحلة التأسيسية، وتهدف إلى توضيح كيفية بناء خدمة برمجية قابلة للتشغيل والاستخدام داخل تطبيق أو نظام أكبر.

يركّز المشروع على:
- تحويل الكود إلى خدمة (Service-oriented thinking)
- بناء RESTful API
- تنظيم الكود وفق مبادئ Clean Code
- التشغيل في بيئة ثابتة باستخدام Docker

المشروع لا يركّز على بناء نموذج ذكاء اصطناعي، بل على إنشاء البنية البرمجية التي يمكن دمج نموذج AI داخلها لاحقًا.

---

## 2. الأدوات والتقنيات المستخدمة (Tools & Technologies)

### لغة البرمجة
- **Python 3.13**

### إطار العمل (Framework)
- **FastAPI**
  - لبناء RESTful APIs
  - دعم التحقق من البيانات (Validation)
  - توليد توثيق تلقائي (Swagger)

### خادم التشغيل
- **Uvicorn**
  - ASGI Server لتشغيل تطبيق FastAPI

### إدارة الإصدارات
- **Git**
- **GitHub**
  - إدارة المستودع
  - تتبع التغييرات عبر commits تدريجية

### الحاويات
- **Docker**
  - تشغيل التطبيق داخل Container
  - ضمان ثبات بيئة التشغيل

---

## 3. المعمارية (Architecture)

يعتمد المشروع على معمارية طبقية بسيطة (Layered Architecture) تفصل المسؤوليات بشكل واضح:

API Layer → routes.py
Business Logic → services.py
Data Models → schemas.py
Error Handling → errors.py
Configuration → config.py
Application Boot → main.py


### شرح المعمارية:
- **API Layer**: مسؤولة عن استقبال الطلبات HTTP وإرجاع الاستجابات.
- **Service Layer**: تحتوي منطق الأعمال المستقل عن HTTP.
- **Schemas**: تعريف نماذج البيانات والتحقق من المدخلات والمخرجات.
- **Error Layer**: إدارة الأخطاء المتوقعة بشكل مركزي.
- **Main Application**: نقطة تشغيل التطبيق وربط جميع المكونات.

هذا الفصل يسهّل:
- قراءة الكود
- اختبار المكونات
- التوسع المستقبلي (إضافة DB أو AI Model)

---

## 4. هيكلية المشروع (Project Structure)

project-root/
│
├── app/
│ ├── init.py
│ ├── main.py # Entry point
│ ├── routes.py # API endpoints
│ ├── services.py # Business logic
│ ├── schemas.py # Request/Response models
│ ├── errors.py # Centralized error handling
│ └── config.py # Application configuration
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md

---

## 5. المتطلبات (Requirements)

### للتشغيل المحلي:
- Python 3.13
- pip
- Git

### للتشغيل باستخدام Docker:
- Docker Desktop

---

## 6. طريقة التشغيل محليًا (Local Run)

1. تثبيت المتطلبات:
pip install -r requirements.txt

2. تشغيل التطبيق:
uvicorn app.main:app --reload

3. الوصول إلى الخدمة:
Health Check:
http://127.0.0.1:8000/health

توثيق API (Swagger):
http://127.0.0.1:8000/docs

## 7. استخدام الـ API (API Usage)
Health Endpoint :
(Request)
GET /health

(Response)
{
  "status": "ok"
}

## 8. التشغيل باستخدام Docker (Docker Run)
1. بناء الصورة:
docker build -t project-backend .

2. تشغيل الحاوية:
docker run --rm -p 8000:8000 project-backend

3. اختبار الخدمة:
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs

## 9. إدارة الأخطاء (Error Handling)
يعتمد المشروع على نظام أخطاء مركزي:

يتم تعريف الأخطاء المتوقعة داخل errors.py
يتم تحويلها إلى HTTP responses موحّدة في main.py
جميع الأخطاء ترجع بصيغة JSON ثابتة

هذا الأسلوب يمنع:
تكرار try/except في كل endpoint
تسريب تفاصيل أخطاء غير ضرورية للمستخدم
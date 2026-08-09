[2508-CDCS230] 2022836324 (06) MUHAMMAD ASYRAF BIN SUHAILE
Real-Time Emotion Recognition in Autistic Children Using Deep Learning For Therapy Assistance

Emotism Hub - Emotion Recognition & Therapy Session Management

A Flask-based web application for managing therapy sessions with automated facial emotion recognition. The system combines YOLOv8 for face detection and a CNN (hybrid model) for emotion classification, storing summarized emotional metrics per session. Includes role-based access (admin/therapist), dashboard, patient management, session scheduling, reporting, and Telegram integration for password reset and report sharing.

Features
- Authentication & Roles: Login, change/reset password; roles for admin and therapist.
- Therapist Dashboard: KPIs, recent activity, upcoming sessions, overall emotion stats.
- Patient Management: Add, edit, list, and delete patients; age auto-calculated.
- Session Management: Schedule, start, and complete sessions; store notes and duration.
- Emotion Recognition: YOLOv8 face detection + CNN emotion classifier per frame.
- Session Summaries: Aggregates counts, dominant emotion, most frequent, longest sustained, shifts, stability score.
- Reports: Per-patient view with charts and session history.
- Telegram Integration: Admin receives password reset codes and can receive shared reports.

Tech Stack
- Python 3.10
- Flask, Flask-Login, Flask-SQLAlchemy, Flask-Migrate
- TensorFlow/Keras, OpenCV, NumPy
- Ultralytics YOLOv8, PyTorch (for YOLO)
- SQLite (default)

Project Structure (high level)
application/
  app.py
  emotion_recognition/
    __init__.py           (DB utilities and seed init)
    __main__.py           (Optional: run DB initializer)
    models.py             (SQLAlchemy models: User, Patient, Session, EmotionalData)
    routes.py             (Blueprint with routes and APIs)
    templates/            (Jinja2 HTML templates)
    database/fyp_system.db
  static/                 (CSS/JS/Images)
  Hybrid Model/           (CNN models and training artifacts)
  migrations/             (Alembic migration scripts)
  init_db.py              (Alternative DB initializer with sample data)
  requirements.txt

Prerequisites
- Windows 10/11 recommended (paths in code are Windows-style). Linux/macOS work if you update paths.
- Python 3.10
- Optional GPU: CUDA/CuDNN compatible with your PyTorch/TensorFlow versions.

Setup
1) Open a terminal in the project root (application).
2) Create and activate a virtual environment (PowerShell):
   python -m venv venv
   ./venv/Scripts/Activate.ps1
3) Install dependencies:
   pip install --upgrade pip
   pip install -r requirements.txt

Model Files & Paths
The app loads two models, configured in emotion_recognition/routes.py:
- YOLOv8 weights (YOLO_PATH):
  Default: C:/Users/asyra/Desktop/FINAL YEAR PROJECT SYSTEM/runs/detect/train6/weights/best.pt
  Change this to your actual best.pt, or place your file at that path.
- CNN emotion classifier (CNN_MODEL_PATH):
  Default: C:/Users/asyra/Desktop/application/Hybrid Model/3_models/Model/triple_hybrid_model_fold5.h5
  Ensure the referenced .h5 exists, or change CNN_MODEL_PATH to a valid file within "Hybrid Model/3_models/Model/".

To change model locations, edit the constants near the top of emotion_recognition/routes.py.

Database
SQLite is used by default. app.py currently points to an absolute path:
  sqlite:///C:/Users/asyra/Desktop/application/emotion_recognition/database/fyp_system.db
You may switch to a relative path for portability, for example:
  sqlite:///emotion_recognition/database/fyp_system.db

Database Initialization
Option A (recommended for first run): drops/recreates tables and seeds data
  python -m emotion_recognition
Creates users:
  Admin: admin / admin123
  Therapist: therapist / therapist123

Option B (alternative seed)
  python init_db.py
Creates a different admin/therapist and sample patients/sessions.

Migrations (optional)
  $env:FLASK_APP = "app.py"
  flask db upgrade

Configuration
- Secret Key: update app.config['SECRET_KEY'] in app.py.
- Telegram: set TELEGRAM_BOT_TOKEN and ADMIN_TELEGRAM_CHAT_ID in emotion_recognition/routes.py.
  For production, move these to environment variables.
- Uploads: avatars are saved under static/img/avatars (auto-created).

Run the App
  python app.py
Visit http://localhost:5000

Default Credentials (after Option A init)
- Admin: admin / admin123
- Therapist: therapist / therapist123

Key Pages and APIs (selection)
- Pages: /login, /dashboard, /patients-list, /new-session, /view-reports, /profile, /change-password
- APIs:
  POST /api/emotion                     (base64 frame -> emotion prediction)
  PUT  /api/sessions/<session_id>       (complete session and persist summary)
  GET  /api/session_summary/<session_id>
  GET  /api/patient/<ic_number>
  POST /api/patient/<ic_number>/appointment
  PATCH/DELETE /api/appointment/<session_id>
  GET  /api/patient-emotional-data/<ic_number>
  GET  /api/get_upcoming_sessions
  POST /api/share-report-telegram

Troubleshooting
- Model load errors: verify YOLO_PATH and CNN_MODEL_PATH point to real files.
- GPU/CUDA issues: install CPU builds or match CUDA/CuDNN versions for PyTorch/TensorFlow.
- OpenCV errors (ffmpeg/codec): upgrade OpenCV or use opencv-python-headless on servers.
- SQLite path/permissions: prefer a relative DB path and ensure the directory exists.
- Telegram failures: check bot token/chat ID and internet access.

Security Notes
- Replace placeholder secrets and remove hard-coded tokens for production.
- Use HTTPS, enforce strong passwords, and restrict admin endpoints.

License
Proprietary/Academic. Replace with your intended license.

Acknowledgements
- Ultralytics YOLOv8
- TensorFlow/Keras
- OpenCV
- Flask ecosystem

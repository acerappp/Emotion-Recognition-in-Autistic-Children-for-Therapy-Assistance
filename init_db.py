from app import app
from emotion_recognition import db
from emotion_recognition.models import User, Patient, Session, EmotionalData
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta, date

def create_user(
    username,
    email,
    password,
    full_name,
    phone,
    bio,
    specialization,
    experience_years,
    profile_picture,
    role='user',
    last_login_days_ago=1
):
    return User(
        username=username,
        email=email,
        password_hash=generate_password_hash(password),
        full_name=full_name,
        phone=phone,
        bio=bio,
        specialization=specialization,
        experience_years=experience_years,
        profile_picture=profile_picture,
        reset_token=None,
        reset_token_expiry=None,
        created_at=datetime.utcnow(),
        last_login=datetime.utcnow() - timedelta(days=last_login_days_ago),
        is_active=True,
        role=role
    )

def initialize_database():
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("✅ Tables created successfully!")

        # --- Create Users ---
        admin = create_user(
            username='admin_master',
            email='admin@example.com',
            password='adminpass2024',
            full_name='System Administrator',
            phone='0112233445',
            bio='Manages platform users and system configuration.',
            specialization='System Administration',
            experience_years=15,
            profile_picture=None,
            role='admin'
        )

        therapist = create_user(
            username='dr_john',
            email='drjohn@example.com',
            password='securepassword123',
            full_name='Dr. John Smith',
            phone='0123456789',
            bio='Specialist in cognitive behavioral therapy.',
            specialization='Cognitive Behavioral Therapy',
            experience_years=10,
            profile_picture='profile_images/john.png',
            role='therapist'
        )

        db.session.add_all([admin, therapist])
        db.session.commit()
        print("✅ Admin and therapist users created.")

        # --- Add Patients ---
        patient1 = Patient(
            ic_number='010101-01-0001',
            name='Ali',
            date_of_birth=date(2015, 1, 1),
            age=9,
            gender='Male',
            status='Active',
            parents_guardian_phone_number='0123456789',
            home_address='123 A Street',
            therapist_id=therapist.id
        )
        patient2 = Patient(
            ic_number='020202-02-0002',
            name='Sarah',
            date_of_birth=date(2013, 2, 2),
            age=11,
            gender='Female',
            status='Active',
            parents_guardian_phone_number='0129876543',
            home_address='456 B Street',
            therapist_id=therapist.id
        )
        db.session.add_all([patient1, patient2])
        db.session.commit()
        print("✅ Sample patients added.")

        # --- Add Sessions ---
        session1 = Session(
            patient_id=patient1.ic_number,
            date=date(2025, 6, 1),
            time=datetime.strptime("10:00", "%H:%M").time(),
            status='Completed',
            notes='Good focus'
        )
        session2 = Session(
            patient_id=patient2.ic_number,
            date=date(2025, 6, 2),
            time=datetime.strptime("11:00", "%H:%M").time(),
            status='Completed',
            notes='Initial hesitation'
        )
        db.session.add_all([session1, session2])
        db.session.commit()
        print("✅ Sessions recorded.")

        # --- Add Emotional Data ---
        emotion1 = EmotionalData(
            session_id=session1.id,
            emotion_counts='{"happy": 8, "neutral": 2}',
            dominant_emotion='happy',
            most_frequent='happy',
            longest_sustained='happy',
            emotional_shifts=1,
            stability_score='8.5',
            notes='Calm session'
        )
        db.session.add(emotion1)
        db.session.commit()
        print("✅ Emotional data inserted.")

if __name__ == '__main__':
    initialize_database()

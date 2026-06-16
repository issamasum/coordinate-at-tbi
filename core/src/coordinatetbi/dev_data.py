# __author__ = Issa Masumbuko

"""Seed data for local development and end-to-end tests.

This module exposes a single :func:`seed` function that inserts a minimal but
representative set of records into an open database session. The caller is
responsible for committing the session.

Seed data created:
  - 2 coordinators (Person + User)
  - 1 guardian linked to one coordinator
  - 3 Ruhi courses (Books 1, 2, 3)
  - 1 upcoming overnight event
  - Course offerings for that event
  - 2 cottages with dorm rooms
  - 1 study circle (standalone, not tied to the event)
"""

from datetime import datetime

from sqlmodel import Session

from coordinatetbi.tables import (
    Person,
    Gender,
    User,
    UserRole,
    Guardian,
    PersonGuardian,
    GuardianRelationship,
    Course,
    CourseProgression,
    CourseProgressionStatus,
    Cottage,
    CottageGender,
    Dorm,
    Event,
    EventStatus,
    EventCourse,
    EventParticipant,
    EventParticipantRole,
    ParticipantRole,
    OvernightStatus,
    AttendanceStatus,
    EventDormRoom,
    DormAssignment,
    DormAssignmentStatus,
    
    StudyCircle,
    StudyCircleStatus,
    StudyCircleMember,
    MemberStatus,
)


def seed(session: Session) -> None:
    """Insert development seed data into the database.

    Args:
        session: An open database session. The caller is responsible for
            committing after this function returns.
    """

   
    # People
   
    main_coord_person = Person(
        name="Main Coordinator",
        email="main@example.com",
        phone="919-555-0001",
        gender=Gender.FEMALE,
    )
    asst_coord_person = Person(
        name="Assistant Coordinator",
        email="assistant@example.com",
        phone="919-555-0002",
        gender=Gender.MALE,
    )
    session.add_all([main_coord_person, asst_coord_person])
    session.flush()


    # Users (coordinator accounts)
  
    main_user = User(
        person_id=main_coord_person.id,
        email="main@example.com",
        hashed_password="$2b$12$placeholder_hashed_password_main",
        role=UserRole.MAIN_COORDINATOR,
        is_active=True,
    )
    asst_user = User(
        person_id=asst_coord_person.id,
        email="assistant@example.com",
        hashed_password="$2b$12$placeholder_hashed_password_asst",
        role=UserRole.ASSISTANT_COORDINATOR,
        is_active=True,
    )
    session.add_all([main_user, asst_user])
    session.flush()

  
    # Guardian linked to Main
   
    guardian = Guardian(
        name="Main Guardian",
        email="guardian@example.com",
        phone="919-555-0099",
    )
    session.add(guardian)
    session.flush()

    session.add(
        PersonGuardian(
            person_id=main_coord_person.id,
            guardian_id=guardian.id,
            relationship=GuardianRelationship.PARENT,
        )
    )
    session.flush()

   
    # Ruhi courses
 
    book1 = Course(
        name="Book 1",
        title="Reflections on the Life of the Spirit",
    )
    book2 = Course(
        name="Book 2",
        title="Arising to Serve",
    )
    book3 = Course(
        name="Book 3",
        title="Teaching Children's Classes, Grade 1",
    )
    session.add_all([book1, book2, book3])
    session.flush()

    # Course progression for the main coordinator
    session.add(
        CourseProgression(
            person_id=main_coord_person.id,
            course_id=book1.id,
            status=CourseProgressionStatus.COMPLETED,
        )
    )
    session.add(
        CourseProgression(
            person_id=main_coord_person.id,
            course_id=book3.id,
            status=CourseProgressionStatus.IN_PROGRESS,
        )
    )
    session.flush()

    
    # Facility — cottages and dorm rooms
  
    male_cottage = Cottage(name="Cottage 1", gender=CottageGender.MALE, is_active=True)
    female_cottage = Cottage(name="Cottage 2", gender=CottageGender.FEMALE, is_active=True)
    session.add_all([male_cottage, female_cottage])
    session.flush()

    male_room_1 = Dorm(name="Room 1", cottage_id=male_cottage.id, capacity=4, is_active=True)
    male_room_2 = Dorm(name="Room 2", cottage_id=male_cottage.id, capacity=4, is_active=True)
    female_room_1 = Dorm(name="Room 9", cottage_id=female_cottage.id, capacity=4, is_active=True)
    female_room_2 = Dorm(name="Room 10", cottage_id=female_cottage.id, capacity=4, is_active=True)
    session.add_all([male_room_1, male_room_2, female_room_1, female_room_2])
    session.flush()

    # Event
  
    event = Event(
        name="SOS 2026, Session 1",
        location="Triangle Baha'i Institute",
        start_date=datetime(2026, 6, 14, 14, 0),
        end_date=datetime(2026, 7, 17, 17, 0),
        overnight=True,
        status=EventStatus.PUBLISHED,
        updated_by=main_coord_person.id,
    )
    session.add(event)
    session.flush()
    assert event.id is not None

    # Courses offered at this event
    session.add_all([
        EventCourse(course_id=book1.id, event_id=event.id),
        EventCourse(course_id=book2.id, event_id=event.id),
    ])
    session.flush()

    # Dorms assigned to this event
    event_male_room = EventDormRoom(dorm_id=male_room_1.id, event_id=event.id)
    event_female_room = EventDormRoom(dorm_id=female_room_1.id, event_id=event.id)
    session.add_all([event_male_room, event_female_room])
    session.flush()

    # Participants
    main_participation = EventParticipant(
        person_id=main_coord_person.id,
        event_id=event.id,
        overnight_status=OvernightStatus.STAYING,
        attendance_status=AttendanceStatus.REGISTERED,
    )
    assistant_participation = EventParticipant(
        person_id=asst_coord_person.id,
        event_id=event.id,
        overnight_status=OvernightStatus.NOT_STAYING,
        attendance_status=AttendanceStatus.REGISTERED,
    )
    session.add_all([main_participation, assistant_participation])
    session.flush()

    # Roles for participants
    session.add(
        EventParticipantRole(
            participant_id=main_participation.id,
            role=ParticipantRole.TUTOR,
        )
    )
    session.add(
        EventParticipantRole(
            participant_id=assistant_participation.id,
            role=ParticipantRole.PARTICIPANT,
        )
    )
    session.flush()

    # Dorm assignment for Layla (staying overnight, female room)
    session.add(
        DormAssignment(
            event_dorm_id=event_female_room.id,
            participant_id=main_participation.id,
            status=DormAssignmentStatus.CONFIRMED,
        )
    )
    session.flush()


    # Standalone study circle (not tied to an event)
    circle = StudyCircle(
        name="Book 1 Unit 1",
        status=StudyCircleStatus.IN_PROGRESS,
        course_id=book1.id,
    )
    session.add(circle)
    session.flush()

    session.add(
        StudyCircleMember(
            study_circle_id=circle.id,
            person_id=main_coord_person.id,
            status=MemberStatus.ACTIVE,
        )
    )
    session.flush()
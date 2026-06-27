# __author__ = Issa Masumbuko

from api.routes.cottages import router as cottages_router
from api.routes.dorms import router as dorms_router
from api.routes.courses import router as courses_router
from api.routes.course_progressions import router as course_progressions_router
from api.routes.guardians import router as guardians_router
from api.routes.people import router as people_router
from api.routes.people_guardians import router as people_guardians_router
from api.routes.event import router as events_router
from api.routes.event_courses import router as event_courses_router
from api.routes.event_dorms import router as event_dorms_router
from api.routes.event_participants import router as event_participants_router
from api.routes.dorm_assignments import router as dorm_assignments_router
from api.routes.orientation import router as orientations_router
from api.routes.study_circles import router as study_circles_router

API_ROUTERS = [
    cottages_router,
    dorms_router,
    courses_router,
    course_progressions_router,
    guardians_router,
    people_router,
    people_guardians_router,
    events_router,
    event_courses_router,
    event_dorms_router,
    event_participants_router,
    dorm_assignments_router,
    orientations_router,
    study_circles_router,
]

__all__ = ["API_ROUTERS"]
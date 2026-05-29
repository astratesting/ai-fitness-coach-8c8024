from __future__ import annotations

import os
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Literal
from uuid import UUID, uuid4

from fastapi import Depends, FastAPI, Header, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field, field_validator


class ActivityLevel(str, Enum):
    sedentary = "sedentary"
    light = "light"
    moderate = "moderate"
    active = "active"
    athlete = "athlete"


class FitnessGoal(str, Enum):
    fat_loss = "fat_loss"
    muscle_gain = "muscle_gain"
    endurance = "endurance"
    general_fitness = "general_fitness"
    strength = "strength"


class DietPreference(str, Enum):
    balanced = "balanced"
    vegetarian = "vegetarian"
    vegan = "vegan"
    pescatarian = "pescatarian"
    keto = "keto"
    mediterranean = "mediterranean"


class SubscriptionTier(str, Enum):
    free = "free"
    pro = "pro"
    premium = "premium"


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str
    version: str
    timestamp: datetime


class UserProfile(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    id: UUID = Field(default_factory=uuid4)
    clerk_user_id: str = Field(min_length=3, max_length=128)
    email: str = Field(min_length=5, max_length=254)
    age: int = Field(ge=18, le=80)
    weight_kg: float = Field(gt=35, lt=300)
    height_cm: float = Field(gt=120, lt=230)
    activity_level: ActivityLevel
    goal: FitnessGoal
    diet_preference: DietPreference = DietPreference.balanced
    dietary_restrictions: list[str] = Field(default_factory=list, max_length=12)
    injuries: list[str] = Field(default_factory=list, max_length=12)
    workouts_per_week: int = Field(default=4, ge=1, le=7)
    workout_minutes: int = Field(default=35, ge=10, le=120)
    subscription_tier: SubscriptionTier = SubscriptionTier.free
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if "@" not in value or value.startswith("@") or value.endswith("@"):
            raise ValueError("valid email required")
        return value.lower()

    @field_validator("dietary_restrictions", "injuries")
    @classmethod
    def normalize_string_list(cls, values: list[str]) -> list[str]:
        clean_values = []
        seen = set()
        for value in values:
            normalized = value.strip().lower()
            if normalized and normalized not in seen:
                clean_values.append(normalized)
                seen.add(normalized)
        return clean_values


class ProfileCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    clerk_user_id: str = Field(min_length=3, max_length=128)
    email: str = Field(min_length=5, max_length=254)
    age: int = Field(ge=18, le=80)
    weight_kg: float = Field(gt=35, lt=300)
    height_cm: float = Field(gt=120, lt=230)
    activity_level: ActivityLevel
    goal: FitnessGoal
    diet_preference: DietPreference = DietPreference.balanced
    dietary_restrictions: list[str] = Field(default_factory=list, max_length=12)
    injuries: list[str] = Field(default_factory=list, max_length=12)
    workouts_per_week: int = Field(default=4, ge=1, le=7)
    workout_minutes: int = Field(default=35, ge=10, le=120)


class ProfileUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    age: int | None = Field(default=None, ge=18, le=80)
    weight_kg: float | None = Field(default=None, gt=35, lt=300)
    height_cm: float | None = Field(default=None, gt=120, lt=230)
    activity_level: ActivityLevel | None = None
    goal: FitnessGoal | None = None
    diet_preference: DietPreference | None = None
    dietary_restrictions: list[str] | None = Field(default=None, max_length=12)
    injuries: list[str] | None = Field(default=None, max_length=12)
    workouts_per_week: int | None = Field(default=None, ge=1, le=7)
    workout_minutes: int | None = Field(default=None, ge=10, le=120)
    subscription_tier: SubscriptionTier | None = None


class Exercise(BaseModel):
    name: str
    sets: int = Field(ge=1, le=8)
    reps: str
    rest_seconds: int = Field(ge=15, le=300)
    notes: str


class WorkoutDay(BaseModel):
    day: int = Field(ge=1, le=7)
    focus: str
    duration_minutes: int = Field(ge=10, le=120)
    warmup: list[str]
    exercises: list[Exercise]
    cooldown: list[str]


class WorkoutPlan(BaseModel):
    user_id: UUID
    generated_at: datetime
    goal: FitnessGoal
    weekly_schedule: list[WorkoutDay]
    progression: str
    safety_notes: list[str]


class Meal(BaseModel):
    name: str
    calories: int = Field(ge=100, le=2000)
    protein_g: int = Field(ge=0, le=200)
    carbs_g: int = Field(ge=0, le=300)
    fat_g: int = Field(ge=0, le=150)
    items: list[str]


class NutritionPlan(BaseModel):
    user_id: UUID
    generated_at: datetime
    daily_calories: int
    protein_g: int
    carbs_g: int
    fat_g: int
    meals: list[Meal]
    hydration_liters: float
    notes: list[str]


class LogEntry(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    kind: Literal["meal", "exercise"]
    name: str = Field(min_length=1, max_length=120)
    quantity: str = Field(min_length=1, max_length=120)
    calories: int | None = Field(default=None, ge=0, le=3000)
    completed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    notes: str | None = Field(default=None, max_length=500)


class ProgressMetric(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    weight_kg: float = Field(gt=35, lt=300)
    body_fat_percent: float | None = Field(default=None, ge=3, le=70)
    workout_completion_percent: float = Field(default=0, ge=0, le=100)
    logged_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Dashboard(BaseModel):
    user: UserProfile
    latest_progress: ProgressMetric | None
    weekly_meals_logged: int
    weekly_exercises_logged: int
    adherence_score: int
    recommendation: str


class CheckoutSessionRequest(BaseModel):
    user_id: UUID
    tier: Literal[SubscriptionTier.pro, SubscriptionTier.premium]


class CheckoutSessionResponse(BaseModel):
    checkout_url: str
    tier: SubscriptionTier
    monthly_price_usd: int


class InMemoryStore:
    def __init__(self) -> None:
        self.users: dict[UUID, UserProfile] = {}
        self.logs: dict[UUID, LogEntry] = {}
        self.progress: dict[UUID, ProgressMetric] = {}

    def create_profile(self, payload: ProfileCreate) -> UserProfile:
        if any(user.clerk_user_id == payload.clerk_user_id for user in self.users.values()):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="profile already exists")
        user = UserProfile(**payload.model_dump())
        self.users[user.id] = user
        return user

    def get_profile(self, user_id: UUID) -> UserProfile:
        user = self.users.get(user_id)
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="profile not found")
        return user

    def update_profile(self, user_id: UUID, payload: ProfileUpdate) -> UserProfile:
        user = self.get_profile(user_id)
        update_data = payload.model_dump(exclude_unset=True)
        updated = user.model_copy(update={**update_data, "updated_at": datetime.now(timezone.utc)})
        self.users[user_id] = updated
        return updated

    def add_log(self, payload: LogEntry) -> LogEntry:
        self.get_profile(payload.user_id)
        self.logs[payload.id] = payload
        return payload

    def add_progress(self, payload: ProgressMetric) -> ProgressMetric:
        self.get_profile(payload.user_id)
        self.progress[payload.id] = payload
        return payload


store = InMemoryStore()

app = FastAPI(
    title="AI Fitness Coach API",
    version="0.1.0",
    description="MVP API for personalized workout, nutrition, logging, progress, and subscription flows.",
)

allowed_origins = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",") if origin.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "X-Request-ID"],
)


@app.exception_handler(ValueError)
async def value_error_handler(_: Request, exc: ValueError) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": str(exc)})


def require_auth(authorization: str | None = Header(default=None)) -> str:
    if os.getenv("DISABLE_AUTH", "false").lower() == "true":
        return "local-dev"
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="bearer token required")
    token = authorization.removeprefix("Bearer ").strip()
    if len(token) < 16:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid bearer token")
    return token


def calculate_bmr(user: UserProfile) -> float:
    return 10 * user.weight_kg + 6.25 * user.height_cm - 5 * user.age + 5


def activity_multiplier(level: ActivityLevel) -> float:
    return {
        ActivityLevel.sedentary: 1.2,
        ActivityLevel.light: 1.375,
        ActivityLevel.moderate: 1.55,
        ActivityLevel.active: 1.725,
        ActivityLevel.athlete: 1.9,
    }[level]


def calorie_target(user: UserProfile) -> int:
    maintenance = calculate_bmr(user) * activity_multiplier(user.activity_level)
    if user.goal == FitnessGoal.fat_loss:
        target = maintenance - 450
    elif user.goal == FitnessGoal.muscle_gain:
        target = maintenance + 300
    elif user.goal == FitnessGoal.endurance:
        target = maintenance + 150
    else:
        target = maintenance
    return max(1400, round(target / 25) * 25)


def build_workout_plan(user: UserProfile) -> WorkoutPlan:
    focus_by_goal: dict[FitnessGoal, list[str]] = {
        FitnessGoal.fat_loss: ["full-body metabolic strength", "zone 2 cardio", "upper-body circuit", "lower-body circuit"],
        FitnessGoal.muscle_gain: ["push hypertrophy", "pull hypertrophy", "legs hypertrophy", "full-body volume"],
        FitnessGoal.endurance: ["tempo intervals", "mobility and core", "long aerobic base", "strength maintenance"],
        FitnessGoal.general_fitness: ["full-body strength", "cardio conditioning", "mobility and core", "functional circuit"],
        FitnessGoal.strength: ["squat focus", "bench focus", "deadlift focus", "overhead press focus"],
    }
    exercise_bank = {
        "strength": [
            Exercise(name="Goblet squat", sets=4, reps="8-10", rest_seconds=90, notes="Keep torso tall and knees tracking over toes."),
            Exercise(name="Dumbbell bench press", sets=4, reps="8-10", rest_seconds=90, notes="Stop one rep before form breaks."),
            Exercise(name="Romanian deadlift", sets=3, reps="10-12", rest_seconds=90, notes="Hinge from hips with neutral spine."),
            Exercise(name="One-arm row", sets=3, reps="10 each side", rest_seconds=75, notes="Pull elbow toward hip."),
        ],
        "conditioning": [
            Exercise(name="Incline treadmill walk", sets=1, reps="20 minutes", rest_seconds=30, notes="Maintain conversational pace."),
            Exercise(name="Kettlebell deadlift", sets=4, reps="12", rest_seconds=60, notes="Explosive hips, controlled return."),
            Exercise(name="Bike intervals", sets=8, reps="30s hard / 90s easy", rest_seconds=90, notes="Hard efforts at 8/10 intensity."),
        ],
    }
    focuses = focus_by_goal[user.goal]
    days: list[WorkoutDay] = []
    for index in range(user.workouts_per_week):
        is_conditioning = user.goal in {FitnessGoal.fat_loss, FitnessGoal.endurance, FitnessGoal.general_fitness} and index % 2 == 1
        days.append(
            WorkoutDay(
                day=index + 1,
                focus=focuses[index % len(focuses)],
                duration_minutes=user.workout_minutes,
                warmup=["5 minutes easy cardio", "Dynamic hip openers", "Band pull-aparts"],
                exercises=exercise_bank["conditioning" if is_conditioning else "strength"],
                cooldown=["Slow nasal breathing", "Hamstring stretch", "Chest doorway stretch"],
            )
        )
    safety = ["Stop if sharp pain occurs", "Keep two rest days weekly when soreness or sleep debt rises"]
    if user.injuries:
        safety.append(f"Avoid aggravating reported injuries: {', '.join(user.injuries)}")
    return WorkoutPlan(
        user_id=user.id,
        generated_at=datetime.now(timezone.utc),
        goal=user.goal,
        weekly_schedule=days,
        progression="Add 1-2 reps weekly until top of rep range, then increase load by smallest available increment.",
        safety_notes=safety,
    )


def build_nutrition_plan(user: UserProfile) -> NutritionPlan:
    calories = calorie_target(user)
    protein = round(user.weight_kg * (2.0 if user.goal in {FitnessGoal.fat_loss, FitnessGoal.muscle_gain, FitnessGoal.strength} else 1.6))
    fat = round((calories * 0.28) / 9)
    carbs = round((calories - protein * 4 - fat * 9) / 4)
    restriction_note = f"Respect restrictions: {', '.join(user.dietary_restrictions)}" if user.dietary_restrictions else "Use minimally processed foods most meals."
    meals = [
        Meal(name="Protein breakfast bowl", calories=round(calories * 0.25), protein_g=round(protein * 0.28), carbs_g=round(carbs * 0.25), fat_g=round(fat * 0.25), items=["Greek yogurt or tofu", "berries", "oats", "chia seeds"]),
        Meal(name="Busy professional lunch", calories=round(calories * 0.35), protein_g=round(protein * 0.35), carbs_g=round(carbs * 0.35), fat_g=round(fat * 0.35), items=["lean protein", "rice or quinoa", "large salad", "olive oil dressing"]),
        Meal(name="Simple dinner plate", calories=round(calories * 0.30), protein_g=round(protein * 0.30), carbs_g=round(carbs * 0.30), fat_g=round(fat * 0.30), items=["protein entree", "roasted vegetables", "potato or legumes"]),
        Meal(name="Planned snack", calories=round(calories * 0.10), protein_g=max(10, round(protein * 0.07)), carbs_g=round(carbs * 0.10), fat_g=round(fat * 0.10), items=["protein shake", "fruit", "nuts"]),
    ]
    return NutritionPlan(
        user_id=user.id,
        generated_at=datetime.now(timezone.utc),
        daily_calories=calories,
        protein_g=protein,
        carbs_g=carbs,
        fat_g=fat,
        meals=meals,
        hydration_liters=round(max(2.0, user.weight_kg * 0.035), 1),
        notes=[restriction_note, "Batch prep two proteins and two carb sources weekly to reduce decision fatigue."],
    )


def latest_progress_for(user_id: UUID) -> ProgressMetric | None:
    metrics = [metric for metric in store.progress.values() if metric.user_id == user_id]
    return max(metrics, key=lambda metric: metric.logged_at, default=None)


def weekly_count(user_id: UUID, kind: Literal["meal", "exercise"]) -> int:
    now = datetime.now(timezone.utc)
    return sum(1 for entry in store.logs.values() if entry.user_id == user_id and entry.kind == kind and (now - entry.completed_at).days < 7)


@app.get("/health", response_model=HealthResponse, tags=["system"])
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="ai-fitness-coach-api", version=app.version, timestamp=datetime.now(timezone.utc))


@app.post("/profiles", response_model=UserProfile, status_code=status.HTTP_201_CREATED, tags=["profiles"])
def create_profile(payload: ProfileCreate, _: str = Depends(require_auth)) -> UserProfile:
    return store.create_profile(payload)


@app.get("/profiles/{user_id}", response_model=UserProfile, tags=["profiles"])
def get_profile(user_id: UUID, _: str = Depends(require_auth)) -> UserProfile:
    return store.get_profile(user_id)


@app.patch("/profiles/{user_id}", response_model=UserProfile, tags=["profiles"])
def update_profile(user_id: UUID, payload: ProfileUpdate, _: str = Depends(require_auth)) -> UserProfile:
    return store.update_profile(user_id, payload)


@app.post("/plans/workout/{user_id}", response_model=WorkoutPlan, tags=["plans"])
def generate_workout_plan(user_id: UUID, _: str = Depends(require_auth)) -> WorkoutPlan:
    return build_workout_plan(store.get_profile(user_id))


@app.post("/plans/nutrition/{user_id}", response_model=NutritionPlan, tags=["plans"])
def generate_nutrition_plan(user_id: UUID, _: str = Depends(require_auth)) -> NutritionPlan:
    return build_nutrition_plan(store.get_profile(user_id))


@app.post("/logs", response_model=LogEntry, status_code=status.HTTP_201_CREATED, tags=["tracking"])
def create_log(payload: LogEntry, _: str = Depends(require_auth)) -> LogEntry:
    return store.add_log(payload)


@app.post("/progress", response_model=ProgressMetric, status_code=status.HTTP_201_CREATED, tags=["tracking"])
def create_progress(payload: ProgressMetric, _: str = Depends(require_auth)) -> ProgressMetric:
    return store.add_progress(payload)


@app.get("/dashboard/{user_id}", response_model=Dashboard, tags=["tracking"])
def get_dashboard(user_id: UUID, _: str = Depends(require_auth)) -> Dashboard:
    user = store.get_profile(user_id)
    meals = weekly_count(user_id, "meal")
    exercises = weekly_count(user_id, "exercise")
    adherence = min(100, round(((meals / 21) * 50 + (exercises / max(1, user.workouts_per_week)) * 50)))
    recommendation = "Keep current plan steady this week."
    if adherence < 50:
        recommendation = "Reduce friction: schedule shorter workouts and repeat easiest meals."
    elif adherence > 85:
        recommendation = "Increase training load slightly or add one mobility session."
    return Dashboard(
        user=user,
        latest_progress=latest_progress_for(user_id),
        weekly_meals_logged=meals,
        weekly_exercises_logged=exercises,
        adherence_score=adherence,
        recommendation=recommendation,
    )


@app.post("/billing/checkout", response_model=CheckoutSessionResponse, tags=["billing"])
def create_checkout_session(payload: CheckoutSessionRequest, _: str = Depends(require_auth)) -> CheckoutSessionResponse:
    store.get_profile(payload.user_id)
    prices = {SubscriptionTier.pro: 19, SubscriptionTier.premium: 39}
    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000").rstrip("/")
    return CheckoutSessionResponse(
        checkout_url=f"{frontend_url}/billing/checkout?user_id={payload.user_id}&tier={payload.tier.value}",
        tier=payload.tier,
        monthly_price_usd=prices[payload.tier],
    )


@app.get("/", tags=["system"])
def root() -> dict[str, Any]:
    return {"name": "AI Fitness Coach API", "health": "/health", "docs": "/docs"}

import Link from "next/link";
import {
  Activity,
  Apple,
  ArrowRight,
  BarChart3,
  CheckCircle2,
  Clock3,
  Dumbbell,
  ShieldCheck,
  Sparkles,
  TrendingUp,
  Utensils,
  Zap,
} from "lucide-react";

const stats = [
  { value: "18 min", label: "daily plan review" },
  { value: "94%", label: "plan adherence target" },
  { value: "3x", label: "weekly adaptation loop" },
];

const features = [
  {
    icon: Dumbbell,
    title: "Workout intelligence",
    text: "Plans adapt around equipment, calendar pressure, recovery, and goal pace so training stays realistic on packed weeks.",
  },
  {
    icon: Utensils,
    title: "Nutrition that fits workdays",
    text: "Meal targets, protein pacing, and logged meals translate biometric goals into choices busy professionals can repeat.",
  },
  {
    icon: BarChart3,
    title: "Progress signal, not noise",
    text: "Weight, activity, workout logs, and adherence roll into a dashboard that highlights what changed and what to do next.",
  },
];

const steps = [
  "Capture age, height, weight, activity level, schedule, dietary preferences, and training goals.",
  "Generate a weekly training and nutrition blueprint tuned to biometrics and available time.",
  "Log meals, exercises, and progress signals so the coach adjusts future recommendations.",
];

const planHighlights = [
  "Clerk-secured onboarding and account flow",
  "AI-generated workout and nutrition plans",
  "Meal and exercise logging for adherence tracking",
  "Subscription-ready upgrade path with Stripe",
];

export default function HomePage() {
  return (
    <main className="min-h-screen overflow-hidden bg-[#0b0f0d] text-stone-100">
      <section className="relative isolate px-6 py-8 sm:px-8 lg:px-12">
        <div className="absolute inset-0 -z-20 bg-[radial-gradient(circle_at_18%_18%,rgba(132,204,22,0.32),transparent_28%),radial-gradient(circle_at_82%_8%,rgba(20,184,166,0.24),transparent_25%),linear-gradient(135deg,#0b0f0d_0%,#111811_46%,#20160d_100%)]" />
        <div className="absolute inset-0 -z-10 opacity-[0.18] [background-image:linear-gradient(rgba(255,255,255,0.12)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.12)_1px,transparent_1px)] [background-size:42px_42px]" />
        <div className="absolute left-1/2 top-16 -z-10 h-72 w-72 -translate-x-1/2 rounded-full bg-lime-300/10 blur-3xl" />

        <nav className="mx-auto flex max-w-7xl items-center justify-between rounded-full border border-white/10 bg-white/[0.04] px-5 py-3 shadow-2xl shadow-black/20 backdrop-blur-xl">
          <Link href="/" className="flex items-center gap-3" aria-label="PulseForge home">
            <span className="grid h-10 w-10 place-items-center rounded-full bg-lime-300 text-[#0b0f0d] shadow-lg shadow-lime-300/30">
              <Activity className="h-5 w-5" aria-hidden="true" />
            </span>
            <span className="font-serif text-xl tracking-tight text-white">PulseForge</span>
          </Link>
          <div className="hidden items-center gap-8 text-sm font-medium text-stone-300 md:flex">
            <a href="#coach" className="transition hover:text-lime-200">Coach</a>
            <a href="#plans" className="transition hover:text-lime-200">Plans</a>
            <a href="#pricing" className="transition hover:text-lime-200">Pricing</a>
          </div>
          <Link
            href="/sign-in"
            className="rounded-full border border-lime-200/40 px-4 py-2 text-sm font-semibold text-lime-100 transition hover:border-lime-200 hover:bg-lime-200 hover:text-[#0b0f0d]"
          >
            Sign in
          </Link>
        </nav>

        <div className="mx-auto grid max-w-7xl gap-12 pb-16 pt-20 lg:grid-cols-[1.04fr_0.96fr] lg:items-center lg:pb-24 lg:pt-28">
          <div>
            <div className="mb-8 inline-flex items-center gap-2 rounded-full border border-lime-200/25 bg-lime-200/10 px-4 py-2 text-sm font-semibold text-lime-100 shadow-lg shadow-lime-950/30">
              <Sparkles className="h-4 w-4" aria-hidden="true" />
              AI fitness coach for busy professionals
            </div>
            <h1 className="max-w-4xl font-serif text-6xl leading-[0.9] tracking-[-0.055em] text-white sm:text-7xl lg:text-8xl">
              Biometrics in. Better training out.
            </h1>
            <p className="mt-7 max-w-2xl text-lg leading-8 text-stone-300 sm:text-xl">
              PulseForge turns age, weight, height, activity level, goals, meal logs, and exercise history into adaptive workout and nutrition plans that respect packed calendars.
            </p>
            <div className="mt-10 flex flex-col gap-4 sm:flex-row">
              <Link
                href="/sign-up"
                className="group inline-flex items-center justify-center gap-3 rounded-full bg-lime-300 px-7 py-4 text-base font-bold text-[#0b0f0d] shadow-2xl shadow-lime-300/20 transition hover:-translate-y-0.5 hover:bg-lime-200"
              >
                Start coaching plan
                <ArrowRight className="h-5 w-5 transition group-hover:translate-x-1" aria-hidden="true" />
              </Link>
              <a
                href="#coach"
                className="inline-flex items-center justify-center rounded-full border border-white/15 bg-white/[0.04] px-7 py-4 text-base font-semibold text-white backdrop-blur transition hover:-translate-y-0.5 hover:border-white/30 hover:bg-white/[0.08]"
              >
                See how it works
              </a>
            </div>
            <div className="mt-12 grid max-w-2xl grid-cols-3 gap-3">
              {stats.map((stat) => (
                <div key={stat.label} className="rounded-3xl border border-white/10 bg-white/[0.045] p-4 backdrop-blur">
                  <div className="font-serif text-3xl tracking-tight text-lime-200">{stat.value}</div>
                  <div className="mt-1 text-xs uppercase tracking-[0.2em] text-stone-400">{stat.label}</div>
                </div>
              ))}
            </div>
          </div>

          <div className="relative mx-auto w-full max-w-xl lg:mx-0">
            <div className="absolute -left-8 top-10 h-28 w-28 rounded-full border border-lime-200/30 bg-lime-200/10 blur-sm" />
            <div className="absolute -right-10 bottom-16 h-36 w-36 rounded-full bg-teal-300/10 blur-2xl" />
            <div className="relative rotate-1 rounded-[2.2rem] border border-white/14 bg-[#10170f]/90 p-4 shadow-[0_35px_120px_rgba(0,0,0,0.5)] backdrop-blur-2xl">
              <div className="rounded-[1.7rem] border border-lime-100/10 bg-[#172015] p-5">
                <div className="flex items-center justify-between border-b border-white/10 pb-5">
                  <div>
                    <p className="text-xs uppercase tracking-[0.28em] text-lime-200/80">Today</p>
                    <h2 className="mt-2 font-serif text-3xl tracking-tight text-white">High-output reset</h2>
                  </div>
                  <div className="grid h-14 w-14 place-items-center rounded-2xl bg-lime-300 text-[#0b0f0d]">
                    <Zap className="h-7 w-7" aria-hidden="true" />
                  </div>
                </div>

                <div className="mt-6 grid gap-4 sm:grid-cols-2">
                  <div className="rounded-3xl bg-[#0c120b] p-5 ring-1 ring-white/10">
                    <div className="flex items-center gap-2 text-sm font-semibold text-lime-200">
                      <Dumbbell className="h-4 w-4" aria-hidden="true" />
                      Training
                    </div>
                    <p className="mt-4 font-serif text-4xl tracking-tight text-white">42 min</p>
                    <p className="mt-2 text-sm leading-6 text-stone-400">Upper strength, short rests, mobility finisher.</p>
                  </div>
                  <div className="rounded-3xl bg-[#0c120b] p-5 ring-1 ring-white/10">
                    <div className="flex items-center gap-2 text-sm font-semibold text-teal-200">
                      <Apple className="h-4 w-4" aria-hidden="true" />
                      Nutrition
                    </div>
                    <p className="mt-4 font-serif text-4xl tracking-tight text-white">142g</p>
                    <p className="mt-2 text-sm leading-6 text-stone-400">Protein target with two travel-safe meal options.</p>
                  </div>
                </div>

                <div className="mt-5 rounded-3xl border border-white/10 bg-white/[0.035] p-5">
                  <div className="mb-4 flex items-center justify-between text-sm">
                    <span className="font-semibold text-white">Weekly adherence</span>
                    <span className="text-lime-200">82%</span>
                  </div>
                  <div className="h-3 overflow-hidden rounded-full bg-white/10">
                    <div className="h-full w-[82%] rounded-full bg-gradient-to-r from-lime-300 via-emerald-300 to-teal-300" />
                  </div>
                  <div className="mt-5 grid grid-cols-7 gap-2" aria-label="Weekly completion streak">
                    {Array.from({ length: 7 }, (_, index) => (
                      <div
                        key={index}
                        className={`h-12 rounded-2xl ${index < 5 ? "bg-lime-300" : "bg-white/10"}`}
                      />
                    ))}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="coach" className="bg-[#f4f0e8] px-6 py-20 text-[#15150f] sm:px-8 lg:px-12">
        <div className="mx-auto max-w-7xl">
          <div className="grid gap-8 lg:grid-cols-[0.8fr_1.2fr] lg:items-end">
            <div>
              <p className="text-sm font-black uppercase tracking-[0.3em] text-lime-700">Adaptive coaching engine</p>
              <h2 className="mt-4 max-w-xl font-serif text-5xl leading-none tracking-[-0.045em] sm:text-6xl">
                Fitness plan that behaves like your calendar matters.
              </h2>
            </div>
            <p className="max-w-2xl text-lg leading-8 text-stone-700 lg:justify-self-end">
              Built for professionals who need high-confidence guidance without reading forums, guessing macros, or forcing gym blocks into impossible days.
            </p>
          </div>

          <div className="mt-14 grid gap-5 lg:grid-cols-3">
            {features.map((feature) => {
              const Icon = feature.icon;
              return (
                <article key={feature.title} className="group rounded-[2rem] border border-[#15150f]/10 bg-white p-7 shadow-[0_20px_70px_rgba(21,21,15,0.08)] transition hover:-translate-y-1 hover:shadow-[0_28px_90px_rgba(21,21,15,0.14)]">
                  <div className="grid h-14 w-14 place-items-center rounded-2xl bg-[#15150f] text-lime-200 transition group-hover:rotate-3 group-hover:bg-lime-300 group-hover:text-[#15150f]">
                    <Icon className="h-7 w-7" aria-hidden="true" />
                  </div>
                  <h3 className="mt-7 font-serif text-3xl tracking-tight">{feature.title}</h3>
                  <p className="mt-4 leading-7 text-stone-600">{feature.text}</p>
                </article>
              );
            })}
          </div>
        </div>
      </section>

      <section id="plans" className="bg-[#0b0f0d] px-6 py-20 text-stone-100 sm:px-8 lg:px-12">
        <div className="mx-auto grid max-w-7xl gap-12 lg:grid-cols-[0.95fr_1.05fr] lg:items-center">
          <div className="rounded-[2rem] border border-white/10 bg-white/[0.04] p-6 backdrop-blur">
            <div className="rounded-[1.5rem] bg-[#f4f0e8] p-6 text-[#15150f]">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-xs font-black uppercase tracking-[0.28em] text-lime-700">Plan snapshot</p>
                  <h3 className="mt-2 font-serif text-4xl tracking-tight">Week 04</h3>
                </div>
                <TrendingUp className="h-10 w-10 text-lime-700" aria-hidden="true" />
              </div>
              <div className="mt-8 space-y-4">
                {steps.map((step, index) => (
                  <div key={step} className="flex gap-4 rounded-3xl bg-white p-5 shadow-sm">
                    <span className="grid h-9 w-9 shrink-0 place-items-center rounded-full bg-[#15150f] font-bold text-lime-200">{index + 1}</span>
                    <p className="leading-7 text-stone-700">{step}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>

          <div>
            <p className="text-sm font-black uppercase tracking-[0.3em] text-lime-200">From biometric profile to weekly action</p>
            <h2 className="mt-4 max-w-2xl font-serif text-5xl leading-none tracking-[-0.045em] text-white sm:text-6xl">
              Coach loop learns from every log.
            </h2>
            <p className="mt-6 max-w-2xl text-lg leading-8 text-stone-300">
              Onboarding creates the first plan. Daily meal and exercise logs refine the next one. Progress tracking keeps recommendations tied to outcomes, not vibes.
            </p>
            <div className="mt-8 grid gap-3 sm:grid-cols-2">
              {planHighlights.map((item) => (
                <div key={item} className="flex items-start gap-3 rounded-2xl border border-white/10 bg-white/[0.04] p-4">
                  <CheckCircle2 className="mt-0.5 h-5 w-5 shrink-0 text-lime-300" aria-hidden="true" />
                  <span className="text-sm leading-6 text-stone-300">{item}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section id="pricing" className="bg-[#f4f0e8] px-6 py-20 text-[#15150f] sm:px-8 lg:px-12">
        <div className="mx-auto max-w-7xl rounded-[2.5rem] bg-[#15150f] p-8 text-white shadow-[0_35px_120px_rgba(21,21,15,0.22)] sm:p-12 lg:p-16">
          <div className="grid gap-10 lg:grid-cols-[1fr_0.9fr] lg:items-center">
            <div>
              <p className="text-sm font-black uppercase tracking-[0.3em] text-lime-200">MVP-ready subscription path</p>
              <h2 className="mt-4 max-w-2xl font-serif text-5xl leading-none tracking-[-0.045em] sm:text-6xl">
                Premium coaching without premium scheduling friction.
              </h2>
              <p className="mt-6 max-w-2xl text-lg leading-8 text-stone-300">
                Launch with a focused offer: biometric onboarding, AI plan generation, progress dashboard, logs, and Stripe-powered subscription management.
              </p>
            </div>
            <div className="rounded-[2rem] border border-lime-200/20 bg-lime-200 p-7 text-[#15150f]">
              <div className="flex items-center gap-3">
                <ShieldCheck className="h-7 w-7" aria-hidden="true" />
                <span className="text-sm font-black uppercase tracking-[0.22em]">Coach Pro</span>
              </div>
              <div className="mt-7 flex items-end gap-2">
                <span className="font-serif text-6xl tracking-tight">$19</span>
                <span className="pb-2 font-semibold text-[#15150f]/70">/ month</span>
              </div>
              <p className="mt-4 leading-7 text-[#15150f]/75">
                Clear MVP pricing for motivated users who want adaptive fitness and nutrition guidance.
              </p>
              <Link
                href="/sign-up"
                className="mt-7 inline-flex w-full items-center justify-center gap-3 rounded-full bg-[#15150f] px-6 py-4 font-bold text-lime-100 transition hover:-translate-y-0.5 hover:bg-[#263122]"
              >
                Create account
                <ArrowRight className="h-5 w-5" aria-hidden="true" />
              </Link>
            </div>
          </div>
        </div>
      </section>

      <footer className="border-t border-white/10 bg-[#0b0f0d] px-6 py-8 text-stone-400 sm:px-8 lg:px-12">
        <div className="mx-auto flex max-w-7xl flex-col gap-4 text-sm sm:flex-row sm:items-center sm:justify-between">
          <div className="flex items-center gap-2 text-stone-300">
            <Clock3 className="h-4 w-4 text-lime-300" aria-hidden="true" />
            Built for busy professionals training between meetings.
          </div>
          <div>© {new Date().getFullYear()} PulseForge Fitness Coach</div>
        </div>
      </footer>
    </main>
  );
}

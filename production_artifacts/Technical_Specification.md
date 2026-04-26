# Reel-to-Action Productivity App — Technical Specification

## Executive Summary

**Tagline:** "A platform that converts content consumption into real-world action."

**Problem:** Users consume valuable content (internships, scholarships, opportunities) on social media but fail to take action on them.

**Solution:** A mobile/web app that transforms reel links into actionable tasks with deadlines, reminders, and gamification to drive completion.

---

## Requirements

### Pages & Features

**1. Add Reel Page**
- Input field to paste reel link
- "Convert to Task" button
- On click → generates mock task and adds to system
- Mock generation: ignore actual link, return dummy data

**2. Tasks Page**
- List of all tasks
- Each task shows: title, deadline, status (pending/completed)
- "Mark complete" action → awards tokens
- Filter by status (All / Pending / Completed)

**3. Calendar Page**
- Monthly view (default)
- Tasks displayed on their deadline dates
- Highlight dates with tasks
- Navigation: previous/next month

**4. Notification Center**
- List of mock notifications
- Types: "Deadline tomorrow", "Task pending", "Tokens earned"
- Static/simulated — no real push notifications

**5. Tokens / Points Page**
- Display total token balance
- Token history list (optional display)
- Tokens earned per completed task

**6. Lien Score Page**
- **Formula:** `(completed tasks / total tasks) × 100`
- Weekly scope
- Progress bar visualization
- Stats: tasks completed this week, total tasks

**7. Shop Page**
- Grid of mock items
- Each item: name, token cost, "Redeem" button
- Items (UI only, no real purchase):
  - T-shirt: 15 tokens
  - Coffee: 10 tokens
  - Notebook: 5 tokens
  - Hoodie: 25 tokens

### Gamification Rules

| Action | Reward |
|--------|--------|
| Complete a task | +5 tokens (default) |
| Redeem shop item | -item cost |
| Lien Score update | Real-time on task completion |

### Out of Scope (Prototype)
- Real Instagram/Reel API integration
- Real AI-powered content extraction
- Backend server or database
- User authentication
- Actual purchase/reward fulfillment
- Push notifications (real device)

### Navigation & UI Direction
**Left Sidebar** with icons and labels: Add Reel, Tasks, Calendar, Notifications, Tokens, Lien Score, Shop.
**Layout:** Left: Fixed sidebar (240px width), Right: Scrollable content area. Mobile: Sidebar collapses to hamburger menu.
**Design Aesthetic:** Clean, modern, gamified
**Color Palette:** Primary (Indigo/Violet #6366f1), Success (Green #22c55e), Warning (Amber #f59e0b), Background (Slate/Gray tones), Cards (White with subtle shadows).
**Typography:** Sans-serif (Inter or system)
**Animations:** Smooth transitions on page change, button feedback, token count animations

### User Flow
1. User lands on app → redirected to Tasks page
2. Clicks "Add Reel" in sidebar
3. Pastes a reel URL
4. Clicks "Convert to Task"
5. System generates mock task, saves to state
6. User sees new task in Tasks list and Calendar
7. User marks task complete → tokens awarded, Lien Score updates
8. User visits Shop to see items (spending is UI-only)

---

## Architecture & Tech Stack

| Layer | Choice |
|-------|--------|
| Framework | React (Vite) |
| Styling | Tailwind CSS |
| State Management | Zustand |
| Storage | localStorage |
| Build Tool | Vite |

### File Structure (Proposed)

```text
src/
├── components/
│   ├── Sidebar.tsx
│   ├── Header.tsx
│   ├── TaskCard.tsx
│   ├── Calendar.tsx
│   ├── TokenDisplay.tsx
│   ├── ProgressBar.tsx
│   └── ShopItem.tsx
├── pages/
│   ├── AddReel.tsx
│   ├── Tasks.tsx
│   ├── Calendar.tsx
│   ├── Notifications.tsx
│   ├── Tokens.tsx
│   ├── LienScore.tsx
│   └── Shop.tsx
├── store/
│   └── useStore.ts        # Zustand store
├── utils/
│   ├── mockExtract.ts     # Fake AI extraction
│   └── helpers.ts         # Date utils, etc.
├── App.tsx
├── main.tsx
└── index.css              # Tailwind imports
```

---

## State Management

Data flows from user actions (like "Add Reel" or "Mark Complete", "Redeem Item") to the globally accessible Zustand store. We use `localStorage` to persist the data so the mock application maintains state across page reloads.

### Data Models

**Task**
```typescript
{
  id: string;           // UUID
  title: string;       // e.g., "Google Internship 2026"
  deadline: string;    // ISO date string
  status: 'pending' | 'completed';
  tokens: number;      // tokens awarded on completion (default: 5)
  createdAt: string;   // ISO date string
  completedAt?: string; // ISO date string, set on completion
}
```

**UserStats**
```typescript
{
  totalTokens: number;
  weeklyCompletedTasks: number;
  weeklyTotalTasks: number;
  lifetimeCompletedTasks: number;
}
```

**Notification**
```typescript
{
  id: string;
  type: 'deadline' | 'pending' | 'reward';
  message: string;
  read: boolean;
  createdAt: string;
}
```

### Mock AI Extraction Logic
When user clicks "Convert to Task":
```typescript
const mockExtract = (url: string) => {
  // Ignore actual URL, generate dummy task
  return {
    title: "Google Summer Internship 2026",
    deadline: getRandomFutureDate(), // 7-30 days from now
    tokens: 5,
  };
};
```

# Reel-to-Action Productivity App — Specification

## 1. Concept & Vision

**Tagline:** "A platform that converts content consumption into real-world action."

**Problem:** Users consume valuable content (internships, scholarships, opportunities) on social media but fail to take action on them.

**Solution:** A mobile/web app that transforms reel links into actionable tasks with deadlines, reminders, and gamification to drive completion.

---

## 2. Tech Stack

| Layer | Choice |
|-------|--------|
| Framework | React (Vite) |
| Styling | Tailwind CSS |
| State Management | Zustand |
| Storage | localStorage |
| Build Tool | Vite |

---

## 3. Pages & Features

### 3.1 Add Reel Page
- Input field to paste reel link
- "Convert to Task" button
- On click → generates mock task and adds to system
- Mock generation: ignore actual link, return dummy data

### 3.2 Tasks Page
- List of all tasks
- Each task shows: title, deadline, status (pending/completed)
- "Mark complete" action → awards tokens
- Filter by status (All / Pending / Completed)

### 3.3 Calendar Page
- Monthly view (default)
- Tasks displayed on their deadline dates
- Highlight dates with tasks
- Navigation: previous/next month

### 3.4 Notification Center
- List of mock notifications
- Types: "Deadline tomorrow", "Task pending", "Tokens earned"
- Static/simulated — no real push notifications

### 3.5 Tokens / Points Page
- Display total token balance
- Token history list (optional display)
- Tokens earned per completed task

### 3.6 Lien Score Page
- **Formula:** `(completed tasks / total tasks) × 100`
- Weekly scope
- Progress bar visualization
- Stats: tasks completed this week, total tasks

### 3.7 Shop Page
- Grid of mock items
- Each item: name, token cost, "Redeem" button
- Items (UI only, no real purchase):
  - T-shirt: 15 tokens
  - Coffee: 10 tokens
  - Notebook: 5 tokens
  - Hoodie: 25 tokens

---

## 4. Navigation

**Left Sidebar** with icons and labels:
1. Add Reel
2. Tasks
3. Calendar
4. Notifications
5. Tokens
6. Lien Score
7. Shop

**Layout:**
- Left: Fixed sidebar (240px width)
- Right: Scrollable content area
- Mobile: Sidebar collapses to hamburger menu

---

## 5. Data Models

### Task
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

### UserStats
```typescript
{
  totalTokens: number;
  weeklyCompletedTasks: number;
  weeklyTotalTasks: number;
  lifetimeCompletedTasks: number;
}
```

### Notification
```typescript
{
  id: string;
  type: 'deadline' | 'pending' | 'reward';
  message: string;
  read: boolean;
  createdAt: string;
}
```

---

## 6. Mock AI Extraction Logic

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

---

## 7. Gamification Rules

| Action | Reward |
|--------|--------|
| Complete a task | +5 tokens (default) |
| Redeem shop item | -item cost |
| Lien Score update | Real-time on task completion |

---

## 8. UI Design Direction

- **Aesthetic:** Clean, modern, gamified
- **Color Palette:**
  - Primary: Indigo/Violet (#6366f1)
  - Success: Green (#22c55e)
  - Warning: Amber (#f59e0b)
  - Background: Slate/Gray tones
  - Cards: White with subtle shadows
- **Typography:** Sans-serif (Inter or system)
- **Layout:** Sidebar + main content area
- **Animations:** Smooth transitions on page change, button feedback, token count animations

---

## 9. Out of Scope (Prototype)

- Real Instagram/Reel API integration
- Real AI-powered content extraction
- Backend server or database
- User authentication
- Actual purchase/reward fulfillment
- Push notifications (real device)

---

## 10. File Structure (Proposed)

```
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

## 11. User Flow

1. User lands on app → redirected to Tasks page
2. Clicks "Add Reel" in sidebar
3. Pastes a reel URL
4. Clicks "Convert to Task"
5. System generates mock task, saves to state
6. User sees new task in Tasks list and Calendar
7. User marks task complete → tokens awarded, Lien Score updates
8. User visits Shop to see items (spending is UI-only)

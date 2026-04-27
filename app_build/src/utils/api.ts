export const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000').replace(/\/$/, '');

// ── Tasks ──────────────────────────────────────────────────────

export async function dbGetTasks() {
  const res = await fetch(`${API_BASE_URL}/db/tasks`);
  if (!res.ok) throw new Error('Failed to fetch tasks');
  return res.json();
}

export async function dbCreateTask(task: object) {
  const res = await fetch(`${API_BASE_URL}/db/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(task),
  });
  if (!res.ok) throw new Error('Failed to save task');
  return res.json();
}

export async function dbCompleteTask(taskId: string) {
  const res = await fetch(`${API_BASE_URL}/db/tasks/${taskId}/complete`, {
    method: 'PATCH',
  });
  if (!res.ok) throw new Error('Failed to complete task');
  return res.json();
}

// ── Stats ──────────────────────────────────────────────────────

export async function dbGetStats() {
  const res = await fetch(`${API_BASE_URL}/db/stats`);
  if (!res.ok) throw new Error('Failed to fetch stats');
  return res.json();
}

export async function dbSaveStats(stats: object) {
  const res = await fetch(`${API_BASE_URL}/db/stats`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(stats),
  });
  if (!res.ok) throw new Error('Failed to save stats');
  return res.json();
}

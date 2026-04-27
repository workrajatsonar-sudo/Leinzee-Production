The uiux for the taksks page

<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Tasks | Reel-to-Action</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "tertiary-container": "#f8a010",
                    "secondary": "#6bff8f",
                    "on-tertiary-container": "#4a2c00",
                    "primary-fixed": "#9396ff",
                    "on-secondary-container": "#e4ffe2",
                    "on-tertiary-fixed-variant": "#563400",
                    "tertiary": "#ffb148",
                    "on-primary-container": "#0a0081",
                    "on-background": "#dee5ff",
                    "inverse-primary": "#494bd7",
                    "surface-dim": "#060e20",
                    "secondary-container": "#006e2f",
                    "secondary-dim": "#5bf083",
                    "on-tertiary": "#573500",
                    "primary-container": "#9396ff",
                    "on-secondary": "#005f28",
                    "surface-variant": "#192540",
                    "error-container": "#a70138",
                    "secondary-fixed-dim": "#5bf083",
                    "surface-tint": "#a3a6ff",
                    "inverse-surface": "#faf8ff",
                    "surface": "#060e20",
                    "tertiary-dim": "#e79400",
                    "on-tertiary-fixed": "#2a1700",
                    "outline-variant": "#40485d",
                    "on-secondary-fixed-variant": "#006a2d",
                    "inverse-on-surface": "#4d556b",
                    "primary": "#a3a6ff",
                    "on-error-container": "#ffb2b9",
                    "surface-container-highest": "#192540",
                    "tertiary-fixed-dim": "#e79400",
                    "on-surface": "#dee5ff",
                    "surface-container": "#0f1930",
                    "on-secondary-fixed": "#004a1d",
                    "primary-fixed-dim": "#8387ff",
                    "on-error": "#490013",
                    "secondary-fixed": "#6bff8f",
                    "on-surface-variant": "#a3aac4",
                    "surface-container-lowest": "#000000",
                    "primary-dim": "#6063ee",
                    "on-primary": "#0f00a4",
                    "surface-bright": "#1f2b49",
                    "background": "#060e20",
                    "error-dim": "#d73357",
                    "on-primary-fixed": "#000000",
                    "tertiary-fixed": "#f8a010",
                    "on-primary-fixed-variant": "#0e009d",
                    "error": "#ff6e84",
                    "surface-container-high": "#141f38",
                    "outline": "#6d758c",
                    "surface-container-low": "#091328"
            },
            "borderRadius": {
                    "DEFAULT": "1rem",
                    "lg": "2rem",
                    "xl": "3rem",
                    "full": "9999px"
            },
            "fontFamily": {
                    "headline": ["Plus Jakarta Sans"],
                    "body": ["Inter"],
                    "label": ["Inter"]
            }
          },
        },
      }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        body {
            background-color: #060e20;
            color: #dee5ff;
            font-family: 'Inter', sans-serif;
        }
        .glass-card {
            background: rgba(25, 37, 64, 0.6);
            backdrop-filter: blur(24px);
        }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="min-h-screen pb-32">
<!-- TopAppBar -->
<header class="fixed top-0 w-full z-50 bg-[#060e20]/80 backdrop-blur-xl flex items-center justify-between px-6 h-16 w-full shadow-none">
<div class="flex items-center gap-4">
<button class="text-[#a3a6ff] hover:bg-[#192540] transition-colors p-2 rounded-full active:scale-95 transition-transform">
<span class="material-symbols-outlined">menu</span>
</button>
<h1 class="text-xl font-black text-[#a3a6ff] tracking-tighter font-['Plus_Jakarta_Sans']">Reel-to-Action</h1>
</div>
<div class="flex items-center gap-3">
<div class="bg-[#192540] rounded-full px-3 py-1 flex items-center gap-2">
<span class="material-symbols-outlined text-secondary text-sm" style="font-variation-settings: 'FILL' 1;">stars</span>
<span class="text-xs font-bold font-label uppercase tracking-widest text-[#a3a6ff]">1,240</span>
</div>
<div class="w-10 h-10 rounded-full overflow-hidden border border-outline-variant/20">
<img class="w-full h-full object-cover" data-alt="close-up portrait of a young professional man with a friendly expression in a modern office setting" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBUXx_tfyvAjdpU2AL-HayiisodQCS1Gno64fO9qknc-4tB9aRs0QbX2cekuP97s6JcewRxVQoDHQZawU69N6HufuiORidSXi_tM7rGoDR_qSHklu4WtuHE3F2O1LS0Qwc9nhO8A9Buw3pPcRKxDo-SToCve_UwRPMJGYLL-ZikN6awwNgGzMTqlCexD5pwyE7YquW-EjHHo-KjK0Ur3AyQXz7ObZ4brTmDRiz-EOGAjJzBrrsRXyWS-zJ5nmQRNJAu64WnbrKmOQ"/>
</div>
</div>
</header>
<main class="pt-24 px-6 max-w-5xl mx-auto">
<!-- Hero Section / Title -->
<div class="mb-8">
<span class="text-secondary font-label text-xs font-bold uppercase tracking-[0.2em]">Productivity Engine</span>
<h2 class="text-4xl md:text-5xl font-headline font-extrabold tracking-tight mt-2 text-on-surface">Your Tasks</h2>
</div>
<!-- Filter Tabs -->
<div class="flex gap-2 mb-10 overflow-x-auto pb-2 no-scrollbar">
<button class="bg-primary text-on-primary px-6 py-2 rounded-full text-sm font-bold transition-all shadow-lg shadow-primary/20">All</button>
<button class="bg-surface-container-highest text-on-surface-variant px-6 py-2 rounded-full text-sm font-bold hover:bg-surface-bright transition-all">Pending</button>
<button class="bg-surface-container-highest text-on-surface-variant px-6 py-2 rounded-full text-sm font-bold hover:bg-surface-bright transition-all">Completed</button>
</div>
<!-- Task List Section -->
<div class="space-y-4">
<!-- Task Card: Urgent -->
<div class="group relative bg-surface-container-high rounded-lg p-6 shadow-xl transition-all hover:translate-y-[-4px] flex flex-col md:flex-row md:items-center justify-between gap-6 border border-outline-variant/10">
<div class="flex-1">
<div class="flex items-center gap-3 mb-2">
<span class="bg-tertiary/10 text-tertiary text-[10px] font-bold uppercase tracking-widest px-2 py-1 rounded border border-tertiary/20">Due Soon</span>
<span class="text-on-surface-variant text-xs font-medium">Reel Editing Phase 1</span>
</div>
<h3 class="text-xl font-headline font-bold text-on-surface mb-1">Finalize Viral Script Hook</h3>
<div class="flex items-center gap-2 text-on-surface-variant">
<span class="material-symbols-outlined text-sm">calendar_month</span>
<span class="text-sm font-label">Oct 24, 2023 • 5:00 PM</span>
</div>
</div>
<div class="flex items-center gap-4">
<button class="bg-primary hover:bg-primary-dim text-on-primary px-6 py-3 rounded-full font-bold text-sm shadow-lg shadow-primary/25 transition-all active:scale-95 flex items-center gap-2">
                        Mark Complete
                    </button>
</div>
</div>
<!-- Task Card: Pending -->
<div class="group relative bg-surface-container-high rounded-lg p-6 shadow-xl transition-all hover:translate-y-[-4px] flex flex-col md:flex-row md:items-center justify-between gap-6 border border-outline-variant/10">
<div class="flex-1">
<div class="flex items-center gap-3 mb-2">
<span class="bg-secondary/10 text-secondary text-[10px] font-bold uppercase tracking-widest px-2 py-1 rounded border border-secondary/20">Active</span>
<span class="text-on-surface-variant text-xs font-medium">Marketing Strategy</span>
</div>
<h3 class="text-xl font-headline font-bold text-on-surface mb-1">Reach out to 5 Influencers</h3>
<div class="flex items-center gap-2 text-on-surface-variant">
<span class="material-symbols-outlined text-sm">calendar_month</span>
<span class="text-sm font-label">Oct 26, 2023 • 10:00 AM</span>
</div>
</div>
<div class="flex items-center gap-4">
<button class="bg-primary hover:bg-primary-dim text-on-primary px-6 py-3 rounded-full font-bold text-sm shadow-lg shadow-primary/25 transition-all active:scale-95 flex items-center gap-2">
                        Mark Complete
                    </button>
</div>
</div>
<!-- Task Card: Completed -->
<div class="group relative bg-surface-container-low opacity-60 rounded-lg p-6 flex flex-col md:flex-row md:items-center justify-between gap-6 border border-outline-variant/5">
<div class="flex-1">
<div class="flex items-center gap-3 mb-2">
<span class="bg-outline-variant/20 text-on-surface-variant text-[10px] font-bold uppercase tracking-widest px-2 py-1 rounded">Finished</span>
</div>
<h3 class="text-xl font-headline font-bold text-on-surface-variant mb-1 line-through decoration-primary/40">Optimize YouTube SEO Tags</h3>
<div class="flex items-center gap-2 text-on-surface-variant/70">
<span class="material-symbols-outlined text-sm">check_circle</span>
<span class="text-sm font-label">Completed Yesterday</span>
</div>
</div>
<div class="flex items-center gap-4">
<div class="bg-secondary/20 text-secondary w-12 h-12 rounded-full flex items-center justify-center">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">check_circle</span>
</div>
</div>
</div>
<!-- Task Card: Pending 2 -->
<div class="group relative bg-surface-container-high rounded-lg p-6 shadow-xl transition-all hover:translate-y-[-4px] flex flex-col md:flex-row md:items-center justify-between gap-6 border border-outline-variant/10">
<div class="flex-1">
<div class="flex items-center gap-3 mb-2">
<span class="bg-primary/10 text-primary text-[10px] font-bold uppercase tracking-widest px-2 py-1 rounded border border-primary/20">Standard</span>
<span class="text-on-surface-variant text-xs font-medium">Daily Routine</span>
</div>
<h3 class="text-xl font-headline font-bold text-on-surface mb-1">Check Daily Dashboard Metrics</h3>
<div class="flex items-center gap-2 text-on-surface-variant">
<span class="material-symbols-outlined text-sm">calendar_month</span>
<span class="text-sm font-label">Today • 11:59 PM</span>
</div>
</div>
<div class="flex items-center gap-4">
<button class="bg-primary hover:bg-primary-dim text-on-primary px-6 py-3 rounded-full font-bold text-sm shadow-lg shadow-primary/25 transition-all active:scale-95 flex items-center gap-2">
                        Mark Complete
                    </button>
</div>
</div>
</div>
<!-- Empty State Hint (Subtle) -->
<div class="mt-12 text-center">
<p class="text-on-surface-variant text-sm font-label italic">All caught up? High performance breeds high rewards.</p>
</div>
</main>
<!-- BottomNavBar -->
<nav class="fixed bottom-0 left-0 w-full flex justify-around items-center px-4 pb-6 pt-3 bg-[#060e20]/90 backdrop-blur-lg z-50 rounded-t-[2rem] shadow-[0_-10px_30px_rgba(0,0,0,0.3)]">
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined">add</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider mt-1">Add</span>
</a>
<a class="flex flex-col items-center justify-center text-[#6bff8f] bg-[#192540] rounded-full px-6 py-2 active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">format_list_bulleted</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider mt-1">Tasks</span>
</a>
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined">toll</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider mt-1">Tokens</span>
</a>
</nav>
</body></html>

converting reel page \

<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Add Reel - Reel-to-Action</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "tertiary-container": "#f8a010",
                        "secondary": "#6bff8f",
                        "on-tertiary-container": "#4a2c00",
                        "primary-fixed": "#9396ff",
                        "on-secondary-container": "#e4ffe2",
                        "on-tertiary-fixed-variant": "#563400",
                        "tertiary": "#ffb148",
                        "on-primary-container": "#0a0081",
                        "on-background": "#dee5ff",
                        "inverse-primary": "#494bd7",
                        "surface-dim": "#060e20",
                        "secondary-container": "#006e2f",
                        "secondary-dim": "#5bf083",
                        "on-tertiary": "#573500",
                        "primary-container": "#9396ff",
                        "on-secondary": "#005f28",
                        "surface-variant": "#192540",
                        "error-container": "#a70138",
                        "secondary-fixed-dim": "#5bf083",
                        "surface-tint": "#a3a6ff",
                        "inverse-surface": "#faf8ff",
                        "surface": "#060e20",
                        "tertiary-dim": "#e79400",
                        "on-tertiary-fixed": "#2a1700",
                        "outline-variant": "#40485d",
                        "on-secondary-fixed-variant": "#006a2d",
                        "inverse-on-surface": "#4d556b",
                        "primary": "#a3a6ff",
                        "on-error-container": "#ffb2b9",
                        "surface-container-highest": "#192540",
                        "tertiary-fixed-dim": "#e79400",
                        "on-surface": "#dee5ff",
                        "surface-container": "#0f1930",
                        "on-secondary-fixed": "#004a1d",
                        "primary-fixed-dim": "#8387ff",
                        "on-error": "#490013",
                        "secondary-fixed": "#6bff8f",
                        "on-surface-variant": "#a3aac4",
                        "surface-container-lowest": "#000000",
                        "primary-dim": "#6063ee",
                        "on-primary": "#0f00a4",
                        "surface-bright": "#1f2b49",
                        "background": "#060e20",
                        "error-dim": "#d73357",
                        "on-primary-fixed": "#000000",
                        "tertiary-fixed": "#f8a010",
                        "on-primary-fixed-variant": "#0e009d",
                        "error": "#ff6e84",
                        "surface-container-high": "#141f38",
                        "outline": "#6d758c",
                        "surface-container-low": "#091328"
                    },
                    "borderRadius": {
                        "DEFAULT": "1rem",
                        "lg": "2rem",
                        "xl": "3rem",
                        "full": "9999px"
                    },
                    "fontFamily": {
                        "headline": ["Plus Jakarta Sans"],
                        "body": ["Inter"],
                        "label": ["Inter"]
                    }
                },
            }
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        body {
            background-color: #060e20;
            color: #dee5ff;
            font-family: 'Inter', sans-serif;
        }
        .glass-panel {
            background: rgba(25, 37, 64, 0.6);
            backdrop-filter: blur(24px);
        }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="min-h-screen pb-24">
<!-- TopAppBar -->
<header class="fixed top-0 w-full z-50 bg-[#060e20]/80 backdrop-blur-xl flex items-center justify-between px-6 h-16 w-full">
<div class="flex items-center gap-4">
<button class="text-[#a3a6ff] hover:bg-[#192540] transition-colors p-2 rounded-full active:scale-95 transition-transform">
<span class="material-symbols-outlined" data-icon="menu">menu</span>
</button>
<h1 class="font-['Plus_Jakarta_Sans'] font-bold tracking-tight text-xl font-black text-[#a3a6ff] tracking-tighter">Reel-to-Action</h1>
</div>
<div class="flex items-center gap-2">
<div class="bg-surface-container-highest px-3 py-1 rounded-full flex items-center gap-2">
<span class="material-symbols-outlined text-secondary text-sm" data-icon="stars" style="font-variation-settings: 'FILL' 1;">stars</span>
<span class="text-xs font-bold font-label tracking-wider">1,240</span>
</div>
</div>
</header>
<main class="pt-24 px-6 max-w-2xl mx-auto">
<!-- Hero Section -->
<div class="mb-12">
<span class="text-secondary font-label text-[10px] uppercase tracking-[0.2em] font-bold mb-2 block">New Workflow</span>
<h2 class="font-headline text-4xl font-extrabold tracking-tight mb-4 leading-tight">Capture <span class="text-primary italic">Inspiration</span>, Trigger Action.</h2>
<p class="text-on-surface-variant text-sm max-w-md leading-relaxed">Paste a short-form video link below. Our AI extracts key tutorials, recipes, or tips and turns them into trackable tasks.</p>
</div>
<!-- Input Section -->
<div class="space-y-6">
<div class="relative group">
<div class="absolute -inset-1 bg-gradient-to-r from-primary/20 to-secondary/20 rounded-lg blur opacity-25 group-focus-within:opacity-100 transition duration-1000 group-focus-within:duration-200"></div>
<div class="relative flex items-center">
<span class="absolute left-4 material-symbols-outlined text-on-surface-variant" data-icon="link">link</span>
<input class="w-full bg-surface-container-lowest border-none rounded-DEFAULT pl-12 pr-4 py-5 focus:ring-2 focus:ring-primary text-on-surface placeholder:text-outline font-body text-base shadow-inner" placeholder="Paste reel link here..." type="text"/>
</div>
</div>
<button class="w-full py-4 bg-gradient-to-r from-primary to-primary-dim text-on-primary font-headline font-bold text-lg rounded-DEFAULT shadow-[0_10px_30px_rgba(163,166,255,0.3)] active:scale-95 transition-all flex items-center justify-center gap-2">
<span class="material-symbols-outlined" data-icon="bolt" style="font-variation-settings: 'FILL' 1;">bolt</span>
                Convert to Task
            </button>
</div>
<!-- Success Feedback Area -->
<div class="mt-16">
<div class="flex items-center justify-between mb-6">
<h3 class="font-headline text-lg font-bold text-on-surface flex items-center gap-2">
<span class="w-2 h-2 rounded-full bg-secondary"></span>
                    Recently Generated
                </h3>
<span class="text-on-surface-variant text-[10px] font-label uppercase tracking-widest">Success Feedback</span>
</div>
<!-- Task Card Preview -->
<div class="glass-panel rounded-lg p-1 overflow-hidden relative group">
<div class="absolute top-0 right-0 p-4 z-10">
<div class="bg-secondary text-on-secondary px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-tighter shadow-lg">
                        Verified Task
                    </div>
</div>
<div class="flex flex-col md:flex-row gap-6 p-4">
<!-- Media Thumbnail -->
<div class="w-full md:w-32 h-48 md:h-32 rounded-DEFAULT overflow-hidden bg-surface-container-lowest shrink-0 shadow-2xl relative">
<img alt="Kitchen setup" class="w-full h-full object-cover opacity-60" data-alt="Close-up of fresh organic ingredients and kitchen tools on a dark rustic table with warm atmospheric lighting" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBZY7TwrfgUMkcYhwDbt_M7vkobrGE8L1W2U2ds6PWm0aFyXLQ8qOjSiBdhgpCwWJiBDHPvumnh3ev3YWL2FcGSzaTggJYfFzt-lPvUzeqUQpRsr4kF1aYUxAMMNqjGUJxtab_1kK71nWSDIvwHKM_h_IYhMT_Tdmdl0I3CyGLAqn6U19x6s0JDkLvhUHv7TzWU3mibOCGgYqtNifIriRIt84828dwi5QKmtsaLbOwFE-Kd7BZvzlWe0gC0-Z21Qd0_XrmEQaMbXg"/>
<div class="absolute inset-0 flex items-center justify-center">
<span class="material-symbols-outlined text-primary text-3xl" data-icon="play_circle" style="font-variation-settings: 'FILL' 1;">play_circle</span>
</div>
</div>
<!-- Content -->
<div class="flex-1 space-y-3 py-1">
<div>
<p class="text-[10px] font-label text-primary font-bold uppercase tracking-widest mb-1">Recipe Automation</p>
<h4 class="font-headline text-xl font-bold leading-tight">Mastering 15-Min Sourdough Pasta</h4>
</div>
<div class="flex flex-wrap gap-2">
<div class="flex items-center gap-1.5 px-3 py-1 bg-surface-container rounded-full text-[10px] font-semibold text-on-surface-variant">
<span class="material-symbols-outlined text-[14px]" data-icon="timer">timer</span>
                                15 Mins
                            </div>
<div class="flex items-center gap-1.5 px-3 py-1 bg-surface-container rounded-full text-[10px] font-semibold text-on-surface-variant">
<span class="material-symbols-outlined text-[14px]" data-icon="restaurant">restaurant</span>
                                Beginner Friendly
                            </div>
</div>
<div class="pt-2 border-t border-outline-variant/10">
<div class="flex items-center gap-3">
<div class="w-8 h-8 rounded-full bg-surface-container-highest flex items-center justify-center">
<span class="material-symbols-outlined text-secondary text-lg" data-icon="checklist">checklist</span>
</div>
<span class="text-sm font-medium text-on-surface">3 Action steps generated</span>
<button class="ml-auto text-primary text-sm font-bold flex items-center gap-1 hover:gap-2 transition-all">
                                    View
                                    <span class="material-symbols-outlined text-sm" data-icon="chevron_right">chevron_right</span>
</button>
</div>
</div>
</div>
</div>
</div>
<!-- Gamified Lien Score Update -->
<div class="mt-4 flex items-center justify-between p-4 bg-surface-container-low rounded-DEFAULT border border-outline-variant/5">
<div class="flex items-center gap-4">
<div class="w-10 h-10 rounded-full bg-gradient-to-br from-tertiary/20 to-tertiary-container/10 flex items-center justify-center">
<span class="material-symbols-outlined text-tertiary" data-icon="trending_up">trending_up</span>
</div>
<div>
<p class="text-xs text-on-surface-variant font-medium">Daily Lien Score</p>
<p class="text-sm font-bold text-on-surface">+15 Points earned</p>
</div>
</div>
<div class="text-right">
<p class="text-xl font-black font-headline text-on-surface">2,450</p>
</div>
</div>
</div>
</main>
<!-- BottomNavBar -->
<nav class="fixed bottom-0 left-0 w-full flex justify-around items-center px-4 pb-6 pt-3 bg-[#060e20]/90 backdrop-blur-lg shadow-[0_-10px_30px_rgba(0,0,0,0.3)] rounded-t-[2rem] z-50">
<a class="flex flex-col items-center justify-center text-[#6bff8f] bg-[#192540] rounded-full px-6 py-2 active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined" data-icon="add" style="font-variation-settings: 'FILL' 1;">add</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider mt-0.5">Add</span>
</a>
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined" data-icon="format_list_bulleted">format_list_bulleted</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider mt-0.5">Tasks</span>
</a>
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined" data-icon="toll">toll</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider mt-0.5">Tokens</span>
</a>
</nav>
</body></html>

calendar uiux

<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Calendar - Reel-to-Action</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "tertiary-container": "#f8a010",
                        "secondary": "#6bff8f",
                        "on-tertiary-container": "#4a2c00",
                        "primary-fixed": "#9396ff",
                        "on-secondary-container": "#e4ffe2",
                        "on-tertiary-fixed-variant": "#563400",
                        "tertiary": "#ffb148",
                        "on-primary-container": "#0a0081",
                        "on-background": "#dee5ff",
                        "inverse-primary": "#494bd7",
                        "surface-dim": "#060e20",
                        "secondary-container": "#006e2f",
                        "secondary-dim": "#5bf083",
                        "on-tertiary": "#573500",
                        "primary-container": "#9396ff",
                        "on-secondary": "#005f28",
                        "surface-variant": "#192540",
                        "error-container": "#a70138",
                        "secondary-fixed-dim": "#5bf083",
                        "surface-tint": "#a3a6ff",
                        "inverse-surface": "#faf8ff",
                        "surface": "#060e20",
                        "tertiary-dim": "#e79400",
                        "on-tertiary-fixed": "#2a1700",
                        "outline-variant": "#40485d",
                        "on-secondary-fixed-variant": "#006a2d",
                        "inverse-on-surface": "#4d556b",
                        "primary": "#a3a6ff",
                        "on-error-container": "#ffb2b9",
                        "surface-container-highest": "#192540",
                        "tertiary-fixed-dim": "#e79400",
                        "on-surface": "#dee5ff",
                        "surface-container": "#0f1930",
                        "on-secondary-fixed": "#004a1d",
                        "primary-fixed-dim": "#8387ff",
                        "on-error": "#490013",
                        "secondary-fixed": "#6bff8f",
                        "on-surface-variant": "#a3aac4",
                        "surface-container-lowest": "#000000",
                        "primary-dim": "#6063ee",
                        "on-primary": "#0f00a4",
                        "surface-bright": "#1f2b49",
                        "background": "#060e20",
                        "error-dim": "#d73357",
                        "on-primary-fixed": "#000000",
                        "tertiary-fixed": "#f8a010",
                        "on-primary-fixed-variant": "#0e009d",
                        "error": "#ff6e84",
                        "surface-container-high": "#141f38",
                        "outline": "#6d758c",
                        "surface-container-low": "#091328"
                    },
                    "borderRadius": {
                        "DEFAULT": "1rem",
                        "lg": "2rem",
                        "xl": "3rem",
                        "full": "9999px"
                    },
                    "fontFamily": {
                        "headline": ["Plus Jakarta Sans"],
                        "body": ["Inter"],
                        "label": ["Inter"]
                    }
                },
            },
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        body {
            background-color: #060e20;
            color: #dee5ff;
            font-family: 'Inter', sans-serif;
        }
        .calendar-grid {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
        }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="bg-surface text-on-surface min-h-screen pb-32">
<!-- TopAppBar -->
<header class="bg-[#060e20]/80 backdrop-blur-xl fixed top-0 w-full z-50 flex items-center justify-between px-6 h-16 w-full">
<div class="flex items-center gap-4">
<button class="text-[#a3a6ff] hover:bg-[#192540] transition-colors p-2 rounded-full active:scale-95 transition-transform">
<span class="material-symbols-outlined">menu</span>
</button>
<h1 class="text-xl font-black text-[#a3a6ff] tracking-tighter font-['Plus_Jakarta_Sans']">Reel-to-Action</h1>
</div>
<div class="flex items-center gap-3">
<button class="text-[#a3aac4] hover:bg-[#192540] transition-colors p-2 rounded-full">
<span class="material-symbols-outlined">search</span>
</button>
<div class="w-8 h-8 rounded-full bg-surface-container-highest flex items-center justify-center overflow-hidden border border-outline-variant/20">
<img class="w-full h-full object-cover" data-alt="close-up portrait of a professional woman with a friendly expression in high-key studio lighting" src="https://lh3.googleusercontent.com/aida-public/AB6AXuC67VuoPSNVSwLkl9xQR6vPeKbmwPdp6gHDFJp8RAY9LML22V6K8uG8pndbF_2ixKD2ICdv1sSI-doQAjr1q3mQY7Rgo7PjrT_HG2aE_CI3KhvzrmJYVX8l2zxFSaECIH38E0HjKo-xyuv3F4tovKOqKv6FUdtFRXke6I4kW1mv_mB7CbvLM0BgC7ikYG42dv_EewirPnGB1GmifRVj4mCY_wKpvwFVE_HZSVspv0tyWqkNNbZdPCx1oUcGn4Mx1RJD-i_blZwK5g"/>
</div>
</div>
</header>
<main class="pt-24 px-6 max-w-4xl mx-auto">
<!-- Calendar Header Section -->
<section class="flex items-end justify-between mb-8">
<div class="space-y-1">
<span class="text-sm font-label uppercase tracking-widest text-primary font-bold">Time Management</span>
<h2 class="text-4xl font-headline font-extrabold tracking-tight">October 2024</h2>
</div>
<div class="flex gap-2">
<button class="w-12 h-12 rounded-full bg-surface-container-high flex items-center justify-center hover:bg-surface-container-highest transition-colors active:scale-90 border border-outline-variant/10">
<span class="material-symbols-outlined text-on-surface-variant">chevron_left</span>
</button>
<button class="w-12 h-12 rounded-full bg-surface-container-high flex items-center justify-center hover:bg-surface-container-highest transition-colors active:scale-90 border border-outline-variant/10">
<span class="material-symbols-outlined text-on-surface-variant">chevron_right</span>
</button>
</div>
</section>
<!-- Calendar Month Grid -->
<section class="bg-surface-container-low rounded-lg p-6 mb-12 shadow-xl border border-outline-variant/5">
<div class="calendar-grid mb-4">
<div class="text-center py-2 text-xs font-bold uppercase tracking-widest text-on-surface-variant/60">Sun</div>
<div class="text-center py-2 text-xs font-bold uppercase tracking-widest text-on-surface-variant/60">Mon</div>
<div class="text-center py-2 text-xs font-bold uppercase tracking-widest text-on-surface-variant/60">Tue</div>
<div class="text-center py-2 text-xs font-bold uppercase tracking-widest text-on-surface-variant/60">Wed</div>
<div class="text-center py-2 text-xs font-bold uppercase tracking-widest text-on-surface-variant/60">Thu</div>
<div class="text-center py-2 text-xs font-bold uppercase tracking-widest text-on-surface-variant/60">Fri</div>
<div class="text-center py-2 text-xs font-bold uppercase tracking-widest text-on-surface-variant/60">Sat</div>
</div>
<div class="calendar-grid gap-2">
<!-- Row 1 (Empty offset) -->
<div class="aspect-square flex items-center justify-center text-on-surface-variant/20 font-medium">29</div>
<div class="aspect-square flex items-center justify-center text-on-surface-variant/20 font-medium">30</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">1</span>
<div class="absolute bottom-2 w-1.5 h-1.5 bg-secondary rounded-full"></div>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">2</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">3</span>
<div class="absolute bottom-2 w-1.5 h-1.5 bg-tertiary rounded-full"></div>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">4</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">5</span>
</div>
<!-- Row 2 -->
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">6</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">7</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer bg-primary-container/20 rounded-full border border-primary/30 shadow-[0_0_20px_rgba(163,166,255,0.2)]">
<span class="z-10 font-bold text-primary">8</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">9</span>
<div class="absolute bottom-2 w-1.5 h-1.5 bg-primary rounded-full"></div>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">10</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">11</span>
<div class="absolute bottom-2 flex gap-1">
<div class="w-1 h-1 bg-secondary rounded-full"></div>
<div class="w-1 h-1 bg-primary rounded-full"></div>
</div>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">12</span>
</div>
<!-- Row 3 -->
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">13</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">14</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">15</span>
<div class="absolute bottom-2 w-1.5 h-1.5 bg-secondary rounded-full"></div>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">16</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">17</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">18</span>
<div class="absolute bottom-2 w-1.5 h-1.5 bg-primary rounded-full"></div>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">19</span>
</div>
<!-- Row 4 -->
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">20</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">21</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">22</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">23</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">24</span>
<div class="absolute bottom-2 w-1.5 h-1.5 bg-primary rounded-full"></div>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">25</span>
</div>
<div class="aspect-square flex items-center justify-center relative group cursor-pointer hover:bg-surface-container-highest rounded-DEFAULT transition-all">
<span class="z-10">26</span>
</div>
</div>
</section>
<!-- Tasks Due Today Section -->
<section class="space-y-6">
<div class="flex items-center justify-between">
<h3 class="text-2xl font-headline font-bold">Tasks Due Today</h3>
<span class="px-4 py-1 bg-surface-container-highest rounded-full text-xs font-bold uppercase tracking-wider text-primary border border-primary/20">3 Items</span>
</div>
<div class="space-y-4">
<!-- Task Card 1 -->
<div class="bg-surface-container-high p-5 rounded-lg flex items-center gap-4 group hover:bg-surface-container-highest transition-all duration-300 border-l-4 border-primary">
<div class="flex-shrink-0 w-12 h-12 rounded-DEFAULT bg-primary/10 flex items-center justify-center">
<span class="material-symbols-outlined text-primary">video_stable</span>
</div>
<div class="flex-grow">
<h4 class="font-bold text-lg mb-1 group-hover:text-primary transition-colors">Finalize Reel Edit: Morning Routine</h4>
<div class="flex gap-4">
<span class="text-sm text-on-surface-variant flex items-center gap-1">
<span class="material-symbols-outlined text-sm">schedule</span> 09:00 AM
                            </span>
<span class="text-sm text-on-surface-variant flex items-center gap-1">
<span class="material-symbols-outlined text-sm">toll</span> +250 Tokens
                            </span>
</div>
</div>
<button class="w-10 h-10 rounded-full border border-outline-variant/30 flex items-center justify-center hover:bg-primary hover:text-on-primary transition-all active:scale-90">
<span class="material-symbols-outlined">check</span>
</button>
</div>
<!-- Task Card 2 -->
<div class="bg-surface-container-high p-5 rounded-lg flex items-center gap-4 group hover:bg-surface-container-highest transition-all duration-300 border-l-4 border-secondary">
<div class="flex-shrink-0 w-12 h-12 rounded-DEFAULT bg-secondary/10 flex items-center justify-center">
<span class="material-symbols-outlined text-secondary">fitness_center</span>
</div>
<div class="flex-grow">
<h4 class="font-bold text-lg mb-1 group-hover:text-secondary transition-colors">Post-Workout Action Log</h4>
<div class="flex gap-4">
<span class="text-sm text-on-surface-variant flex items-center gap-1">
<span class="material-symbols-outlined text-sm">schedule</span> 11:30 AM
                            </span>
<span class="text-sm text-on-surface-variant flex items-center gap-1">
<span class="material-symbols-outlined text-sm">stars</span> +150 Points
                            </span>
</div>
</div>
<button class="w-10 h-10 rounded-full border border-outline-variant/30 flex items-center justify-center hover:bg-secondary hover:text-on-secondary transition-all active:scale-90">
<span class="material-symbols-outlined">check</span>
</button>
</div>
<!-- Task Card 3 -->
<div class="bg-surface-container-high p-5 rounded-lg flex items-center gap-4 group hover:bg-surface-container-highest transition-all duration-300 border-l-4 border-tertiary">
<div class="flex-shrink-0 w-12 h-12 rounded-DEFAULT bg-tertiary/10 flex items-center justify-center">
<span class="material-symbols-outlined text-tertiary">notification_important</span>
</div>
<div class="flex-grow">
<h4 class="font-bold text-lg mb-1 group-hover:text-tertiary transition-colors">Review Engagement Analytics</h4>
<div class="flex gap-4">
<span class="text-sm text-on-surface-variant flex items-center gap-1">
<span class="material-symbols-outlined text-sm">schedule</span> 04:00 PM
                            </span>
<span class="text-sm text-on-surface-variant flex items-center gap-1">
<span class="material-symbols-outlined text-sm">bolt</span> Urgent
                            </span>
</div>
</div>
<button class="w-10 h-10 rounded-full border border-outline-variant/30 flex items-center justify-center hover:bg-tertiary hover:text-on-tertiary transition-all active:scale-90">
<span class="material-symbols-outlined">check</span>
</button>
</div>
</div>
</section>
</main>
<!-- BottomNavBar -->
<nav class="fixed bottom-0 left-0 w-full bg-[#060e20]/90 backdrop-blur-lg flex justify-around items-center px-4 pb-6 pt-3 z-50 rounded-t-[2rem] shadow-[0_-10px_30px_rgba(0,0,0,0.3)]">
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined mb-1">add</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Add</span>
</a>
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined mb-1">format_list_bulleted</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Tasks</span>
</a>
<a class="flex flex-col items-center justify-center text-[#6bff8f] bg-[#192540] rounded-full px-6 py-2 transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined mb-1">calendar_month</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Calendar</span>
</a>
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined mb-1">toll</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Tokens</span>
</a>
</nav>
</body></html>

Notification tab

<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Notifications | Reel-to-Action</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "tertiary-container": "#f8a010",
                    "secondary": "#6bff8f",
                    "on-tertiary-container": "#4a2c00",
                    "primary-fixed": "#9396ff",
                    "on-secondary-container": "#e4ffe2",
                    "on-tertiary-fixed-variant": "#563400",
                    "tertiary": "#ffb148",
                    "on-primary-container": "#0a0081",
                    "on-background": "#dee5ff",
                    "inverse-primary": "#494bd7",
                    "surface-dim": "#060e20",
                    "secondary-container": "#006e2f",
                    "secondary-dim": "#5bf083",
                    "on-tertiary": "#573500",
                    "primary-container": "#9396ff",
                    "on-secondary": "#005f28",
                    "surface-variant": "#192540",
                    "error-container": "#a70138",
                    "secondary-fixed-dim": "#5bf083",
                    "surface-tint": "#a3a6ff",
                    "inverse-surface": "#faf8ff",
                    "surface": "#060e20",
                    "tertiary-dim": "#e79400",
                    "on-tertiary-fixed": "#2a1700",
                    "outline-variant": "#40485d",
                    "on-secondary-fixed-variant": "#006a2d",
                    "inverse-on-surface": "#4d556b",
                    "primary": "#a3a6ff",
                    "on-error-container": "#ffb2b9",
                    "surface-container-highest": "#192540",
                    "tertiary-fixed-dim": "#e79400",
                    "on-surface": "#dee5ff",
                    "surface-container": "#0f1930",
                    "on-secondary-fixed": "#004a1d",
                    "primary-fixed-dim": "#8387ff",
                    "on-error": "#490013",
                    "secondary-fixed": "#6bff8f",
                    "on-surface-variant": "#a3aac4",
                    "surface-container-lowest": "#000000",
                    "primary-dim": "#6063ee",
                    "on-primary": "#0f00a4",
                    "surface-bright": "#1f2b49",
                    "background": "#060e20",
                    "error-dim": "#d73357",
                    "on-primary-fixed": "#000000",
                    "tertiary-fixed": "#f8a010",
                    "on-primary-fixed-variant": "#0e009d",
                    "error": "#ff6e84",
                    "surface-container-high": "#141f38",
                    "outline": "#6d758c",
                    "surface-container-low": "#091328"
            },
            "borderRadius": {
                    "DEFAULT": "1rem",
                    "lg": "2rem",
                    "xl": "3rem",
                    "full": "9999px"
            },
            "fontFamily": {
                    "headline": ["Plus Jakarta Sans"],
                    "body": ["Inter"],
                    "label": ["Inter"]
            }
          },
        },
      }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        body {
            background-color: #060e20;
            color: #dee5ff;
            font-family: 'Inter', sans-serif;
        }
        .glass-card {
            background: rgba(25, 37, 64, 0.6);
            backdrop-filter: blur(24px);
        }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="min-h-screen">
<!-- TopAppBar -->
<header class="bg-[#060e20]/80 backdrop-blur-xl fixed top-0 w-full z-50 flex items-center justify-between px-6 h-16 w-full">
<div class="flex items-center gap-4">
<span class="material-symbols-outlined text-[#a3a6ff] cursor-pointer active:scale-95 transition-transform" data-icon="menu">menu</span>
<h1 class="font-['Plus_Jakarta_Sans'] font-bold tracking-tight text-xl font-black text-[#a3a6ff] tracking-tighter">Reel-to-Action</h1>
</div>
<div class="flex items-center gap-4">
<div class="w-8 h-8 rounded-full overflow-hidden bg-surface-container-highest">
<img class="w-full h-full object-cover" data-alt="professional male portrait with soft blue studio lighting and modern aesthetic" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBgTOJCuDiPrZc1PmDtmTAOb6Wi5g0DbKcXnD0VBIsh4nD5xRu5XrJQPbr_WnEv9NVDTI-8yrS1Le4L5gGAFOOCWwRN67yF0yuDOR6c0Ds37i0W3LlRvPt37Jw_PfYwf1US5gTqRPPzFtcJXOEnUuXpDThBbJvtzkl15sQVC5oAZ-_j9GfBNca00eGiZxvfG10ajcHIL4UbqUKOK37lVCq0Gqu1zIObkI5W0x5hq9aRTBogItdH6Z8Q_c_hJk_NeaBIV7BK79nQTA"/>
</div>
</div>
</header>
<!-- NavigationDrawer (Sidebar - Desktop) -->
<aside class="hidden md:flex fixed inset-y-0 left-0 w-[240px] z-[60] bg-[#060e20]/95 backdrop-blur-2xl flex flex-col p-6 gap-4 shadow-[20px_0_40px_rgba(0,0,0,0.4)]">
<div class="mb-8">
<h2 class="font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest text-[#a3a6ff]">Menu</h2>
</div>
<nav class="flex flex-col gap-2">
<a class="flex items-center gap-3 px-4 py-3 text-[#a3aac4] hover:text-[#6bff8f] transition-all hover:translate-x-1 duration-300 font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">
<span class="material-symbols-outlined" data-icon="add_circle">add_circle</span> Add Reel
            </a>
<a class="flex items-center gap-3 px-4 py-3 text-[#a3aac4] hover:text-[#6bff8f] transition-all hover:translate-x-1 duration-300 font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">
<span class="material-symbols-outlined" data-icon="checklist">checklist</span> Tasks
            </a>
<a class="flex items-center gap-3 px-4 py-3 text-[#a3aac4] hover:text-[#6bff8f] transition-all hover:translate-x-1 duration-300 font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">
<span class="material-symbols-outlined" data-icon="calendar_month">calendar_month</span> Calendar
            </a>
<a class="flex items-center gap-3 px-4 py-3 text-[#a3a6ff] bg-[#192540] rounded-full transition-all hover:translate-x-1 duration-300 font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">
<span class="material-symbols-outlined" data-icon="notifications">notifications</span> Notifications
            </a>
<a class="flex items-center gap-3 px-4 py-3 text-[#a3aac4] hover:text-[#6bff8f] transition-all hover:translate-x-1 duration-300 font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">
<span class="material-symbols-outlined" data-icon="stars">stars</span> Tokens
            </a>
<a class="flex items-center gap-3 px-4 py-3 text-[#a3aac4] hover:text-[#6bff8f] transition-all hover:translate-x-1 duration-300 font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">
<span class="material-symbols-outlined" data-icon="leaderboard">leaderboard</span> Lien Score
            </a>
<a class="flex items-center gap-3 px-4 py-3 text-[#a3aac4] hover:text-[#6bff8f] transition-all hover:translate-x-1 duration-300 font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">
<span class="material-symbols-outlined" data-icon="shopping_bag">shopping_bag</span> Shop
            </a>
</nav>
</aside>
<!-- Main Content Canvas -->
<main class="pt-24 pb-32 px-6 md:ml-[240px] max-w-4xl mx-auto">
<header class="mb-10 relative">
<span class="label-sm text-[10px] uppercase tracking-[0.2em] text-primary font-bold">Activity Feed</span>
<h2 class="text-4xl md:text-5xl font-headline font-extrabold text-on-surface tracking-tighter mt-2">Notifications</h2>
<div class="absolute -top-12 -right-12 w-64 h-64 bg-primary/10 rounded-full blur-[100px] -z-10"></div>
</header>
<!-- Notifications List -->
<div class="flex flex-col gap-4">
<!-- Deadline Card -->
<div class="surface-container-low p-6 rounded-lg flex items-start gap-5 relative group transition-all hover:bg-surface-container hover:translate-y-[-2px]">
<div class="flex-shrink-0 w-12 h-12 rounded-full bg-tertiary/10 flex items-center justify-center text-tertiary">
<span class="material-symbols-outlined text-2xl" data-icon="schedule">schedule</span>
</div>
<div class="flex-grow">
<div class="flex items-center justify-between mb-1">
<h3 class="font-headline font-bold text-lg text-on-surface">Deadline Approaching</h3>
<span class="text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">2m ago</span>
</div>
<p class="text-on-surface-variant text-sm leading-relaxed max-w-md">Your task "Quarterly Growth Strategy" is due in less than 2 hours. Submit your progress reel now.</p>
</div>
<div class="w-3 h-3 bg-tertiary rounded-full shadow-[0_0_12px_rgba(255,177,72,0.6)] mt-2"></div>
</div>
<!-- Reward Card -->
<div class="surface-container-low p-6 rounded-lg flex items-start gap-5 relative group transition-all hover:bg-surface-container hover:translate-y-[-2px]">
<div class="flex-shrink-0 w-12 h-12 rounded-full bg-secondary/10 flex items-center justify-center text-secondary">
<span class="material-symbols-outlined text-2xl" data-icon="stars" data-weight="fill" style="font-variation-settings: 'FILL' 1;">stars</span>
</div>
<div class="flex-grow">
<div class="flex items-center justify-between mb-1">
<h3 class="font-headline font-bold text-lg text-on-surface">Reward Earned</h3>
<span class="text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">1h ago</span>
</div>
<p class="text-on-surface-variant text-sm leading-relaxed max-w-md">Stellar performance! You've been awarded 50 Tokens for completing your weekly streak.</p>
</div>
<div class="w-3 h-3 bg-secondary rounded-full shadow-[0_0_12px_rgba(107,255,143,0.6)] mt-2"></div>
</div>
<!-- Pending Card -->
<div class="surface-container-low p-6 rounded-lg flex items-start gap-5 relative group transition-all hover:bg-surface-container hover:translate-y-[-2px]">
<div class="flex-shrink-0 w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center text-primary">
<span class="material-symbols-outlined text-2xl" data-icon="notification_important">notification_important</span>
</div>
<div class="flex-grow">
<div class="flex items-center justify-between mb-1">
<h3 class="font-headline font-bold text-lg text-on-surface">Pending Verification</h3>
<span class="text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">5h ago</span>
</div>
<p class="text-on-surface-variant text-sm leading-relaxed max-w-md">Your latest submission is being reviewed by the curator panel. Stay tuned for your Lien Score update.</p>
</div>
</div>
<!-- Yesterday Section -->
<div class="mt-8 mb-4">
<span class="font-headline font-bold text-xs uppercase tracking-[0.3em] text-outline">Yesterday</span>
</div>
<!-- Reward Card (Read) -->
<div class="surface-container-low/50 p-6 rounded-lg flex items-start gap-5 opacity-80">
<div class="flex-shrink-0 w-12 h-12 rounded-full bg-surface-container-highest flex items-center justify-center text-on-surface-variant">
<span class="material-symbols-outlined text-2xl" data-icon="toll">toll</span>
</div>
<div class="flex-grow">
<div class="flex items-center justify-between mb-1">
<h3 class="font-headline font-bold text-lg text-on-surface-variant">Tokens Redeemed</h3>
<span class="text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">24h ago</span>
</div>
<p class="text-on-surface-variant/70 text-sm leading-relaxed">You redeemed 200 Tokens for the "Aesthetic Motion" pack in the Shop.</p>
</div>
</div>
<!-- Deadline Card (Read) -->
<div class="surface-container-low/50 p-6 rounded-lg flex items-start gap-5 opacity-80">
<div class="flex-shrink-0 w-12 h-12 rounded-full bg-surface-container-highest flex items-center justify-center text-on-surface-variant">
<span class="material-symbols-outlined text-2xl" data-icon="timer">timer</span>
</div>
<div class="flex-grow">
<div class="flex items-center justify-between mb-1">
<h3 class="font-headline font-bold text-lg text-on-surface-variant">Task Completed</h3>
<span class="text-[10px] font-bold text-on-surface-variant uppercase tracking-widest">Yesterday</span>
</div>
<p class="text-on-surface-variant/70 text-sm leading-relaxed">Mission "Daily Motion Capture" was finished on time. Great consistency.</p>
</div>
</div>
</div>
<!-- Glass Detail Panel (Bento Style) -->
<div class="mt-16 grid grid-cols-1 md:grid-cols-2 gap-6">
<div class="glass-card p-8 rounded-lg relative overflow-hidden group">
<div class="z-10 relative">
<h4 class="font-headline font-bold text-xl mb-2 text-secondary">Summary</h4>
<p class="text-on-surface-variant text-sm">You have 3 unread high-priority notifications. Complete your actions to maintain your streak.</p>
</div>
<div class="absolute -bottom-4 -right-4 text-9xl text-white opacity-5 pointer-events-none material-symbols-outlined" data-icon="bolt">bolt</div>
</div>
<div class="bg-primary/10 p-8 rounded-lg border border-primary/20 flex flex-col justify-between">
<div>
<h4 class="font-headline font-bold text-xl mb-2 text-primary">Preferences</h4>
<p class="text-on-surface-variant text-sm">Customize how and when you receive action alerts.</p>
</div>
<button class="mt-4 self-start px-6 py-2 bg-primary text-on-primary rounded-full font-bold text-xs uppercase tracking-widest active:scale-95 transition-transform">Manage Settings</button>
</div>
</div>
</main>
<!-- BottomNavBar (Mobile) -->
<nav class="md:hidden fixed bottom-0 left-0 w-full flex justify-around items-center px-4 pb-6 pt-3 bg-[#060e20]/90 backdrop-blur-lg shadow-[0_-10px_30px_rgba(0,0,0,0.3)] rounded-t-[2rem] z-50">
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined" data-icon="add">add</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Add</span>
</a>
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined" data-icon="format_list_bulleted">format_list_bulleted</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Tasks</span>
</a>
<a class="flex flex-col items-center justify-center text-[#6bff8f] bg-[#192540] rounded-full px-6 py-2 transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined" data-icon="notifications" data-weight="fill" style="font-variation-settings: 'FILL' 1;">notifications</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Alerts</span>
</a>
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined" data-icon="toll">toll</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Tokens</span>
</a>
</nav>
</body></html>

Lein score page

<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Lien Score | Reel-to-Action</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "tertiary-container": "#f8a010",
                    "secondary": "#6bff8f",
                    "on-tertiary-container": "#4a2c00",
                    "primary-fixed": "#9396ff",
                    "on-secondary-container": "#e4ffe2",
                    "on-tertiary-fixed-variant": "#563400",
                    "tertiary": "#ffb148",
                    "on-primary-container": "#0a0081",
                    "on-background": "#dee5ff",
                    "inverse-primary": "#494bd7",
                    "surface-dim": "#060e20",
                    "secondary-container": "#006e2f",
                    "secondary-dim": "#5bf083",
                    "on-tertiary": "#573500",
                    "primary-container": "#9396ff",
                    "on-secondary": "#005f28",
                    "surface-variant": "#192540",
                    "error-container": "#a70138",
                    "secondary-fixed-dim": "#5bf083",
                    "surface-tint": "#a3a6ff",
                    "inverse-surface": "#faf8ff",
                    "surface": "#060e20",
                    "tertiary-dim": "#e79400",
                    "on-tertiary-fixed": "#2a1700",
                    "outline-variant": "#40485d",
                    "on-secondary-fixed-variant": "#006a2d",
                    "inverse-on-surface": "#4d556b",
                    "primary": "#a3a6ff",
                    "on-error-container": "#ffb2b9",
                    "surface-container-highest": "#192540",
                    "tertiary-fixed-dim": "#e79400",
                    "on-surface": "#dee5ff",
                    "surface-container": "#0f1930",
                    "on-secondary-fixed": "#004a1d",
                    "primary-fixed-dim": "#8387ff",
                    "on-error": "#490013",
                    "secondary-fixed": "#6bff8f",
                    "on-surface-variant": "#a3aac4",
                    "surface-container-lowest": "#000000",
                    "primary-dim": "#6063ee",
                    "on-primary": "#0f00a4",
                    "surface-bright": "#1f2b49",
                    "background": "#060e20",
                    "error-dim": "#d73357",
                    "on-primary-fixed": "#000000",
                    "tertiary-fixed": "#f8a010",
                    "on-primary-fixed-variant": "#0e009d",
                    "error": "#ff6e84",
                    "surface-container-high": "#141f38",
                    "outline": "#6d758c",
                    "surface-container-low": "#091328"
            },
            "borderRadius": {
                    "DEFAULT": "1rem",
                    "lg": "2rem",
                    "xl": "3rem",
                    "full": "9999px"
            },
            "fontFamily": {
                    "headline": ["Plus Jakarta Sans"],
                    "body": ["Inter"],
                    "label": ["Inter"]
            }
          },
        },
      }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .circular-progress {
            background: radial-gradient(closest-side, #060e20 79%, transparent 80% 100%),
                        conic-gradient(#a3a6ff 84%, #192540 0);
        }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="bg-surface text-on-surface font-body selection:bg-primary selection:text-on-primary">
<!-- TopAppBar -->
<header class="fixed top-0 w-full z-50 bg-[#060e20]/80 backdrop-blur-xl flex items-center justify-between px-6 h-16 w-full">
<div class="flex items-center gap-4">
<button class="text-[#a3a6ff] hover:bg-[#192540] transition-colors p-2 rounded-full active:scale-95 transition-transform">
<span class="material-symbols-outlined">menu</span>
</button>
<h1 class="font-['Plus_Jakarta_Sans'] font-bold tracking-tight text-xl font-black text-[#a3a6ff] tracking-tighter">Reel-to-Action</h1>
</div>
<div class="flex items-center gap-4">
<div class="hidden md:flex gap-6">
<a class="text-[#a3aac4] font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest hover:text-[#a3a6ff] transition-all" href="#">Add Reel</a>
<a class="text-[#a3aac4] font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest hover:text-[#a3a6ff] transition-all" href="#">Tasks</a>
<a class="text-[#a3a6ff] font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">Lien Score</a>
</div>
<div class="w-10 h-10 rounded-full bg-surface-container-highest flex items-center justify-center overflow-hidden">
<img class="w-full h-full object-cover" data-alt="close up portrait of a young man with a slight smile and confident expression in cinematic mood lighting" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCCZBXJwCGqANsZVmz1fZXWoZcOXNXnTQSOpdtNPbH8LWLvaW7p8LVZN_vkvcXeKHDwtiqEmPQq17eJa0BTJvidxhHN67s3nD1rz_88IGf9nF9K5E7FD4tNJ0FF7mkrUc1Od2C3ZhkukACKPkhbGHGt-eDFOzr1sW75xa-LgWoiVho1w9DD7GqzIUKxstRCvY2eV8Xb0KjMRwyRgrRBKgCZ2pPqKLf0xzqIS4mGOqQ-RxysnNSmlnrLtGPg_9DH-49VtZ285sIFWA"/>
</div>
</div>
</header>
<!-- Side Navigation (Web) -->
<aside class="fixed inset-y-0 left-0 w-[240px] z-[60] bg-[#060e20]/95 backdrop-blur-2xl hidden md:flex flex-col p-6 gap-4 shadow-[20px_0_40px_rgba(0,0,0,0.4)]">
<div class="text-[#a3a6ff] font-bold py-4">
<span class="font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest">Menu</span>
</div>
<nav class="flex flex-col gap-2">
<a class="flex items-center gap-4 px-4 py-3 text-[#a3aac4] hover:text-[#6bff8f] hover:translate-x-1 duration-300 transition-all font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">
<span class="material-symbols-outlined">add_circle</span> Add Reel
            </a>
<a class="flex items-center gap-4 px-4 py-3 text-[#a3aac4] hover:text-[#6bff8f] hover:translate-x-1 duration-300 transition-all font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">
<span class="material-symbols-outlined">checklist</span> Tasks
            </a>
<a class="flex items-center gap-4 px-4 py-3 text-[#a3aac4] hover:text-[#6bff8f] hover:translate-x-1 duration-300 transition-all font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">
<span class="material-symbols-outlined">calendar_month</span> Calendar
            </a>
<a class="flex items-center gap-4 px-4 py-3 text-[#a3a6ff] bg-[#192540] rounded-full font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">
<span class="material-symbols-outlined">leaderboard</span> Lien Score
            </a>
<a class="flex items-center gap-4 px-4 py-3 text-[#a3aac4] hover:text-[#6bff8f] hover:translate-x-1 duration-300 transition-all font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">
<span class="material-symbols-outlined">stars</span> Tokens
            </a>
<a class="flex items-center gap-4 px-4 py-3 text-[#a3aac4] hover:text-[#6bff8f] hover:translate-x-1 duration-300 transition-all font-['Plus_Jakarta_Sans'] text-sm font-semibold uppercase tracking-widest" href="#">
<span class="material-symbols-outlined">shopping_bag</span> Shop
            </a>
</nav>
</aside>
<main class="md:pl-[240px] pt-24 pb-32 px-6 min-h-screen">
<!-- Hero Section: Score Display -->
<section class="max-w-4xl mx-auto flex flex-col items-center">
<div class="relative w-72 h-72 md:w-96 md:h-96 flex items-center justify-center rounded-full circular-progress shadow-[0_0_80px_rgba(163,166,255,0.15)] group transition-all duration-700">
<div class="text-center z-10">
<span class="block font-headline text-[5rem] md:text-[8rem] font-extrabold leading-none tracking-tighter text-on-surface">84</span>
<span class="block font-label text-sm uppercase tracking-[0.2em] text-primary font-bold">Lien Score</span>
</div>
<!-- Ambient Glow Behind Progress -->
<div class="absolute inset-0 rounded-full bg-primary/10 blur-[60px] -z-10 group-hover:bg-primary/20 transition-all duration-500"></div>
</div>
<!-- Stats Row -->
<div class="mt-12 w-full grid grid-cols-1 md:grid-cols-2 gap-4">
<div class="bg-surface-container-low rounded-lg p-6 flex items-center justify-between shadow-none border-none">
<div>
<p class="text-on-surface-variant font-label text-xs uppercase tracking-widest mb-1">Weekly Task Volume</p>
<p class="text-2xl font-headline font-bold text-on-surface">24 of 28 <span class="text-secondary text-sm ml-2">Done</span></p>
</div>
<div class="w-12 h-12 rounded-full bg-secondary/10 flex items-center justify-center text-secondary">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">check_circle</span>
</div>
</div>
<div class="bg-surface-container-low rounded-lg p-6 flex items-center justify-between shadow-none border-none">
<div>
<p class="text-on-surface-variant font-label text-xs uppercase tracking-widest mb-1">Productivity Streak</p>
<p class="text-2xl font-headline font-bold text-on-surface">12 Days</p>
</div>
<div class="w-12 h-12 rounded-full bg-tertiary/10 flex items-center justify-center text-tertiary">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">local_fire_department</span>
</div>
</div>
</div>
<!-- Weekly Productivity Chart Section -->
<div class="mt-10 w-full bg-surface-container-low rounded-lg p-8">
<div class="flex justify-between items-end mb-8">
<div>
<h2 class="font-headline text-xl font-bold text-on-surface">Weekly Trend</h2>
<p class="text-on-surface-variant text-sm">Your action-to-reel ratio over the last 7 days</p>
</div>
<div class="flex gap-2">
<span class="w-3 h-3 rounded-full bg-primary inline-block"></span>
<span class="font-label text-[10px] uppercase tracking-wider text-on-surface-variant">Lien Power</span>
</div>
</div>
<!-- Simple Bar Chart -->
<div class="flex items-end justify-between h-48 gap-4 px-2">
<div class="flex flex-col items-center flex-1 group">
<div class="w-full bg-surface-container-highest rounded-t-full relative h-[40%] transition-all group-hover:bg-primary-dim">
<div class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-primary text-on-primary text-[10px] px-2 py-1 rounded font-bold">40%</div>
</div>
<span class="mt-4 font-label text-[10px] text-on-surface-variant font-bold">MON</span>
</div>
<div class="flex flex-col items-center flex-1 group">
<div class="w-full bg-surface-container-highest rounded-t-full relative h-[65%] transition-all group-hover:bg-primary-dim">
<div class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-primary text-on-primary text-[10px] px-2 py-1 rounded font-bold">65%</div>
</div>
<span class="mt-4 font-label text-[10px] text-on-surface-variant font-bold">TUE</span>
</div>
<div class="flex flex-col items-center flex-1 group">
<div class="w-full bg-surface-container-highest rounded-t-full relative h-[55%] transition-all group-hover:bg-primary-dim">
<div class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-primary text-on-primary text-[10px] px-2 py-1 rounded font-bold">55%</div>
</div>
<span class="mt-4 font-label text-[10px] text-on-surface-variant font-bold">WED</span>
</div>
<div class="flex flex-col items-center flex-1 group">
<div class="w-full bg-primary rounded-t-full relative h-[90%] transition-all">
<div class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-primary text-on-primary text-[10px] px-2 py-1 rounded font-bold">90%</div>
</div>
<span class="mt-4 font-label text-[10px] text-primary font-bold">THU</span>
</div>
<div class="flex flex-col items-center flex-1 group">
<div class="w-full bg-surface-container-highest rounded-t-full relative h-[70%] transition-all group-hover:bg-primary-dim">
<div class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-primary text-on-primary text-[10px] px-2 py-1 rounded font-bold">70%</div>
</div>
<span class="mt-4 font-label text-[10px] text-on-surface-variant font-bold">FRI</span>
</div>
<div class="flex flex-col items-center flex-1 group">
<div class="w-full bg-surface-container-highest rounded-t-full relative h-[45%] transition-all group-hover:bg-primary-dim">
<div class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-primary text-on-primary text-[10px] px-2 py-1 rounded font-bold">45%</div>
</div>
<span class="mt-4 font-label text-[10px] text-on-surface-variant font-bold">SAT</span>
</div>
<div class="flex flex-col items-center flex-1 group">
<div class="w-full bg-surface-container-highest rounded-t-full relative h-[30%] transition-all group-hover:bg-primary-dim">
<div class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-primary text-on-primary text-[10px] px-2 py-1 rounded font-bold">30%</div>
</div>
<span class="mt-4 font-label text-[10px] text-on-surface-variant font-bold">SUN</span>
</div>
</div>
</div>
<!-- Bento Card: Milestones -->
<div class="mt-10 w-full grid grid-cols-1 md:grid-cols-3 gap-6">
<div class="bg-surface-container-high rounded-lg p-6 border-none flex flex-col justify-between h-48">
<span class="material-symbols-outlined text-secondary text-3xl">military_tech</span>
<div>
<h3 class="font-headline font-bold text-on-surface">Top 1% Rank</h3>
<p class="text-xs text-on-surface-variant uppercase tracking-widest mt-2">Elite Curator</p>
</div>
</div>
<div class="bg-primary/20 rounded-lg p-6 flex flex-col justify-between h-48 relative overflow-hidden backdrop-blur-xl group">
<div class="absolute -right-4 -top-4 w-24 h-24 bg-primary/20 blur-3xl rounded-full"></div>
<span class="material-symbols-outlined text-primary text-3xl">bolt</span>
<div>
<h3 class="font-headline font-bold text-on-surface">Next Reward</h3>
<div class="w-full bg-surface-container-lowest h-1.5 rounded-full mt-3 overflow-hidden">
<div class="bg-primary h-full w-[80%] rounded-full"></div>
</div>
<p class="text-[10px] text-on-surface-variant uppercase tracking-widest mt-2">800/1000 Tokens</p>
</div>
</div>
<div class="bg-surface-container-high rounded-lg p-6 border-none flex flex-col justify-between h-48">
<span class="material-symbols-outlined text-tertiary text-3xl">speed</span>
<div>
<h3 class="font-headline font-bold text-on-surface">Focus Flow</h3>
<p class="text-xs text-on-surface-variant uppercase tracking-widest mt-2">+12% vs last week</p>
</div>
</div>
</div>
</section>
</main>
<!-- BottomNavBar (Mobile) -->
<nav class="md:hidden fixed bottom-0 left-0 w-full flex justify-around items-center px-4 pb-6 pt-3 bg-[#060e20]/90 backdrop-blur-lg z-50 rounded-t-[2rem] shadow-[0_-10px_30px_rgba(0,0,0,0.3)]">
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined">add</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Add</span>
</a>
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined">format_list_bulleted</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Tasks</span>
</a>
<a class="flex flex-col items-center justify-center text-[#6bff8f] bg-[#192540] rounded-full px-6 py-2 active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined">leaderboard</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Score</span>
</a>
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined">toll</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Tokens</span>
</a>
</nav>
</body></html>

Tokens page

<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "tertiary-container": "#f8a010",
                    "secondary": "#6bff8f",
                    "on-tertiary-container": "#4a2c00",
                    "primary-fixed": "#9396ff",
                    "on-secondary-container": "#e4ffe2",
                    "on-tertiary-fixed-variant": "#563400",
                    "tertiary": "#ffb148",
                    "on-primary-container": "#0a0081",
                    "on-background": "#dee5ff",
                    "inverse-primary": "#494bd7",
                    "surface-dim": "#060e20",
                    "secondary-container": "#006e2f",
                    "secondary-dim": "#5bf083",
                    "on-tertiary": "#573500",
                    "primary-container": "#9396ff",
                    "on-secondary": "#005f28",
                    "surface-variant": "#192540",
                    "error-container": "#a70138",
                    "secondary-fixed-dim": "#5bf083",
                    "surface-tint": "#a3a6ff",
                    "inverse-surface": "#faf8ff",
                    "surface": "#060e20",
                    "tertiary-dim": "#e79400",
                    "on-tertiary-fixed": "#2a1700",
                    "outline-variant": "#40485d",
                    "on-secondary-fixed-variant": "#006a2d",
                    "inverse-on-surface": "#4d556b",
                    "primary": "#a3a6ff",
                    "on-error-container": "#ffb2b9",
                    "surface-container-highest": "#192540",
                    "tertiary-fixed-dim": "#e79400",
                    "on-surface": "#dee5ff",
                    "surface-container": "#0f1930",
                    "on-secondary-fixed": "#004a1d",
                    "primary-fixed-dim": "#8387ff",
                    "on-error": "#490013",
                    "secondary-fixed": "#6bff8f",
                    "on-surface-variant": "#a3aac4",
                    "surface-container-lowest": "#000000",
                    "primary-dim": "#6063ee",
                    "on-primary": "#0f00a4",
                    "surface-bright": "#1f2b49",
                    "background": "#060e20",
                    "error-dim": "#d73357",
                    "on-primary-fixed": "#000000",
                    "tertiary-fixed": "#f8a010",
                    "on-primary-fixed-variant": "#0e009d",
                    "error": "#ff6e84",
                    "surface-container-high": "#141f38",
                    "outline": "#6d758c",
                    "surface-container-low": "#091328"
            },
            "borderRadius": {
                    "DEFAULT": "1rem",
                    "lg": "2rem",
                    "xl": "3rem",
                    "full": "9999px"
            },
            "fontFamily": {
                    "headline": ["Plus Jakarta Sans"],
                    "body": ["Inter"],
                    "label": ["Inter"]
            }
          },
        },
      }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        body {
            background-color: #060e20;
            color: #dee5ff;
            font-family: 'Inter', sans-serif;
        }
        .glass-card {
            background: rgba(25, 37, 64, 0.6);
            backdrop-filter: blur(24px);
        }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="bg-surface selection:bg-primary selection:text-on-primary">
<!-- TopAppBar -->
<header class="fixed top-0 w-full z-50 bg-[#060e20]/80 backdrop-blur-xl flex items-center justify-between px-6 h-16 w-full">
<div class="flex items-center gap-4">
<button class="text-[#a3a6ff] hover:bg-[#192540] transition-colors p-2 rounded-full active:scale-95 transition-transform">
<span class="material-symbols-outlined" data-icon="menu">menu</span>
</button>
<span class="text-xl font-black text-[#a3a6ff] tracking-tighter font-['Plus_Jakarta_Sans']">Reel-to-Action</span>
</div>
<div class="flex items-center gap-2">
<div class="bg-[#192540] rounded-full px-4 py-1.5 flex items-center gap-2">
<span class="material-symbols-outlined text-[#6bff8f] text-sm" data-icon="stars" style="font-variation-settings: 'FILL' 1;">stars</span>
<span class="font-bold text-xs text-[#dee5ff]">2,450</span>
</div>
</div>
</header>
<main class="pt-24 pb-32 px-6 max-w-5xl mx-auto">
<!-- Hero Token Balance Section -->
<section class="relative mb-12">
<div class="absolute -top-24 -left-24 w-64 h-64 bg-primary/20 blur-[120px] rounded-full pointer-events-none"></div>
<div class="absolute -bottom-12 right-0 w-48 h-48 bg-secondary/10 blur-[100px] rounded-full pointer-events-none"></div>
<div class="glass-card p-10 rounded-lg flex flex-col items-center justify-center text-center overflow-hidden relative border border-outline-variant/10">
<!-- Background visual element -->
<div class="absolute top-0 right-0 p-8 opacity-10 rotate-12">
<span class="material-symbols-outlined text-9xl text-primary" data-icon="toll" style="font-variation-settings: 'FILL' 1;">toll</span>
</div>
<p class="font-headline text-sm font-bold uppercase tracking-[0.2em] text-on-surface-variant mb-4">Total Tokens</p>
<div class="flex items-center gap-4 mb-2">
<span class="material-symbols-outlined text-6xl md:text-8xl text-secondary" data-icon="toll" style="font-variation-settings: 'FILL' 1;">toll</span>
<h1 class="text-7xl md:text-9xl font-headline font-black text-on-surface tracking-tighter">2,450</h1>
</div>
<div class="mt-6 flex flex-wrap justify-center gap-3">
<button class="bg-gradient-to-r from-primary to-primary-dim text-on-primary px-8 py-3 rounded-full font-bold text-sm shadow-xl shadow-primary/20 hover:scale-105 active:scale-95 transition-all">
                        Earn More
                    </button>
<button class="bg-surface-container-highest text-on-surface px-8 py-3 rounded-full font-bold text-sm border border-outline-variant/15 hover:bg-surface-bright transition-all">
                        Withdraw
                    </button>
</div>
</div>
</section>
<!-- Stats Grid (Bento Style) -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
<div class="bg-surface-container-low p-6 rounded-lg flex flex-col gap-1">
<span class="text-on-surface-variant text-xs font-bold uppercase tracking-widest">This Week</span>
<span class="text-2xl font-headline font-bold text-secondary">+450</span>
<div class="h-1 w-full bg-surface-container-highest rounded-full mt-4 overflow-hidden">
<div class="h-full bg-secondary w-3/4"></div>
</div>
</div>
<div class="bg-surface-container-low p-6 rounded-lg flex flex-col gap-1">
<span class="text-on-surface-variant text-xs font-bold uppercase tracking-widest">Spent</span>
<span class="text-2xl font-headline font-bold text-tertiary">-120</span>
<div class="h-1 w-full bg-surface-container-highest rounded-full mt-4 overflow-hidden">
<div class="h-full bg-tertiary w-1/4"></div>
</div>
</div>
<div class="bg-surface-container-low p-6 rounded-lg flex flex-col gap-1">
<span class="text-on-surface-variant text-xs font-bold uppercase tracking-widest">Rank</span>
<span class="text-2xl font-headline font-bold text-primary">Elite</span>
<div class="flex gap-1 mt-4">
<div class="h-1 w-full bg-primary rounded-full"></div>
<div class="h-1 w-full bg-primary rounded-full"></div>
<div class="h-1 w-full bg-primary rounded-full"></div>
<div class="h-1 w-full bg-surface-container-highest rounded-full"></div>
</div>
</div>
</div>
<!-- Token History Section -->
<section>
<div class="flex items-center justify-between mb-8">
<h2 class="text-2xl font-headline font-extrabold text-on-surface tracking-tight">Token History</h2>
<button class="text-primary text-xs font-bold uppercase tracking-widest hover:underline">View All</button>
</div>
<div class="space-y-4">
<!-- History Item 1 -->
<div class="flex items-center justify-between p-5 bg-surface-container rounded-lg border border-outline-variant/5 hover:bg-surface-container-high transition-colors cursor-pointer group">
<div class="flex items-center gap-4">
<div class="w-12 h-12 rounded-full bg-secondary/10 flex items-center justify-center">
<span class="material-symbols-outlined text-secondary" data-icon="task_alt">task_alt</span>
</div>
<div>
<p class="font-bold text-on-surface group-hover:text-primary transition-colors">Task Completed</p>
<p class="text-xs text-on-surface-variant font-medium">Daily Workout Routine • Oct 24, 2023</p>
</div>
</div>
<div class="text-right">
<p class="font-headline font-black text-lg text-secondary">+50</p>
</div>
</div>
<!-- History Item 2 -->
<div class="flex items-center justify-between p-5 bg-surface-container-low rounded-lg border border-outline-variant/5 hover:bg-surface-container-high transition-colors cursor-pointer group">
<div class="flex items-center gap-4">
<div class="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center">
<span class="material-symbols-outlined text-primary" data-icon="celebration" style="font-variation-settings: 'FILL' 1;">celebration</span>
</div>
<div>
<p class="font-bold text-on-surface group-hover:text-primary transition-colors">Bonus Reward</p>
<p class="text-xs text-on-surface-variant font-medium">7-Day Consistency Streak • Oct 23, 2023</p>
</div>
</div>
<div class="text-right">
<p class="font-headline font-black text-lg text-secondary">+250</p>
</div>
</div>
<!-- History Item 3 -->
<div class="flex items-center justify-between p-5 bg-surface-container rounded-lg border border-outline-variant/5 hover:bg-surface-container-high transition-colors cursor-pointer group">
<div class="flex items-center gap-4">
<div class="w-12 h-12 rounded-full bg-tertiary/10 flex items-center justify-center">
<span class="material-symbols-outlined text-tertiary" data-icon="redeem">redeem</span>
</div>
<div>
<p class="font-bold text-on-surface group-hover:text-primary transition-colors">Item Redeemed</p>
<p class="text-xs text-on-surface-variant font-medium">Premium UI Pack • Oct 21, 2023</p>
</div>
</div>
<div class="text-right">
<p class="font-headline font-black text-lg text-tertiary">-100</p>
</div>
</div>
<!-- History Item 4 -->
<div class="flex items-center justify-between p-5 bg-surface-container-low rounded-lg border border-outline-variant/5 hover:bg-surface-container-high transition-colors cursor-pointer group">
<div class="flex items-center gap-4">
<div class="w-12 h-12 rounded-full bg-secondary/10 flex items-center justify-center">
<span class="material-symbols-outlined text-secondary" data-icon="rocket_launch" style="font-variation-settings: 'FILL' 1;">rocket_launch</span>
</div>
<div>
<p class="font-bold text-on-surface group-hover:text-primary transition-colors">Task Completed</p>
<p class="text-xs text-on-surface-variant font-medium">Learn 10 new words • Oct 20, 2023</p>
</div>
</div>
<div class="text-right">
<p class="font-headline font-black text-lg text-secondary">+25</p>
</div>
</div>
</div>
</section>
<!-- Promotion Card -->
<section class="mt-16 bg-[#192540]/40 rounded-lg p-8 relative overflow-hidden flex flex-col md:flex-row items-center gap-8 border border-primary/20">
<div class="md:w-2/3 z-10">
<h3 class="text-3xl font-headline font-black text-on-surface mb-2">Power Up Your Action</h3>
<p class="text-on-surface-variant mb-6 max-w-md">Multiply your earnings by 2.5x with a Pro Membership. Unlock exclusive rewards and premium skins.</p>
<button class="bg-secondary text-on-secondary px-6 py-2.5 rounded-full font-bold text-sm hover:brightness-110 active:scale-95 transition-all">Go Pro Now</button>
</div>
<div class="md:w-1/3 relative z-10">
<div class="relative w-full aspect-square rounded-lg overflow-hidden rotate-3 shadow-2xl">
<img class="w-full h-full object-cover" data-alt="Abstract vibrant purple and blue flowing energy waves with glowing particles and neon lights high quality digital art" src="https://lh3.googleusercontent.com/aida-public/AB6AXuD9tKquo8HnOaRYgu7c3u-CqF6RpkWPrWw9nHwj3Vu23d4D19JZlCq9BToCASHC2iUUSMma1Iz7mpc7r3kNQRg-xi_vRqbinJFhga3bWYP-KwI5th7i1yQPDzxu46CC4sa4RV1zh65nlJxzLewmojWC91KuepIitG8PaVUr1toCwyIRhRkJhRp6hYf2acDYAhHQTPAK_0rXGgBcviGseqUPv8YVSnVOsjRnUEajO3BiR_szcQ2IEza6gC4kwUoenecAstfMtKlW2Q"/>
</div>
</div>
<!-- Decorative circle -->
<div class="absolute -right-20 -bottom-20 w-64 h-64 bg-primary/20 rounded-full blur-[80px]"></div>
</section>
</main>
<!-- BottomNavBar -->
<nav class="fixed bottom-0 left-0 w-full flex justify-around items-center px-4 pb-6 pt-3 bg-[#060e20]/90 backdrop-blur-lg z-50 rounded-t-[2rem] shadow-[0_-10px_30px_rgba(0,0,0,0.3)]">
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined" data-icon="add">add</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider mt-1">Add</span>
</a>
<a class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined" data-icon="format_list_bulleted">format_list_bulleted</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider mt-1">Tasks</span>
</a>
<a class="flex flex-col items-center justify-center text-[#6bff8f] bg-[#192540] rounded-full px-6 py-2 active:scale-90 duration-200" href="#">
<span class="material-symbols-outlined" data-icon="toll" style="font-variation-settings: 'FILL' 1;">toll</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider mt-1">Tokens</span>
</a>
</nav>
</body></html>

pages of shop

<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "tertiary-container": "#f8a010",
                        "secondary": "#6bff8f",
                        "on-tertiary-container": "#4a2c00",
                        "primary-fixed": "#9396ff",
                        "on-secondary-container": "#e4ffe2",
                        "on-tertiary-fixed-variant": "#563400",
                        "tertiary": "#ffb148",
                        "on-primary-container": "#0a0081",
                        "on-background": "#dee5ff",
                        "inverse-primary": "#494bd7",
                        "surface-dim": "#060e20",
                        "secondary-container": "#006e2f",
                        "secondary-dim": "#5bf083",
                        "on-tertiary": "#573500",
                        "primary-container": "#9396ff",
                        "on-secondary": "#005f28",
                        "surface-variant": "#192540",
                        "error-container": "#a70138",
                        "secondary-fixed-dim": "#5bf083",
                        "surface-tint": "#a3a6ff",
                        "inverse-surface": "#faf8ff",
                        "surface": "#060e20",
                        "tertiary-dim": "#e79400",
                        "on-tertiary-fixed": "#2a1700",
                        "outline-variant": "#40485d",
                        "on-secondary-fixed-variant": "#006a2d",
                        "inverse-on-surface": "#4d556b",
                        "primary": "#a3a6ff",
                        "on-error-container": "#ffb2b9",
                        "surface-container-highest": "#192540",
                        "tertiary-fixed-dim": "#e79400",
                        "on-surface": "#dee5ff",
                        "surface-container": "#0f1930",
                        "on-secondary-fixed": "#004a1d",
                        "primary-fixed-dim": "#8387ff",
                        "on-error": "#490013",
                        "secondary-fixed": "#6bff8f",
                        "on-surface-variant": "#a3aac4",
                        "surface-container-lowest": "#000000",
                        "primary-dim": "#6063ee",
                        "on-primary": "#0f00a4",
                        "surface-bright": "#1f2b49",
                        "background": "#060e20",
                        "error-dim": "#d73357",
                        "on-primary-fixed": "#000000",
                        "tertiary-fixed": "#f8a010",
                        "on-primary-fixed-variant": "#0e009d",
                        "error": "#ff6e84",
                        "surface-container-high": "#141f38",
                        "outline": "#6d758c",
                        "surface-container-low": "#091328"
                    },
                    "borderRadius": {
                        "DEFAULT": "1rem",
                        "lg": "2rem",
                        "xl": "3rem",
                        "full": "9999px"
                    },
                    "fontFamily": {
                        "headline": ["Plus Jakarta Sans"],
                        "body": ["Inter"],
                        "label": ["Inter"]
                    }
                },
            },
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        body {
            background-color: #060e20;
            color: #dee5ff;
            font-family: 'Inter', sans-serif;
        }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="bg-surface text-on-surface antialiased">
<header class="fixed top-0 w-full z-50 bg-[#060e20]/80 backdrop-blur-xl flex items-center justify-between px-6 h-16 w-full">
<div class="flex items-center gap-4">
<span class="material-symbols-outlined text-[#a3a6ff] cursor-pointer active:scale-95 transition-transform" data-icon="menu">menu</span>
<h1 class="font-['Plus_Jakarta_Sans'] font-bold tracking-tight text-xl font-black text-[#a3a6ff] tracking-tighter">Reel-to-Action</h1>
</div>
<div class="flex items-center gap-3 bg-surface-container-highest px-4 py-1.5 rounded-full shadow-none">
<span class="material-symbols-outlined text-tertiary text-sm" data-icon="stars" style="font-variation-settings: 'FILL' 1;">stars</span>
<span class="text-on-surface font-bold text-sm tracking-tight">42 Tokens</span>
</div>
</header>
<main class="pt-24 pb-32 px-6 max-w-5xl mx-auto">
<div class="mb-10">
<h2 class="font-headline text-4xl font-extrabold tracking-tighter text-on-surface mb-2">Exclusive Rewards</h2>
<p class="text-on-surface-variant text-sm font-medium uppercase tracking-[0.2em]">Redeem your hard-earned action tokens</p>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
<div class="group relative bg-surface-container-low rounded-lg overflow-hidden flex flex-col transition-all duration-300 hover:translate-y-[-4px]">
<div class="aspect-[4/3] w-full overflow-hidden bg-surface-container-lowest">
<img alt="Minimalist T-shirt" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="Minimalist white organic cotton t-shirt folded neatly on a dark slate surface with soft cinematic top lighting and deep shadows" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBUl4v59FrDQqRgnEczyitSu8_ff7hMoHMpML_6d1SCFr-yVX4AsartqP21IEJKuCj32IAsDnqPwiHwYrVCANR6SVQyJyUvmwg_hzHf3TKHoy3T_AXoQTl6AbtY2J2Cs_Y1xjRPsTlgzJ63E-VxP-x58QlxDdwa2AfiAZzwoAZVC8oH1yCYcUzOR9F-vOeduFD_ZxlbnB6q5xUBoIFEJoOf4eIvwQMTzsrgvLzxDB-7XBMqHnO5ypPGHt0FnrVE9OAfs---0HNmgQ"/>
</div>
<div class="p-6 flex flex-col flex-grow">
<div class="flex justify-between items-start mb-4">
<h3 class="font-headline text-xl font-bold text-on-surface tracking-tight">Classic "Action" Tee</h3>
<span class="bg-surface-variant text-primary font-bold text-xs px-3 py-1 rounded-full border border-outline-variant/20">15 Tokens</span>
</div>
<p class="text-on-surface-variant text-sm mb-8 leading-relaxed">High-quality organic cotton featuring the signature kinetic logo.</p>
<button class="mt-auto w-full py-4 rounded-full bg-gradient-to-r from-primary to-primary-dim text-on-primary font-bold tracking-wide active:scale-95 transition-all shadow-lg shadow-primary/20">
                        Redeem
                    </button>
</div>
</div>
<div class="group relative bg-surface-container-low rounded-lg overflow-hidden flex flex-col transition-all duration-300 hover:translate-y-[-4px]">
<div class="aspect-[4/3] w-full overflow-hidden bg-surface-container-lowest">
<img alt="Premium Coffee Beans" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="Bag of specialty coffee beans on a dark reflective surface with green neon accent lighting reflecting in the background" src="https://lh3.googleusercontent.com/aida-public/AB6AXuA1tzc1-MZ78xovM59tqnqa6uLi0JsKfHh32ijVCO05tlZvY8rz--IQt53t3VWIf_Dn1tPtB8p4vIPy0DI6vjjkG5g-0E-yio5c5mmKErR6KNc1hQ8zn7vG5gbneD72KEaBz1d36Vivs8cjLkUY072CcZww9L1WmZ3Eli4YmuGe0SMYQDsUKPf20aQllrYUBJ-nEEMiixXyxuSdd7_Cb7LV5ARNEUlia0_4g2GCO0MOhrUikTkOOG1UA-ezAXMsZbcVW9Bq2MWjXQ"/>
</div>
<div class="p-6 flex flex-col flex-grow">
<div class="flex justify-between items-start mb-4">
<h3 class="font-headline text-xl font-bold text-on-surface tracking-tight">Focus Brew Blend</h3>
<span class="bg-surface-variant text-primary font-bold text-xs px-3 py-1 rounded-full border border-outline-variant/20">10 Tokens</span>
</div>
<p class="text-on-surface-variant text-sm mb-8 leading-relaxed">Dark roast Ethiopian beans specifically curated for deep work sessions.</p>
<button class="mt-auto w-full py-4 rounded-full bg-gradient-to-r from-primary to-primary-dim text-on-primary font-bold tracking-wide active:scale-95 transition-all shadow-lg shadow-primary/20">
                        Redeem
                    </button>
</div>
</div>
<div class="group relative bg-surface-container-low rounded-lg overflow-hidden flex flex-col transition-all duration-300 hover:translate-y-[-4px]">
<div class="aspect-[4/3] w-full overflow-hidden bg-surface-container-lowest">
<img alt="Executive Notebook" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="Elegant black leather notebook with silver foil lettering on a dark wooden desk with dramatic indigo mood lighting" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAYBVZWOqUlbSb7GgFvH-qRhNasjuun8epPtlvDDI4_Iuf8P51cV_T-cYlVBa3gK0zm0uNOib6u8ICiKTDXkBE2MsFPCyka4jw7kNY99esCNVDstYV4Lz13VOL7gXwtbQSSGfnydwbMaV6ER3cqLlIBkWL-EsI-BrG8efdO_5WpIgbgxC_fTwW06ywzXmfTGqaABf_UNGFFJ3EH-gLXno8egvr2DoFJBlmYwo4qUnWswmTLuiRmymbEMtP_Ajw7xbXC4dSzGe6q8w"/>
</div>
<div class="p-6 flex flex-col flex-grow">
<div class="flex justify-between items-start mb-4">
<h3 class="font-headline text-xl font-bold text-on-surface tracking-tight">The Vision Ledger</h3>
<span class="bg-surface-variant text-tertiary font-bold text-xs px-3 py-1 rounded-full border border-outline-variant/20">25 Tokens</span>
</div>
<p class="text-on-surface-variant text-sm mb-8 leading-relaxed">Hardcover dot-grid notebook for mapping out your high-velocity projects.</p>
<button class="mt-auto w-full py-4 rounded-full bg-gradient-to-r from-primary to-primary-dim text-on-primary font-bold tracking-wide active:scale-95 transition-all shadow-lg shadow-primary/20">
                        Redeem
                    </button>
</div>
</div>
<div class="group relative bg-surface-container-low rounded-lg overflow-hidden flex flex-col opacity-80">
<div class="aspect-[4/3] w-full overflow-hidden bg-surface-container-lowest grayscale contrast-125">
<img alt="Pro Hoodie" class="w-full h-full object-cover" data-alt="Heavyweight black hoodie draped over a chair in a dark studio with harsh side lighting and deep tonal contrast" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCR4WXIiwA-ltrlhS053ofieRh6ABZMnwd-N5IOheGLmaOktnDVhMIXduoRiclkCumfMHsm9XRUNHQYTeEt3eOc0JEGbNMWg3DtYZ5Fmj8N4tJ6KOJEkOO6fPDxSQmLMMTzWS72BKzcB5AM-olY7Av5bA1uM8lFKPK0ytGJM0rl-wQTtMH6_hBmBfcOYrWd2gOE4VbNDsjAmPVvn6isWObsShF_hqvgjMMfP84Ev2nuqU0lVLaG7ONshjgKa6s0ujlFSlZJfgaDfQ"/>
<div class="absolute inset-0 bg-surface-container-lowest/40 flex items-center justify-center backdrop-blur-[2px]">
<span class="material-symbols-outlined text-on-surface-variant text-4xl" data-icon="lock">lock</span>
</div>
</div>
<div class="p-6 flex flex-col flex-grow">
<div class="flex justify-between items-start mb-4">
<h3 class="font-headline text-xl font-bold text-on-surface-variant tracking-tight">Elite Series Hoodie</h3>
<span class="bg-surface-container-highest text-on-surface-variant font-bold text-xs px-3 py-1 rounded-full">150 Tokens</span>
</div>
<p class="text-on-surface-variant text-sm mb-8 leading-relaxed">Limited edition heavyweight fleece for top-tier creators only.</p>
<button class="mt-auto w-full py-4 rounded-full bg-surface-container-highest text-outline font-bold tracking-wide cursor-not-allowed border border-outline-variant/10" disabled="">
                        Insufficient Tokens
                    </button>
</div>
</div>
</div>
<section class="mt-20 p-8 rounded-lg bg-gradient-to-br from-surface-container-high to-surface-container relative overflow-hidden">
<div class="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
<div class="max-w-md">
<h4 class="font-headline text-2xl font-bold text-secondary mb-2">Token Multiplier Active!</h4>
<p class="text-on-surface-variant text-sm leading-relaxed">Complete 3 daily reels today to earn a 2x bonus on your next task completion.</p>
</div>
<div class="bg-surface-container-lowest/50 backdrop-blur-md px-6 py-4 rounded-lg flex items-center gap-4">
<span class="material-symbols-outlined text-secondary" data-icon="bolt" style="font-variation-settings: 'FILL' 1;">bolt</span>
<div>
<div class="text-[10px] uppercase tracking-widest text-on-surface-variant font-bold">Current Boost</div>
<div class="text-xl font-black text-on-surface tracking-tighter">LEVEL 04</div>
</div>
</div>
</div>
<div class="absolute -right-20 -top-20 w-64 h-64 bg-secondary/10 blur-[100px] rounded-full"></div>
</section>
</main>
<nav class="fixed bottom-0 left-0 w-full z-50 rounded-t-[2rem] bg-[#060e20]/90 backdrop-blur-lg shadow-[0_-10px_30px_rgba(0,0,0,0.3)] flex justify-around items-center px-4 pb-6 pt-3">
<div class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200 cursor-pointer">
<span class="material-symbols-outlined mb-1" data-icon="add">add</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Add</span>
</div>
<div class="flex flex-col items-center justify-center text-[#a3aac4] hover:text-[#a3a6ff] transition-all active:scale-90 duration-200 cursor-pointer">
<span class="material-symbols-outlined mb-1" data-icon="format_list_bulleted">format_list_bulleted</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Tasks</span>
</div>
<div class="flex flex-col items-center justify-center text-[#6bff8f] bg-[#192540] rounded-full px-6 py-2 active:scale-90 duration-200 cursor-pointer">
<span class="material-symbols-outlined mb-1" data-icon="toll" style="font-variation-settings: 'FILL' 1;">toll</span>
<span class="font-['Inter'] text-[10px] font-bold uppercase tracking-wider">Shop</span>
</div>
</nav>
</body></html>

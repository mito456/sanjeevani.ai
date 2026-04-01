# Project File Structure

```
sanjeevini-frontend/
│
├── 📄 package.json                    # Dependencies and scripts
├── 📄 vite.config.js                  # Vite bundler config
├── 📄 tailwind.config.js              # Tailwind CSS theme
├── 📄 postcss.config.js               # PostCSS config
├── 📄 .eslintrc.json                  # ESLint rules
├── 📄 .gitignore                      # Git ignore patterns
├── 📄 .env.example                    # Environment template
│
├── 📄 index.html                      # HTML entry point
│
├── 📄 README.md                       # Full documentation (90+ KB)
├── 📄 GETTING_STARTED.md              # Quick start guide
├── 📄 DEVELOPMENT.md                  # Dev guide + best practices
│
├── 📁 public/                         # Static assets
│   └── 📄 index.html                  # (duplicated in root during build)
│
└── 📁 src/                            # Source code
    │
    ├── 📄 main.jsx                    # React entry point
    ├── 📄 App.jsx                     # Main app component + routing
    ├── 📄 index.css                   # Global styles + Tailwind
    │
    ├── 📁 components/                 # Reusable UI components
    │   ├── 📄 UI.jsx                  # 180+ lines
    │   │   ├── Button
    │   │   ├── Card
    │   │   ├── StatusBadge
    │   │   ├── RiskMeter
    │   │   ├── LoadingSpinner
    │   │   ├── AlertBox
    │   │   ├── Header
    │   │   └── Container
    │   │
    │   ├── 📄 Layout.jsx              # 120+ lines
    │   │   ├── Navigation (responsive)
    │   │   ├── Footer
    │   │   └── Layout wrapper
    │   │
    │   └── 📄 VoiceRecorder.jsx       # 150+ lines
    │       ├── VoiceRecorder
    │       └── TextToSpeech
    │
    ├── 📁 pages/                      # Page/route components
    │   ├── 📄 HomePage.jsx            # 260+ lines
    │   │   • Dashboard with status cards
    │   │   • Activity, mood, fall risk
    │   │   • Quick actions
    │   │   • Health tips
    │   │
    │   ├── 📄 RemindersPage.jsx       # 280+ lines
    │   │   • List reminders by category
    │   │   • Create/edit/delete reminders
    │   │   • Snooze and complete actions
    │   │   • Form modal
    │   │
    │   ├── 📄 MoodInsightsPage.jsx    # 300+ lines
    │   │   • Mood status display
    │   │   • Charts (line, pie, progress)
    │   │   • Historical analysis
    │   │   • Voice logging
    │   │
    │   └── 📄 EmergencyContactsPage.jsx # 320+ lines
    │       • Contact management
    │       • Emergency info display
    │       • Add/edit/delete contacts
    │       • Safety guidelines
    │
    ├── 📁 services/                   # API layer
    │   └── 📄 api.js                  # 100+ lines
    │       ├── profileAPI
    │       ├── activityAPI
    │       ├── routineAPI
    │       ├── reminderAPI
    │       ├── moodAPI
    │       ├── fallRiskAPI
    │       ├── alertAPI
    │       ├── emergencyAPI
    │       └── cognitiveAPI
    │
    ├── 📁 context/                    # React Context
    │   └── 📄 NotificationContext.jsx # 180+ lines
    │       ├── NotificationProvider
    │       ├── useNotification hook
    │       ├── NotificationContainer
    │       ├── AlertModal
    │       └── BrowserNotification
    │
    ├── 📁 hooks/                      # Custom React hooks
    │   └── 📄 useCustomHooks.js       # 280+ lines
    │       ├── useFetch
    │       ├── useForm
    │       ├── useLocalStorage
    │       ├── useDebounce
    │       ├── usePrevious
    │       ├── useMount/useUnmount
    │       ├── useAsync
    │       ├── useMediaQuery
    │       └── useViewport
    │
    ├── 📁 utils/                      # Helper functions
    │   └── 📄 helpers.js              # 400+ lines
    │       ├── Date formatting
    │       ├── Validation
    │       ├── Text utilities
    │       ├── Mood/Risk utilities
    │       ├── LocalStorage helpers
    │       ├── Notifications
    │       ├── Object utilities
    │       └── More...
    │
    └── 📁 constants/                  # App constants
        └── 📄 index.js                # 280+ lines
            ├── Routes
            ├── API config
            ├── Status types
            ├── Moods, Risks
            ├── Reminder types
            ├── Colors
            ├── Error messages
            └── Storage keys
```

## 📊 Code Statistics

- **Total Components**: 7 major components
- **Total Pages**: 4 full-featured pages
- **API Services**: 9 service modules
- **Custom Hooks**: 9 hooks
- **Helper Functions**: 40+ utilities
- **Constants**: 30+ constants
- **Total Lines of Code**: 2500+
- **Total Documentation**: 500+ lines

## 🎨 Component Hierarchy

```
App
├── NotificationProvider
│   ├── Layout
│   │   ├── Navigation
│   │   ├── Main Routes
│   │   │   ├── HomePage
│   │   │   ├── RemindersPage
│   │   │   ├── MoodInsightsPage
│   │   │   └── EmergencyContactsPage
│   │   └── Footer
```

## 📋 Features by Page

### HomePage (Dashboard)
- Welcome greeting with date
- Quick voice interaction button
- 3 primary status cards
- 4 quick stat cards
- Today's reminders list
- Quick action buttons
- Health tips
- Routine deviation alerts

### RemindersPage
- Categorized reminders (Today/Upcoming/Completed)
- Add reminder button
- Reminder detail cards with actions
- Complete, snooze, delete buttons
- Form modal for creating reminders
- Multiple reminder types
- Time-based scheduling

### MoodInsightsPage
- Current mood display with emoji
- Average score calculation
- Trend indicator
- Time period selector (7/14/30 days)
- Line chart showing mood trends
- Pie chart of mood distribution
- Progress bars for mood stats
- Voice mood logging
- Wellness recommendations

### EmergencyContactsPage
- Emergency information banner
- Quick alert button
- Emergency contact cards
- Add/edit/delete contacts
- Contact details (phone, email, address)
- Send alert to individual contacts
- Relationship tracking
- Safety guidelines

## 🔗 API Integration Points

Each page connects to specific API endpoints:

**HomePage**
- `GET /api/dashboard/stats` → Display stats
- `GET /api/get-mood-status` → Current mood
- `GET /api/get-fall-risk` → Risk assessment

**RemindersPage**
- `GET /api/reminders` → List all
- `POST /api/set-reminder` → Create
- `POST /api/reminders/{id}/complete` → Mark done
- `POST /api/reminders/{id}/snooze` → Snooze
- `DELETE /api/reminders/{id}` → Delete

**MoodInsightsPage**
- `GET /api/get-mood-status` → Current status
- `GET /api/mood/history` → Historical data
- `POST /api/mood/analyze-speech` → Voice analysis

**EmergencyContactsPage**
- `GET /api/emergency-contacts` → List contacts
- `POST /api/emergency-contacts` → Add contact
- `POST /api/emergency-contacts/{id}/notify` → Send alert

## 🎯 Key Features Across App

✅ **Voice Support**
- Speech recognition for input
- Text-to-speech for output
- Browser Speech API integration

✅ **Notifications**
- Toast notifications for feedback
- Browser notifications for alerts
- In-app notification center
- Context-based alerts

✅ **Responsive Design**
- Mobile-first approach
- Grid layouts
- Breakpoints: sm, md, lg
- Touch-friendly interactions

✅ **Accessibility**
- ARIA labels on interactive elements
- Keyboard navigation support
- High contrast colors (WCAG AA)
- 44x44px minimum touch targets
- Screen reader support

✅ **Data Visualization**
- Line charts for trends
- Pie charts for distribution
- Progress bars for metrics
- Status badges
- Risk meters

✅ **State Management**
- React Context for notifications
- useState for component state
- localStorage for persistence
- Custom hooks for logic

---

**Total Implementation**: Full frontend application with 2500+ lines of production-ready code

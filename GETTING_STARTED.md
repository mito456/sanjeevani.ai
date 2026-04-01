# Sanjeevini AI Frontend - Quick Start Guide 🚀

## What You Have

A complete, production-ready React web application frontend for the Sanjeevini AI healthcare assistant, designed specifically for elderly users with accessibility as a priority.

## ✨ Built-In Features

✅ **Mobile-First Responsive Design** - Works perfectly on phones, tablets, and desktops
✅ **Voice Interaction** - Speak to the assistant using speech recognition
✅ **Dashboard** - Real-time health metrics and status indicators
✅ **Reminder Management** - Create, track, and get notifications for reminders
✅ **Mood Tracking** - Log emotional wellbeing with charts and insights
✅ **Emergency Contacts** - Quick alerts to trusted contacts
✅ **Accessibility Features** - Large buttons, high contrast, keyboard navigation
✅ **Beautiful Healthcare UI** - Clean, professional design with soft colors
✅ **Notification System** - In-app alerts and browser notifications
✅ **Data Visualization** - Charts for mood trends and health metrics

## 📦 Included Files & Folders

```
sanjeevini-frontend/
├── src/
│   ├── components/         # Reusable UI components
│   ├── context/           # State management (notifications)
│   ├── pages/             # Page components (4 main pages)
│   ├── services/          # API integration layer
│   ├── hooks/             # Custom React hooks
│   ├── utils/             # Helper functions
│   ├── constants/         # App constants and configs
│   ├── App.jsx            # Main application
│   ├── main.jsx           # Entry point
│   └── index.css          # Global styles
├── public/                # Static assets
├── package.json           # Dependencies
├── tailwind.config.js     # Tailwind CSS config
├── vite.config.js         # Vite config
├── README.md              # Full documentation
├── DEVELOPMENT.md         # Development guide
├── .env.example           # Environment template
└── .gitignore             # Git ignore
```

## 🎯 Main Pages

1. **Home Dashboard** (`/`)
   - Activity status
   - Current mood
   - Fall risk assessment
   - Quick reminders
   - Health tips

2. **Reminders** (`/reminders`)
   - View all reminders
   - Create new reminders
   - Categorized by: Today, Upcoming, Completed
   - Snooze and complete actions

3. **Mood Insights** (`/mood`)
   - Current mood status
   - Mood trends chart
   - Historical data analysis
   - Mood distribution pie chart
   - Voice-based mood logging

4. **Emergency Contacts** (`/emergency`)
   - Manage trusted contacts
   - Send emergency alerts
   - Contact information storage
   - Safety guidelines

## 🛠️ Technology Stack

- **React 18.2** - UI framework
- **Vite** - Build tool (fast!)
- **Tailwind CSS** - Styling
- **React Router** - Navigation
- **Axios** - API calls
- **Recharts** - Data visualization
- **React Speech Recognition** - Voice input
- **React Icons** - Icon library
- **Date-fns** - Date formatting

## 🚀 Getting Started (5 Minutes)

### Step 1: Install Dependencies
```bash
cd sanjeevini-frontend
npm install
```

### Step 2: Start Development Server
```bash
npm run dev
```
Opens at `http://localhost:3000`

### Step 3: Connect Backend
Create `.env.local`:
```bash
cp .env.example .env.local
```

Edit `.env.local`:
```
VITE_API_BASE_URL=http://localhost:8000/api
```

### Step 4: Test the App
- Click "Talk to Sanjeevini" to test voice
- Add a reminder
- Log your mood
- Set up emergency contacts

## 📱 Key UI Components

All components are in `src/components/UI.jsx`:

```jsx
// Buttons
<Button variant="primary" size="lg">Click me</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="danger">Delete</Button>

// Cards
<Card title="My Card" subtitle="Optional subtitle">
  Content here
</Card>

// Status indicators
<StatusBadge status="active" label="Active" />
<RiskMeter level="low" label="Fall Risk" />

// Loading
<LoadingSpinner label="Loading..." />

// Alerts
<AlertBox type="success" message="Done!" />
```

## 🔌 API Integration

The app expects these API endpoints from your backend:

### Required Endpoints
- `GET /api/profile` - User profile
- `POST /api/set-reminder` - Create reminder
- `GET /api/reminders` - List reminders
- `GET /api/get-mood-status` - Current mood
- `POST /api/mood` - Log mood
- `GET /api/mood/history` - Mood history
- `GET /api/get-fall-risk` - Fall risk assessment
- `POST /api/emergency-contacts` - Add contact
- `GET /api/dashboard/stats` - Dashboard data

All API calls are abstracted in `src/services/api.js` - modify there if needed.

## 🎨 Customization

### Change Theme Colors
Edit `tailwind.config.js`:
```javascript
colors: {
  'healthcare-blue': '#E8F4F8',
  'healthcare-accent': '#0EA5A0',
  // Change these to customize the theme
}
```

### Add New Pages
1. Create component in `src/pages/`
2. Add route to `App.jsx`
3. Add navigation link to `Layout.jsx`

### Customize API Base URL
```env
VITE_API_BASE_URL=https://your-backend.com/api
```

## 🔐 Accessibility Features (Built-in)

✅ WCAG AA compliant
✅ Keyboard navigation
✅ ARIA labels
✅ High contrast colors
✅ Large touch targets (44x44px minimum)
✅ Voice interaction
✅ Screen reader support
✅ Semantic HTML

## 📊 Development Workflow

```bash
# Development
npm run dev          # Start dev server

# Build
npm run build        # Create production build

# Preview
npm run preview      # Preview production build

# Testing
npm run lint         # Check code quality
```

## 📁 Project Structure Explained

```
src/
├── components/
│   ├── UI.jsx              # Base components (Button, Card, etc.)
│   ├── Layout.jsx          # Nav, Footer, Layout wrapper
│   └── VoiceRecorder.jsx   # Voice input/output
│
├── pages/
│   ├── HomePage.jsx        # Dashboard with stats
│   ├── RemindersPage.jsx   # Reminder management
│   ├── MoodInsightsPage.jsx # Mood charts and tracking
│   └── EmergencyContactsPage.jsx # Emergency setup
│
├── services/
│   └── api.js              # API service layer (all calls here)
│
├── context/
│   └── NotificationContext.jsx # Toast notifications
│
├── hooks/
│   └── useCustomHooks.js   # useFetch, useForm, useLocalStorage, etc.
│
├── utils/
│   └── helpers.js          # Helper functions
│
├── constants/
│   └── index.js            # Application constants
│
├── App.jsx                 # Main app + routing
├── main.jsx                # React entry point
└── index.css               # Global styles
```

## 🐛 Common Issues & Solutions

### "Cannot find module" error
```bash
# Clear cache and reinstall
rm -rf node_modules
npm install
npm run dev
```

### Microphone not working
- Check browser permissions
- Must use HTTPS in production
- Some browsers need `allow="microphone"` in iframe

### API calls failing
- Verify backend is running
- Check CORS settings
- Ensure VITE_API_BASE_URL is correct
- Check browser console for errors

### Styling looks wrong
- Clear browser cache (Ctrl+Shift+R)
- Restart dev server
- Check tailwind.config.js

## 📚 Additional Resources

- [React Docs](https://react.dev)
- [Tailwind CSS](https://tailwindcss.com)
- [Vite Docs](https://vitejs.dev)
- [React Router](https://reactrouter.com)
- [Web Accessibility](https://www.w3.org/WAI/)

## 🚀 Deployment

### Deploy to Vercel (Recommended)
```bash
npm install -g vercel
vercel
```

### Deploy to Netlify
```bash
npm run build
# Connect dist folder to Netlify
```

### Deploy with Docker
See `DEVELOPMENT.md` for Docker instructions

## 📞 Support

For detailed development guide, see `DEVELOPMENT.md`

Quick troubleshooting:
1. Check browser console for errors
2. Verify API connection
3. Test on a different browser
4. Check network tab for failed requests
5. Review backend logs

## ✅ Ready to Use Features

- ✨ Voice-to-text input
- 📊 Data visualization
- 🔔 Smart notifications
- 📱 Mobile responsive
- ♿ Accessible design
- 🎨 Professional UI
- 🔄 Real-time updates
- 💾 Local data caching

## 🎓 Next Steps

1. **Setup Backend**: Ensure Python FastAPI backend is running
2. **Configure API URL**: Update `.env.local` with backend address
3. **Test Voice**: Grant microphone permissions when prompted
4. **Add Sample Data**: Create test reminders and contacts
5. **Customize**: Adapt colors, text, and features to your needs

## 📝 Notes

- App uses localStorage for client-side caching
- Notifications require user permission
- Voice features need HTTPS in production
- Mobile should be tested on actual devices
- All data flows through API to backend

---

**You're all set!** 🎉 Start the dev server and explore the app.

Questions? Check `DEVELOPMENT.md` or `README.md` for detailed documentation.

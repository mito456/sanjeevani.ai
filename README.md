# Sanjeevini AI - Healthcare Assistant Frontend

A mobile-first React web application designed to help elderly users maintain independence through predictive routine learning, smart reminders, fall risk estimation, emotional monitoring, and cognitive engagement.

## 📱 Features

### Core Features
- **Voice-Friendly Interface**: Talk to Sanjeevini AI using speech recognition
- **Dashboard**: Real-time activity status, mood tracking, and fall risk assessment
- **Daily Reminders**: Manage medications, meals, exercises, and appointments
- **Mood Insights**: Track emotional wellbeing with charts and trends
- **Emergency Contacts**: One-click alerts to trusted contacts
- **Accessibility**: Large buttons, high contrast text, minimal animations

### Technical Stack

**Frontend:**
- React 18.2
- React Router DOM for navigation
- Axios for API calls
- Recharts for data visualization
- React Speech Recognition
- Tailwind CSS for styling
- React Icons for UI icons
- Date-fns for date formatting

**Key Libraries:**
```
react@18.2.0
react-dom@18.2.0
react-router-dom@6.18.0
axios@1.6.0
react-speech-recognition@3.10.0
recharts@2.10.3
react-icons@4.12.0
date-fns@2.30.0
tailwindcss@3.3.6
```

## 🚀 Getting Started

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn

### Installation

1. Navigate to the project directory:
```bash
cd sanjeevini-frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file (optional):
```bash
cp .env.example .env
# Edit .env with your backend API URL
REACT_APP_API_URL=http://localhost:8000/api
```

### Development

1. Start the development server:
```bash
npm run dev
```

2. Open your browser and navigate to `http://localhost:3000`

### Build for Production

```bash
npm run build
```

The optimized build will be created in the `dist` folder.

## 📁 Project Structure

```
sanjeevini-frontend/
├── src/
│   ├── components/
│   │   ├── UI.jsx                 # Reusable UI components
│   │   ├── Layout.jsx             # Navigation, Footer, Layout wrapper
│   │   └── VoiceRecorder.jsx      # Voice interaction components
│   ├── context/
│   │   └── NotificationContext.jsx # Notifications & alerts
│   ├── pages/
│   │   ├── HomePage.jsx           # Dashboard
│   │   ├── RemindersPage.jsx      # Reminders management
│   │   ├── MoodInsightsPage.jsx   # Mood tracking & charts
│   │   └── EmergencyContactsPage.jsx # Emergency setup
│   ├── services/
│   │   └── api.js                 # API service layer
│   ├── App.jsx                    # Main app component
│   ├── main.jsx                   # Entry point
│   └── index.css                 # Global styles
├── public/
│   └── index.html                 # HTML template
├── package.json
├── tailwind.config.js
├── postcss.config.js
├── vite.config.js
└── README.md
```

## 🎨 UI Components

### Available Components (UI.jsx)

- **Button**: Customizable button with variants (primary, secondary, danger, ghost)
- **Card**: Content container with optional title and subtitle
- **StatusBadge**: Status indicator (active, inactive, warning, danger, etc.)
- **RiskMeter**: Visual risk level indicator
- **LoadingSpinner**: Loading state indicator
- **AlertBox**: Alert messages with optional actions
- **Header**: Page header with title and optional right action
- **Container**: Max-width container for layouts

### Voice Components (VoiceRecorder.jsx)

- **VoiceRecorder**: Speech-to-text input component
- **TextToSpeech**: Text-to-speech output component
- **BrowserNotification**: Browser notification utilities

## 🔌 API Integration

The app communicates with the backend via RESTful API. Key endpoints:

### Activity API
- `POST /api/log-activity` - Log user activity
- `GET /api/activities` - Get activity history
- `GET /api/activities/today` - Get today's activities

### Routine API
- `GET /api/get-routine-pattern` - Get routine pattern
- `POST /api/check-deviation` - Check routine deviations
- `PUT /api/routine` - Update routine

### Reminder API
- `POST /api/set-reminder` - Create reminder
- `GET /api/reminders` - Get all reminders
- `POST /api/reminders/{id}/complete` - Mark as complete
- `POST /api/reminders/{id}/snooze` - Snooze reminder
- `DELETE /api/reminders/{id}` - Delete reminder

### Mood API
- `GET /api/get-mood-status` - Get current mood status
- `POST /api/mood` - Log mood
- `GET /api/mood/history` - Get mood history
- `POST /api/mood/analyze-speech` - Analyze mood from speech

### Fall Risk API
- `GET /api/get-fall-risk` - Get fall risk assessment
- `POST /api/fall-risk/update` - Update risk factors
- `POST /api/fall-risk/log` - Log fall event

### Emergency API
- `GET /api/emergency-contacts` - Get contacts
- `POST /api/emergency-contacts` - Add contact
- `POST /api/emergency-contacts/{id}/notify` - Send alert

## 🎯 Usage Examples

### Adding a Reminder
1. Click "Add Reminder" button
2. Enter reminder details (title, type, date/time)
3. Submit to create

### Tracking Mood
1. Click "Log Mood" button
2. Speak to describe your mood
3. System records and analyzes your emotional state

### Emergency Contact Alert
1. Go to Emergency Contacts page
2. Set up trusted contacts
3. Click "Notify All" in emergency situations

### Voice Interaction
- Click "Talk to Sanjeevini" on dashboard
- Speak naturally
- System processes voice commands

## 🔐 Accessibility Features

✅ **Large Buttons**: Min 44x44px touch targets
✅ **High Contrast**: WCAG AA compliant color ratios
✅ **Voice Input**: Speech recognition for hands-free operation
✅ **Keyboard Navigation**: Full keyboard support
✅ **ARIA Labels**: Semantic HTML with proper labels
✅ **Readable Fonts**: 16px+ default font sizes
✅ **Simple Navigation**: Clear, predictable menu structure
✅ **Color Independence**: Information not conveyed by color alone

## 🌐 Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📦 Environment Variables

Create a `.env.local` file:

```
VITE_API_BASE_URL=http://localhost:8000/api
VITE_APP_NAME=Sanjeevini AI
VITE_ENABLE_NOTIFICATIONS=true
```

## 🔧 Development Tips

### Adding a New Page
1. Create component in `src/pages/`
2. Import in `App.jsx`
3. Add route in Routes section
4. Add navigation link in `Layout.jsx`

### Styling
- Uses Tailwind CSS utility classes
- Custom colors in `tailwind.config.js`
- Global styles in `index.css`

### API Calls
- Use services from `src/services/api.js`
- All services return Promises
- Use `useNotification()` hook for feedback

## 🐛 Troubleshooting

### Microphone not working
- Check browser permissions
- Ensure HTTPS in production (required for audio)
- Try a different browser

### API connection failed
- Verify backend is running on correct port
- Check API URL in environment variables
- Check CORS settings on backend

### Styling issues
- Clear browser cache
- Rebuild Tailwind CSS: `npm run dev`
- Check tailwind.config.js for custom colors

## 📝 Notes

- The app uses localStorage for caching (optional)
- Notifications require user permission
- Voice features need HTTPS in production
- Mobile-first design means best on small screens

## 🤝 Contributing

When adding features:
1. Follow existing component structure
2. Use Tailwind CSS for styling
3. Add proper accessibility attributes
4. Include error handling
5. Update this README

## 📄 License

This project is part of the Sanjeevini AI healthcare initiative.

## 🆘 Support

For issues or questions:
- Check documentation
- Review API error messages
- Check browser console for errors
- Ensure backend is running

## 🎓 Learning Resources

- [React Documentation](https://react.dev)
- [Tailwind CSS](https://tailwindcss.com)
- [React Router](https://reactrouter.com)
- [Recharts](https://recharts.org)
- [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)

---

**Built with ❤️ for healthy aging and senior wellness**

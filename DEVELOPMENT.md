# Sanjeevini AI - Frontend Development Guide

## 📋 Table of Contents
1. [Quick Start](#quick-start)
2. [Project Structure](#project-structure)
3. [Component Development](#component-development)
4. [State Management](#state-management)
5. [API Integration](#api-integration)
6. [Styling](#styling)
7. [Accessibility](#accessibility)
8. [Testing](#testing)
9. [Performance](#performance)
10. [Deployment](#deployment)

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linter
npm run lint
```

## 📁 Project Structure

```
src/
├── components/          # Reusable React components
│   ├── UI.jsx          # Core UI components
│   ├── Layout.jsx      # App layout
│   └── VoiceRecorder.jsx # Voice interaction
├── context/            # React Context for state
│   └── NotificationContext.jsx
├── pages/              # Page components
│   ├── HomePage.jsx
│   ├── RemindersPage.jsx
│   ├── MoodInsightsPage.jsx
│   └── EmergencyContactsPage.jsx
├── services/           # API services
│   └── api.js
├── hooks/              # Custom React hooks
│   └── useCustomHooks.js
├── utils/              # Utility functions
│   └── helpers.js
├── constants/          # App constants
│   └── index.js
├── App.jsx            # Main app component
├── main.jsx           # Entry point
├── index.css          # Global styles
```

## 🧩 Component Development

### Creating a New Component

1. **Create component file** in appropriate directory:
```jsx
// src/components/MyComponent.jsx
import React from 'react';
import './MyComponent.css'; // Optional

export const MyComponent = ({ title, children, onClick }) => {
  return (
    <div onClick={onClick}>
      <h2>{title}</h2>
      {children}
    </div>
  );
};
```

2. **Export from index** (if using barrel exports):
```jsx
// src/components/index.js
export { MyComponent } from './MyComponent';
```

3. **Use in pages**:
```jsx
import { MyComponent } from '../components';

export const MyPage = () => {
  return <MyComponent title="Hello" />;
};
```

### Component Best Practices

- Keep components small and focused (Single Responsibility)
- Use functional components with hooks
- Prop destructuring in function signature
- Add JSDoc comments for props
- Handle loading and error states
- Use semantic HTML
- Add ARIA labels for accessibility

### Example Component with All Best Practices

```jsx
/**
 * StatusCard Component
 * @param {string} label - Display label
 * @param {string|number} value - Status value to display
 * @param {string} status - Status type (success, warning, error)
 * @param {Function} onClick - Click handler
 */
export const StatusCard = ({ label, value, status = 'info', onClick }) => {
  const statusStyles = {
    success: 'bg-green-50 border-green-200',
    warning: 'bg-yellow-50 border-yellow-200',
    error: 'bg-red-50 border-red-200',
    info: 'bg-blue-50 border-blue-200',
  };

  return (
    <Card 
      className={`border-l-4 cursor-pointer hover:shadow-md transition-shadow ${statusStyles[status]}`}
      onClick={onClick}
      role="button"
      tabIndex={0}
      aria-label={`${label}: ${value}`}
    >
      <p className="text-sm text-gray-600">{label}</p>
      <p className="text-2xl font-bold text-gray-900">{value}</p>
    </Card>
  );
};
```

## 🔄 State Management

### Using Context API

```jsx
import { NotificationContext, useNotification } from '../context/NotificationContext';

// In a component
export const MyComponent = () => {
  const { addNotification } = useNotification();

  const handleClick = () => {
    addNotification('Action completed', 'success');
  };

  return <Button onClick={handleClick}>Click me</Button>;
};
```

### Using useState

```jsx
import { useState } from 'react';

export const Counter = () => {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>{count}</p>
      <Button onClick={() => setCount(count + 1)}>Increment</Button>
    </div>
  );
};
```

### Using Custom Hooks

```jsx
import { useFetch, useForm } from '../hooks/useCustomHooks';

export const DataPage = () => {
  // Fetch data automatically
  const { data, loading, error, refetch } = useFetch(
    () => api.getData(),
    []
  );

  // Form management
  const { values, handleChange, handleSubmit } = useForm(
    { name: '', email: '' },
    async (values) => {
      await api.submit(values);
    }
  );

  return (
    <div>
      {loading ? <LoadingSpinner /> : <div>{/* render data */}</div>}
      <form onSubmit={handleSubmit}>
        <input name="name" value={values.name} onChange={handleChange} />
      </form>
    </div>
  );
};
```

## 🔌 API Integration

### Making API Calls

```jsx
import { reminderAPI, moodAPI } from '../services/api';
import { useNotification } from '../context/NotificationContext';

export const RemindersPage = () => {
  const { addNotification } = useNotification();
  const [reminders, setReminders] = useState([]);

  useEffect(() => {
    const fetchReminders = async () => {
      try {
        const response = await reminderAPI.getReminders();
        setReminders(response.data);
      } catch (error) {
        addNotification('Failed to load reminders', 'error');
      }
    };

    fetchReminders();
  }, []);

  return <div>{/* render reminders */}</div>;
};
```

### Adding New API Services

```jsx
// src/services/api.js
export const newAPI = {
  getData: () => api.get('/endpoint'),
  postData: (data) => api.post('/endpoint', data),
  putData: (id, data) => api.put(`/endpoint/${id}`, data),
  deleteData: (id) => api.delete(`/endpoint/${id}`),
};
```

## 🎨 Styling

### Tailwind CSS Classes

```jsx
// Container and spacing
<div className="max-w-4xl mx-auto px-4 md:px-6 py-8">

// Flexbox
<div className="flex items-center justify-between gap-4">

// Grid
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

// Text
<h1 className="text-2xl md:text-3xl font-bold text-gray-900">
</h1>

// Colors (healthcare theme)
<div className="bg-healthcare-blue text-healthcare-accent border-2 border-healthcare-accent">
</div>

// Responsive
<div className="hidden md:block">Only visible on medium+ screens</div>
<div className="md:hidden">Only visible on small screens</div>
```

### Custom Colors

Available in tailwind.config.js:
- `healthcare-blue`: Light blue background
- `healthcare-accent`: Teal accent color
- `healthcare-gray`: Light gray background
- `health-success`: Green for success
- `health-warning`: Orange for warnings
- `health-danger`: Red for dangers

### Creating Custom Styles

```css
/* src/styles/custom.css */
@layer components {
  .card-elevated {
    @apply bg-white rounded-lg shadow-lg p-6;
  }

  .btn-primary {
    @apply px-4 py-2 bg-healthcare-accent text-white rounded-lg hover:bg-teal-600;
  }
}
```

## ♿ Accessibility

### ARIA Attributes

```jsx
// Buttons
<Button aria-label="Add reminder">+</Button>

// Lists
<ul role="list">
  <li role="listitem">Item 1</li>
</ul>

// Form inputs
<input 
  type="text" 
  aria-label="Search reminders"
  aria-describedby="search-help"
/>
<p id="search-help">Enter reminder title or date</p>

// Live regions
<div role="status" aria-live="polite">
  Reminder created successfully
</div>

// Headings hierarchy
<h1>Page Title</h1>
<h2>Section Title</h2>
<h3>Subsection</h3>
```

### Keyboard Navigation

```jsx
<div 
  role="button" 
  tabIndex={0}
  onKeyDown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      handleClick();
    }
  }}
>
  Click me
</div>
```

### Color Contrast

- Use high contrast color combinations
- Test with accessibility tools
- Don't rely on color alone for information
- Use our pre-defined healthcare colors (tested for AA compliance)

### Screen Reader Text

```jsx
<span className="sr-only">Additional context for screen readers</span>
```

## 🧪 Testing

### Manual Testing Checklist

- [ ] Test on mobile (Chrome DevTools)
- [ ] Test on tablet
- [ ] Test on desktop
- [ ] Test keyboard navigation
- [ ] Test with screen reader
- [ ] Test with notifications disabled
- [ ] Test with JavaScript disabled (graceful degradation)
- [ ] Test API error scenarios
- [ ] Test with slow network
- [ ] Test with offline (localStorage fallback)

### Browser Testing

Use real devices or Browserstack:
- iOS Safari
- Android Chrome
- Desktop Chrome, Safari, Firefox, Edge

## ⚡ Performance

### Code Splitting

```jsx
import { lazy, Suspense } from 'react';

const MoodInsights = lazy(() => import('../pages/MoodInsightsPage'));

export const App = () => {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      <MoodInsights />
    </Suspense>
  );
};
```

### Memoization

```jsx
import { memo, useMemo, useCallback } from 'react';

export const MemoComponent = memo(({ data }) => {
  const processedData = useMemo(() => {
    return data.filter(item => item.active);
  }, [data]);

  const handleClick = useCallback(() => {
    // handle click
  }, []);

  return <div>{/* render */}</div>;
});
```

### Image Optimization

```jsx
// Always specify width and height
<img 
  src="image.jpg" 
  alt="Description"
  width={300}
  height={200}
  loading="lazy"
/>
```

### Avoiding Unnecessary Re-renders

```jsx
// ❌ Bad - new object created each render
const config = { size: 'lg' };
return <Component config={config} />;

// ✅ Good - constant outside component
const CONFIG = { size: 'lg' };
return <Component config={CONFIG} />;

// ✅ Good - memoized
const config = useMemo(() => ({ size: 'lg' }), []);
return <Component config={config} />;
```

## 🚀 Deployment

### Build Process

```bash
# Build for production
npm run build

# Output is in dist/ folder
# Contains optimized bundles and assets
```

### Environment Setup

Create `.env.production`:
```
VITE_API_BASE_URL=https://api.sanjeevini.com/api
VITE_APP_NAME=Sanjeevini AI
VITE_ENABLE_NOTIFICATIONS=true
```

### Hosting Options

**1. Vercel** (Recommended for Vite)
```bash
npm install -g vercel
vercel
```

**2. Netlify**
```bash
npm run build
# Connect dist/ folder to Netlify
```

**3. Docker**
```dockerfile
FROM node:18 as builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

**4. GitHub Pages**
```bash
npm run build
# Push dist/ folder to gh-pages branch
```

### Performance Audit

```bash
# Use Lighthouse in DevTools
# Check Core Web Vitals
# Optimize images, bundles
# Monitor performance metrics
```

## 📚 Resources

- [React Documentation](https://react.dev)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [MDN Web Docs](https://developer.mozilla.org)
- [Web Accessibility Guidelines](https://www.w3.org/WAI/)
- [Vite Documentation](https://vitejs.dev)

## 🐛 Common Issues

### Issue: Microphone not working
**Solution**: Check browser permissions, ensure HTTPS in production

### Issue: API calls fail
**Solution**: Check CORS settings on backend, verify API URL

### Issue: Styles not applying
**Solution**: Clear cache, restart dev server, check Tailwind config

### Issue: Notifications not showing
**Solution**: Request permission, check notification settings, enable in browser

---

Happy coding! 🎉

/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {
      colors: {
        'healthcare-blue': '#E8F4F8',
        'healthcare-accent': '#0EA5A0',
        'healthcare-gray': '#F3F4F6',
        'health-success': '#10B981',
        'health-warning': '#F59E0B',
        'health-danger': '#EF4444',
      },
      spacing: {
        '128': '32rem',
      },
      fontSize: {
        'xs': ['12px', '16px'],
        'sm': ['14px', '20px'],
        'base': ['16px', '24px'],
        'lg': ['18px', '28px'],
        'xl': ['20px', '28px'],
        '2xl': ['24px', '32px'],
      }
    },
  },
  plugins: [],
}

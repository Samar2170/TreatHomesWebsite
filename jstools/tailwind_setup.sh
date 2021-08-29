npm init -y && npm install tailwindcss autoprefixer clean-css-cli && npx tailwindcss init -p

rm tailwind.config.js
rm package.json



cat << EQF > package.json
{
  "name": "jstools",
  "version": "1.0.0",
  "description": "",
  "core": "index.js",
  "scripts": {
    "build": "tailwind build ../core/static/css/tailwind.css -o ../core/static/css/style.css && cleancss -o ../core/static/css/style.min.css ../core/static/css/style.css"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "autoprefixer": "^10.2.5",
    "clean-css-cli": "^5.3.0",
    "tailwindcss": "^2.1.2"
  }
}
EQF

cat << EQF > tailwind.config.js
const colors = require('tailwindcss/colors')
module.exports = {
  darkMode: 'class',
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
  purge: {
      enabled: false, //true for production build
      content: [
          '../**/templates/*.html',
          '../**/templates/**/*.html'
      ]
  },
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },
    colors: {
      p2:'#1EE118',
      primary:'#02B159',
      secondary:'#006AF5',
      white:'#ffffff',
      offwhite:colors.coolGray[50],
      black:colors.coolGray[800],
      gray: colors.coolGray,
      blue: colors.lightBlue,
      red: colors.rose,
      pink: colors.fuchsia,
      yellow: colors.amber,
      green: colors.green,
    },
    fontWeight: {
      hairline: 100,
      'extra-light': 100,
      thin: 200,
      light: 300,
      normal: 400,
      medium: 500,
      semibold: 600,
      bold: 700,
      extrabold: 800,
      'extra-bold': 800,
      black: 900,
     },
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      mw: ['Merriweather', 'serif'],
      ss: ['ui-sans-serif', 'system-ui'],
      serif: ['ui-serif', 'Georgia'],
      mono: ['ui-monospace', 'SFMono-Regular'],
    },
    extend: {
      spacing: {
        '128': '32rem',
        '144': '36rem',
      },
      borderRadius: {
        '4xl': '2rem',
      }
    }
  },
  variants: {},
  plugins: [],
}
EQF

cat << EQF > ../core/static/css/tailwind.css
@tailwind base;
@tailwind components;
@tailwind utilities;
EQF


npm run build
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
      p2:'#4895d1',
      primary:'#4451de',
      secondary:'#3d8fd0',
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

import { createTheme } from '@mui/material/styles'

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2', // Blue for primary actions
    },
    secondary: {
      main: '#ff4081', // Pink for secondary actions
    },
    background: {
      default: '#f5f5f5', // Light gray background for the app
      paper: '#ffffff', // White for card backgrounds
    },
    text: {
      primary: '#333333', // Dark text for primary content
      secondary: '#555555', // Gray text for secondary content
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif', // Main font
    h1: {
      fontWeight: 700,
      fontSize: '2.5rem',
    },
    h2: {
      fontWeight: 600,
      fontSize: '2rem',
    },
    h3: {
      fontWeight: 600,
      fontSize: '1.75rem',
    },
    h4: {
      fontWeight: 600,
      fontSize: '1.5rem',
    },
    h5: {
      fontWeight: 500,
      fontSize: '1.25rem',
    },
    h6: {
      fontWeight: 500,
      fontSize: '1rem',
    },
    body1: {
      fontWeight: 400,
      fontSize: '1rem',
    },
    body2: {
      fontWeight: 400,
      fontSize: '0.875rem',
    },
  },
  shape: {
    borderRadius: 8, // Rounded corners for cards and buttons
  },
  components: {
    MuiButton: {
      defaultProps: {
        variant: 'contained', // Default button variant
      },
      styleOverrides: {
        root: {
          borderRadius: '8px', // Custom border radius for buttons
          textTransform: 'none', // Prevent uppercase text
        },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          boxShadow: '0 3px 6px rgba(0, 0, 0, 0.1)', // Soft shadow for cards
        },
      },
    },
    MuiAppBar: {
      styleOverrides: {
        root: {
          boxShadow: 'none', // Remove shadow for AppBar
        },
      },
    },
  },
})

export default theme

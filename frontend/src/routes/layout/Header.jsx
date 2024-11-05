/* eslint-disable react/no-unstable-nested-components */
import React, { useState } from 'react'
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Box,
  IconButton,
  Drawer,
} from '@mui/material'
import { Link, useNavigate } from 'react-router-dom'
import MenuIcon from '@mui/icons-material/Menu'
import { getItem, removeItem } from '../../utils/localStorageUtils'

function Header() {
  const [drawerOpen, setDrawerOpen] = useState(false)
  const navigate = useNavigate()
  const userToken = getItem('token')

  const handleSignOut = () => {
    removeItem('token')
    navigate('/signin')
  }

  // Reusable button styles for DRY code
  const buttonStyles = {
    fontWeight: 600,
    borderRadius: '20px',
    padding: '0.5rem 1.5rem',
    backgroundColor: 'white',
    color: 'text.secondary',
    transition: 'color 0.3s, background-color 0.3s',
    '&:hover': {
      color: 'white',
      backgroundColor: 'rgba(0, 0, 0, 0.2)',
    },
  }

  const toggleDrawer = open => () => {
    setDrawerOpen(open)
  }

  const menuItems = [
    { text: 'Home', path: '/' },
    { text: 'Apartments', path: '/apartments' },
    { text: 'Bookings', path: '/bookings' },
    { text: 'About Us', path: '/aboutus' },
    { text: 'Contact', path: '/contact' },
  ]

  function DrawerContent() {
    return (
      <Box
        sx={{ width: 250 }}
        role='presentation'
        onClick={toggleDrawer(false)}
        onKeyDown={toggleDrawer(false)}
      >
        {menuItems.map((item, index) => (
          <Button
            key={index}
            component={Link}
            to={item.path}
            sx={{
              display: 'block',
              width: '100%',
              textAlign: 'left',
              ...buttonStyles,
            }}
          >
            {item.text}
          </Button>
        ))}
        {userToken ? (
          <Button
            onClick={handleSignOut}
            sx={{
              display: 'block',
              width: '100%',
              textAlign: 'left',
              ...buttonStyles,
            }}
          >
            Log Out
          </Button>
        ) : (
          <Button
            component={Link}
            to='/signin'
            sx={{
              display: 'block',
              width: '100%',
              textAlign: 'left',
              ...buttonStyles,
            }}
          >
            Sign In
          </Button>
        )}
      </Box>
    )
  }

  return (
    <AppBar
      position='static'
      color='primary'
      elevation={3}
      sx={{ padding: '0.5rem 0' }}
    >
      <Toolbar
        sx={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}
      >
        {/* Logo */}
        <Typography
          variant='h5'
          component={Link}
          to='/'
          sx={{
            fontWeight: 'bold',
            color: 'inherit',
            textDecoration: 'none',
          }}
        >
          Apartment Rentals
        </Typography>

        {/* Hamburger Menu */}
        <IconButton
          edge='end'
          color='inherit'
          aria-label='menu'
          onClick={toggleDrawer(true)}
          sx={{ display: { xs: 'block', md: 'none' } }} // Only show on mobile
        >
          <MenuIcon />
        </IconButton>

        {/* Desktop Navigation Links */}
        <Box sx={{ display: { xs: 'none', md: 'flex' }, gap: 3 }}>
          {menuItems.map((item, index) => (
            <Button
              key={index}
              component={Link}
              to={item.path}
              sx={buttonStyles}
            >
              {item.text}
            </Button>
          ))}
          {userToken ? (
            <Button
              onClick={handleSignOut}
              sx={{
                ...buttonStyles,
                backgroundColor: 'secondary',
                color: 'white',
                '&:hover': {
                  backgroundColor: 'secondary.dark',
                },
              }}
            >
              Log Out
            </Button>
          ) : (
            <Button
              component={Link}
              to='/signin'
              sx={{
                ...buttonStyles,
                backgroundColor: 'secondary',
                color: 'white',
                '&:hover': {
                  backgroundColor: 'secondary.dark',
                },
              }}
            >
              Sign In
            </Button>
          )}
        </Box>
      </Toolbar>

      {/* Drawer for Mobile Menu */}
      <Drawer anchor='right' open={drawerOpen} onClose={toggleDrawer(false)}>
        <DrawerContent />
      </Drawer>
    </AppBar>
  )
}

export default Header

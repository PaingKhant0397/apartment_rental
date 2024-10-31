// src/components/Footer.js
import React from 'react'
import {
  Box,
  Typography,
  Link as MuiLink,
  Grid,
  IconButton,
} from '@mui/material'
import { Facebook, Twitter, Instagram } from '@mui/icons-material'

function Footer() {
  return (
    <Box
      sx={{
        bgcolor: 'primary.main',
        color: 'white',
        py: 4,
        // mt: 4,
      }}
    >
      <Grid
        container
        justifyContent='space-between'
        sx={{ maxWidth: 1200, mx: 'auto', px: 3 }}
      >
        {/* Left Side: Company Info */}
        <Grid item xs={12} md={4}>
          <Typography variant='h6' gutterBottom>
            Apartment Rentals
          </Typography>
          <Typography variant='body2' color='inherit'>
            High-quality apartments across top locations with a focus on comfort
            and convenience.
          </Typography>
        </Grid>

        {/* Center: Quick Links */}
        <Grid item xs={12} md={4}>
          <Typography variant='h6' gutterBottom>
            Quick Links
          </Typography>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
            <MuiLink href='/' color='inherit' underline='hover'>
              Home
            </MuiLink>
            <MuiLink href='/catalog' color='inherit' underline='hover'>
              Apartments
            </MuiLink>
            <MuiLink href='/about' color='inherit' underline='hover'>
              About Us
            </MuiLink>
            <MuiLink href='/contact' color='inherit' underline='hover'>
              Contact
            </MuiLink>
          </Box>
        </Grid>

        {/* Right Side: Social Media Links */}
        <Grid item xs={12} md={4}>
          <Typography variant='h6' gutterBottom>
            Connect with Us
          </Typography>
          <Box>
            <IconButton
              href='https://facebook.com'
              target='_blank'
              rel='noopener'
              sx={{ color: 'white' }}
            >
              <Facebook />
            </IconButton>
            <IconButton
              href='https://twitter.com'
              target='_blank'
              rel='noopener'
              sx={{ color: 'white' }}
            >
              <Twitter />
            </IconButton>
            <IconButton
              href='https://instagram.com'
              target='_blank'
              rel='noopener'
              sx={{ color: 'white' }}
            >
              <Instagram />
            </IconButton>
          </Box>
        </Grid>
      </Grid>
    </Box>
  )
}

export default Footer

// src/pages/Contact.js
import React from 'react'
import {
  Container,
  Typography,
  Box,
  Grid,
  TextField,
  Button,
  Card,
  CardContent,
  Divider,
} from '@mui/material'
import PhoneIcon from '@mui/icons-material/Phone'
import EmailIcon from '@mui/icons-material/Email'
import LocationOnIcon from '@mui/icons-material/LocationOn'

function Contact() {
  return (
    <Container maxWidth='md' sx={{ py: 5 }}>
      {/* Page Header */}
      <Box textAlign='center' sx={{ mb: 5 }}>
        <Typography
          variant='h3'
          sx={{ fontWeight: 'bold', color: 'primary.main', mb: 2 }}
        >
          Contact Us
        </Typography>
        <Typography variant='body1' color='textSecondary'>
          We'd love to hear from you! Feel free to reach out with any questions,
          feedback, or inquiries.
        </Typography>
      </Box>

      {/* Contact Form */}
      <Box sx={{ mb: 6 }}>
        <Typography
          variant='h4'
          gutterBottom
          sx={{ fontWeight: 'medium', color: 'primary.dark' }}
        >
          Send Us a Message
        </Typography>
        <Divider sx={{ mb: 3 }} />
        <Grid container spacing={2}>
          <Grid item xs={12} sm={6}>
            <TextField fullWidth label='Your Name' variant='outlined' />
          </Grid>
          <Grid item xs={12} sm={6}>
            <TextField fullWidth label='Your Email' variant='outlined' />
          </Grid>
          <Grid item xs={12}>
            <TextField fullWidth label='Subject' variant='outlined' />
          </Grid>
          <Grid item xs={12}>
            <TextField
              fullWidth
              label='Message'
              variant='outlined'
              multiline
              rows={4}
            />
          </Grid>
          <Grid item xs={12} textAlign='center'>
            <Button variant='contained' color='primary' size='large'>
              Submit
            </Button>
          </Grid>
        </Grid>
      </Box>

      {/* Contact Information Section */}
      <Box sx={{ mb: 6 }}>
        <Typography
          variant='h4'
          gutterBottom
          sx={{ fontWeight: 'medium', color: 'primary.dark' }}
        >
          Our Contact Information
        </Typography>
        <Divider sx={{ mb: 3 }} />
        <Grid container spacing={3}>
          {[
            {
              icon: <PhoneIcon sx={{ color: 'primary.main', fontSize: 40 }} />,
              title: 'Phone',
              info: '+1 (555) 123-4567',
            },
            {
              icon: <EmailIcon sx={{ color: 'primary.main', fontSize: 40 }} />,
              title: 'Email',
              info: 'contact@apartmentrentals.com',
            },
            {
              icon: (
                <LocationOnIcon sx={{ color: 'primary.main', fontSize: 40 }} />
              ),
              title: 'Address',
              info: '1234 Main St, Apartment City, 56789',
            },
          ].map((contact, index) => (
            <Grid item xs={12} sm={4} key={index}>
              <Card sx={{ textAlign: 'center', p: 3 }}>
                {contact.icon}
                <Typography variant='h6' sx={{ fontWeight: 'bold', mt: 1 }}>
                  {contact.title}
                </Typography>
                <Typography variant='body2' color='textSecondary'>
                  {contact.info}
                </Typography>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Box>

      {/* Map Section */}
      <Box sx={{ mb: 6 }}>
        <Typography
          variant='h4'
          gutterBottom
          sx={{ fontWeight: 'medium', color: 'primary.dark' }}
        >
          Our Location
        </Typography>
        <Divider sx={{ mb: 3 }} />
        <Box
          sx={{
            height: 400,
            borderRadius: 2,
            overflow: 'hidden',
            boxShadow: 2,
          }}
        >
          <iframe
            title='Google Maps'
            src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.409759360141!2d-122.4199063!3d37.7749295!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858064c4516b47%3A0xd53f67a0c8a7f5e4!2sSan%20Francisco%2C%20CA!5e0!3m2!1sen!2sus!4v1614068670481!5m2!1sen!2sus'
            width='100%'
            height='100%'
            style={{ border: 0 }}
            allowFullScreen=''
            loading='lazy'
          />
        </Box>
      </Box>
    </Container>
  )
}

export default Contact

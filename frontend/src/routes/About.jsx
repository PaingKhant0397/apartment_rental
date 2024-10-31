// src/pages/About.js
import React from 'react'
import {
  Container,
  Typography,
  Box,
  Grid,
  Card,
  CardContent,
  Avatar,
  Divider,
} from '@mui/material'
import ApartmentIcon from '@mui/icons-material/Apartment'
import StarBorderIcon from '@mui/icons-material/StarBorder'
import PeopleIcon from '@mui/icons-material/People'
import PlaceIcon from '@mui/icons-material/Place'

function About() {
  return (
    <Container maxWidth='lg' sx={{ py: 5 }}>
      {/* Header Section */}
      <Box textAlign='center' sx={{ mb: 4 }}>
        <Typography
          variant='h3'
          sx={{ fontWeight: 'bold', color: 'primary.main', mb: 2 }}
        >
          About Us
        </Typography>
        <Typography
          variant='body1'
          color='textSecondary'
          sx={{ maxWidth: '600px', mx: 'auto' }}
        >
          We’re dedicated to providing high-quality, comfortable, and stylish
          living spaces for everyone. Our team works tirelessly to make renting
          an apartment a smooth and delightful experience.
        </Typography>
      </Box>

      {/* Mission Section */}
      <Box sx={{ mb: 6 }}>
        <Typography
          variant='h4'
          gutterBottom
          sx={{ fontWeight: 'medium', color: 'primary.dark' }}
        >
          Our Mission
        </Typography>
        <Divider sx={{ mb: 3 }} />
        <Typography variant='body1' color='textSecondary'>
          We aim to create a seamless experience for renters by connecting them
          with carefully selected properties that meet high standards of quality
          and comfort. We believe everyone deserves a place to call home that
          they can truly enjoy, and we strive to make this vision a reality.
        </Typography>
      </Box>

      {/* Core Values Section */}
      <Box sx={{ mb: 6 }}>
        <Typography
          variant='h4'
          gutterBottom
          sx={{ fontWeight: 'medium', color: 'primary.dark' }}
        >
          Our Core Values
        </Typography>
        <Divider sx={{ mb: 3 }} />
        <Grid container spacing={3}>
          {[
            {
              title: 'Quality',
              icon: <ApartmentIcon />,
              description:
                'We only offer properties that meet our high standards of quality and comfort.',
            },
            {
              title: 'Integrity',
              icon: <StarBorderIcon />,
              description:
                'We maintain transparency and honesty in all interactions with clients and partners.',
            },
            {
              title: 'Customer Focus',
              icon: <PeopleIcon />,
              description:
                'We are dedicated to providing exceptional customer service and support.',
            },
            {
              title: 'Location Expertise',
              icon: <PlaceIcon />,
              description:
                'We know the best areas and offer properties in prime locations to meet your lifestyle needs.',
            },
          ].map((value, index) => (
            <Grid item xs={12} sm={6} md={3} key={index}>
              <Card sx={{ textAlign: 'center', p: 3 }}>
                <Box sx={{ color: 'primary.main', fontSize: 40, mb: 2 }}>
                  {value.icon}
                </Box>
                <Typography variant='h6' sx={{ fontWeight: 'bold' }}>
                  {value.title}
                </Typography>
                <Typography variant='body2' color='textSecondary'>
                  {value.description}
                </Typography>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Box>

      {/* Meet the Team Section */}
      <Box sx={{ mb: 6 }}>
        <Typography
          variant='h4'
          gutterBottom
          sx={{ fontWeight: 'medium', color: 'primary.dark' }}
        >
          Meet the Team
        </Typography>
        <Divider sx={{ mb: 3 }} />
        <Grid container spacing={3}>
          {[
            {
              name: 'Jane Doe',
              role: 'CEO & Founder',
              image: '/path/to/image1.jpg',
            },
            {
              name: 'John Smith',
              role: 'Head of Customer Service',
              image: '/path/to/image2.jpg',
            },
            {
              name: 'Alice Johnson',
              role: 'Marketing Manager',
              image: '/path/to/image3.jpg',
            },
            {
              name: 'Mike Brown',
              role: 'Lead Developer',
              image: '/path/to/image4.jpg',
            },
          ].map((member, index) => (
            <Grid item xs={12} sm={6} md={3} key={index}>
              <Card>
                <CardContent sx={{ textAlign: 'center' }}>
                  <Avatar
                    alt={member.name}
                    src={member.image}
                    sx={{ width: 80, height: 80, mx: 'auto', mb: 2 }}
                  />
                  <Typography variant='h6' sx={{ fontWeight: 'bold' }}>
                    {member.name}
                  </Typography>
                  <Typography variant='body2' color='textSecondary'>
                    {member.role}
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Box>

      {/* Closing Section */}
      <Box sx={{ textAlign: 'center', mt: 4 }}>
        <Typography
          variant='h5'
          color='primary.main'
          sx={{ fontWeight: 'bold', mb: 2 }}
        >
          Join Us on Our Journey
        </Typography>
        <Typography
          variant='body1'
          color='textSecondary'
          sx={{ maxWidth: '700px', mx: 'auto' }}
        >
          At Apartment Rentals, we believe in constantly improving and expanding
          our reach. Whether you’re looking for a place to call home or want to
          join our dedicated team, we’d love to have you with us on this
          journey.
        </Typography>
      </Box>
    </Container>
  )
}

export default About

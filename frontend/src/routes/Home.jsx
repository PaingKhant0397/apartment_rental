// src/pages/Home.js
import React from 'react'
import {
  Container,
  Typography,
  Box,
  Button,
  Grid,
  Card,
  CardContent,
} from '@mui/material'
import { useNavigate } from 'react-router-dom'
import ApartmentCatalog from '../components/apartment/ApartmentCatalog'

function Home() {
  const navigate = useNavigate()

  const handleExplore = () => {
    document.getElementById('catalog').scrollIntoView({ behavior: 'smooth' })
  }

  return (
    <Container maxWidth='lg' sx={{ padding: '2rem 0' }}>
      {/* Hero Section */}
      <Box
        sx={{
          height: '60vh',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          backgroundImage: `url('https://equiton.com/wp-content/uploads/2024/02/Emerald-Hills-Landing-4-EDITED.jpg')`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          color: 'white',
          textAlign: 'center',
          flexDirection: 'column',
          mb: 4,
          borderRadius: '8px',
        }}
      >
        <Typography variant='h2' fontWeight='bold' gutterBottom>
          Discover Your Dream Apartment
        </Typography>
        <Typography variant='h6' sx={{ maxWidth: 600 }}>
          Find the perfect space for your lifestyle with our wide range of
          high-quality apartments tailored to suit all needs and preferences.
        </Typography>
        <Button
          variant='contained'
          color='secondary'
          size='large'
          sx={{ mt: 3 }}
          onClick={handleExplore}
        >
          Explore Apartments
        </Button>
      </Box>

      {/* Key Benefits Section */}
      <Box sx={{ py: 6 }}>
        <Typography variant='h4' align='center' gutterBottom>
          Why Choose Us?
        </Typography>
        <Typography
          variant='body1'
          align='center'
          color='textSecondary'
          paragraph
        >
          We offer premium apartments with modern amenities and flexible rental
          options to fit your lifestyle.
        </Typography>
        <Grid container spacing={4} justifyContent='center'>
          <Grid item xs={12} md={4}>
            <Card sx={{ height: '100%', textAlign: 'center', boxShadow: 3 }}>
              <CardContent>
                <Typography variant='h6' fontWeight='bold'>
                  Prime Locations
                </Typography>
                <Typography color='textSecondary' variant='body2' paragraph>
                  Our apartments are located in the most sought-after areas,
                  ensuring convenience and accessibility.
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} md={4}>
            <Card sx={{ height: '100%', textAlign: 'center', boxShadow: 3 }}>
              <CardContent>
                <Typography variant='h6' fontWeight='bold'>
                  Diverse Room Options
                </Typography>
                <Typography color='textSecondary' variant='body2' paragraph>
                  Whether you’re looking for a studio or a two-bedroom
                  apartment, we have options to fit every need.
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} md={4}>
            <Card sx={{ height: '100%', textAlign: 'center', boxShadow: 3 }}>
              <CardContent>
                <Typography variant='h6' fontWeight='bold'>
                  Transparent Pricing
                </Typography>
                <Typography color='textSecondary' variant='body2' paragraph>
                  No hidden fees. Our pricing structure is clear and designed to
                  be budget-friendly.
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </Box>

      {/* Apartment Catalog Section */}

      <ApartmentCatalog />
    </Container>
  )
}

export default Home
